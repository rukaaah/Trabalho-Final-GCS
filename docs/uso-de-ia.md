# Registro de Uso de Inteligência Artificial

Este documento serve como declaração obrigatória do uso de ferramentas de IA generativa (ChatGPT, Gemini, GitHub Copilot, etc.) como auxílio na implementação técnica deste projeto.
Conforme as regras de GCS, a utilização de IA não exime o desenvolvedor da responsabilidade de explicar oralmente o código sob seu nome.

---

## 📋 Template de Registro
*(Desenvolvedor: Copie o bloco abaixo, preencha com suas informações e adicione no topo da seção de "Logs de Utilização" sempre que utilizar IA para gerar ou refatorar lógicas de métodos).*

### Módulo: `[Nome da Classe]` - Método: `[Nome do Método]`
* **Data:** DD/MM/2026
* **Desenvolvedor Responsável:** @[seu_usuario]
* **Métodos Implementados/Auxiliados:** `[Ex: JString.regionMatches]`
* **Ferramenta Utilizada:** `[Ex: ChatGPT / Gemini]`
* **Prompt Representativo:**
  > "[Cole aqui a essência ou a cópia exata do prompt que você enviou para a IA. Ex: 'Como posso simular o comportamento de offset de CodePoints do Java em Python 3.10 preservando a performance?']"

---

## 🗄️ Logs de Utilização
*(Adicione os novos registros abaixo desta linha)*
### Módulo: `JInteger` - Método: `toString(int, radix), toBinaryString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.toString` (estendido), `JInteger.toBinaryString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Unifique toString(int)/toString(int, radix) estáticos do Java usando argumento default em Python. Implemente um conversor genérico para base 2-36 e replique o fallback do Java para radix inválido (volta a base 10). Implemente toBinaryString tratando o valor como bits sem sinal de 32 bits."
* **Observação:** A IA acelerou a escrita do conversor de base. Validei manualmente o fallback de radix inválido (conferido contra o Javadoc) e o comportamento unsigned de toBinaryString(-1).

### Módulo: `JInteger` - Método: `toOctalString, toHexString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.toOctalString`, `JInteger.toHexString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente toOctalString e toHexString para JInteger, reaproveitando a lógica de bits sem sinal de 32 bits usada em toBinaryString."
* **Observação:** Conferi que toHexString(-1) retorna "ffffffff" e toOctalString(-1) retorna "37777777777", batendo com a saída real do javac.
### Módulo: `JInteger` - Método: `doubleValue, toString, hashCode`
* **Data:** 16/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.doubleValue`, `JInteger.toString`, `JInteger.hashCode`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente doubleValue() (widening exato int->double), toString() (representação decimal) e hashCode() (deve retornar o próprio valor int, como Integer.hashCode() do Java) para JInteger."
* **Observação:** A IA acelerou a redação dos três métodos, mas a decisão de hashCode() retornar diretamente o valor encapsulado (e não um hash calculado) foi conferida manualmente contra a especificação oficial do Integer.hashCode(), já que esse é o ponto onde uma implementação genérica erraria. Validei doubleValue() comparando com casos de borda (MAX_VALUE, MIN_VALUE) para confirmar ausência de perda de precisão.

### Módulo: `JInteger` - Método: `equals, compareTo`
* **Data:** 16/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.equals`, `JInteger.compareTo`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente equals(Object) e compareTo(Integer) para JInteger fiéis ao contrato Java: equals só compara com outro JInteger (sem coerção com int puro), compareTo retorna -1/0/1 por comparação numérica."
* **Observação:** A IA acelerou a escrita, mas testei manualmente o ponto de maior risco de infidelidade: confirmei que equals() retorna False ao comparar com um int puro (JInteger(5).equals(5)), reproduzindo a rejeição de tipo do Java, e validei compareTo() nos três casos de sinal (maior, menor, igual).

### Módulo: `JInteger` - Constantes e Construtor (Issue #11)
* **Data:** 16/06/2026
* **Desenvolvedor Responsável:** @GomesYV
* **Métodos Implementados/Auxiliados:** Testes de `JInteger.MAX_VALUE`, `MIN_VALUE`, `SIZE`, `BYTES`, `TYPE` e do construtor `Integer(int value)`.
* **Ferramenta Utilizada:** Claude (Anthropic)
* **Prompt Representativo:**
  > "Escreva os testes em pytest para as constantes estáticas e o construtor primário da classe JInteger, cobrindo o contrato da Issue #11, em blocos de até 3 testes por commit, seguindo o fluxo TDD descrito (testes em RED, sem abrir PR contra a main)."

  ### Módulo: JInteger - Métodos: Aritmética Unsigned

- **Data:** 18/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.compareUnsigned`, `JInteger.divideUnsigned` e `JInteger.remainderUnsigned`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar operações aritméticas de divisão, resto e comparação interpretando os inteiros como unsigned de 32 bits em Python através de máscaras binárias?"
  ### Módulo: JInteger - Métodos: Aritmética e Comparação Básica

- **Data:** 17/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.sum`, `JInteger.max`, `JInteger.min` e `JInteger.compare`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar os métodos utilitários sum, max, min e compare do Java 8 em Python?"
  ### Módulo: JInteger - Método: toUnsignedString

- **Data:** 17/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.toUnsignedString`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como simular o método JInteger.toUnsignedString(int i, int radix) do Java 8 em Python usando a máscara & 0xFFFFFFFF para tratar números negativos e fazendo a conversão de base de 2 a 36?"
  ### Módulo: JInteger - Métodos: parseInt e parseUnsignedInt

- **Data:** 17/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.parseInt` e `JInteger.parseUnsignedInt`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  > ""Como implementar os métodos parseInt e parseUnsignedInt (com e sem radix) do Java 8 em Python, garantindo as exceções corretas"
### Módulo: `JInteger` - Método: `Conversões (long/float) e Integer(String s)`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.longValue`, `JInteger.floatValue`, `JInteger.__init__` (Integer(String s))
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Para JInteger, implemente longValue() (widening), floatValue() coagindo para float de 32 bits como o (float) do Java, e estenda o __init__ para aceitar str (Integer(String s)), fazendo passar os testes da QA."
* **Observação:** Uso da IA apenas para agilizar. Conferi as asserções da QA (string "42" == int 42, floatValue de 10 == 10.0) e entendo por que floatValue coage para 32 bits.
