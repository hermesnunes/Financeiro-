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
