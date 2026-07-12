from langgraph.graph import StateGraph, START, END

from src.base_models import AgentState
from src.chains import executar_triagem, executar_rag

# --- DEFINIÇÃO DOS NÓS DO GRAFO ---

def node_triagem(state: AgentState) -> AgentState:
    print('🤖 Executando nó de triagem...')
    msg = state.get('mensagem') or state.get('pergunta')
    return {'triagem': executar_triagem(msg)}

def node_auto_resolver(state: AgentState) -> AgentState:
    print('🔍 Executando nó de auto resolver (RAG)...')
    resposta_rag = executar_rag(state['pergunta'])

    update: AgentState = {
        'resposta': resposta_rag['answer'],
        'citacoes': resposta_rag['citacoes'],
        'rag_sucesso': resposta_rag['contexto_encontrado'],
        'acao_final': 'AUTO_RESOLVER' if resposta_rag['contexto_encontrado'] else state.get('acao_final', '')
    }
    return update

def node_pedir_info(state: AgentState) -> AgentState:
    print('📝 Executando nó de pedir informações adicionais...')
    faltantes = state['triagem'].get('campos_faltantes', [])
    detalhe = ', '.join(faltantes) if faltantes else 'Tema e contexto específico'
    return {
        'resposta': f'Para avançar, preciso de detalhes sobre: {detalhe}',
        'citacoes': [],
        'acao_final': 'PEDIR_INFO'
    }

def node_abrir_chamado(state: AgentState) -> AgentState:
    print('⚖️ Executando nó de acionamento/abertura de chamado para o Jurídico...')
    triag = state['triagem']
    return {
        'resposta': f"Abrindo chamado com urgência {triag.get('urgencia', 'MEDIA')}. Descrição preliminar: {state['pergunta'][:140]}",
        'citacoes': [],
        'acao_final': 'ABRIR_CHAMADO'
    }

# --- REGRAS DE ROTEAMENTO (CONDITIONAL EDGES) ---

KEYWORDS_ABRIR_TICKET = ['aprovação', 'exceção', 'liberação', 'acesso especial', 'abrir ticket', 'abrir chamado', 'denúncia', 'denunciar']

def decidir_pos_triagem(state: AgentState) -> str:
    decisao = state['triagem']['decisao']
    if decisao == 'AUTO_RESOLVER': return 'auto'
    if decisao == 'PEDIR_INFO': return 'info'
    return 'chamado'

def decidir_pos_auto_resolver(state: AgentState) -> str:
    if state.get('rag_sucesso'):
        return 'ok'

    state_da_pergunta = (state.get('pergunta') or '').lower()
    if any(k in state_da_pergunta for k in KEYWORDS_ABRIR_TICKET):
        print('⚠️ RAG falhou, mas foram encontradas palavras-chave críticas. Encaminhando para Chamado...')
        return 'chamado'

    return 'info'

# --- MONTAGEM E COMPILAÇÃO DO WORKFLOW ---

workflow = StateGraph(AgentState)

# Adiciona os nós mapeados
workflow.add_node('triagem', node_triagem)
workflow.add_node('auto_resolver', node_auto_resolver)
workflow.add_node('pedir_info', node_pedir_info)
workflow.add_node('abrir_chamado', node_abrir_chamado)

# Conecta o fluxo
workflow.add_edge(START, 'triagem')
workflow.add_conditional_edges('triagem', decidir_pos_triagem, {
    'auto': 'auto_resolver',
    'info': 'pedir_info',
    'chamado': 'abrir_chamado'
})
workflow.add_conditional_edges('auto_resolver', decidir_pos_auto_resolver, {
    'info': 'pedir_info',
    'chamado': 'abrir_chamado',
    'ok': END
})
workflow.add_edge('pedir_info', END)
workflow.add_edge('abrir_chamado', END)

# Exporta o grafo compilado pronto para uso
grafo = workflow.compile()