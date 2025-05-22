from flask import Flask, request, jsonify
from database import get_connection
from models import criar_tabela_clientes
import time

app = Flask(__name__)

# Tenta se conectar várias vezes ao banco antes de iniciar a API
for _ in range(10):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        criar_tabela_clientes(cursor)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Conexão com banco bem-sucedida!")
        break
    except Exception as e:
        print(f"⏳ Aguardando banco de dados... {e}")
        time.sleep(5)
else:
    print("❌ Não foi possível conectar ao banco após várias tentativas.")
    exit(1)

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        data = request.json
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (%s, %s)",
            (data["nome"], data["email"])
        )
        conn.commit()
        return {"mensagem": "Cliente adicionado com sucesso"}, 201

    cursor.execute("SELECT * FROM clientes")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
