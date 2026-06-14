# ADR 0004: Adoção de TDD (Test-First) como Fluxo de Integração

## Sobre este documento
Este arquivo é um Registro de Decisão Arquitetural (ADR). Ele documenta o fluxo oficial de desenvolvimento e testes adotado pela equipe.
**Responsável pela manutenção:** Gerente de Configuração, [Angelo Antônio](https://github.com/angelo-acds).

## Status
Aceito

## Contexto
A equipe precisava definir a ordem de execução entre a codificação das classes (`JString`, `JInteger`, `JFloat`) e a criação dos testes automatizados. A ausência dessa definição poderia gerar quebras de contrato com a especificação original do Java SE 8 ou causar retrabalho severo durante a integração nos Pull Requests.

## Decisão
A equipe decidiu adotar a abordagem **Test-Driven Development (TDD) / Test-First**:
1. O time de Quality (QA) é responsável por iniciar o ciclo de cada funcionalidade, escrevendo os testes automatizados com base na documentação oficial do Java SE 8.
2. O desenvolvimento do código só poderá ser iniciado em cima da suíte de testes já criada pelo QA.
3. Os desenvolvedores utilizarão os testes (inicialmente falhos) como guia estrito de implementação e deverão escrever o código apenas com o objetivo de fazê-los passar.

## Consequências
* **Positivas:** Garante aderência de 100% à especificação exigida pelo escopo do trabalho, evitando que o código seja enviesado pela lógica do desenvolvedor.
* **Negativas:** Cria um bloqueio de cronograma inicial; os desenvolvedores ficarão ociosos aguardando a finalização da suíte básica de testes. Exigirá um planejamento rigoroso de tarefas para mitigar esse gargalo.