import json

usuarios = [
    {"id": 1, "nome": "João", "saldo": 50.0},
    {"id": 2, "nome": "Maria", "saldo": 500.0},
    {"id": 3, "nome": "Carlos", "saldo": 2500.0}
]

def gerar_mensagem(saldo):
    if saldo < 100:
        return "Atenção aos gastos! Que tal organizar melhor seu orçamento?"
    elif saldo < 1000:
        return "Bom trabalho! Continue controlando seus gastos para evoluir financeiramente."
    else:
        return "Excelente! Você tem um bom saldo para pensar em investimentos."

for usuario in usuarios:
    usuario["mensagem"] = gerar_mensagem(usuario["saldo"])

with open("output.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

print("ETL concluído com sucesso! Arquivo 'output.json' gerado.")
