import os
from fpdf import FPDF

# Garante que a pasta PDF exista no seu projeto
os.makedirs("PDF", exist_ok=True)

texto_politica = """RF_Projetos S.A.
POLÍTICA DE COMPLIANCE, BOA GOVERNANÇA CORPORATIVA E PREVENÇÃO A ILÍCITOS

1. OBJETIVO E ESCOPO
Esta Política de Compliance estabelece as diretrizes de integridade, transparência e governança corporativa aplicáveis a todos os colaboradores, diretores, conselheiros, fornecedores e parceiros comerciais da RF_Projetos S.A. Nosso compromisso é garantir a conformidade legal em toda a cadeia produtiva do agronegócio, mitigando riscos reputacionais, regulatórios e financeiros institucionais.

2. CONFORMIDADE LEGAL E COMBATE À CORRUPÇÃO
A RF_Projetos S.A. adota o princípio de tolerância zero contra qualquer forma de corrupção ou suborno, em estrita conformidade com os ditames da Lei nº 12.846/2013 (Lei Anticorrupção Brasileira). É terminantemente proibido prometer, oferecer ou dar, direta ou indiretamente, qualquer vantagem indevida a agente público ou a terceiros a ele relacionados.

As interações ordinárias com qualquer agente público, o que inclui, mas não se limita aos fiscais agropecuários do Ministério da Agricultura e Pecuária (MAPA), auditores fiscais da Receita Federal e agentes de órgãos de licenciamento ambiental (IBAMA e autarquias estaduais), devem ser pautadas pela estrita transparência, formalidade e legalidade, sendo obrigatório o registro em ata ou sistema de qualquer reunião agendada.

3. PREVENÇÃO À LAVAGEM DE DINHEIRO 
Em estrita conformidade com a Lei nº 9.613/1998 e com as diretrizes normativas do Conselho de Controle de Atividades Financeiras (COAF), a RF_Projetos S.A. mantém uma postura rigorosa de monitoramento financeiro sobre as operações mercantis de alta liquidez inerentes ao setor produtivo, tais como a comercialização de commodities e operações de financiamento agrícola (CPR e Barter).

Constituem sinais de alerta e gatilhos obrigatórios de reporte imediato ao Departamento Jurídico as seguintes irregularidades e condutas operacionais:

* Solicitações de liquidação financeira de transações ou contratos de Barter por meio de contas bancárias de terceiros que não possuam vínculo jurídico ou comercial formalizado com a operação original;
* Propostas de adimplemento ou pagamentos fracionados em espécie (dinheiro vivo) para a aquisição de insumos, maquinários ou grãos;
* Recusa injustificada na entrega de informações cadastrais ou inconsistências graves identificadas nos procedimentos obrigatórios de Due Diligence e Know Your Customer (KYC - Conheça seu Cliente);
* Operações comerciais cujos montantes negociados sejam técnica e flagrantemente incompatíveis com a capacidade econômico-financeira presumida ou com o patrimônio declarado da contraparte rural.

4. PROTOCOLO DE ACIONAMENTO DO DEPARTAMENTO JURÍDICO
O Departamento Jurídico da RF_Projetos S.A. deve ser formalmente acionado de maneira imediata por meio do canal eletrônico institucional prioritário sempre que identificados indícios mínimos, materialidade suspeita ou evidências de práticas ilícitas financeiras, fiscais ou ambientais.

DEVER DE SIGILO (ANTI TIPPING-OFF): É expressamente vedado a qualquer colaborador dar ciência direta ou indireta ao investigado, cliente, fornecedor ou terceiros estranhos à investigação de que uma atividade suspeita foi reportada ao Departamento Jurídico ou está sob análise confidencial. A violação deste dever configura falta grave para fins de rescisão por justa causa e responsabilização civil.

Uma vez formalizado o acionamento, o Departamento Jurídico avaliará a admissibilidade da suspeita em até 48 horas úteis, determinando, se cabível, a abertura de Processo Administrativo de Investigação Interna, com livre acesso aos sistemas corporativos, e posterior envio de relatório ao Comitê de Ética e autoridades administrativas competentes (incluindo o COAF, se constatada a lavagem de dinheiro).

5. COMPLIANCE AMBIENTAL E SUSTENTABILIDADE (ESG)
O agronegócio exige responsabilidade socioambiental rigorosa. A RF_Projetos S.A. exige a devida diligência (due diligence) e veda veementemente a aquisição de matéria-prima ou grãos de propriedades agrícolas que possuam embargos ambientais ativos emitidos pelo IBAMA ou órgãos estaduais congêneres. Adicionalmente, é proibida a homologação de parceiros rurais em áreas de desmatamento ilegal ou que sobreponham Terras Indígenas e Unidades de Conservação demarcadas. Todos os imóveis rurais parceiros devem apresentar o Cadastro Ambiental Rural (CAR) regularizado e ativo.

6. DIREITOS HUMANOS E RELAÇÕES TRABALHISTAS
A companhia atua ativamente no combate e erradicação de qualquer prática análoga à escravidão ou exploração de trabalho infantil em suas operações ou na respectiva cadeia de fornecedores. Consultas periódicas à "Lista Suja do Trabalho Escravo" do Governo Federal são obrigatórias antes da celebração de qualquer contrato comercial ou de logística rústica.

7. POLÍTICA DE BRINDES, PRESENTES E HOSPITALIDADE
Para mitigar potenciais conflitos de interesse, os colaboradores não podem aceitar ou oferecer presentes, entretenimento ou vantagens de parceiros comerciais que excedam o valor comercial de R$ 150,00. Qualquer exceção de hospitalidade corporativa para dias de campo ou feiras agrícolas deve ser previamente aprovada e registrada pela Diretoria de Compliance com antecedência mínima de 5 dias úteis.

8. PROTEÇÃO DE DADOS PESSOAIS E PRIVACIDADE (LGPD)
Em estrita observância à Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018), a RF_Projetos S.A. assegura que todo tratamento de dados pessoais realizado no âmbito de suas atividades de compliance — incluindo investigações internas, processos de Due Diligence, homologação de fornecedores e gestão do Canal de Denúncias — é pautado pelos princípios da finalidade, necessidade e minimização. As informações coletadas restringem-se ao estritamente essencial para o cumprimento de obrigações legais, regulatórias e mitigação de riscos corporativos. A companhia garante a confidencialidade e a segurança da informação dos titulares, e qualquer compartilhamento de dados com autoridades competentes ou auditorias externas ocorrerá exclusivamente mediante base legal adequada.

9. CANAL DE DENÚNCIAS OFICIAL 
A RF_Projetos S.A. disponibiliza os seguintes canais oficiais, confidenciais e seguros para o recebimento de denúncias de fraudes, lavagem de dinheiro ou desvios éticos:

* Portal de Denúncias na Web: www.denuncias.rfprojetos.com.br
* E-mail do Comitê de Ética: comite.etica@rfprojetos.com.br

Departamento Jurídico e Recursos Humanos"""

# Configuração do documento
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=11)

# Escreve as linhas no PDF tratando os caracteres especiais do português
for linha in texto_politica.split('\n'):
    linha_formatada = linha.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 6, txt=linha_formatada)

# Define o caminho de salvamento e exporta
caminho_arquivo = "PDF/politica_compliance_agro.pdf"
pdf.output(caminho_arquivo)

print(f"✅ Operação concluída! O arquivo foi substituído em: {caminho_arquivo}")