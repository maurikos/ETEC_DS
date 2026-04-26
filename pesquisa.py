# Inicialização dos contadores
excelente = 0
bom = 0
ruim = 0

# Loop para até 50 entrevistados
for i in range(50):
    print(f"\nEntrevistado {i+1}")

    nome = input("Digite o nome (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        print("Pesquisa encerrada antecipadamente.")
        break

    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    print("0 - ENCERRAR PESQUISA")

    opiniao = int(input("Digite a opção: "))

    # Encerrar pelo número
    if opiniao == 0:
        print("Pesquisa encerrada antecipadamente.")
        break

    # Validação
    while opiniao not in [1, 2, 3]:
        opiniao = int(input("Opção inválida! Digite 1, 2, 3 ou 0 para sair: "))

    # Contagem
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

# Total de respostas válidas
total = excelente + bom + ruim

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Total de entrevistados: {total}")
print(f"EXCELENTE: {excelente}")
print(f"BOM: {bom}")
print(f"RUIM: {ruim}")