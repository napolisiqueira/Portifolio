# Portfólio Pessoal - Desenvolvido em Django

Este é um projeto de portfólio pessoal desenvolvido com **Django**, com o objetivo de apresentar seus principais projetos, habilidades e experiências de forma organizada, moderna e responsiva. Ideal para servir como um cartão de visitas online profissional.

## ✨ Funcionalidades

- Página inicial com apresentação pessoal
- Sessão de projetos com descrições e links
- Destaque para habilidades técnicas
- Design limpo, responsivo e fácil de manter

## 🛠️ Tecnologias Utilizadas

- **Backend:** [Python 3](https://www.python.org/), [Django](https://www.djangoproject.com/)
- **Frontend:** HTML5, CSS3 puro
- **Banco de Dados:** SQLite3
- **Gerenciamento de pacotes:** [uv](https://github.com/astral-sh/uv)
- **Versionamento:** Git

## 📁 Estrutura do Projeto

```bash
Portifolio/
├── manage.py
├── pyproject.toml
├── db.sqlite3
├── app/ # Aplicação principal
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ └── static/
├── templates/ # HTMLs principais
├── static/ # CSS, JS, imagens
└── wiki/ # Documentação (SAD, SRS, Diagramas)
```

## 🚀 Como Executar Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd Portifolio
```
2. **Crie e ative um ambiente virtual:**
```bash
uv venv
uv pip install -r requirements.txt  # ou use o pyproject.toml
```
3. **Execute as migrações:**
```bash
python manage.py migrate
```
4. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

## 📚 Documentação Técnica

A pasta wiki/ contém:

- Documento de Arquitetura de Software (SAD)

- Especificação de Requisitos (SRS)

- Casos de Uso e Fluxos de Usuário

- Diagramas (Componentes, Implantação, ER, Sequência)

## 📌 Status do Projeto

- ✅ Em desenvolvimento ativo
- 🧩 Fácil de expandir (admin, blog, área restrita, etc.).
- 👨‍💻 Autor: Felipe Napoli Siqueira
