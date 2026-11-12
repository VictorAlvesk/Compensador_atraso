# Compensador de Atraso


Projeto de um compensador do tipo atraso para o Exemplo 2 do material *SC_Cap4_03a_atraso.pdf*, fazendo o tempo de acomodação ficar 4 vezes maior que o do sistema sem compensação (C = 1).

## Arquivos

- `compensador_atraso.py` – código do projeto
- `requirements.txt` – bibliotecas necessárias

## Como executar

É preciso ter o Python instalado. Abra o terminal na pasta do projeto e rode:

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

## Resultados

Parâmetros obtidos:

- K = 9,25
- α = 16
- T = 0,125

C(s) = 9,25 · (1 + 0,125s) / (1 + 2s)

| | Sem compensação | Com atraso |
|---|---|---|
| Máximo sobressinal | 0,88 % | 30,60 % |
| Tempo de acomodação | 0,673 s | 3,092 s |
| Tempo de pico | 0,947 s | 0,947 s |

O tempo de acomodação ficou cerca de 4,6 vezes maior. A diferença em relação a 4 vem da aproximação Ts ≈ 4/σ usada no projeto. O tempo de pico se manteve, como esperado.

## Problemas comuns

- **`No module named 'control'`**: o ambiente virtual não está ativado. Rode o comando `activate` de novo.
- **`Permissão negada` ao ativar no Linux**: falta o `source` na frente do comando.
- **Erro envolvendo NumPy e SciPy**: acontece quando os pacotes são misturados com os do sistema. Usando o ambiente virtual como descrito acima, isso não ocorre.
