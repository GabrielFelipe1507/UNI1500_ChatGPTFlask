from flask import render_template, request, jsonify
from api.gpt import gerar_resposta

def init_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/chat", methods=["POST"])
    def chat():
        data = request.get_json()
        user_message = data.get("message", "")

        resposta = gerar_resposta(user_message)

        return jsonify({"response": resposta})
