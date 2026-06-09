---
name: Decisão Arquitetural / Adaptação
about: Propor uma adaptação de método ou nova regra de projeto
title: 'decision: [Qual é a decisão a ser tomada?]'
labels: decision
assignees: ''
---

<!-- 
SOBRE ESTE ARQUIVO:
Responsabilidade principal: Gerente de Configuração.
Uso: Formalizar discussões prévias sobre limitações do Python em relação ao Java. O resultado desta issue deve alimentar o arquivo adaptacoes.md ou gerar um novo ADR.
-->

## Contexto e Motivação
[Qual é o impasse técnico? Ex: O método String.intern() no Java lida com o pool de memória de forma específica que não pode ser forçada no CPython sem perda de desempenho]

## Alternativa Proposta
[Descreva qual será a abordagem da equipe. Ex: Deixar o método de fora da implementação e documentar a justificativa técnica]

## Impacto da Decisão
[Quais arquivos precisarão ser atualizados pelo Gerente de Configuração se essa decisão for aprovada pela equipe?]
- [ ] Atualizar `docs/adaptacoes.md`
- [ ] Criar novo ADR em `docs/adr/`
- [ ] Atualizar `README.md`