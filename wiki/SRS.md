# Especificação de Requisitos de Software (SRS) para Website de Portfólio Pessoal

## 1. Introdução

### 1.1 Propósito

Este documento descreve os requisitos para um website de portfólio pessoal projetado para exibir os artigos, projetos, informações pessoais, métricas e detalhes de contato do proprietário. O website visa fornecer uma plataforma interativa com artigos e projetos, uma página inicial dinâmica com resumos e integração com perfis externos (por exemplo, GitHub, LinkedIn).

### 1.2 Escopo

O sistema será uma aplicação web construída usando Django para o backend e HTML, CSS e JavaScript para o frontend. Inclui:

- Uma página inicial com uma introdução cativante e módulos de resumo para artigos, projetos, "sobre" e métricas.
- Uma página de artigos para listar todos os artigos a partir do paginator.
- Uma página de detalhes do artigo mostrando o conteúdo .
- Uma página de detalhes do projetos para exibir documentação.
- Uma seção "sobre" com informações pessoais e métricas chave.
- Uma barra de navegação com links para todas as seções e link para perfi externo do GitHub.
- Um rodapé com detalhes de contato e links para perfis externos (GitHub, LinkedIn, etc.).

### 1.3 Definições, Acrônimos e Abreviações

- **SRS**: Software Requirements Specification (Especificação de Requisitos de Software)
- **Django**: Um framework web baseado em Python para desenvolvimento de backend
- **Frontend**: Interface de usuário construída com HTML, CSS e JavaScript
- **CMS**: Content Management System (Sistema de Gerenciamento de Conteúdo - para gerenciamento de artigos e projetos)
- **CRUD**: Create, Read, Update, Delete (Criar, Ler, Atualizar, Excluir operações)
- **UUID**: Universally Unique Identifier (Identificador Único Universal)

---

## 2. Descrição Geral

### 2.1 Necessidades do Usuário

- **Proprietário**: Capacidade de publicar e gerenciar artigos e projetos.
- **Visitantes**: Capacidade de ler artigos, visualizar projetos e acessar informações de contato ou links de perfil externo.

### 2.2 Pressupostos e Dependências

- O sistema pressupõe que os usuários possuem um navegador web moderno (por exemplo, Chrome, Firefox, Safari).
- Django será usado com um banco de dados relacional (por exemplo, SQLite para desenvolvimento, PostgreSQL para produção).
- Os links de perfil externo (GitHub, LinkedIn) são válidos e fornecidos pelo proprietário.
- Conectividade com a internet é necessária para acessar o website.

---

## 3. Funcionalidades do Sistema

### 3.1 Página Inicial

- **Descrição**: Uma página inicial dinâmica com uma introdução cativante e módulos de resumo para outras seções.
- **Funcionalidades**:
    - Barra de navegação com links para todas as seções, pagina de listagem de artigos, e link externo para o GitHub.
    - Seção de herói com uma introdução visualmente atraente (por exemplo, texto animado ou plano de fundo).
    - Resumo da seção "Sobre Mim" com uma breve biografia.
    - Exibição de 2 a 4 métricas únicas (por exemplo, anos de experiência, número de projetos concluídos).
    - Módulo mostrando 3 ou 6 projetos recentes.
    - Módulo mostrando os 3 artigos mais recentes com um link "Ver Mais" para a seção de artigos.
    - Rodapé com informações de contato e links para perfis externos (GitHub, LinkedIn, etc.).
- **Prioridade**: Alta
- **Entrada**: Nenhuma (conteúdo buscado dinamicamente do banco de dados).
- **Saída**: Página HTML renderizada com design responsivo.

### 3.2 Seção de Artigos

- **Descrição**: Uma seção para listar 10 cards de artigos com titulo, descrição, data de publicação, autor e categorias, através de paginator.
- **Funcionalidades**:
    - Página de listagem de artigos com paginação e resumos (título, trecho, data de publicação, categorias, autor).
    - Página de artigo individual com conteúdo completo, metadados (autor, data, categorias)
    - Operações CRUD para artigos (somente proprietário, via Django admin).
    - Design responsivo para legibilidade em dispositivos móveis e desktop.
- **Prioridade**: Alta
- **Entrada**: Conteúdo do artigo (título, corpo, miniatura opcional) do proprietário.
- **Saída**: Páginas de artigo renderizadas com comentários exibidos abaixo de cada artigo.

### 3.3 Seção de Projetos

- **Descrição**: Uma seção para exibir projetos com documentação detalhada.
- **Funcionalidades**:
    - Página de detalhes do projetos com título,  miniatura, texto, autor, categorias, data de publicação.
    - Operações CRUD para projetos (somente proprietário, via Django admin).
    - Design responsivo para acessibilidade em todos os dispositivos.
- **Prioridade**: Alta
- **Entrada**: Detalhes do projeto (título, descrição, documentação, mídia opcional) do proprietário; comentários de visitantes.
- **Saída**: Páginas de projeto renderizadas com documentação e comentários.

### 3.4 Seção Sobre Mim

