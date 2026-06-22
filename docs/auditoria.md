# Auditoria Interna - Release v1.0.0 (Product)

## Sobre este documento
Este documento formaliza a auditoria interna da equipe referente ao projeto *Javalang-py* para a disciplina de Gerência de Configuração de Software (GCS 2026.1). O objetivo é demonstrar a integridade do processo seguido, a rastreabilidade dos artefatos e apresentar uma reflexão crítica sobre a execução das metodologias ágeis e de configuração.

---

### 1. Os processos definidos no início do projeto foram seguidos? Onde houve desvios e por quê?
*Resposta:* Sim, a fundação processual estabelecida na Baseline v0.1-functional foi rigorosamente mantida. O *GitHub Flow* (ADR 0002) foi seguido, mantendo a branch main protegida contra commits diretos. A metodologia *Test-Driven Development* (ADR 0004) guiou a implementação: os desenvolvedores só submetiam lógicas após a Engenharia de Qualidade (QA) estruturar os casos falhos (ciclo RED/GREEN). Além disso, a Integração Contínua (CI) operou validando lint (ruff) e testes (pytest) em 100% dos PRs.

*Desvios Justificados:* O principal desvio referiu-se ao engessamento inicial causado pelo TDD atrelado à regra de limite de contribuição (máximo de 7 métodos por PR). O fluxo estrito bloqueava os desenvolvedores enquanto os testes não eram integrados. Para mitigar isso sem quebrar a regra, a equipe desviou para um fluxo de "fragmentação extrema", visível na classe JString, onde o desenvolvimento precisou ser quebrado em quase 10 issues concorrentes (Ex: *Issues #52 a #61). Outro desvio temporário foi um débito técnico na JFloat (Issue #40*), que foi retido intencionalmente e incorporado posteriormente de forma segura.
Exceção de Trabalho na Interoperabilidade: Conforme o escopo original, a integração entre classes deveria ocorrer nas baselines v0.3 e v0.4. No entanto, a equipe adotou uma exceção de trabalho formal, deslocando a execução da suíte de testes de interoperabilidade cruzada (e as respectivas correções nos métodos base) para a release final v1.0.0.

### 2. A rastreabilidade entre issues, PRs e commits está íntegra?
*Resposta:* Sim, a rastreabilidade do projeto é completa de ponta a ponta. 
* *Issues e PRs:* Nenhuma linha de código lógico foi mesclada sem nascer de uma Issue pré-aprovada e classificada com labels formais (feature, bug, docs, decision). Os Pull Requests utilizaram sistematicamente as palavras-chave de fechamento (ex: Closes #X).
* *Commits Semânticos:* Todos os commits seguiram o padrão de prefixos (feat:, docs:, chore:, test:) com referência final à issue trabalhada (ex: refs #67, refs #80).
* *Tratamento de Duplicatas:* A integridade do Kanban foi mantida com o tratamento formal de gargalos. Um grande exemplo de rastreabilidade limpa ocorreu com a *Issue #57, que, ao colidir escopos de busca, foi devidamente identificada e fechada com a *label Duplicate, preservando a clareza do histórico.
* *Uso de IA:* A declaração de uso de ferramentas generativas foi extensamente documentada em docs/uso-de-ia.md, evidenciando os prompts exatos e as funções geradas, confirmando a autoria e responsabilidade dos desenvolvedores.

### 3. As baselines foram efetivamente respeitadas, ou houve mudanças posteriores não-formais?
*Resposta:* As baselines foram integralmente respeitadas e demarcadas através das marcações de Tag/Release (v0.1-functional, v0.2-jinteger, v0.3-jfloat, v0.4-jstring, v1.0.0-product). 

Não houve nenhuma alteração não-formal ("ajuste silencioso") e o uso de force push não foi feito em momento algum na branch principal. Prova do respeito à imutabilidade e resolução de processos são as atas geradas para os grandes conflitos de merge enfrentados pela equipe. Os conflitos não foram reescritos na história, mas resolvidos na ramificação e registrados na *Issue #62* (Conflito no arquivo de testes) e na *Issue #65* (Conflito secundário de merge), demonstrando domínio do sistema de controle de versão distribuído.

### 4. Quais foram as principais lições aprendidas, e o que seria feito diferente em um próximo projeto?
*Lições Aprendidas:*
1. *Fidelidade à Especificação e Limitações Linguísticas:* A equipe aprendeu profundamente sobre o modelo de memória de diferentes linguagens. Simular as coerções primitivas (narrowing cast), precisões fixas de 32 bits (onde o Python possui precisão arbitrária) e o armazenamento interno IEEE 754 (onde Python usa 64 bits nativos) exigiu maestria matemática, resultando em soluções de baixo nível com máscaras binárias (& 0xFFFFFFFF) e manipulação direta de bytes usando o módulo nativo struct.
2. *Custo do Processo:* Comprovamos na prática que o controle de versão restrito (limite baixo de commits) força um design modular e PRs extremamente coesos, embora aumente vertiginosamente o overhead de integração (discussão, Code Review, resolução de conflitos).

*O que faríamos diferente:*
Em um projeto futuro, paralelizaríamos melhor a fase de infraestrutura de QA. Criaríamos imediatamente stubs estéreis de todas as classes com retorno vazio apenas para unificar os imports, evitando assim a alta frequência de quebra de testes e gargalos que seguraram os feature branches nos Sprints de JInteger e JFloat.