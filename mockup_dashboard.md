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
