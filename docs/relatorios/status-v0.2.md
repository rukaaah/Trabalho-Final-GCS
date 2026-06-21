# Relatório de Status - Baseline v0.2 (Allocated · JInteger)

## Sobre este documento

Este documento é de responsabilidade do **Relator**, [Cleiton Pinheiro](https://github.com/Ton-07), da equipe. O relatório de status é gerado e submetido via Pull Request ao final de cada ciclo de desenvolvimento, servindo como um "retrato" oficial da saúde do projeto no momento em que uma nova baseline (Release/Tag) é fechada.

O objetivo é garantir total transparência sobre o que foi entregue, as métricas de qualidade, os riscos identificados no período e o planejamento para o próximo ciclo de desenvolvimento.

---

## Relatório Atual: v0.2.0 (Allocated · JInteger)

**Data de Fechamento:** 20/06/2026
**Período de Referência:** 17/06/2026 até 20/06/2026
**Responsável pelo Relatório:** [Cleiton Pinheiro](https://github.com/Ton-07)

### 1. Resumo Executivo
Nesta segunda etapa (Sprint 2), a equipe alcançou a **Baseline v0.2-jinteger** entregando a implementação completa da classe `JInteger` (~40 métodos), replicando o contrato público do Java SE 8. O desenvolvimento seguiu estritamente o fluxo TDD (Test-First) estabelecido na ADR 0004. Enfrentamos e superamos os desafios de tipagem do Python (precisão arbitrária vs. 32-bits) documentando todas as adaptações arquiteturais. A integração contínua manteve-se verde, e as regras anti-atalho (limites estritos de métodos por commit e PR) foram rigorosamente respeitadas através da fragmentação de tarefas.

### 2. Entregas Realizadas
Todo o escopo da classe `JInteger` foi construído e homologado. A equipe fragmentou o desenvolvimento em múltiplas issues para não violar o limite de 7 métodos/testes da disciplina.

* **Issues Fechadas / Resolvidas (Milestone v0.2):**
  * **Issue #11:** `feat: [Integer] Implementar Constantes e Construtor Integer(int)`
  * **Issue #12:** `feat: [Integer] Implementar Integer(String) e Conversões Numéricas Primitivas`
  * **Issue #13:** `feat: [Integer] Implementar métodos herdados de Object (toString, equals, hashCode) em JInteger`
  * **Issue #19:** `feat: [Integer] Implementar Parsing Básico em JInteger (parseInt e parseUnsignedInt)`
  * **Issue #20:** `feat: [Integer] Implementar Formatação por Base (toString, toBinary, toHex, toOctal) em JInteger`
  * **Issue #21:** `feat: [Integer] Implementar Parsing Avançado (valueOf e decode) em JInteger`
  * **Issue #22:** `feat: [Integer] Implementar Formatação Unsigned em JInteger`
  * **Issue #23:** `feat: [Integer] Implementar Aritmética Estática Básica em JInteger`
  * **Issue #24:** `feat: [Integer] Implementar Aritmética Estática Unsigned em JInteger`
  * **Issue #25:** `feat: [Integer] Implementar Operações Bit a Bit (Contagem e Sinal) em JInteger`
  * **Issue #27:** `feat: [Integer] Implementar Operações Bit a Bit (Zeros e Rotação) em JInteger`
  * **Issue #28:** `feat: [Integer] Implementar Operações Bit a Bit (Reversão) em JInteger`
  * **Issue #48:** `docs: padronizar entradas do docs/adaptacoes.md da baseline JInteger conforme template oficial`
  * **Issue #62:** `docs: Resgatar registro de resolução de conflito de merge`

* **Pull Requests Mesclados (Aprovados):**
  *(Nota: Todos os PRs abaixo foram revisados por pares e passaram pelo pipeline de testes)*
  * PRs referentes à integração das **Issues #11, #12 e #13** (Núcleo base, conversões primitivas e Object).
  * PRs referentes à integração das **Issues #19, #20, #21 e #22** (Parsing numérico, formatação de bases e strings Unsigned).
  * PRs referentes à integração das **Issues #23, #24, #25, #27 e #28** (Aritmética básica/unsigned, contagem, rotação e espelhamento de bits).
  * PRs de infraestrutura e documentação: Resolução de conflito (**Issue #62**) e documentação oficial de adaptações (**Issue #48**).

### 3. Métricas do Período
Nesta baseline começamos a gerar código lógico de produção e casos de testes reais. A suíte em `tests/test_jinteger.py` conta agora com dezenas de validações exaustivas de *boundary values* (como `MAX_VALUE`, `MIN_VALUE` e comportamento de inteiros negativos em métodos *unsigned* e bitwise). A Integração Contínua (CI) via GitHub Actions foi disparada a cada PR e operou 100% no verde. A cobertura de testes do arquivo `javalang/jinteger.py` atende aos padrões do fluxo TDD. A rastreabilidade do uso de ferramentas de IA generativa foi extensa e devidamente registrada com prompts detalhados no arquivo `docs/uso-de-ia.md`.

### 4. Adaptações e Decisões Formais
O desenvolvimento do `JInteger` gerou uma carga densa de adaptações arquiteturais devido à ausência de tipos primitivos (de 32-bits) e suporte a *method overloading* no Python. Todas foram oficializadas no PR de adaptações (**Issue #48**):
* **Aritmética e Bitwise Unsigned:** Como o Python tem inteiros de precisão arbitrária, adotamos internamente a máscara bitwise `& 0xFFFFFFFF` para simular o comportamento de truncamento estrito de 32 bits do Java e tratar corretamente números negativos em operações de *shift*, formatação e divisão *unsigned*.
* **Sobrecarga de Métodos:** Não havendo suporte nativo no Python, métodos como `parseInt`, `valueOf`, `toUnsignedString` e `toString` tiveram suas assinaturas unificadas através de argumentos de *default* (ex: `radix=10`) e *type dispatch* interno, respeitando estritamente a semântica e exceções originais do Java.
* **IntegerCache:** O *pool* nativo do Java para otimização de valores entre -128 a 127 foi perfeitamente simulado com um dicionário interno no nível do módulo, acessado via `valueOf`.

### 5. Riscos e Impedimentos Atuais
Como antecipado no relatório anterior, o rigor do processo fragmentado de GCS impôs desafios de integração e versionamento cruzado. Tivemos nossos primeiros casos de conflito de merge estruturais, com um importante na suíte de testes documentado na **Issue #62** e um segundo conflito em tratamento neste exato momento (**Issue Aberta #65 - conflito de merge 02**). A equipe resolveu o conflito inicial priorizando a base de testes correta do TDD. A ação foi documentada em ata no final do `README.md` como prova de auditoria e destreza da equipe com o controle de versão distribuído.

### 6. Próximos Passos (Para a Baseline v0.3)
Com o `JInteger` entregue e a equipe rodando em velocidade de cruzeiro no GitHub Flow, o Sprint 3 focará paralelamente na classe `JFloat` e nas bases da classe `JString`.
* **Mapeamento de Tarefas do Próximo Ciclo (Milestones v0.3 e v0.4):**
  * `feat: [jfloat] implementar comparações e validações de estado IEEE 754` (Issue #39)
  * `feat: [jfloat] implementar parsing de strings e formatação` (Issue #40)
  * `feat: [jfloat] implementar manipulação de bits e aritmética` (Issue #41)
  * Iniciar núcleo e construtores base da ramificação `v0.4-jstring` (Issues #52, #53).