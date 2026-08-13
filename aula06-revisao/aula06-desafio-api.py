endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500], # /login
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# função que verifica se um codigo_http é sucesso
# 200 -> True
# 299 -> True
# 404 -> False
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# print(eh_sucesso(401))

# FUNÇÃO que verifica se tem 2 erros seguidos em UM endpoint
# verificar os códigos http daquele endpoint
# [200, 200, 401, 200, 500] --> False
# [201, 500, 502, 201, 500] --> True

def dois_erros(requisicoes):
    for i in range(len(requisicoes) - 1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# print(dois_erros(status[2]))

# [200, 200, 401, 200, 500] /login
# 3 sucessos
# 2 erros
def analisar_endpoint(requisicoes):
    qtd_sucessos = 0

    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_requisicoes = len(requisicoes)
    qtd_erros = qtd_requisicoes - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_requisicoes) * 100

    tem_erros_seguidos = dois_erros(requisicoes)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

# PERCORRER TODA A MATRIZ!!
maior_qtd_erros = -1
endpoint_mais_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    requisicoes_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(requisicoes_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {requisicoes_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual:.1f}%")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_mais_erros = nome_endpoint

print(f"Endpoint com + erros é: {endpoint_mais_erros} ({maior_qtd_erros})")