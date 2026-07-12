import sys
from pathlib import Path

# Garante que o Python encontre a pasta 'src' ao rodar a partir da raiz
sys.path.append(str(Path(__file__).parent))

from src.graph import grafo

def rodar_chatbot():
    print("\n" + "="*50)
    print("🌾 AGROAVANTE S.A. - ASSISTENTE JURÍDICO & COMPLIANCE 🌾")
    print("Digite 'sair' para encerrar o atendimento.")
    print("="*50 + "\n")

    while True:
        pergunta = input("👤 Você: ")
        
        if pergunta.strip().lower() == 'sair':
            print("\n🤖 Assistente: Atendimento encerrado. Até logo!")
            break
            
        if not pergunta.strip():
            continue

        print("\n" + "-"*40)
        # Invoca o grafo passando a pergunta do usuário
        resultado_final = grafo.invoke({'pergunta': pergunta})
        
        # Exibe a resposta final gerada pelo nó que encerrou o fluxo
        print(f"\n🤖 Assistente:\n{resultado_final.get('resposta')}")
        
        # Se houver citações do RAG (documentos encontrados), exibe na tela
        citacoes = resultado_final.get('citacoes')
        if citacoes:
            print("\n📄 CITAÇÕES REGULATÓRIAS:")
            for c in citacoes:
                # Extrai metadados do documento carregado pelo PyMuPDF
                nome_doc = Path(c.metadata.get('source', 'desconhecido')).name
                pagina = c.metadata.get('page', 0) + 1
                print(f"  - Documento: {nome_doc} | Página: {pagina}")
                
        print("-"*40 + "\n")

if __name__ == "__main__":
    rodar_chatbot()