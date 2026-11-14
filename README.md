# Compensador de Atraso – Exemplo 2

**Aluno:** Victor Alves Freire De Queiroz
**Matrícula:** 202307122

Projeto de um compensador do tipo Atraso, fazendo o tempo de acomodação ficar 4 vezes maior que o do sistema sem compensação (C = 1).

## Arquivos

- `compensador_atraso.py` – código do projeto
- `requirements.txt` – bibliotecas necessárias

## Como executar

É preciso ter o Python 3 instalado. Abra o terminal na pasta do projeto e rode:

**Linux / Mac**

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python compensador_atraso.py
```

**Windows**

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python compensador_atraso.py
```


## O que aparece

No terminal são mostrados os parâmetros do compensador e os dados da resposta ao degrau, com e sem compensação. Em seguida abre o gráfico comparando as duas respostas, que também é salvo como `resposta_degrau.png`.

## Como foi feito

1. Sem compensação, os polos ficam em s = −5 ± j3,3166, o que dá Ts ≈ 4/σ = 0,8 s e Tp = 0,9472 s.
2. Para Ts 4x maior, σ passa a 5/4 = 1,25, mantendo ωd = 3,3166 rad/s para o Tp não mudar. O polo desejado é s1 = −1,25 ± j3,3166, com equação s² + 2,5s + 12,5625 = 0.
3. O zero do compensador foi colocado em −8, cancelando o polo mais afastado da planta (T = 1/8).
4. Comparando os coeficientes de s² + (2 + 8/α)s + (16 + 20K)/α = 0 com a equação desejada, saem α = 16 e K = 9,25.

## Resultados alcançados

### Parâmetros do compensador de atraso

- **K = 9,25**
- **α = 16**
- **T = 0,125**

C(s) = 9,25 · (1 + 0,125s) / (1 + 2s) = 0,5781 · (s + 8) / (s + 0,5)

### Resposta ao degrau unitário após a compensação

- **Máximo sobressinal:** 30,60 %
- **Tempo de acomodação (critério de 2%):** 3,092 s
- **Tempo de pico:** 0,947 s

### Comparação com o sistema sem compensação

| | Sem compensação | Com atraso |
|---|---|---|
| Máximo sobressinal | 0,88 % | 30,60 % |
| Tempo de acomodação | 0,673 s | 3,092 s |
| Tempo de pico | 0,947 s | 0,947 s |
| Valor final | 0,556 | 0,920 |
| Erro estacionário | 0,444 | 0,080 |

### Especificações atendidas

| Especificação | Pedido | Obtido |
|---|---|---|
| Aumento do tempo de acomodação | 4x maior | 4,59x maior |

O tempo de acomodação ficou cerca de 4,6 vezes maior. A diferença em relação a 4 vem da aproximação Ts ≈ 4/σ usada no projeto, a mesma que aparece no exemplo do material (o pedido de 2x resultou em 2,1x). O tempo de pico se manteve, e o erro estacionário caiu de 0,444 para 0,080. O sobressinal aumentou porque σ diminuiu com ωd fixo, o que reduz o amortecimento.