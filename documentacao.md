# Documentação do Sistema Financeiro

## Visão Geral

O Sistema Financeiro é uma aplicação web completa para gerenciamento de fluxo de caixa, contas a pagar e contas a receber. Desenvolvido com tecnologias modernas, o sistema oferece uma interface intuitiva e recursos avançados para controle financeiro empresarial.

## Tecnologias Utilizadas

### Backend
- **Python 3.10** com **FastAPI** - Framework web de alta performance
- **SQLAlchemy** - ORM para interação com banco de dados
- **PostgreSQL** - Sistema de gerenciamento de banco de dados
- **Pydantic** - Validação de dados e configurações
- **Uvicorn** - Servidor ASGI para Python

### Frontend
- **React.js** - Biblioteca JavaScript para construção de interfaces
- **Material UI** - Biblioteca de componentes React
- **Recharts** - Biblioteca para criação de gráficos
- **Axios** - Cliente HTTP para requisições à API
- **React Router** - Gerenciamento de rotas no frontend

## Arquitetura do Sistema

O sistema segue uma arquitetura de aplicação web moderna, com separação clara entre frontend e backend:

### Estrutura do Backend (FastAPI)
```
backend/
├── app/
│   ├── core/
│   │   ├── config.py       # Configurações da aplicação
│   │   └── database.py     # Configuração do banco de dados
│   ├── crud/
│   │   ├── contas_pagar.py # Operações CRUD para contas a pagar
│   │   └── contas_receber.py # Operações CRUD para contas a receber
│   ├── models/
│   │   └── models.py       # Modelos de dados (SQLAlchemy)
│   ├── routes/
│   │   ├── contas_pagar.py # Rotas para contas a pagar
│   │   └── contas_receber.py # Rotas para contas a receber
│   ├── schemas/
│   │   └── schemas.py      # Schemas para validação (Pydantic)
│   └── main.py             # Ponto de entrada da aplicação
└── .env                    # Variáveis de ambiente
```

### Estrutura do Frontend (React)
```
frontend/
├── public/
│   └── index.html          # HTML base
├── src/
│   ├── components/
│   │   └── Layout.js       # Componente de layout principal
│   ├── pages/
│   │   ├── Dashboard.js    # Página de dashboard
│   │   ├── ContasReceber.js # Página de contas a receber
│   │   ├── ContasPagar.js  # Página de contas a pagar
│   │   └── Configuracoes.js # Página de configurações
│   ├── App.js              # Componente principal
│   └── index.js            # Ponto de entrada do React
└── package.json            # Dependências do projeto
```

## Funcionalidades Implementadas

### 1. Cadastro de Contas a Receber
- Registro de valores a receber
- Controle de datas (prevista e efetiva)
- Categorização por origem e cliente
- Gestão de status (pendente, recebido, atrasado)
- Registro de meio de pagamento

### 2. Cadastro de Contas a Pagar
- Registro de valores a pagar
- Controle de datas de vencimento e pagamento
- Categorização por destino
- Gestão de status (pendente, pago, atrasado)
- Registro de meio de pagamento

### 3. Dashboard Financeiro
- Resumo de valores a pagar e receber
- Saldo projetado
- Gráfico de fluxo de caixa mensal
- Gráfico de status das contas
- Gráfico de distribuição financeira

### 4. Recursos Complementares
- Exportação de dados (CSV, Excel, PDF)
- Configuração de alertas para vencimentos
- Lançamentos recorrentes

## Banco de Dados

O sistema utiliza PostgreSQL como banco de dados relacional. As principais tabelas são:

- **contas_receber**: Armazena informações sobre contas a receber
- **contas_pagar**: Armazena informações sobre contas a pagar
- **funcionarios**: Armazena informações sobre funcionários (preparado para implementação futura)
- **impostos**: Armazena informações sobre impostos (preparado para implementação futura)

## API REST

O backend expõe uma API REST com os seguintes endpoints principais:

