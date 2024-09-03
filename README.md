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
