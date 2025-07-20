# 📊 Estimador de Gênero por Nome - API FastAPI

Esta aplicação é uma API construída com **FastAPI** que estima o gênero de uma pessoa com base no nome fornecido. A resposta inclui o gênero estimado, a probabilidade da estimativa e o total de amostras disponíveis no banco de dados.

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- pip

### Ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
````

### Instalação das dependências

```bash
pip install fastapi uvicorn
```

---

## 📂 Estrutura do Projeto

```
.
├── main.py                # Código principal da API
├── nomes_data.json        # Base de dados com nomes e estimativas
├── analisar_nome.txt      # Registro de nomes não encontrados
└── test_api.http          # Arquivo para testar a API via REST Client
```

---

## ▶️ Como executar a API

Execute o arquivo diretamente com:

```bash
python main.py
```

Ou, se preferir, com `uvicorn`:

```bash
uvicorn main:app --reload
```

Caso deseje subir em um docker
```
docker build -t estimador-genero .
docker run -d -p 8000:8000 estimador-genero
```

Acesse a documentação interativa:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Testando a API

Você pode usar ferramentas como **Postman**, **curl** ou a extensão **REST Client** do VS Code.

### Exemplo de requisições no arquivo `.http`

Arquivo: `test_api.http`

```http
### Rota raiz
GET http://127.0.0.1:8000/
Accept: application/json

### Nome encontrado
GET http://127.0.0.1:8000/nome/Jefferson
Accept: application/json

### Nome não encontrado
GET http://127.0.0.1:8000/nome/Xablau
Accept: application/json
```

---

## 📥 Entrada

**GET** `/nome/{nome}`

* Parâmetro: `nome` (string) — nome a ser consultado

---

## 📤 Respostas esperadas

### ✅ Nome encontrado

```json
{
  "nome": "Jefferson",
  "genero_estimado": "Masculino",
  "probabilidade": 0.977,
  "total_amostras": 25112
}
```

### ❌ Nome não encontrado

```json
{
  "nome": "Xablau",
  "mensagem": "Não há registro do nome no banco de dados."
}
```

O nome ausente será registrado no arquivo `analisar_nome.txt` para posterior análise.

---

## 🧠 Tecnologias

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* Python Standard Library (`json`, `contextlib`)

---

## 📌 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Autor

Desenvolvido com 💻 por \[Jefferson]

