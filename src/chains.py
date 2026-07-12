from pathlib import Path
from typing import Dict

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from src.config import GOOGLE_API_KEY, MODEL_LLM, MODEL_EMBEDDING
from src.base_models import TriagemOut
from src.prompts import TRIAGEM_PROMPT, RAG_SYSTEM_PROMPT

# ---  LLM
llm_triagem = ChatGoogleGenerativeAI(
    model=MODEL_LLM,
    temperature=0.0,
    api_key=GOOGLE_API_KEY
)

# Acopla o Pydantic para forçar saída estruturada em JSON
triagem_chain = llm_triagem.with_structured_output(TriagemOut)

# --- 2. INFRAESTRUTURA DE DADOS (RAG) ---
def inicializar_retriever():
    docs = []
    caminho_pdf = Path('./PDF') 

    if caminho_pdf.exists():
        for n in caminho_pdf.glob('*.pdf'):
            try:
                loader = PyMuPDFLoader(str(n))
                docs.extend(loader.load())
                print(f'📦 Banco de Dados: {n.name} carregado com sucesso.')
            except Exception as e:
                print(f'❌ Erro ao carregar arquivo {n.name}: {e}')
    else:
        print(f"⚠️ Alerta: A pasta {caminho_pdf.absolute()} não foi encontrada.")

    if not docs:
        print("⚠️ Alerta: Nenhum documento PDF foi indexado no RAG.")
        return None

    
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    
    embeddings = GoogleGenerativeAIEmbeddings(
        model=MODEL_EMBEDDING,
        google_api_key=GOOGLE_API_KEY
    )

    
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever(
        search_type='similarity_score_threshold',
        search_kwargs={'score_threshold': 0.3, 'k': 4}
    )

retriever = inicializar_retriever()

# Prompt estruturado para o RAG
prompt_rag = ChatPromptTemplate.from_messages([
   ("system", RAG_SYSTEM_PROMPT),
   ("human", "Pergunta: {input}\n\nContexto Regulatório:\n{context}")
])

document_chain = prompt_rag | llm_triagem

# --- 3. FUNÇÕES EXECUTÁVEIS ---
def executar_triagem(mensagem: str) -> Dict:
    saida: TriagemOut = triagem_chain.invoke([
        SystemMessage(content=TRIAGEM_PROMPT),
        HumanMessage(content=mensagem)
    ])
    return saida.model_dump()

def executar_rag(pergunta: str) -> Dict:
    if not retriever:
        return {'answer': 'Não sei (Base de conhecimento vazia)', 'citacoes': [], 'contexto_encontrado': False}
        
    docs_relacionados = retriever.invoke(pergunta)

    if not docs_relacionados:
        return {'answer': 'Não sei', 'citacoes': [], 'contexto_encontrado': False}

    
    contexto_formatado = "\n\n".join(doc.page_content for doc in docs_relacionados)

    answer = document_chain.invoke({'input': pergunta, 'context': contexto_formatado})
    
    txt = (answer.content if hasattr(answer, 'content') else str(answer)).strip()

    if txt.rstrip('.!?') == 'Não sei':
        return {'answer': 'Não sei', 'citacoes': [], 'contexto_encontrado': False}

    return {'answer': txt, 'citacoes': docs_relacionados, 'contexto_encontrado': True}