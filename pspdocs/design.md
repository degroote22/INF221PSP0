# Casos de uso

## Jogador impedido:
Um jogador está impedido se ele está mais próximo da linha do gol do oponente do que o penúltimo adversário.


## Jogador não impedido
Um jogador não está impedido se:
* ele está na mesma linha que o penúltimo adversário ou
* ele está na mesma linha que os dois últimos adversários.
* ele está mais longe da linha do gol do que o penúltimo adversário.


# Algoritmo
## Validação da entrada

> O programa lê a primeira linha do arquivo de texto. Esta linha contem dois números. A e D que representam o número de jogadores do time atacante envolvidos na entrada seguidos do número de jogadores do time defensor envolvidos na jogada. Nas duas linhas seguintes, estão as distâncias dos jogadores do time atacante e defensivo, distribuídas uma linha para cada time.

> A entrada do programa pode executar quantos casos desses quiser e ao final da execução de cada caso é impresso Y caso exista jogador do time A impedido e N caso contrário.

> O programa finaliza a execução quando for encontrado uma entrada tal que A == 0 e D == 0.

> O número de atacantes deve ser maior ou igual a 2 e menor ou igual a 11.

> O número de defensores deve ser maior ou igual a 2 e menor ou igual a 11.

## Solução do problema
> Sejam An os jogadores atacantes.

> Sejam Bn os jogadores defensivos, ordenados pela distância do gol, sendo B0 o mais próximo.

> Haverá impedimento se a *Posição de A* for **estritamente** menor do que a *Posição de B1*. Caso contrário, não há impedimento.