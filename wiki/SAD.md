# Documento de Arquitetura de Software (SAD) para Website de Portfólio Pessoal

## 1. Introdução

### 1.1 Propósito

Este Documento de Arquitetura de Software (SAD) descreve a arquitetura de um website de portfólio pessoal projetado para exibir artigos, projetos, informações pessoais, métricas e detalhes de contato. O sistema suporta gerenciamento dinâmico de projetos e artigos. Este documento fornece uma visão geral da estrutura, componentes e decisões de design do sistema para guiar o desenvolvimento e a manutenção.

### 1.2 Escopo

O website é uma aplicação web construída com Django para o backend e HTML, CSS e JavaScript para o frontend. Inclui:

- Uma página inicial com resumos de artigos, projetos e informações pessoais.
- Seções para listar artigos, detalhes de artigos e projetos.
- Uma seção "Sobre" com resumos, experiencias e métricas.
- Uma arquitetura modular e escalável para suportar o gerenciamento de conteúdo e a interação do usuário.

### 1.3 Definições, Acrônimos e Abreviações

- **SAD**: Software Architecture Document (Documento de Arquitetura de Software)
- **Django**: Framework web baseado em Python para desenvolvimento de backend
- **ORM**: Object-Relational Mapping (Mapeamento Objeto-Relacional - camada de abstração de banco de dados do Django)
- **MVC**: Model-View-Controller (Modelo-Visão-Controlador - padrão arquitetural do Django, adaptado como MTV: Model-Template-View)
- **CRUD**: Create, Read, Update, Delete (Criar, Ler, Atualizar, Excluir operações)
- **REST**: Representational State Transfer (para potenciais endpoints de API)
- **WCAG**: Web Content Accessibility Guidelines (Diretrizes de Acessibilidade de Conteúdo Web)

### 1.4 Referências

- Especificação de Requisitos de Software (SRS) para Website de Portfólio Pessoal (artifact_id: 694986fc-d32c-4f9a-9f39-dac5f85e80ee)

---

## 2. Metas e Restrições Arquiteturais

### 2.1 Metas

- **Modularidade**: Separar as preocupações entre a lógica de backend, a apresentação de frontend e o armazenamento de dados para facilitar a manutenção.
- **Escalabilidade**: Suportar o aumento do tráfego e do crescimento de conteúdo com mínima degradação de desempenho.
- **Usabilidade**: Fornecer uma interface de usuário responsiva e acessível em todos os dispositivos.
- **Segurança**: Proteger contra vulnerabilidades web comuns (por exemplo, XSS, CSRF) e garantir o gerenciamento seguro de conteúdo.
- **Manutenibilidade**: Garantir um código limpo e documentado com uma clara separação de preocupações.

### 2.2 Restrições

- Usar Django para o desenvolvimento de backend com um banco de dados relacional (SQLite para desenvolvimento, PostgreSQL para produção).
- Frontend limitado a Template Django, HTML, CSS e JavaScript "puro".
- Conformidade com WCAG 2.1 para acessibilidade.
- Implantação em plataformas de nuvem (por exemplo, Heroku, AWS, Render) com aplicação de HTTPS.

---

## 3. Visão Geral da Arquitetura do Sistema

### 3.1 Padrão Arquitetural

O sistema segue o padrão **Model-Template-View (MTV)**, adaptação do MVC pelo Django:

- **Model (Modelo)**: Gerencia dados e lógica de negócio (por exemplo, modelos `Article`, `Project`, `Comment`).
- **Template (Template)**: Lida com a lógica de apresentação usando HTML/CSS/JavaScript.
- **View (Visão)**: Gerencia o tratamento de requisições e a geração de respostas, conectando modelos a templates.

Este padrão garante uma clara separação de preocupações, com o ORM do Django gerenciando as interações com o banco de dados e os templates fornecendo um frontend flexível.

### 3.2 Pilha Tecnológica

- **Backend**: Django (Python 3.12) com Django ORM para gerenciamento de banco de dados.
- **Banco de Dados**: SQLite (desenvolvimento), PostgreSQL (produção).
- **Frontend**: HTML5, CSS3, JavaScript (puro).
- **Estilização**: CSS personalizado para design responsivo.
- **Implantação**: Plataforma de nuvem (por exemplo, Heroku, AWS Elastic Beanstalk, Render) com Gunicorn como servidor WSGI.
- **Segurança**: Recursos de segurança embutidos do Django (proteção CSRF, prevenção XSS) e HTTPS.
- **APIs Opcionais**: Integração com APIs do GitHub para dados de perfil dinâmicos (se necessário).

### 3.3 Componentes do Sistema

O sistema está dividido nos seguintes componentes:

1. **Backend (Django)**:
    - **Modelos**: Definem estruturas de dados para artigos, projetos, categorias, comentários e perfis de usuário.
    - **Views**: Lidam com requisições HTTP e renderizam templates ou retornam JSON (para possivel REST API).
    - **URLs**: Rotas que direcionam requisições para as views apropriadas.
    - **Interface Administrativa**: Django admin para gerenciamento de conteúdo e Meta dados dos modelos (artigos, projetos, comentários, categorias).
