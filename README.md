# API de Veículos

## Descrição
Esta API RESTful permite gerenciar veículos, incluindo a listagem, criação, detalhamento, atualização e exclusão de veículos. A API também implementa autenticação JWT para garantir que apenas usuários autenticados possam acessar os endpoints.

## Endpoints

### Listar Veículos
- **GET** `/api/veiculos/`
- Retorna uma lista de veículos.

### Criar Veículo
- **POST** `/api/veiculos/`
- Cria um novo veículo.

### Detalhar Veículo
- **GET** `/api/veiculos/<id>/`
- Retorna os detalhes de um veículo específico.

### Atualizar Veículo
- **PUT** `/api/veiculos/<id>/`
- Atualiza o status de um veículo para "CONECTADO" ou "DESCONECTADO".

### Excluir Veículo
- **DELETE** `/api/veiculos/<id>/`
- Exclui um veículo.

## Autenticação
- A API utiliza JWT para autenticação.
- Para obter o token:
  - **POST** `/api/token/` com `username` e `password`.

## Execução Local

### Pré-requisitos
- Python 3.x
- pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado)

### Passos para execução:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   
2. Crie e ative um ambiente virtual:
- bash
- Copiar código
- python -m venv venv
- source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
- bash
- Copiar código
- pip install -r requirements.txt

4. Realize as migrações:
- bash
- Copiar código
- python manage.py migrate

5.Crie um superusuário para acessar o Django Admin:
- bash
- Copiar código
- python manage.py createsuperuser


6.Inicie o servidor de desenvolvimento:
- bash
- Copiar código
- python manage.py runserver

7.Acesse a API:
- Visite http://127.0.0.1:8000/ para acessar a API.
- Utilize as credenciais criadas para autenticação via /api/token/.


8.Testes Unitários
- Para executar os testes unitários:
- bash
- Copiar código
- python manage.py test
- Documentação da API
- A API está documentada utilizando o Swagger e pode ser acessada em: http://127.0.0.1:8000/swagger/

Contato
Em caso de dúvidas, entre em contato pelo e-mail mayconmottadasilva@outlook.com.
