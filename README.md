# 🧾 DimDimApp – CP3 DevOps & Cloud

API Flask + MySQL desenvolvida para o 3º Checkpoint da disciplina **DevOps & Cloud Computing** no curso de Análise e Desenvolvimento de Sistemas da FIAP.

---

## 👨‍💻 Desenvolvedor
- **Nome:** Marcus Vinicius de Souza Calazans  
- **RM:** 556620  
- **GitHub:** [calazans-99](https://github.com/calazans-99)  
- **Repositório:** [dimdimapp_cp3](https://github.com/calazans-99/dimdimapp_cp3)

---

## 📦 Tecnologias Utilizadas

- Python 3.11
- Flask
- MySQL 8.0
- Docker & Docker Compose

---

## ⚙️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/calazans-99/dimdimapp_cp3.git
   cd dimdimapp_cp3
   ```

2. Construa e execute os containers:
   ```bash
   docker-compose up --build -d
   ```

3. Acesse a API:
   ```
   http://localhost:5000/clientes
   ```

---

## 🔁 Endpoints da API

### ➕ POST /clientes

Cadastra um novo cliente.

```json
{
  "nome": "Marcus Calazans",
  "email": "marcus@email.com"
}
```

---

### 🔍 GET /clientes

Retorna a lista de clientes cadastrados.

```json
[
  {
    "id": 1,
    "nome": "Marcus Calazans",
    "email": "marcus@email.com"
  }
]
```

---

## 🧪 Evidências da Aplicação

O PDF com todas as evidências exigidas pelo checkpoint está disponível aqui:

📄 [Evidencias_CP3_Organizado_MarcusCalazans.pdf](./Evidencias_CP3_Organizado_MarcusCalazans.pdf)

Inclui:
- `docker ps`, `whoami`, `ls && pwd`
- `POST` e `GET` no Postman
- Conexão bem-sucedida ao MySQL com logs
- Persistência de dados
- Build do Dockerfile funcionando

---

## 📁 Estrutura do Projeto

```
dimdimapp_cp3/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── Evidencias_CP3_Organizado_MarcusCalazans.pdf
```

---

## ✅ Requisitos Atendidos

- [x] 2 containers (API + MySQL)
- [x] Banco com volume
- [x] API com CRUD
- [x] Dockerfile com usuário não-root, diretório definido e variáveis
- [x] Mesma rede Docker
- [x] Execução em background
- [x] Prints com `docker exec`, `whoami`, `ls`, `GET`, `POST`
- [x] Projeto versionado no GitHub com PDF final

---