2. **Frontend**:
    - **Templates**: Arquivos HTML com linguagem de template Django incorporada para conteúdo dinâmico.
    - **Arquivos Estáticos**: CSS para estilização, JavaScript para interatividade (por exemplo, barra de navagação oculta com botão, marquee slider icons de tecnologia).
    - **Design Responsivo**: Abordagem mobile-first com media queries.
3. **Banco de Dados**: Banco de dados relacional gerenciado pelo Django ORM, armazenando conteúdo e interações do usuário.
4. **Integrações Externas**: Links para GitHub ou outros perfis; possíveis chamadas de API para dados dinâmicos.
    
    ![ComponentDiagram.svg](attachment:b3b8bef4-98a2-42a0-b882-685db5b5f308:ComponentDiagram.svg)
    

---

## 4. View Arquitetura

### 4.1 View Lógica

A view lógica descreve os principais componentes e suas interações:

- **Modelos**:
    - `User`: Armazena dados do proprietário e, opcionalmente, de visitantes (para comentários autenticados, modelo reutilizado do django).
    - `Article`: Armazena dados de artigos (título, corpo, categorias, data de publicação, autor).
    - `Project`: Armazena dados de projetos (título, resumo, descrição, documentação, miniatura, categorias, data de publicação, autor).
    - `Comment`: Armazena dados de comentários (conteúdo, nome do autor, data de publicação, artigo/projeto).
    - `Category`: Categoria sobre o assunto dos projetos e artigos.
- **Views**:
    - View da Página Inicial: Busca artigos recentes, projetos.
    - Views de Artigos: Views de lista para artigos com paginator.
    - Views de Detalhes de Artigo: Views para conteudo do artigo.
    - Views de Projetos: Views para documentação do projetos.
    - Views "Sobre/Contato": Exibem dados de perfil estáticos ou dinâmicos.
- **Templates**:
    - `base.html`: Template base com cabeçalho, rodapé e navegação.
    - `index.html`: Página inicial com seção de herói e módulos de resumo.
    - `article_list.html`, `article_detail.html`: Páginas de listagem e detalhes de artigos.
    - `project_list.html`, `project_detail.html`: Páginas de listagem e detalhes de projetos.
    - `about.html`, `contact.html`: Páginas "Sobre" e de contato.

### 4.2 Vista de Dados

O esquema do banco de dados é gerenciado pelo Django ORM:

- **Tabelas**:
    - `auth_user`: Tabela de usuário embutida do Django para autenticação do proprietário.
    - `articles_article`: Armazena dados de artigos (id, título, texto, data de publicação, categorias, autor).
    - `projects_project`: Armazena dados de projetos (id, título, resumo, texto, documentação, imagens, autor).
    - `comments_comment`: Armazena dados de comentários (conteúdo, autor, data de publicação, id do artigo/projeto).
    - `categoryes_category`: Categoria sobre o assunto dos projetos e artigos (nome).
- **Relacionamentos**:
    - Um-Obrigatório-para-Muitos-Opcionais: `Article`/`Project` para `Comment`.
    - Muitos-Opcionais-para-Um-Obrigatorio: `Comment` para `User`.
    - Um-Opcional-para-Muitos-Opcionais: `Category` para `Article`/`Project`
    - Um-Obrigatório-para-Muitos-Opcionais: `User` para `Project`/`Article`

![ERDiagram.svg](attachment:90ab4106-2024-4651-b892-d23af8a0175b:ERDiagram.svg)

## Diagrama de Entidade de Relacionamento

### 4.3 View de Processo

O fluxo de processo para as principais interações:

1. **Carregamento da Página Inicial**:
    - O cliente envia uma requisição HTTP GET para `/`.
    - A view do Django consulta artigos recentes e projetos.
    - O template renderiza a seção de herói, módulos de resumo e rodapé.
2. **Visualização de Artigo/Projeto**:
    - O cliente navega para `/articles`, `/articles/<id>` ou `/projects/<id>`.
    - A view busca o artigo/projeto via paginator ou não.
    - O template renderiza o conteúdo.
3. **Gerenciamento de Conteúdo**:
    - O proprietário faz login no Django admin ou interface personalizada.
    - Realiza operações CRUD em artigos, e projetos.

![SequencialDiagram.svg](attachment:a33ca9cd-5f47-49cf-88af-fa5a752b8c9d:SequencialDiagram.svg)

### 4.4 View de Implantação

- **Ambiente de Desenvolvimento**:
    - Configuração local com o servidor de desenvolvimento do Django e SQLite.
    - Arquivos estáticos servidos diretamente pelo Django.
