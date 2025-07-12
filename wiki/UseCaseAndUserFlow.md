# Especificação de Casos de Uso e Diagramas de Fluxo de Usuário para Website de Portfólio Pessoal

## 1. Introdução

### 1.1 Propósito

Este documento define os **casos de uso** e as **descrições de fluxo de usuário** para um website de portfólio pessoal construído com Django (backend) e HTML, CSS e JavaScript (frontend). Ele descreve as interações entre os usuários (proprietário e visitantes) e o sistema, cobrindo funcionalidades-chave como visualização da página inicial, navegação por artigos e projetos, envio de comentários e gerenciamento de conteúdo. As descrições de fluxo de usuário são fornecidas para guiar a criação de diagramas (a serem adicionados posteriormente).

### 1.2 Escopo

Os casos de uso cobrem:

- Visualização da página inicial com resumos de artigos, projetos, seção "sobre" e métricas.
- Navegação de listagem de artigos e  leitura dos detalhes de artigos.
- Navegação e visualização de detalhes de projetos.
- Visualização das seções "sobre" e de contato.
- Gerenciamento de artigos, projetos (somente proprietário).

Os fluxos de usuário descrevem os caminhos de navegação e interação para essas funcionalidades.

### 1.3 Definições, Acrônimos e Abreviações

- **Proprietário**: O administrador do website que gerencia o conteúdo.
- **Visitante**: Qualquer usuário que acessa o website público.
- **CRUD**: Create, Read, Update, Delete (Criar, Ler, Atualizar, Excluir operações).
- **Django Admin**: Interface administrativa embutida do Django para gerenciamento de conteúdo.
- **WCAG**: Web Content Accessibility Guidelines (Diretrizes de Acessibilidade de Conteúdo Web).

### 1.4 Referências

- Especificação de Requisitos de Software (SRS) para Website de Portfólio Pessoal (artifact_id: 694986fc-d32c-4f9a-9f39-dac5f85e80ee)
- Documento de Arquitetura de Software (SAD) para Website de Portfólio Pessoal (artifact_id: 73afbdd2-79df-423a-971c-4c211e1a5c24)

---

## 2. Atores

- **Proprietário**: O indivíduo que possui o portfólio, responsável por criar, atualizar e excluir artigos, projetos. Acessa o Django admin.
- **Visitante**: Qualquer usuário que acessa o website para visualizar conteúdo, ou contatar o proprietário. Nenhuma autenticação é necessária para as ações.

---

## 3. Casos de Uso

### 3.1 CU-01: Visualizar Página Inicial

- **Descrição**: Um visitante visualiza a página inicial, que inclui uma introdução, resumos de projetos e artigos recentes, uma seção "sobre", métricas e um rodapé com informações de contato.
- **Atores**: Visitante
- **Pré-condições**: O website está acessível via navegador web; o banco de dados contém artigos, projetos e dados de perfil.
- **Fluxo Básico**:
    1. Visitante navega para a página inicial (`/`).
    2. O sistema busca artigos recentes (3), projetos (3 ou 6), biografia do perfil, métricas e links de contato.
    3. O sistema renderiza a página inicial com:
        - Barra de Navegação com NOME que leva a pagina inicial, links para home, projetos, artigos, sobre mim e GitHub.
        - Seção de herói com conteúdo chamativo (por exemplo, texto animado).
        - Resumo da seção "Sobre" com uma breve biografia e uma foto.
        - Exibição de métricas (por exemplo, anos de experiência, contagem de projetos).
        - Módulo de resumo de projetos com títulos, miniaturas e um link "Ver Mais".
        - Módulo de resumo de artigos com títulos, trechos e um link "Ver Mais".
        - Rodapé com detalhes de contato e links externos (GitHub, LinkedIn, WhatsApp).
    4. O visitante interage com os links (por exemplo, clica em "Ver Mais" ou em links de perfil externo).
- **Pós-condições**: A página inicial é exibida; o visitante pode navegar para outras seções.
- **Fluxos Alternativos**:
    - **A1**: Se não houver artigos/projetos, exibir uma mensagem de placeholder no respectivo módulo.
    - **A2**: Se o banco de dados estiver indisponível, exibir uma página de erro com uma opção de tentar novamente.
- **Exceções**: Erros de rede ou tempo de inatividade do servidor impedem o carregamento da página.
- **Prioridade**: Alta

### 3.2 CU-02: Navegar e Ler Artigos

