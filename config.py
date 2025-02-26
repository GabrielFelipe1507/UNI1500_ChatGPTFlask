import os

class Config:
    # Chave secreta para a aplicação Flask (usada para sessões, cookies, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY", "minha_chave_secreta")

    # Chave da API do Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Removi o valor padrão, pois está no .env

    # Configuração do banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:ifsp@localhost:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False