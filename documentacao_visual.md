# Documentação Visual do Sistema Financeiro (Mockups)

**Introdução:**

Devido a instabilidades técnicas temporárias com o ambiente de demonstração ao vivo, esta documentação apresenta mockups de alta fidelidade das principais telas do Sistema Financeiro. Estes mockups descrevem detalhadamente o design, layout, componentes e funcionalidades implementadas, permitindo uma visualização clara do sistema finalizado.

---




## 1. Dashboard

# Mockup de Alta Fidelidade - Dashboard

**Título da Página:** Dashboard Financeiro

**Layout Geral:**
- Barra de navegação superior com o título "Sistema Financeiro" e um ícone de menu.
- Menu lateral esquerdo (persistente ou recolhível) com links para: Dashboard, Contas a Receber, Contas a Pagar, Funcionários, Impostos, Configurações.
- Área de conteúdo principal à direita.

**Conteúdo Principal:**

1.  **Título:** "Dashboard Financeiro" (Typography h5)

2.  **Cards de Resumo (Grid com 4 colunas):**
    *   **Card 1:**
        *   Título: "Total a Receber"
        *   Valor: Exibido em formato de moeda (ex: R$ 15.000,00), cor primária (azul).
    *   **Card 2:**
        *   Título: "Total a Pagar"
        *   Valor: Exibido em formato de moeda (ex: R$ 8.500,00), cor de erro (vermelho).
    *   **Card 3:**
        *   Título: "Saldo Projetado"
        *   Valor: Exibido em formato de moeda (ex: R$ 6.500,00), cor primária (azul) se positivo, cor de erro (vermelho) se negativo.
    *   **Card 4:**
        *   Título: "Contas Pendentes/Atrasadas"
        *   Valor: Exibido como "X / Y" (ex: 12 / 3), onde X é o número de contas pendentes e Y o número de contas atrasadas.

3.  **Área de Gráficos (Paper com abas):**
    *   **Abas:** "Fluxo de Caixa", "Status das Contas", "Distribuição"
    *   **Conteúdo da Aba "Fluxo de Caixa":**
        *   Título: "Fluxo de Caixa Mensal"
        *   Gráfico: Gráfico de barras (BarChart) responsivo.
        *   Eixo X: Meses do ano (Jan, Fev, Mar, ...)
        *   Eixo Y: Valores em moeda.
        *   Barras: Duas barras por mês, uma para "A Receber" (verde) e outra para "A Pagar" (vermelho).
        *   Tooltip: Exibe os valores exatos ao passar o mouse.
        *   Legenda: Indica as cores para "A Receber" e "A Pagar".
    *   **Conteúdo da Aba "Status das Contas":**
        *   Título: "Status das Contas"
        *   Gráfico: Gráfico de barras (BarChart) responsivo.
        *   Eixo X: Status ("Pendente", "Concluído", "Atrasado")
        *   Eixo Y: Número de contas.
        *   Barras: Duas barras por status, uma para "Contas a Receber" (verde) e outra para "Contas a Pagar" (vermelho).
        *   Tooltip: Exibe os números exatos ao passar o mouse.
        *   Legenda: Indica as cores para "Contas a Receber" e "Contas a Pagar".
    *   **Conteúdo da Aba "Distribuição":**
        *   Título: "Distribuição Financeira"
        *   Gráfico: Gráfico de pizza (PieChart) responsivo.
        *   Fatias: Duas fatias, uma para "A Receber" (verde) e outra para "A Pagar" (vermelho).
        *   Labels: Exibem o nome e a porcentagem de cada fatia (ex: "A Receber: 64%").
        *   Tooltip: Exibe os valores exatos em moeda ao passar o mouse.

---




## 2. Contas a Receber

# Mockup de Alta Fidelidade - Contas a Receber

**Título da Página:** Contas a Receber

**Layout Geral:**
- Barra de navegação superior e menu lateral (conforme Dashboard).
- Área de conteúdo principal.

**Conteúdo Principal:**

1.  **Título:** "Contas a Receber" (Typography h5)

