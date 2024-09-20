# Sisbank 2.0

## Descrição

**Sisbank 2.0** é um sistema bancário básico desenvolvido em Python, projetado para gerenciar clientes, contas correntes e transações financeiras (saques e depósitos). O sistema utiliza o paradigma de programação orientada a objetos, com classes como `Cliente`, `Conta`, `ContaCorrente`, `PessoaFisica`, `Historico` e diferentes tipos de transações (`Deposito` e `Saque`).

Este sistema permite criar clientes e contas, além de realizar operações financeiras como depósitos, saques e consulta de extratos bancários. Há também um controle de limite de saques e saldo para contas correntes.

## Requisitos

- **Python 3.6+**
- Nenhuma biblioteca externa necessária

## Funcionalidades

- **Criar Cliente**: Cadastra um cliente com CPF, nome, data de nascimento e endereço.
- **Criar Conta Corrente**: Cria uma conta corrente e a associa a um cliente existente.
- **Realizar Depósito**: Permite realizar depósitos em uma conta corrente.
- **Realizar Saque**: Permite realizar saques em uma conta, respeitando os limites de saque e saldo.
- **Exibir Extrato**: Mostra o histórico de transações e o saldo atual de uma conta.
- **Listar Contas**: Exibe todas as contas cadastradas no sistema.

## Estrutura de Classes

### Cliente

- `Cliente`: Representa um cliente com um endereço e uma lista de contas associadas.
- `PessoaFisica`: Herda de `Cliente`, adicionando informações como nome, data de nascimento e CPF.

### Conta

- `Conta`: Classe base que gerencia saldo, agência, número da conta e histórico de transações.
- `ContaCorrente`: Herda de `Conta` e adiciona controle de limite de saque.

### Transações

- `Transacao`: Interface abstrata que define o método para registrar uma transação.
- `Deposito`: Herda de `Transacao` e representa uma operação de depósito.
- `Saque`: Herda de `Transacao` e representa uma operação de saque.

### Historico

- `Historico`: Armazena o histórico de transações associadas a uma conta.
