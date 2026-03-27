# Solicita os dados do usuário
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o tempo de uso diário (em horas): "))

# Cálculo do consumo mensal (kWh)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Valor da energia (R$/kWh)
valor_kwh = 0.75

# Cálculo do custo mensal
custo_mensal = consumo_mensal * valor_kwh

# Exibe o resultado
print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
print(f"Custo estimado: R$ {custo_mensal:.2f}")