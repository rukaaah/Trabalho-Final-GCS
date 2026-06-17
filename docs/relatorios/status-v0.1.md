# Relatório de Status - Baseline v0.1 (Setup Inicial)

## Sobre este documento

Este documento é de responsabilidade do **Relator**, [Cleiton Pinheiro](https://github.com/Ton-07), da equipe. O relatório de status é gerado e submetido via Pull Request ao final de cada ciclo de desenvolvimento, servindo como um "retrato" oficial da saúde do projeto no momento em que uma nova baseline (Release/Tag) é fechada.

O objetivo é garantir total transparência sobre o que foi entregue, as métricas de qualidade, os riscos identificados no período e o planejamento para o próximo ciclo de desenvolvimento.

---

## Relatório Atual: v0.1.0 (Functional / Setup)

**Data de Fechamento:** 16/06/2026
**Período de Referência:** Início do projeto até 16/06/2026
**Responsável pelo Relatório:** [Cleiton Pinheiro](https://github.com/Ton-07)

### 1. Resumo Executivo
Nesta primeira etapa (Sprint 1), a equipe concluiu com sucesso o setup inicial do repositório, estabelecendo toda a infraestrutura e a documentação de processos exigidas pela disciplina. O foco desta baseline foi preparar o ambiente, configurar o pipeline de Integração Contínua (CI/CD), estruturar os templates de GitHub e aprovar as decisões arquiteturais (ADRs). Com isso, garantimos que o repositório esteja maduro e pronto para o início do desenvolvimento técnico. A equipe de Qualidade encontra-se, neste exato momento, estruturando as suítes bases de testes (TDD).

### 2. Entregas Realizadas
Durante este período, consolidamos os itens de configuração base do projeto e inicializamos o fluxo de controle de mudanças. Todos os artefatos obrigatórios foram devidamente mapeados, revisados e integrados.

* **Issues Fechadas / Resolvidas:**
  * **Issue #3:** `decision: [Qual é a decisão a ser tomada?]` — Discussão técnica e fechamento das primeiras definições arquiteturais da equipe.
  * **Issue #9:** `docs: Relatório de status da Baseline v0.1-functional` — Elaboração formal deste próprio documento de auditoria e acompanhamento.
  * **Issue #10:** `chore: Configuração do pipeline de Integração Contínua (CI)` — Estruturação do fluxo automatizado de integração contínua.

* **Pull Requests Mesclados (Aprovados):**
  * **PR #1:** `docs(adr): adiciona ADR 0001 sobre nomenclatura de classes e metodos` — Formaliza as regras de nomenclatura do projeto.
  * **PR #2:** `docs(adr): adiciona ADR 0002 sobre modelo de ramificacao e integracao` — Consolida as diretrizes do GitHub Flow.
  * **PR #4:** `docs(adr): adiciona ADR 0004 sobre fluxo de desenvolvimento TDD` — Estabelece a metodologia de testes iniciais.
  * **PR #5:** `docs(adr): adiciona ADR 0003 sobre dependencias da classe Locale` — Define a política de omissão e tratamento regional.
  * **PR #8:** `chore: configura pipeline de CI com ruff e pytest` — Estruturação do fluxo automatizado de integração contínua (vinculado à Issue #10).

### 3. Métricas do Período
Como nos encontramos na etapa "Functional" e as construções das suítes de testes estão em andamento e revisão no momento, não houve submissão de código lógico interno das classes; logo, a cobertura de testes atual está em 0%. Contudo, o pipeline de Integração Contínua via GitHub Actions foi homologado com sucesso e encontra-se plenamente ativo (`PR #8`). O ambiente virtual está validado para executar automações de análise estática (`ruff`) e execução de testes (`pytest`), garantindo que nenhum código fora dos padrões definidos seja mesclado a partir dos próximos sprints.

### 4. Adaptações e Decisões Formais
A equipe debateu, aprovou e documentou quatro diretrizes de arquitetura fundamentais para o andamento do projeto:
* **ADR 0001 (Nomenclatura):** Decisão deliberada de adotar a grafia `camelCase`.
* **ADR 0002 (Modelo de Ramificação):** Implementação estrita do GitHub Flow, blindando a branch `main` contra commits diretos e estabelecendo revisões por pares obrigatórias em todos os Pull Requests.
* **ADR 0003 (Tratamento de Locale):** Omissão de métodos dependentes de instâncias complexas de `Locale`, mapeando as assinaturas no catálogo de `adaptacoes.md`.
* **ADR 0004 (Fluxo de Integração):** Instituição do modelo Test-Driven Development (TDD / Test-First), obrigando o time de Engenharia de Qualidade a redigir e acoplar a suíte de testes antes do início do desenvolvimento lógico de qualquer método.

### 5. Riscos e Impedimentos Atuais
A dinâmica estrita de TDD revelou que a elaboração das suítes de testes precisará de atenção extra e revisões profundas para não gerar quebra de contrato. Pull Requests referentes aos testes base precisaram de recusa e correção neste fim de ciclo, caracterizando-se como o bloqueio imediato para o time de desenvolvimento. O Engenheiro de Qualidade focará em alinhar essa implementação para disponibilizar a base do `JInteger`. Adicionalmente, o time precisará monitorar de perto os limites rígidos de GCS (máximo de 3 métodos por commit e 7 métodos/testes por PR).

### 6. Próximos Passos (Para a Baseline v0.2)
Com a homologação desta fundação inicial e do pipeline de CI, o trabalho do Sprint 2 será inteiramente direcionado ao desenvolvimento da classe `JInteger`.
* **Mapeamento de Tarefas do Próximo Ciclo (Milestone v0.2-jinteger):**
  * **Issue #11:** `feat: [Integer] Implementar Constantes e Construtor Integer(int)`
  * **Issue #12:** `feat: [Integer] Implementar Integer(String) e Conversões Numéricas Primitivas`
  * **Issue #13:** `feat: [Integer] Implementar métodos herdados de Object (toString, equals, hashCode) em JInteger`