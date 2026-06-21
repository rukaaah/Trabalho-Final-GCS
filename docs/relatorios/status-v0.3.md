# Relatório de Status - Baseline v0.3 (Allocated · JFloat)

## Sobre este documento

Este documento é de responsabilidade do **Relator**, [Cleiton Pinheiro](https://github.com/Ton-07), da equipe. O relatório de status é gerado e submetido via Pull Request ao final de cada ciclo de desenvolvimento, servindo como um retrato oficial da saúde do projeto no momento em que uma nova baseline (Release/Tag) é fechada.

O objetivo é garantir total transparência sobre o que foi entregue, as métricas de qualidade, os riscos identificados no período e o planejamento para o próximo ciclo de desenvolvimento.

---

## Relatório Atual: v0.3.0 (Allocated · JFloat)

**Data de Fechamento:** 21/06/2026
**Período de Referência:** 20/06/2026 até 21/06/2026
**Responsável pelo Relatório:** [Cleiton Pinheiro](https://github.com/Ton-07)

### 1. Resumo Executivo
Nesta terceira etapa (Sprint 3), a equipe consolidou a **Baseline v0.3-jfloat**. O foco deste ciclo foi a implementação da classe `JFloat`, lidando com as complexidades da especificação IEEE 754 (constantes de infinito, `NaN` e limites de precisão). O processo exigiu adaptações estruturais significativas e manipulação explícita de bits, dado que o Python nativamente não diferencia precisão simples (32-bits) de dupla (64-bits) em seu tipo `float`. Continuamos a operar com o pipeline de Integração Contínua (CI) operante e verde. Também resolvemos com sucesso nosso segundo conflito de merge documentado.

### 2. Entregas Realizadas
A maior parte do escopo da classe `JFloat` foi construída, com as issues divididas estrategicamente para respeitar a métrica de limite de métodos/commits do repositório.

* **Issues Fechadas / Resolvidas (Milestone v0.3):**
  * **Issue #37:** `feat: [jfloat]: implementar construtores e conversões para inteiros`
  * **Issue #38:** `feat: [jfloat] implementar conversões numéricas, Object e ordenação`
  * **Issue #39:** `feat: [jfloat] implementar comparações e validações de estado IEEE 754`
  * **Issue #41:** `feat: [jfloat] implementar manipulação de bits e aritmética`
  * **Issue #47:** `feat: [Float] Padronização de metódos para implementação`
  * **Issue #65:** `decision: comflito de merge 02` (Mapeamento e resolução de conflito no repositório)

* **Pull Requests Mesclados (Aprovados):**
  *(Nota: Todos os PRs abaixo foram revisados por pares, respeitaram a regra de não auto-aprovação e passaram pelo pipeline de testes)*
  * PRs referentes à padronização de métodos, construtores e conversões numéricas base (**Issues #37, #38 e #47**).
  * PRs de implementações técnicas de IEEE 754, manipulação de bits e comparações (**Issues #39 e #41**).

### 3. Métricas do Período
A suíte de testes do `JFloat` focou fortemente na validação de *edge cases* matemáticos. Garantimos a consistência do `hashCode`, provamos que conversões primitivas com limites extrapolados truncam corretamente, e validamos regras estritas do contrato Java, como a identidade do `NaN` (onde `Float.NaN.equals(Float.NaN)` retorna `True` mesmo com `math.isnan`). A cobertura no CI foi mantida através do GitHub Actions. A rastreabilidade de decisões e arquitetura continua documentada em PRs e no controle de versões.

### 4. Adaptações e Decisões Formais
O desenvolvimento do `JFloat` gerou desafios únicos de infraestrutura da linguagem, documentados formalmente pela equipe:
* **Conversões e Overflow Numérico:** O Python possui inteiros de precisão arbitrária. Para implementar corretamente o *narrowing* cast do Java em `byteValue`, `shortValue`, `intValue` e `longValue`, a equipe implementou manualmente o isolamento de bits (`& 0xFF`, `& 0xFFFF`, etc.) combinado com a verificação de sinal (`& 0x80`) para forçar o limite do complemento de 2.
* **Ausência de Float de 32-bits nativo:** Como o tipo `float` do CPython opera em dupla precisão (64-bits), operações de bits (`floatToIntBits`, `hashCode`, `equals` e `compareTo`) precisaram ser adaptadas. Utilizamos a biblioteca nativa `struct` com *format characters* (`>f`, `>I`) para forçar o empacotamento, desempacotamento e comparação na precisão simples de 32-bits, garantindo o ordenamento correto de `NaN` e dos Infinitos.

### 5. Riscos e Impedimentos Atuais
Neste ciclo de fechamento, mapeamos a **Issue #40** (`feat: [jfloat] implementar parsing de strings, instanciação e formatação`) como um **débito técnico intencional e parcial**. Embora o construtor primário com strings (`JFloat("3.14")`) tenha sido implementado e testado, os métodos utilitários estáticos de parsing e formatação (`parseFloat`, `valueOf`, `toString`, `toHexString`) permanecem pendentes. Esta issue continuará aberta para conectar as *features* no Sprint 4. Adicionalmente, a frequência de conflitos de merge aumentou (Issue #65), exigindo atenção dobrada para a próxima etapa.

### 6. Próximos Passos (Para a Baseline v0.4)
O próximo e último sprint funcional será o mais denso de todos, contemplando a classe `JString` (~60 métodos). A equipe já realizou a abertura do escopo técnico completo para atacar paralelamente as *features*.
* **Mapeamento de Tarefas do Próximo Ciclo (Milestone v0.4-jstring):**
  * Concluir o débito técnico de parsing estático do JFloat (Issue #40).
  * Trabalhar as ramificações simultâneas de JString (Issues abertas **#52 a #61**), que contemplam o Núcleo Base, Busca, Regex, Comparações Lexicográficas, Substrings, Tratamento de Unicode e Formatação.