2.  **Barra de Ações (acima da tabela):**
    *   **Botão "Nova Conta"**: Botão (variant="contained", color="primary") para abrir o diálogo de criação.
    *   **Filtros:**
        *   Campo de texto para busca por cliente ou origem.
        *   Dropdown (Select) para filtrar por status (Todos, Pendente, Recebido, Atrasado).
        *   Seletores de data (DatePicker) para filtrar por período (Data Inicial, Data Final).
        *   Botão "Aplicar Filtros".

3.  **Tabela de Contas a Receber (TableContainer, Table):**
    *   **Cabeçalho (TableHead):**
        *   Colunas: ID, Cliente, Origem, Valor, Data Prevista, Data Recebimento, Status, Ações.
    *   **Corpo (TableBody):**
        *   Linhas (TableRow) representando cada conta.
        *   Células (TableCell) com os dados da conta.
        *   Coluna "Status": Exibido com um chip colorido (ex: Verde para Recebido, Amarelo para Pendente, Vermelho para Atrasado).
        *   Coluna "Ações": Ícones (IconButton) para Editar (EditIcon) e Excluir (DeleteIcon).
    *   **Paginação (TablePagination):** Controles para navegar entre as páginas da tabela.

4.  **Diálogo de Criação/Edição de Conta (Dialog):**
    *   **Título:** "Nova Conta a Receber" ou "Editar Conta a Receber".
    *   **Campos do Formulário (TextField, Select, DatePicker):**
        *   Cliente (String)
        *   Origem (String)
        *   Valor (Float, com formatação de moeda)
        *   Data Prevista (Date)
        *   Data Recebimento (Date, opcional)
        *   Descrição (Text, multiline)
        *   Meio de Pagamento (Select: PIX, Boleto, Cartão, Dinheiro, Transferência)
        *   Conta de Recebimento (String, opcional)
        *   Status (Select: Pendente, Recebido, Atrasado)
        *   Comprovante (Input para upload de arquivo, opcional)
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Salvar" (variant="contained", color="primary").

5.  **Diálogo de Confirmação de Exclusão (Dialog):**
    *   **Título:** "Confirmar Exclusão"
    *   **Mensagem:** "Tem certeza que deseja excluir esta conta a receber?"
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Excluir" (variant="contained", color="error").

6.  **Notificações (Snackbar):** Mensagens de sucesso ou erro após criar, editar ou excluir uma conta.

---




## 3. Contas a Pagar

# Mockup de Alta Fidelidade - Contas a Pagar

**Título da Página:** Contas a Pagar

**Layout Geral:**
- Barra de navegação superior e menu lateral (conforme Dashboard).
- Área de conteúdo principal.

**Conteúdo Principal:**

1.  **Título:** "Contas a Pagar" (Typography h5)

2.  **Barra de Ações (acima da tabela):**
    *   **Botão "Nova Conta"**: Botão (variant="contained", color="primary") para abrir o diálogo de criação.
    *   **Filtros:**
        *   Campo de texto para busca por destino ou descrição.
        *   Dropdown (Select) para filtrar por status (Todos, Pendente, Pago, Atrasado).
        *   Seletores de data (DatePicker) para filtrar por período de vencimento (Data Inicial, Data Final).
        *   Botão "Aplicar Filtros".

3.  **Tabela de Contas a Pagar (TableContainer, Table):**
    *   **Cabeçalho (TableHead):**
        *   Colunas: ID, Destino, Descrição, Valor, Data Vencimento, Data Pagamento, Status, Ações.
    *   **Corpo (TableBody):**
        *   Linhas (TableRow) representando cada conta.
        *   Células (TableCell) com os dados da conta.
        *   Coluna "Status": Exibido com um chip colorido (ex: Verde para Pago, Amarelo para Pendente, Vermelho para Atrasado).
        *   Coluna "Ações": Ícones (IconButton) para Editar (EditIcon) e Excluir (DeleteIcon).
    *   **Paginação (TablePagination):** Controles para navegar entre as páginas da tabela.

