# FastAPI MVC App

Este é um exemplo básico de aplicação FastAPI usando o padrão MVC (Model-View-Controller), com rotas que retornam JSON fixo (sem banco de dados).

## 📁 Estrutura

- `models/` → Dados simulados e lógica de acesso.
- `controllers/` → Lógica intermediária.
- `views/` → Rotas expostas pela API.

## 🚀 Como rodar

1. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute a aplicação:

```
uvicorn app.main:app --reload
```

4. Acesse em: http://127.0.0.1:8000/docs

📌 Rotas disponíveis
- GET /users → Lista todos os usuários

- GET /users/{id} → Retorna usuário pelo ID

