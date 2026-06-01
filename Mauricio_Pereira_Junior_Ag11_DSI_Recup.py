
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init()

# Lista com as situações do reservatório
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que define a cor de acordo com o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função que exibe a mensagem do reservatório
def exibir_alerta(nivel):
    cor = definir_cor(nivel)
    situacao = situacoes[nivel - 1]

    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)

# Simulação de monitoramento do reservatório
print("=== SISTEMA DE MONITORAMENTO DO RESERVATÓRIO ===")
print("Informe um nível de 1 a 5.")
print("Se não quiser digitar, pressione ENTER para rodar a simulação automática.")

entrada = input("Digite o nível atual do reservatório: ")

if entrada == "":
    print("\nSimulação automática dos níveis do reservatório:\n")

    for nivel in range(1, 6):
        exibir_alerta(nivel)

else:
    nivel_atual = int(entrada)

    if nivel_atual >= 1 and nivel_atual <= 5:
        print("\nSituação atual do reservatório:\n")
        exibir_alerta(nivel_atual)
    else:
        print(Fore.RED + "Erro: informe apenas valores de 1 a 5." + Style.RESET_ALL)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)
