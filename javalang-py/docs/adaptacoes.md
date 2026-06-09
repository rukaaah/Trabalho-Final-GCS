# Registro de Adaptações

## Sobre este documento

Este documento é de responsabilidade formal do **Gerente de Configuração**, [Angelo Antônio](https://github.com/angelo-acds). Seu objetivo é centralizar e oficializar todas as adaptações e exclusões de métodos da especificação Java SE 8 (das classes String, Integer e Float) para a linguagem Python.

Como Python e Java diferem em fundamentos importantes (tipagem, sistema de tipos primitivos, gerenciamento de memória, suporte a Unicode, sobrecarga de métodos e locale), a equipe não precisa contornar essas diferenças à força. A exigência é que haja consciência documentada.

**Regras de Processo para Adaptações:**
1. A decisão de não implementar ou adaptar um método deve ser tomada em equipe.
2. A proposta deve ser registrada em uma issue dedicada contendo a label `decision`.
3. A atualização deste arquivo deve ser feita exclusivamente via Pull Request normal.
4. Decisões individuais ou exclusões silenciosas não documentadas resultarão em penalização na nota final de GCS.

---

## Categorias Típicas de Não-Implementação

Para guiar as decisões da equipe, as seguintes restrições intrínsecas já estão previstas:
* **Sobrecarga por tipo primitivo distinto:** Java diferencia int, long, byte, short; Python tem um único int. Métodos variados podem ser representados por um único método com nota técnica.
* **Dependências de Locale, Charset e Comparator:** Exigem infraestrutura ampla e podem ser substituídos por stubs com fallback documentado.
* **Métodos depreciados na especificação Java 8:** Devem ser listados, mas não implementados, referenciando a recomendação oficial.
* **Dependências estruturais:** Sobrecargas por StringBuffer e StringBuilder não serão implementadas.
* **Otimizações de runtime:** Como `String.intern()`, cujo pool interno difere do gerenciamento do CPython.

---

## Catálogo de Métodos Adaptados / Não Implementados

*(Atenção Gerente de Configuração: Adicione as novas ocorrências abaixo utilizando o template padrão).*

### Template de Inclusão
**Assinatura do Método:** `[Inserir assinatura completa conforme Javadoc]`
* **Motivo da não-implementação:** `[Explicar restrição da linguagem, falta de tipo, comportamento indefinido ou decisão da equipe]`
* **Alternativa Proposta:** `[Demonstrar como atingir o mesmo comportamento de forma idiomática no Python, se aplicável]`

---

### Módulo JInteger
*(Nenhuma adaptação registrada até o momento)*

### Módulo JFloat
*(Nenhuma adaptação registrada até o momento)*

### Módulo JString
*(Nenhuma adaptação registrada até o momento)*