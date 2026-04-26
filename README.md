# Data Portfolio - Arthur Porto

Portfolio de estudos e projetos praticos em dados, reunindo notebooks, bases, graficos e entregaveis desenvolvidos ao longo de cursos, desafios e analises aplicadas.

## Objetivo

Organizar minha evolucao tecnica em Python, analise de dados, visualizacao, estatistica aplicada e projetos de portfolio. O repositorio tambem serve como vitrine para recrutadores, mentores e pessoas interessadas em acompanhar meu desenvolvimento na area de dados.

## Estrutura do repositorio

| Pasta | Conteudo |
| --- | --- |
| `alura/` | Estudos da trilha de Python para Data Science, com notebooks, desafios e bases de apoio. |
| `fiap/` | Projetos e estudos da Pos Tech FIAP, incluindo analises exploratorias e tech challenge. |
| `google-data-analytics/` | Organizacao dos estudos do certificado Google Data Analytics. |
| `docs/` | Documentos auxiliares, prompts e materiais de apoio ao aprendizado. |
| `requirements.txt` | Dependencias Python usadas no portfolio. |
| `server.py` | API Flask simples para expor informacoes basicas do portfolio. |

## Destaques

- Analises em Jupyter Notebook com foco em Python, NumPy, Pandas e visualizacao.
- Bases de dados em CSV, XLSX, JSON, XML e HTML para pratica de leitura e tratamento.
- Trilha estruturada por fonte de estudo (Alura, FIAP, Google) para facilitar revisao e manutencao.
- Trabalho com pipelines de dados, exploracao estatistica e construcao de relatorios executivos.

## Como usar localmente

1. Clone o repositorio:

```bash
git clone https://github.com/Art-Porto/data-portfolio.git
cd data-portfolio
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Abra os notebooks:

```bash
jupyter lab
```

5. Opcionalmente, rode a API local:

```bash
python server.py
```

## Informacoes de Git

- Repositorio remoto: `https://github.com/Art-Porto/data-portfolio.git`
- Branch principal: `main`
- Remote padrao: `origin`

Comandos uteis:

```bash
git status
git pull origin main
git add <arquivos>
git commit -m "mensagem"
git push origin main
```

## Privacidade e dados sensiveis

Projetos com dados pessoais ou de terceiros (clientes, fornecedores, dados financeiros) ficam em repositorio privado separado, fora deste portfolio publico. O `.gitignore` protege credenciais (`credenciais.json`, `.env`, tokens, chaves) por padrao.

## Contato

- LinkedIn: https://www.linkedin.com/in/arthursporto/
- Email: arthursporto@gmail.com
