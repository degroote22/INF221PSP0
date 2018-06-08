# Detector de impedimentos - Requerimentos de Software

## Requisitos funcionais:
1. Determinar se algum jogador atacante está impedido.
    > Um jogador está impedido se ele está mais próximo da linha do gol do oponente do que o penúltimo adversário. Um jogador não está impedido se:
    >* ele está na mesma linha que o penúltimo adversário ou
    >* ele está na mesma linha que os dois últimos adversários.

## Requisitos não funcionais:
1. Determinar a resposta em menos de 1 segundo.
2. Validar a entrada do programa para garantir execução segura.
2. Fornecer erros claros quando a entrada for mal formatada.