# Assistente de Compliance e Prevenção a Ilícitos no Agronegócio

## Visão Geral do Projeto
Este projeto consiste no desenvolvimento de um assistente virtual inteligente e automatizado para suporte a políticas de compliance corporativo e prevenção à lavagem de dinheiro (PLD), focado nas particularidades e exigências regulatórias do setor do agronegócio. O sistema utiliza técnicas avançadas de processamento de linguagem natural e arquitetura de agentes para triar, buscar e responder a consultas complexas baseadas estritamente em documentações institucionais e conformidades legais.

---

## Arquitetura e Fluxo do Sistema
O motor do assistente foi desenvolvido de forma modular e desacoplada, abandonando os scripts lineares tradicionais e adotando uma estrutura baseada em grafos de estado. O fluxo operacional é dividido em três etapas principais:

* **Módulo de Triagem Estruturada:** A mensagem enviada pelo usuário é inicialmente interceptada por um modelo de linguagem configurado para validação de dados via Pydantic. Esse módulo classifica a intenção em categorias operacionais predefinidas e atribui dinamicamente o nível de urgência do atendimento.
* **Módulo de Recuperação de Informação (RAG):** Caso a demanda exija uma consulta normativa, o sistema aciona um banco de dados vetorial local. Os documentos institucionais em formato PDF são segmentados em partições de texto e indexados em memória através de algoritmos de busca por similaridade. A resposta é gerada combinando o contexto recuperado ao modelo de linguagem de forma restrita, eliminando o risco de alucinações.
* **Orquestração e Roteamento:** Utilizando uma estrutura de grafo de estado, o sistema gerencia as transições entre os nós de atendimento. Caso a busca por similaridade falhe ou sejam detectadas palavras-chave críticas associadas a ilícitos financeiros, o fluxo é automaticamente desviado para o protocolo de acionamento emergencial e abertura de chamados para o Departamento Jurídico.

---

## Tecnologias e Ferramentas Utilizadas
* **Linguagem de Programação:** Python para o desenvolvimento de toda a lógica de microsserviços, manipulação de arquivos e estruturação das funções.
* **Orquestração de Agentes:** LangGraph para a criação dos nós de decisão, gerenciamento de estados internos e regras de transição condicional do fluxo de atendimento.
* **Processamento de Linguagem Natural e RAG:** LangChain para a estruturação de prompts e conexões com modelos de inteligência artificial via LangChain Expression Language (LCEL).
* **Banco de Dados Vetorial:** FAISS para o armazenamento de vetores em memória e execução de buscas semânticas eficientes por similaridade de alta performance.
* **Modelos de Linguagem e Embeddings:** Modelos da família Gemini integrados via Google GenAI para geração de respostas textuais e conversão de documentos em embeddings matemáticos.
* **Validação de Dados:** Pydantic para a tipagem rigorosa de dados e garantia de que as saídas do modelo de inteligência artificial respeitem formatos JSON estritos para consumo do sistema.