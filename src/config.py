import os

MODEL_LLM = "gemini-2.5-flash"
MODEL_EMBEDDING = "models/gemini-embedding-001"

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY') or "SUA_API_KEY_AQUI"

if GOOGLE_API_KEY == "SUA_API_KEY_AQUI":
    print("⚠️ Aviso: Utilizando a string de fallback para GOOGLE_API_KEY. Considere configurar sua variável de ambiente.")