- **Descrição**: Um visitante navega pela lista de artigos e lê um artigo específico, com a opção de visualizar.
- **Atores**: Visitante
- **Pré-condições**: Artigos existem no banco de dados; o website está acessível.
- **Fluxo Básico**:
    1. Visitante navega para a seção de artigos (`/articles/` e posrteriormente `/articles/<id>/`).
    2. O sistema busca e exibe uma lista paginada de resumos de artigos (título, trecho, categorias, autor, data).
    3. Visitante clica em um card de artigo.
    4. O sistema busca detalhes do artigo.
    5. O sistema renderiza a página de detalhes do artigo com conteúdo completo, metadados.
- **Pós-condições**: O artigo é exibido.
- **Fluxos Alternativos**:
    - **A1**: Se não houver artigos, exibir uma mensagem "Nenhum artigo disponível".
- **Exceções**: Erros de banco de dados impedem a recuperação de artigos.
- **Prioridade**: Alta

### 3.3 CU-03: Navegar e Visualizar Projetos

- **Descrição**: Um visitante seleciona um projeto na pagina inicial e visualiza os detalhes de um projeto específico.
- **Atores**: Visitante
- **Pré-condições**: Projetos existem no banco de dados; o website está acessível.
- **Fluxo Básico**:
    1. Visitante clica em um título ou miniatura de projeto.
    2. O sistema busca detalhes do projeto (documentação, mídia).
    3. Visitante navega para um projeto especifico (`/projects/<id>/`).
    4. O sistema renderiza a página de detalhes do projeto com documentação.
- **Pós-condições**: O projeto é exibido.
- **Fluxos Alternativos**:
- **Exceções**: Erros de banco de dados impedem a recuperação de projetos ou comentários.
- **Prioridade**: Alta

### 3.4 CU-04: Visualizar Seção "Sobre" e Métricas

- **Descrição**: Um visitante visualiza a seção "sobre", incluindo uma biografia e métricas pessoais.
- **Atores**: Visitante
- **Pré-condições**: Dados de perfil (biografia, métricas) existem no banco de dados.
- **Fluxo Básico**:
    1. Visitante navega para a seção "sobre" (`/about-me/`).
    2. O sistema busca dados de perfil (biografia, métricas, imagem de perfil opcional).
    3. O sistema renderiza a página "sobre" com biografia e métricas (por exemplo, anos de experiência, contagem de projetos).
- **Pós-condições**: A página "sobre" é exibida.
- **Fluxos Alternativos**:
    - **A1**: Se os dados de perfil estiverem ausentes, exibir um placeholder ou mensagem padrão.
- **Exceções**: Erros de banco de dados impedem a recuperação de dados de perfil.
- **Prioridade**: Média

### 3.6 CU-06: Gerenciar Conteúdo (Proprietário)

- **Descrição**: O proprietário cria, atualiza ou exclui artigos, projetos ou comentários via Django admin ou interface personalizada.
- **Atores**: Proprietário
- **Pré-condições**: O proprietário está autenticado e tem acesso ao Django admin ou interface personalizada.
- **Fluxo Básico**:
    1. Proprietário faz login no Django admin (`/admin/`) ou interface personalizada.
    2. Proprietário navega para a seção de artigos, projetos.
    3. Para artigos/projetos:
        - **Criar**: Proprietário insere título, corpo/descrição, miniatura e metadados; salva a entrada.
        - **Atualizar**: Proprietário edita uma entrada existente e salva as alterações.
        - **Excluir**: Proprietário exclui uma entrada.
    4. O sistema salva as alterações no banco de dados e atualiza a exibição do frontend.
- **Pós-condições**: O conteúdo é criado, atualizado ou excluído; as alterações são refletidas no website.
- **Fluxos Alternativos**:
    - **A1**: Se a autenticação falhar, redirecionar para a página de login.
    - **A2**: Se a validação de entrada falhar (por exemplo, campos obrigatórios ausentes), exibir um erro e solicitar nova tentativa.
- **Exceções**: Erros de banco de dados impedem atualizações de conteúdo.
- **Prioridade**: Alta

---

## 4. Diagramas de Fluxo de Usuário (Descrições Textuais)

**Nota**: Estas descrições são projetadas para serem convertidas em diagramas visuais (por exemplo, usando ferramentas UML ou de fluxograma). Os diagramas podem ser adicionados posteriormente.

### 4.1 Fluxo de Usuário: Visualizar Página Inicial

- **Início**: Visitante acessa `/`.
- **Etapas**:
    1. O sistema exibe a seção de herói (texto/imagem animado).
    2. O sistema mostra o resumo da seção "sobre" (breve biografia) e métricas (por exemplo, contagem de projetos).
    3. O sistema mostra o módulo de resumo de projetos (3 ou 6 projetos).
    4. O sistema mostra o módulo de resumo de artigos (3 artigos, link "Ver Mais").
    5. O sistema exibe o rodapé com informações de contato e links externos.
- **Pontos de Decisão**:
    - Visitante clica em "Ver Mais" → Redireciona para `/articles/`.
    - Visitante clica em link externo → Abre GitHub/LinkedIn em uma nova aba.
