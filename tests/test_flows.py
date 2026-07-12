import sys
from pathlib import Path

# Permite que o script de teste acesse o pacote 'src' localizado na pasta pai
sys.path.append(str(Path(__file__).parent.parent))

from src.graph import grafo

def executar_bateria_de_testes():
    # Cenários diversificados baseados na política de compliance do agro e PLD
    perguntas_teste = [
        "Qual é o site oficial para fazer uma denúncia anônima na empresa?",
        "Um fornecedor de Barter quer receber em uma conta de terceiro, o que faço?",
        "Quero uma exceção para aceitar um presente de R$ 500 de um produtor rural rural.",
        "Como funciona a triagem de fazendas quanto ao CAR e embargos do IBAMA?",
        "Preciso de ajuda com um contrato.",
        "Gostaria de abrir um chamado urgente para o compliance de lavagem de dinheiro."
    ]

    print("\n🧪 INICIANDO BATERIA DE TESTES AUTOMATIZADOS DO GRAFO 🧪")
    print("=" * 60)

    for i, pergunta in enumerate(perguntas_teste, 1):
        print(f"\n[Caso de Teste #{i}]")
        print(f"PERGUNTA: '{pergunta}'")
        
        # Execução do fluxo no LangGraph
        resposta_final = grafo.invoke({'pergunta': pergunta})
        triag = resposta_final.get('triagem', {})
        
        # Métricas de decisão tomadas pela IA corporativa
        print(f"📋 DECISÃO DE TRIAGEM: {triag.get('decisao')}")
        print(f"🚨 URGÊNCIA ATRIBUÍDA: {triag.get('urgencia')}")
        print(f"🎯 NÓ DE AÇÃO FINAL:  {resposta_final.get('acao_final')}")
        print(f"💬 RESPOSTA DA IA:\n{resposta_final.get('resposta')}")
        
        if resposta_final.get('citacoes'):
            print(f"📚 RAG: Buscou informações em {len(resposta_final.get('citacoes'))} trechos do PDF.")
            
        print("-" * 60)

if __name__ == "__main__":
    executar_bateria_de_testes()