- **Descrição**: Uma página fornecendo informações pessoais e métricas chave sobre o proprietário.
- **Funcionalidades**:
    - Breve biografia com texto e imagem de perfil.
    - Exibição de métricas únicas (por exemplo, anos de experiência, número de projetos, certificações).
    - Experiencias profisionais com data, reumo, cargo.
    - Arquivo de curriculo disponivel via download.
    - Editável via Django admin (somente proprietário).
    - Design responsivo para acessibilidade.
- **Prioridade**: Média
- **Entrada**: Biografia e dados de métricas do proprietário.
- **Saída**: Página HTML renderizada com biografia e métricas, arquivo para download.

---

## 4. Requisitos Não Funcionais

### 4.1 Desempenho

- O tempo de carregamento da página não deve exceder 3 segundos em condições normais.
- O sistema deve lidar com pelo menos 100 usuários simultâneos sem degradação significativa de desempenho.

### 4.2 Escalabilidade

- O sistema deve suportar escalabilidade para lidar com o aumento do tráfego (por exemplo, via hospedagem em nuvem com PostgreSQL).
- As consultas ao banco de dados devem ser otimizadas para recuperação rápida de artigos e projetos.

### 4.3 Segurança

- Autenticação de usuário para acesso do proprietário às operações CRUD (Django admin ou interface personalizada).
- Proteção contra vulnerabilidades comuns (por exemplo, XSS, CSRF) usando os recursos de segurança embutidos do Django.
- Aplicação de HTTPS para transmissão segura de dados.

### 4.4 Usabilidade

- Design responsivo compatível com dispositivos móveis, tablets e desktops.
- Navegação intuitiva com uma estrutura de menu clara.
- Design acessível seguindo as diretrizes WCAG 2.1 (por exemplo, contraste adequado, texto alt para imagens).

### 4.5 Manutenibilidade

- Código-base Django modular com documentação clara.
- Separação de preocupações entre backend (Django) e frontend (HTML/CSS/JavaScript).
- Conteúdo fácil de atualizar via Django admin.

---

## 5. Arquitetura do Sistema

### 5.1 Stack Tecnológica

- **Backend**: Django (Python) com um banco de dados relacional (SQLite para desenvolvimento, PostgreSQL para produção).
- **Frontend**: HTML5, CSS3, JavaScript (puro).
- **Banco de Dados**: Django ORM para gerenciar artigos, projetos, e dados de usuário.
- **Hospedagem**: Implementável em plataformas de nuvem (por exemplo, Heroku, AWS ou Render).
- **APIs Externas**: Integração opcional com APIs do GitHub/LinkedIn para dados de perfil dinâmicos (se necessário).

### 5.2 Esquema do Banco de Dados (Conceitual)

- **User (Usuário)**: Armazena dados do proprietário e, opcionalmente, de visitantes (para comentários autenticados).
    - **Campos**: username, email, password (hashed), role (owner/visitor).
- **Article (Artigo)**: Armazena conteúdo do artigo.
    - **Campos**: id, title, content, publish_date, categories, author (foreign key para User).
- **Project (Projeto)**: Armazena detalhes do projeto.
    - **Campos**: id, title, sumary, description, documentation, image, publish_date, author (foreign key para User).
- **Comment (Comentário)**: Armazena comentários para artigos e projetos.
    - **Campos**: id, content, author_name, date, article/project (foreign key), owner.
- **Profile (Perfil)**: Armazena informações "sobre" e de contato do proprietário.
    - **Campos**: bio, metrics (JSON ou tabela separada), contact_email, github_url, linkedin_url.

![ERDiagram.svg](attachment:90ab4106-2024-4651-b892-d23af8a0175b:ERDiagram.svg)

### 5.3 Componentes do Sistema

- **Backend Django**:
    - **Modelos**: User, Article, Project, Comment.
    - **Views**: Lidam com a renderização de páginas e processamento de formulários.
    - **Templates**: Arquivos HTML para cada página (página inicial, artigos, projetos, sobre, contato).
    - **Admin**: Interface de administração Django para gerenciamento de conteúdo.
- **Frontend**:
    - **Arquivos Estáticos**: CSS para estilização, JavaScript para interatividade.
    - **Design Responsivo**: CSS personalizado.
- **Banco de Dados**: Gerenciado via Django ORM com migrações para atualizações de esquema.

---

## 6. Restrições

- O sistema deve ser desenvolvido dentro das capacidades do ecossistema Django.
- O frontend deve evitar frameworks JavaScript pesados (por exemplo, React), a menos que explicitamente necessário para o desempenho.

---

## 7. Aprimoramentos Futuros

- Integração com um CMS completo para gerenciamento de conteúdo mais fácil.
- Análises avançadas para rastrear o engajamento do visitante (por exemplo, visualizações de página, atividade de comentários).
- Funcionalidade de busca para artigos e projetos.
- Botões de compartilhamento social para artigos e projetos.

---

## 8. Critérios de Aceitação

- A página inicial exibe todos os módulos necessários (herói, projetos, artigos, sobre, métricas, rodapé) com design responsivo.
- As seções de artigos e projetos permitem operações CRUD (somente proprietário) e comentários (visitantes).
- As seções "Sobre" e de contato exibem os dados fornecidos pelo proprietário com precisão.
- O sistema é implementável em uma plataforma de nuvem sem erros críticos.
- Todas as páginas são acessíveis e atendem às diretrizes WCAG 2.1.