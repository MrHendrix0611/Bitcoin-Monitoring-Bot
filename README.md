# 🚀 Bitcoin Monitoring Bot

Bot de monitoramento de preço do Bitcoin utilizando a API da CoinGecko.
O sistema analisa o mercado em tempo real e identifica possíveis oportunidades de compra com base em:

* Região de suporte
* Queda percentual
* Indicador RSI (Relative Strength Index)

---

# 📌 Funcionalidades

✅ Monitoramento automático do preço do Bitcoin
✅ Consulta em tempo real via API da CoinGecko
✅ Cálculo simplificado de RSI
✅ Detecção de sobrevenda
✅ Identificação de quedas bruscas
✅ Sistema de alerta de oportunidade
✅ Atualização contínua em loop

---

# 🧠 Estratégia Utilizada

O bot gera um alerta quando pelo menos **2 dos critérios abaixo** forem atendidos:

### 1. Preço próximo do suporte

```python
SUPORTE = 520000
```

---

### 2. Queda percentual relevante

```python
QUEDA_PERCENTUAL = 5
```

Exemplo:

* Se o preço cair mais de 5% em relação ao valor anterior.

---

### 3. RSI abaixo do limite

```python
RSI_LIMITE = 30
```

RSI abaixo de 30 normalmente indica condição de sobrevenda.

---

# 📦 Tecnologias Utilizadas

* Python 3
* Requests
* API CoinGecko
* Datetime
* Time

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/MrHendrix0611/Bitcoin-Monitoring-Bot.git
```

Entre na pasta:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install requests
```

---

# ▶️ Como Executar

Execute o arquivo principal:

```bash
python main.py
```

---

# 🔧 Configurações

Você pode alterar facilmente os parâmetros do bot:

```python
CRIPTO = "bitcoin"
MOEDA = "brl"
INTERVALO = 60
SUPORTE = 520000
QUEDA_PERCENTUAL = 5
RSI_LIMITE = 30
```

| Configuração       | Descrição                  |
| ------------------ | -------------------------- |
| `CRIPTO`           | Criptomoeda monitorada     |
| `MOEDA`            | Moeda de conversão         |
| `INTERVALO`        | Tempo entre consultas      |
| `SUPORTE`          | Região de suporte          |
| `QUEDA_PERCENTUAL` | Percentual mínimo de queda |
| `RSI_LIMITE`       | Limite inferior do RSI     |

---

# 📊 Exemplo de Saída

```bash
[14:22:01] BTC atual: 518000 BRL
RSI atual: 28.5

==================================================
🚨 ALERTA DE OPORTUNIDADE - BITCOIN 🚨
BTC: 518000 BRL
Suporte: 520000 BRL
RSI: 28.5
Possível oportunidade de compra.
==================================================
```

---

# 🌐 API Utilizada

Este projeto utiliza a API pública da CoinGecko:

https://www.coingecko.com/

---

# 📈 Melhorias Futuras

* [ ] Notificações no Windows
* [ ] Dashboard gráfico
* [ ] Integração com Telegram
* [ ] Suporte a múltiplas criptomoedas
* [ ] Banco de dados para histórico
* [ ] Estratégias mais avançadas
* [ ] Média móvel
* [ ] MACD
* [ ] Backtesting

---

# ⚠️ Aviso

Este projeto possui finalidade educacional e não representa recomendação financeira.

O mercado de criptomoedas possui alto risco. Utilize por sua conta e risco.

---

# 👨‍💻 Autor

Desenvolvido por Guilherme Silva 🚀
Github: https://github.com/MrHendrix0611
