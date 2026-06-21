# Relatório de Status - Baseline v0.4 (Allocated · JString)

## Sobre este documento

Este documento é de responsabilidade do **Relator**, [Cleiton Pinheiro](https://github.com/Ton-07), da equipe. O relatório de status é gerado e submetido via Pull Request ao final de cada ciclo de desenvolvimento, servindo como um "retrato" oficial da saúde do projeto no momento em que uma nova baseline (Release/Tag) é fechada.

O objetivo é garantir total transparência sobre o que foi entregue, as métricas de qualidade, os riscos identificados no período e o planejamento para o próximo ciclo de desenvolvimento.

---

## Relatório Atual: v0.4.0 (Allocated · JString)

**Data de Fechamento:** 22/06/2026
**Período de Referência:** 21/06/2026 até 22/06/2026
**Responsável pelo Relatório:** [Cleiton Pinheiro](https://github.com/Ton-07)

### 1. Resumo Executivo
Nesta quarta etapa (Sprint 4), a equipe superou o maior desafio técnico do repositório, consolidando a **Baseline v0.4-jstring**. Entregamos a implementação massiva da classe `JString` (~60 métodos). O processo de engenharia foi intenso, exigindo uma extensa fragmentação de tarefas para evitar violações das regras anti-atalho de limite de commits. A equipe lidou brilhantemente com as diferenças entre a gestão de *arrays* (`char[]`, `byte[]`) do Java e do Python, padronizou tratamentos de codificação (UTF-8, codepoints) e implementou substituições idiomáticas com o módulo `re` (Regex). O pipeline de CI permaneceu impecável e a rastreabilidade está garantida.

### 2. Entregas Realizadas
A totalidade do núcleo da classe `JString` foi implementada e testada. A equipe precisou gerenciar quase uma dezena de ramificações concorrentes.

* **Issues Fechadas / Resolvidas (Milestone v0.4):**
  * **Issue #52:** `feat: [String] Implementar Núcleo Base (Construtores Simples e Acesso)`
  * **Issue #53:** `feat: [String] Implementar Construtores de Arrays e Decodificação`
  * **Issue #54:** `feat: [String] Implementar Comparações Lexicográficas e Igualdade`
  * **Issue #55:** `feat: [String] Implementar Tratamento de Unicode e Codificação`
  * **Issue #56:** `feat: [String] Implementar Busca Base (indexOf e lastIndexOf Parte 1)`
  * **Issue #57:** `feat: [String] Implementar Extração (Substring) e Busca Complementar` *(Fechada como Duplicata de rastreamento - Duplicate)*
  * **Issue #58:** `feat: [String] Implementar Extração (Substring) e Busca Complementar`
  * **Issue #59:** `feat: [String] Implementar Transformações e Formatação Base`
  * **Issue #60:** `feat: [String] Implementar Regex, Splits e Controle Interno`
  * **Issue #61:** `feat: [String] Implementar Utilitários Estáticos (valueOf e format)`
  * **Issue #76:** `feat: [String] Criação de stubs para o módulo String`

* **Pull Requests Mesclados (Aprovados):**
  *(Nota: Todos os PRs abaixo foram revisados por pares e mesclados após validação TDD na pipeline verde)*
  * PRs do núcleo, acesso, construtores de *array* (char/bytes) e manipulação de Unicode (**Issues #52, #53 e #55**).
  * PRs de buscas, igualdade, comparações lexicográficas e extração (**Issues #54, #56 e #58**).
  * PRs de transformações, Regex (`re`), formatação e métodos estáticos utilitários (**Issues #59, #60, #61** e os stubs iniciais da **#76**).

### 3. Métricas do Período
Devido à vasta quantidade de métodos (~60), a suíte de testes `test_jstring.py` foi amplamente explorada. Garantimos mais de 40 cenários de *asserts* distintos cobrindo instâncias vazias, limites de índices (`IndexError`), *overloading* em buscas e conversões de *codepoints*. A inteligência do rastreio de issues brilhou ao identificarmos e fecharmos formalmente a **Issue #57** como *Duplicate*, mantendo a higiene do Kanban.

### 4. Adaptações e Decisões Formais
Para suportar as especificidades da `JString` sem ferir os conceitos do Python, a equipe adicionou adaptações avançadas em `docs/adaptacoes.md`:
* **Ausência de Overloading:** Quase todas as categorias de métodos (`valueOf`, `substring`, `indexOf`, construtores) tiveram suas sobrecargas aglutinadas utilizando parâmetros variáveis (`*args`), checagem dinâmica (`isinstance`) e valores `default` (*type dispatch* idiomático).
* **StringBuilder:** Conforme acordado arquiteturalmente, o Python não se beneficia da classe `StringBuilder` para otimização de concatenação. O construtor focado nessa integração não foi portado, lançando formalmente um `NotImplementedError` caso invocado.
* **String Pool (`intern`):** O gerenciamento de memória em *pool* do CPython difere do Java. O método `intern()` foi mantido estruturalmente, mas adaptado como um *stub* que retorna a própria instância (`return self`), visto que a otimização de runtime requerida não se aplica.
* **Unicode/CodePoints:** Como o Python 3 trata strings de forma nativa sem problemas com *surrogate pairs* (comum no Java), métodos como `codePointAt` e `codePointCount` foram simplificados utilizando as funções buit-in `ord()` e `len()` em blocos segmentados da string, otimizando drasticamente o desempenho.

### 5. Riscos e Impedimentos Atuais
O grande gargalo desta Sprint foi, sem dúvida, orquestrar a regra anti-atalho de *7 métodos por PR/Issue* num escopo tão largo. A criação dos stubs iniciais (Issue #76) foi crucial para evitar *merge conflicts* em blocos adjacentes. Como todos os métodos funcionais foram entregues, não há débitos técnicos para as classes. O foco (e risco final) volta-se para a integração sistêmica (Interop).

### 6. Próximos Passos (Para a Baseline v1.0.0 - Product)
O desenvolvimento das três classes (JInteger, JFloat e JString) foi concluído e isoladamente testado. Entramos na fase final (Sprint 5) de entrega do produto.
* **Mapeamento de Tarefas do Próximo Ciclo (Milestone v1.0.0-product):**
  * Desenvolver a suíte de testes de Interoperabilidade (`test_interop.py`) conectando JString, JInteger e JFloat.
  * Elaborar e preencher as Atas de Auditoria interna (`auditoria.md`).
  * Finalizar o `README.md` de apresentação para avaliação.
  * Preparação da demonstração técnica/vídeo exigida pelos critérios de aprovação.