### Contas a Receber
- `GET /api/contas-receber/` - Lista todas as contas a receber
- `GET /api/contas-receber/{id}` - Obtém uma conta a receber específica
- `POST /api/contas-receber/` - Cria uma nova conta a receber
- `PUT /api/contas-receber/{id}` - Atualiza uma conta a receber existente
- `DELETE /api/contas-receber/{id}` - Remove uma conta a receber

### Contas a Pagar
- `GET /api/contas-pagar/` - Lista todas as contas a pagar
- `GET /api/contas-pagar/{id}` - Obtém uma conta a pagar específica
- `POST /api/contas-pagar/` - Cria uma nova conta a pagar
- `PUT /api/contas-pagar/{id}` - Atualiza uma conta a pagar existente
- `DELETE /api/contas-pagar/{id}` - Remove uma conta a pagar

## Guia de Uso

### Acessando o Sistema
O sistema está disponível através dos seguintes links:

- **Frontend**: https://5173-i5tg5z62jxwof3a8q2fm8-6f1212ed.manus.computer
- **API**: https://8000-i5tg5z62jxwof3a8q2fm8-6f1212ed.manus.computer

### Navegação
- O menu lateral permite navegar entre as diferentes seções do sistema
- A página inicial apresenta o Dashboard com resumo financeiro
- As páginas de Contas a Receber e Contas a Pagar permitem gerenciar os respectivos lançamentos
- A página de Configurações oferece acesso a recursos complementares

### Gerenciando Contas a Receber/Pagar
1. Acesse a página correspondente através do menu lateral
2. Para adicionar uma nova conta, clique no botão "Nova Conta"
3. Preencha o formulário com as informações necessárias
4. Para editar uma conta existente, clique no ícone de edição na tabela
5. Para excluir uma conta, clique no ícone de exclusão na tabela

### Utilizando o Dashboard
- Visualize o resumo financeiro nos cards superiores
- Alterne entre os diferentes gráficos usando as abas
- Os gráficos são interativos e exibem informações detalhadas ao passar o mouse

## Implantação em Produção

Para uma implantação permanente em ambiente de produção, recomendamos:

### Backend (FastAPI)
1. Escolha um provedor de nuvem (AWS, DigitalOcean, Azure, etc.)
2. Configure um servidor com PostgreSQL
3. Implante o backend usando Docker ou diretamente no servidor
4. Configure variáveis de ambiente para produção
5. Configure um servidor web (Nginx, Apache) como proxy reverso

### Frontend (React)
1. Execute `pnpm build` para gerar os arquivos estáticos otimizados
2. Hospede os arquivos em um serviço de hospedagem estática (Netlify, Vercel, AWS S3)
3. Configure o domínio e HTTPS

### Segurança
Para ambiente de produção, recomenda-se implementar:
- Autenticação de usuários
- Controle de acesso baseado em funções
- HTTPS para todas as comunicações
- Backup regular do banco de dados

## Próximos Passos e Melhorias Futuras

O sistema foi desenvolvido com base nos requisitos prioritários, mas pode ser expandido com:

1. **Módulo de Funcionários**
   - Cadastro completo de funcionários
   - Controle de pagamentos de salários
   - Histórico de pagamentos

2. **Módulo de Impostos**
   - Cadastro de obrigações fiscais
   - Alertas de vencimento
   - Histórico de pagamentos

3. **Integrações**
   - Integração com APIs bancárias para conciliação automática
   - Integração com sistemas de emissão de notas fiscais
   - Exportação para sistemas contábeis

4. **Relatórios Avançados**
   - Relatórios gerenciais customizáveis
   - Análises preditivas de fluxo de caixa
   - Exportação em múltiplos formatos

## Suporte e Manutenção

Para suporte técnico, manutenção ou desenvolvimento de novas funcionalidades, entre em contato com a equipe de desenvolvimento.

---

Documentação elaborada em 28 de abril de 2025.
