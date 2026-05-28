import requests
# pip install requests plyer pandas

import time
from datetime import datetime

# ======================================
# CONFIGURAÇÕES
# ======================================

CRIPTO = "bitcoin"
MOEDA = "brl"
INTERVALO = 60  

# Critérios de entrada
SUPORTE = 520000          # região de suporte
QUEDA_PERCENTUAL = 5      # queda mínima (%)
RSI_LIMITE = 30           # RSI abaixo disso = sobrevenda

# ======================================
# FUNÇÕES
# ======================================


def buscar_preco(cripto, moeda):
    """Busca preço atual pela API da CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": cripto,
        "vs_currencies": moeda
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        return dados[cripto][moeda]

    except Exception as erro:
        print(f"[ERRO] Falha ao buscar preço: {erro}")
        return None



def calcular_rsi(lista_precos, periodo=14):
    """
    Versão simplificada de RSI para estudo.
    Requer ao menos 15 preços.
    """

    if len(lista_precos) < periodo + 1:
        return None

    ganhos = []
    perdas = []

    for i in range(1, len(lista_precos)):
        diferenca = lista_precos[i] - lista_precos[i - 1]

        if diferenca > 0:
            ganhos.append(diferenca)
            perdas.append(0)
        else:
            ganhos.append(0)
            perdas.append(abs(diferenca))

    media_ganho = sum(ganhos[-periodo:]) / periodo
    media_perda = sum(perdas[-periodo:]) / periodo

    if media_perda == 0:
        return 100

    rs = media_ganho / media_perda
    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 2)



def verificar_alerta(preco_atual, preco_anterior, historico_precos):
    """
    Dispara alerta quando:
    - preço está próximo do suporte
    - houve queda relevante
    - RSI está abaixo do limite
    """

    proximo_suporte = preco_atual <= SUPORTE

    if preco_anterior is None:
        queda_relevante = False
    else:
        variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
        queda_relevante = variacao <= -QUEDA_PERCENTUAL

    rsi = calcular_rsi(historico_precos)
    rsi_baixo = rsi is not None and rsi < RSI_LIMITE

    print(f"RSI atual: {rsi if rsi is not None else 'coletando dados...'}")

    sinais = sum([proximo_suporte, queda_relevante, rsi_baixo])

    return sinais >= 2, rsi



def enviar_alerta(preco, rsi):
    """Envia notificação oficial do Windows."""

    mensagem = (
        f"BTC: {preco} {MOEDA.upper()}\n"
        f"Suporte: {SUPORTE} {MOEDA.upper()}\n"
        f"RSI: {rsi}\n"
        f"Possível oportunidade de compra."
    )

    print("\n" + "=" * 50)
    print("🚨 ALERTA DE OPORTUNIDADE - BITCOIN 🚨")
    print(mensagem)
    print(f"Horário: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 50 + "\n")



def monitorar():
    """Loop principal do bot."""

    print("\n=== BOT PROFISSIONAL DE MONITORAMENTO BTC ===")
    print(f"Cripto: {CRIPTO}")
    print(f"Moeda: {MOEDA.upper()}")
    print(f"Suporte definido: {SUPORTE}")
    print(f"Queda mínima: {QUEDA_PERCENTUAL}%")
    print(f"RSI limite: {RSI_LIMITE}")
    print(f"Intervalo: {INTERVALO} segundos")
    print("=============================================\n")

    preco_anterior = None
    historico_precos = []

    while True:
        preco = buscar_preco(CRIPTO, MOEDA)

        if preco is not None:
            agora = datetime.now().strftime("%H:%M:%S")
            print(f"[{agora}] BTC atual: {preco} {MOEDA.upper()}")

            historico_precos.append(preco)

            if len(historico_precos) > 30:
                historico_precos.pop(0)

            alerta, rsi = verificar_alerta(
                preco,
                preco_anterior,
                historico_precos
            )

            if alerta:
                enviar_alerta(preco, rsi)
                continue

            preco_anterior = preco

        time.sleep(INTERVALO)


# ======================================
# EXECUÇÃO
# ======================================

if __name__ == "__main__":
    monitorar()
