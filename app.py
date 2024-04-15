from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": 200, "message": "API de LIVIA_EDUARDA_SANTOS_CIRILO"})

@app.route("/aleatorios") # decorator de rotas
def aleatorios(): # função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome })



if __name__ == '_main_':
    app.run(debug=True)