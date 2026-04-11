escolha_usuario = 121

match escolha_usuario:
    case 0:
        status = "Sair do programa"
    case 1:
        status = "Entrar no programa"
    case _:
        status = "Erro"

print(status)