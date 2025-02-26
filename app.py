from flask import Flask, request, jsonify, render_template
from models import db, InseminacaoEstruturaDados  # Importa o banco de dados e modelos
from sqlalchemy import text  # Importa a função text do SQLAlchemy
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Configuração do Gemini
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("A chave de API do Gemini não foi carregada corretamente. Verifique o arquivo .env.")
genai.configure(api_key=gemini_api_key)

# Configuração do Flask e SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:ifsp@localhost:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Função para limpar a query SQL
def limpar_query(query):
    # Remove marcadores de código (```sql) e espaços extras
    query = query.replace("```sql", "").replace("```", "").strip()
    return query

# Função para verificar se a pergunta é relacionada à base de dados
def pergunta_relacionada_a_base(pergunta):
    palavras_chave = ["fazenda", "fazendas", "inseminacao", "animal", "animais", "raca", "lote", "protocolo", "iatf", "touro", "inseminador"]
    return any(palavra in pergunta.lower() for palavra in palavras_chave)

# Rota para o chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    # Verifica se a mensagem é uma saudação
    if user_message in ["olá", "oi", "tudo bem?", "olá tudo bem?"]:
        return jsonify({"response": "Olá! Como posso ajudar você hoje?"})

    try:
        # Verifica se a pergunta é relacionada à base de dados
        if pergunta_relacionada_a_base(user_message):
            # Passa a pergunta para o Gemini gerar uma query SQL
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(
                f"""
                Com base na tabela 'inseminacaoestruturadados' do schema 'uni1500', gere uma query SQL para a seguinte pergunta: {user_message}.
                A tabela tem as colunas: fazenda, estado, municipio, "Nº ANIMAL", lote, raca, categoria, ecc, ciclicidade, protocolo, "IMPLANTE P4", empresa, "GnRH NA IA", "PGF NO D0", "Dose PGF retirada", "Marca PGF retirada", "Dose CE", ecg, "DOSE eCG", touro, "RAÇA TOURO", "EMPRESA TOURO", inseminador, "Nº da IATF", dg, "VAZIA COM OU SEM CL", perda.
                A query deve começar com 'SELECT', ser compatível com PostgreSQL e referenciar a tabela como 'uni1500.inseminacaoestruturadados'.
                Retorne APENAS a query SQL, sem explicações ou comentários.
                """
            )
            query_sql = response.text.strip()  # Remove espaços em branco

            # Limpa a query SQL
            query_sql = limpar_query(query_sql)

            # Executa a query no banco de dados usando text()
            result = db.session.execute(text(query_sql))
            rows = result.fetchall()

            # Converte as linhas em uma lista de dicionários
            if rows:
                # Obtém os nomes das colunas
                columns = result.keys()
                # Cria uma lista de dicionários com os resultados
                results_list = [dict(zip(columns, row)) for row in rows]
            else:
                results_list = []

            # Retorna os resultados
            if results_list:
                return jsonify({"response": results_list})
            else:
                return jsonify({"response": "Nenhum resultado encontrado na base de dados."})
        else:
            # Se a pergunta não for relacionada à base de dados, responde com o Gemini
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_message)
            return jsonify({"response": response.text})

    except Exception as e:
        print(f"Erro ao processar a pergunta: {e}")
        return jsonify({"response": f"Desculpe, ocorreu um erro ao processar sua solicitação. Detalhes: {str(e)}"})

# Rota para a página inicial
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados (se não existirem)
    app.run(debug=True)