# Consulta CPF com Python

Aplicação simples desenvolvida em Python para realizar consultas de um determinado CPF utilizando a API do CPFHub.io.

---

# 📌 Tecnologias Utilizadas

- Python 3
- Requests
  

---

# 📂 Estrutura do Projeto

```bash
api_cpf/
│
├── cpf.py
```

---

# 🚀 Funcionalidades

- Busca de CPF via API
- Multipla escolha de dados para consulta

---

# 🖥️ Pré-requisitos

Antes de executar o projeto, instale:

- Python 3.10 ou superior

Download oficial:

https://www.python.org

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/devbyenzo/api_cpf.git
```

## 2. Acesse a pasta do projeto

```bash
cd api_cpf
```

## 3. Crie um ambiente virtual (Opcional, mas recomendado)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Instalação das Dependências

## Instale manualmente

```bash
pip install requests
```

## Ou utilize o requirements.txt

Crie o arquivo:

```txt
requests
```

Depois execute:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o arquivo principal:

```bash
python cpf.py
```

---

# 🧠 Explicação do Código

## Importação das Bibliotecas

```python
import requests
```

- `requests` → permite a comunicação com a API via requests http

---




---

## Capturando o CPF via user input

```python
cpf = input("Digite o CPF: ")
```

Obtém o CPF digitado pelo usuario.

---

## Chamando a URL da API

```python
url = f'https://api.cpfhub.io/cpf/{cpf}'
```

- Chama o link da API do CPFHUB.io
- Pega o CPF digitado pelo input do usuario diretamente para dentro da URL

---

## Headers

### IMPORTANTE!

```python
headers = {
                'x-api-key': 'API-KEY',
                'Accept': 'application/json'
            }
```

- Essa função é essencial para passar a sua API key do CPFHub.io para poder consultar.


---

# 💡 Melhorias Futuras

- Implementação Visual (customtkinter)
- Barra de progresso
- Tema claro/escuro dinâmico
- Integração com o sistema de busca CNPJ

---

# ✅ Boas Práticas Aplicadas

- Organização simples do projeto
- Separação da lógica em função

---

# ⚠️ Melhorias Recomendadas no Código

Atualmente o código NÃO utiliza:

```python
except:
```

O ideal é utilizar exceções específicas:

```python
except Exception as erro:
    status.configure(text=f"Erro: {erro}", text_color="red")
```

Isso facilita:

- Depuração
- Manutenção
- Identificação de problemas

---

# 🔒 Observações

- Os dados que serão buscados, são APENAS os que a API disponibilizam!.
- Utilize apenas para fins educacionais e pessoais.

---



---

# 👨‍💻 Autor

Projeto desenvolvido para estudos de:

- Python
- Consumo de API
- Consumo de API utilizando KEYS

---

# ⭐ Contribuição

Contribuições são bem-vindas.

Faça um fork do projeto e envie um pull request.

---

# 📄 Licença

Este projeto está sob a licença MIT.
