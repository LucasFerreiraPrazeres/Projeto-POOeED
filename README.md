# Projeto Final - Programação e Estrutura de Dados

## Parte 1: Resolução de Tabela de endereços MAC
A tabela MAC é usada por um switch para mapear os endereços MAC (correspondente a algum dispositivo) conectado a interfaces (portas) específicas do Switch. Essa tabela expira a cada 5 minutos e é atualizada através da leitura dos dispositivos conectados a cada interface. A Figura 1 ilustra um exemplo de tabela de endereços MAC armazenada na memória do switch. 

Implemente um programa que seja capaz de descobrir a porta a qual um dispositivo está conectado a partir de um endereço MAC fornecido

## Requisitos funcionais:
* REQ 1. Cadastrar switches: importar informações dos switches que fazem parte da rede. O cadastro poderá ser feito através da criação manual ou a partir da leitura de um arquivo CSV. 
* REQ 2. Estruturar o objeto Switch contendo ao menos os seguintes atributos: nome, ip, mac, portas e tabela_mac. Um switch pode ter 4, 8, 16 ou 24 portas.
* REQ 3. Criar e popular tabela de endereços para armazenar um conjunto de endereços MAC e a porta correspondente. Cada switch deverá ter sua própria tabela de endereços.
* REQ 4. Não permitir que um endereço MAC inválido seja cadastrado na tabela de endereços
* REQ 5. Não permitir que múltiplos endereços MAC sejam armazenados em uma mesma porta na tabela de endereços. Qualquer estratégia de resolução de conflitos pode ser utilizada.
* REQ 6. Criar uma operação capaz de descobrir a porta na qual o dispositivo está conectado a partir de um endereço MAC fornecido como entrada.

## Requisitos não-funcionais:
* Implementar o projeto utilizando o Paradigma Orientado a Objetos. 
* Utilizar uma Tabela Hash para armazenar tabela de endereços MAC, tendo como índice a porta e como valor o endereço MAC. (não usar o dicionário de python)
* Utilizar exceções para o tratamento de erros (ex.: endereço mac inválido fornecido como entrada)

