# Projeto ETL - Santander Dev Week

## 📌 Descrição
Este projeto foi desenvolvido como parte do desafio da **Santander Dev Week** com o objetivo de demonstrar o fluxo **ETL (Extract, Transform, Load)** utilizando Python.

Devido à possível indisponibilidade da API original do projeto, os dados foram simulados por meio de uma lista de usuários fictícios, mantendo o foco no aprendizado do processo de ETL.

---

## 🔄 Fluxo ETL

### 🔹 Extract (Extração)
Os dados dos usuários são extraídos de uma lista criada diretamente no código Python, simulando uma fonte externa de dados.

### 🔹 Transform (Transformação)
Para cada usuário, é gerada uma mensagem personalizada com base no saldo disponível, utilizando regras condicionais (`if / else`).

### 🔹 Load (Carregamento)
Os dados transformados são salvos em um arquivo `output.json`, representando a etapa final do processo de ETL.

---

## 🛠 Tecnologias Utilizadas
- Python 3
- Biblioteca padrão `json`

---

## ▶️ Como Executar o Projeto
1. Clone o repositório
2. Execute o arquivo:
   ```bash
   python main.py