4.  **Diálogo de Criação/Edição de Conta (Dialog):**
    *   **Título:** "Nova Conta a Pagar" ou "Editar Conta a Pagar".
    *   **Campos do Formulário (TextField, Select, DatePicker):**
        *   Destino (String)
        *   Descrição (Text, multiline)
        *   Valor (Float, com formatação de moeda)
        *   Data Vencimento (Date)
        *   Data Pagamento (Date, opcional)
        *   Meio de Pagamento (Select: PIX, Boleto, Cartão, Dinheiro, Transferência)
        *   Conta de Pagamento (String, opcional)
        *   Status (Select: Pendente, Pago, Atrasado)
        *   Comprovante (Input para upload de arquivo, opcional)
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Salvar" (variant="contained", color="primary").

5.  **Diálogo de Confirmação de Exclusão (Dialog):**
    *   **Título:** "Confirmar Exclusão"
    *   **Mensagem:** "Tem certeza que deseja excluir esta conta a pagar?"
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Excluir" (variant="contained", color="error").

6.  **Notificações (Snackbar):** Mensagens de sucesso ou erro após criar, editar ou excluir uma conta.

---




## 4. Configurações

# Mockup de Alta Fidelidade - Configurações

**Título da Página:** Configurações e Recursos Adicionais

**Layout Geral:**
- Barra de navegação superior e menu lateral (conforme Dashboard).
- Área de conteúdo principal.

**Conteúdo Principal:**

1.  **Título:** "Configurações e Recursos Adicionais" (Typography h5)

2.  **Grid de Opções (Grid container spacing={3}):**
    *   **Item 1 (Grid item xs={12} md={6}):**
        *   **Card (Paper):**
            *   Título: "Exportação de Dados" (Typography h6)
            *   Descrição: "Exporte seus dados financeiros para análise em outras ferramentas ou para backup." (Typography body1)
            *   Botão: "Exportar Dados" (variant="contained", startIcon=<FileDownloadIcon />) - Abre o diálogo de exportação.
    *   **Item 2 (Grid item xs={12} md={6}):**
        *   **Card (Paper):**
            *   Título: "Configuração de Alertas" (Typography h6)
            *   Descrição: "Configure alertas para vencimentos, recebimentos e atrasos." (Typography body1)
            *   Botão: "Configurar Alertas" (variant="contained", startIcon=<NotificationsIcon />) - Abre o diálogo de alertas.
    *   **Item 3 (Grid item xs={12}):**
        *   **Card (Paper):**
            *   Título: "Lançamentos Recorrentes" (Typography h6)
            *   Descrição: "Configure lançamentos que se repetem automaticamente todos os meses, como aluguel, salários e assinaturas." (Typography body1)
            *   **Tabela (TableContainer, Table):**
                *   Cabeçalho: Descrição, Tipo, Valor, Dia do Mês, Status.
                *   Corpo: Mensagem "Nenhum lançamento recorrente configurado" ou linhas com dados.
            *   Botão: "Adicionar Lançamento Recorrente" (variant="contained", color="primary").

3.  **Diálogo de Exportação de Dados (Dialog):**
    *   **Título:** "Exportar Dados"
    *   **Campos (FormControl, Select):**
        *   Tipo de Dados (Contas a Receber, Contas a Pagar, Fluxo de Caixa, Todos)
        *   Formato (CSV, Excel, PDF)
        *   Período (Mês Atual, Mês Anterior, Trimestre, Ano, Todos)
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Exportar" (variant="contained", color="primary").

4.  **Diálogo de Configuração de Alertas (Dialog):**
    *   **Título:** "Configurar Alertas"
    *   **Campos (TextField, Select):**
        *   Dias de Antecedência para Alertas (Number)
        *   Notificar Vencimentos (Sim/Não)
        *   Notificar Recebimentos (Sim/Não)
        *   Notificar Atrasos (Sim/Não)
    *   **Ações (DialogActions):**
        *   Botão "Cancelar".
        *   Botão "Salvar" (variant="contained", color="primary").

5.  **Notificações (Snackbar):** Mensagens de sucesso após exportar dados ou salvar configurações de alertas.

---

