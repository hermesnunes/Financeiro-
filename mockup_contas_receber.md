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