- **Fim**: Visitante navega para outra seção ou site externo.

### 4.2 Fluxo de Usuário: Navegar

- **Início**: Visitante acessa `/articles/`.
- **Etapas**:
    1. O sistema exibe a lista paginada de artigos (título, trecho).
    2. Visitante clica em um artigo → Redireciona para `/articles/<id>/`.
    3. O sistema exibe o conteúdo do artigo.
- **Pontos de Decisão**:
    - Se não houver artigos, exibe "Nenhum artigo disponível".
- **Fim**: Visitante lê o artigo.

### 4.3 Fluxo de Usuário: Navegar

- **Início**: Visitante acessa `/projects/`.
- **Etapas**:
    1. Visitante clica em um projeto → Redireciona para `/projects/<id>/`.
    2. O sistema exibe a documentação do projeto.
- **Fim**: Visitante visualiza o projeto.

### 4.4 Fluxo de Usuário: Visualizar Seções "Sobre"

- **Início**: Visitante acessa `/about/`.
- **Etapas**:
    1. Para `/about/`, o sistema exibe biografia e métricas.
    2. Visitante clica em um link externo (por exemplo, GitHub) → Abre em uma nova aba.
- **Pontos de Decisão**:
    - Se os dados estiverem ausentes, exibe texto de placeholder.
- **Fim**: Visitante visualiza informações ou navega para perfis externos.

### 4.5 Fluxo de Usuário: Gerenciar Conteúdo (Proprietário)

- **Início**: Proprietário acessa `/admin/`.
- **Etapas**:
    1. Proprietário faz login com credenciais.
    2. Proprietário seleciona a seção de artigos ou projetos.
    3. Proprietário realiza operações CRUD:
        - **Criar**: Insere e salva novo conteúdo.
        - **Atualizar**: Edita e salva conteúdo existente.
        - **Excluir**: Remove conteúdo.
    4. O sistema atualiza o banco de dados e reflete as alterações no frontend.
- **Pontos de Decisão**:
    - Se o login falhar, redireciona para a página de login.
    - Se a validação de entrada falhar, mostra erro e solicita nova tentativa.
- **Fim**: O conteúdo é atualizado; as alterações são visíveis no website.

---

## 5. Requisitos Não Funcionais

- **Desempenho**: As páginas carregam em até 3 segundos em condições normais.
- **Segurança**: Autenticação do proprietário para gerenciamento de conteúdo; proteção CSRF para formulários.
- **Usabilidade**: Navegação intuitiva; design responsivo para dispositivos móveis e desktop; conformidade com WCAG 2.1.
- **Confiabilidade**: O sistema lida com 100 usuários simultâneos sem erros.

---

## 6. Pressupostos e Restrições

### Pressupostos:

- Visitantes possuem navegadores web modernos (por exemplo, Chrome, Firefox).
- O proprietário tem acesso às credenciais do Django admin.
- Conectividade com a internet está disponível.

### Restrições:

- O backend deve ser desenvolvido dentro das capacidades do ecossistema Django.
- O frontend usa HTML, CSS e JavaScript puro.
- O sistema de comentários evita o registro obrigatório do usuário.

---

## 7. Aprimoramentos Futuros

- Adicionar funcionalidade de busca para artigos/projetos.
- Implementar login social para comentários (por exemplo, OAuth do GitHub).
- Adicionar rastreamento de análises para interações de visitantes.
- Suportar endpoints de API para acesso externo ao conteúdo.

---

## 8. Espaço Reservado para Diagramas

- **Diagrama de Caso de Uso**:
    
    ![UseCases.svg](attachment:e36370ec-b9cd-42e7-ac47-b1504f7e2c45:UseCases.svg)
    
- **Diagramas de Fluxo de Usuário**:
    
    ![UserFlux5.svg](attachment:9b41c921-0da8-46cf-9ed7-42774f602c5e:UserFlux5.svg)
    
    ![UserFlux4.svg](attachment:54fbafc8-a000-483d-8f9c-23ed70ed77fe:UserFlux4.svg)
    
    ![UserFlux3.svg](attachment:bef3febe-7a6f-4c3b-afeb-b93f86ab97c0:UserFlux3.svg)
    
    ![UserFlux2.svg](attachment:8fda6923-f666-4863-b2e9-389203976274:UserFlux2.svg)
    
    ![UserFlux.svg](attachment:b9303686-cafa-4cc0-9ad5-081b6880d6ce:UserFlux.svg)
    
- **Diagramas de Sequência**

![SequencialDiagram.svg](attachment:a33ca9cd-5f47-49cf-88af-fa5a752b8c9d:SequencialDiagram.svg)