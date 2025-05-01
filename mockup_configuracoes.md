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
