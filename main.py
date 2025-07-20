import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import json


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando aplicação e carregando JSON...")

    try:
        with open("nomes_data.json", "r", encoding="utf-8") as f:
            app.state.nomes_data = json.load(f)
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo 'nomes_data.json' não encontrado.")
        app.state.nomes_data = {}
    except json.JSONDecodeError as e:
        print(f"Erro ao carregar JSON: {e}")
        app.state.nomes_data = {}

    yield

    print("Encerrando aplicação.")


app = FastAPI(lifespan=lifespan)


@app.get("/nome/{nome}", summary="Estimar Gênero")
async def estimar_genero(nome: str, request: Request) -> dict:
    """
    Retorna o gênero estimado, probabilidade e total de amostras para um nome.

    **Parâmetros**:
    - `nome` (str): Nome da pessoa a ser consultada.

    **Retorno (se encontrado)**:
    ```json
    {
        "nome": "Jefferson",
        "genero_estimado": "Masculino",
        "probabilidade": 0.977,
        "total_amostras": 25112
    }
    ```

    **Retorno (se não encontrado)**:
    ```json
    {
        "nome": "Xablau",
        "mensagem": "Não há registro do nome no banco de dados."
    }
    ```
    """
    nomes_data = request.app.state.nomes_data

    if not nomes_data:
        return JSONResponse(status_code=500, content={
            "mensagem": "Base de dados ainda não carregada ou indisponível."
        })

    nome = nome.strip().upper()

    if nome not in nomes_data:
        with open("analisar_nome.txt", 'a') as add_pos:
            add_pos.write(f'{nome.title()}\n')
            add_pos.close()
        return {
            "nome": nome.title(),
            "mensagem": "Não há registro do nome no banco de dados."
        }


    dados_nome = nomes_data[nome]
    genero = "Masculino" if dados_nome["id_genero"] == 1.0 else "Feminino"

    return {
        "nome": nome.title(),
        "genero_estimado": genero,
        "probabilidade": round(dados_nome["taxa"], 3),
        "total_amostras": dados_nome["total_nome"]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)