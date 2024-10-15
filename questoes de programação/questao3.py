import json

def carregar_dados_faturamento(filename):
 
    with open(filename, 'r') as file:
        return json.load(file)

def calcular_estatisticas_faturamento(dados):

    faturamento_validos = [dia["faturamento"] for dia in dados if dia["faturamento"] > 0]

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)


    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

   
    dias_acima_da_media = sum(1 for dia in faturamento_validos if dia > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media


dados_faturamento = carregar_dados_faturamento('faturamento.json')

menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_estatisticas_faturamento(dados_faturamento)


print(f"Menor faturamento: R$ {menor_faturamento}")
print(f"Maior faturamento: R$ {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
