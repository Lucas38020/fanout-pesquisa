from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class FanoutInput(BaseModel):
    keyword: str
    matriz_semantica: Optional[Dict] = None

@app.post("/api/fanout-pesquisa")
def gerar_fanout(data: FanoutInput):
    keyword = data.keyword
    matriz = data.matriz_semantica

    return {
        "fanouts": [
            {"pergunta": f"Como atua um {keyword}?", "tipo": "TOFU"},
            {"pergunta": f"Vale a pena contratar um {keyword}?", "tipo": "MOFU"},
            {"pergunta": f"Quanto custa o serviço de um {keyword}?", "tipo": "BOFU"},
            {"pergunta": f"Erros comuns ao buscar um {keyword}", "tipo": "BOFU"}
        ],
        "pontuacao": {
            "aderencia": 3,
            "cobertura": 3,
            "nao_redundancia": 3
        },
        "entidades_acionadas": {
            "nucleo": ["advogado de família"],
            "suporte": ["divórcio", "guarda", "pensão"]
        }
    }

# ✅ ROTA EXTRA PARA SERVIR O ARQUIVO openapi.json
@app.get("/openapi.json")
def serve_openapi():
    return FileResponse("openapi.json", media_type="application/json")