- **Ambiente de Produção**:
    - Implantado em uma plataforma de nuvem (por exemplo, Heroku, AWS).
    - Gunicorn como servidor WSGI, Nginx como proxy reverso.
    - PostgreSQL para o banco de dados.
    - Arquivos estáticos hospedados em CDN ou armazenamento em nuvem (por exemplo, AWS S3).
    - HTTPS aplicado via certificados SSL/TLS.

![ImplantationDiagram.svg](attachment:316eb63b-19fc-4241-be02-723a09ba5904:ImplantationDiagram.svg)

---

## 5. Decisões de Design

### 5.1 Framework Backend

- **Decisão**: Usar Django por seu ORM robusto, recursos de segurança e interface de administração.
- **Justificativa**: O Django simplifica o desenvolvimento de backend, fornece segurança embutida (proteção CSRF, filtragem XSS) e suporta o gerenciamento rápido de conteúdo via painel de administração. Além de ser um framework python sendo a stack principal.

### 5.2 Banco de Dados

- **Decisão**: SQLite para desenvolvimento, PostgreSQL para produção.
- **Justificativa**: SQLite é leve para desenvolvimento, enquanto PostgreSQL oferece escalabilidade e desempenho para produção.

### 5.3 Frontend

- **Decisão**: Usar HTML, CSS e JavaScript puro.
- **Justificativa**: Facilidade de construção e inicio rapido, evita dependências pesadas, garantindo tempos de carregamento rápidos e simplicidade para um site de portfólio.

### 5.4 Design Responsivo

- **Decisão**: Usar uma abordagem mobile-first com CSS personalizado  a partir de media querys.
- **Justificativa**: Garante acessibilidade em todos os dispositivos e conformidade com WCAG 2.1.

---

## 6. Atributos de Qualidade

### 6.1 Desempenho

- Otimizar consultas ao banco de dados usando `select_related`/`prefetch_related` do Django ORM para recuperação eficiente de dados.
- Implementar caching (por exemplo, framework de cache do Django ou Redis) para páginas frequentemente acessadas.
- Garantir tempos de carregamento de página abaixo de 3 segundos para cenários de usuário típicos.

### 6.2 Escalabilidade

- Usar PostgreSQL para produção para lidar com o aumento do tráfego.
- Implantar em uma plataforma de nuvem escalável com balanceamento de carga, se necessário.
- Projetar o esquema do banco de dados para suportar paginação para listagens de artigos/projetos.

### 6.3 Segurança

- Aproveitar as proteções embutidas do Django (tokens CSRF, filtragem XSS).
- Implementar HTTPS e gerenciamento de sessão seguro.
- Usar CAPTCHA ou limitação de taxa para requisições e prevenir bot-spam.

### 6.4 Manutenibilidade

- Seguir as melhores práticas do Django para código modular dentro da proposta de seus desenvolvedores e comunidade.
- Documentar o código e usar convenções de nomenclatura consistentes.
- Usar migrações do Django para atualizações de esquema de banco de dados.

### 6.5 Usabilidade

- Projetar navegação intuitiva com uma estrutura de menu clara.
- Garantir design responsivo com testes em todos os dispositivos (celular, tablet, desktop).
- Aderir ao WCAG 2.1 para acessibilidade (por exemplo, contraste adequado, texto alt).

---

## 7. Considerações Futuras

- Adicionar endpoints de API REST para artigos/projetos para suportar potenciais aplicativos móveis ou integrações de terceiros.
- Implementar funcionalidade de busca usando a busca de texto completo do Django ou ferramentas externas (por exemplo, Elasticsearch).
- Integrar análises para rastrear o engajamento do visitante (por exemplo, Google Analytics).
- Expandir o sistema de comentários com autenticação de usuário (por exemplo, OAuth para login GitHub/LinkedIn).

---

## 8. Espaço Reservado para Diagramas

- **Diagrama de Entidade-Relacionamento (ERD)**:

![ERDiagram.svg](attachment:90ab4106-2024-4651-b892-d23af8a0175b:ERDiagram.svg)

- **Diagramas de Sequência**
    
    ![SequencialDiagram.svg](attachment:acab97dd-c10d-4223-b2b3-f9c7ea223bf6:SequencialDiagram.svg)
    
- **Diagrama de Implantação:**
    
    ![ImplantationDiagram.svg](attachment:316eb63b-19fc-4241-be02-723a09ba5904:ImplantationDiagram.svg)
    
- **Diagrama de Componentes**:

![ComponentDiagram.svg](attachment:b3b8bef4-98a2-42a0-b882-685db5b5f308:ComponentDiagram.svg)

---

## 9. Riscos e Mitigação

- **Risco**: Vulnerabilidades de segurança na entrada do usuário.
    - **Mitigação**: Confiar nos recursos de segurança do Django e validar/sanitizar todas as entradas.
- **Risco**: UI inconsistente entre dispositivos.
    - **Mitigação**: Testar extensivamente com ferramentas como BrowserStack e usar um framework CSS responsivo.