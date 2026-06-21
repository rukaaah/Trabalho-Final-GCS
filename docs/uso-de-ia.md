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

  ### Módulo: JInteger - Métodos: Contagem e Manipulação de Bits

- **Data:** 18/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.bitCount`, `JInteger.signum`, `JInteger.highestOneBit` e `JInteger.lowestOneBit`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar os métodos highestOneBit e lowestOneBit do Java 8 em Python garantindo que o retorno simule um inteiro com sinal de 32 bits quando o bit de maior ordem estiver ativo?"
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


  ### Módulo: JInteger - Métodos: Rotação de Bits e Contagem de Zeros

- **Data:** 18/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.numberOfLeadingZeros`, `JInteger.numberOfTrailingZeros`, `JInteger.rotateLeft` e `JInteger.rotateRight`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar os métodos rotateLeft e rotateRight do Java 8 em Python garantindo que distâncias maiores que 32 funcionem de forma circular e aplicando máscara para simular estouro em complemento de dois?"

  ### Módulo: JInteger - Métodos: Reversão de Bits e Bytes

- **Data:** 18/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.reverse` e `JInteger.reverseBytes`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar os métodos de espelhamento binário reverse e inversão de endianness reverseBytes do Java 8 em Python garantindo o estouro para signed int de 32 bits?"

  ### Módulo: JFloat - Estado e Comparações IEEE 754 (#39)

- **Data:** 20/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JFloat.isInfinite_static`, `JFloat.isFinite_static`, `JFloat.compare`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como garantir a distinção correta de zero negativo e positivo em um método estático de comparação de floats simulando a especificação do Java SE 8 sem usar operadores de comparação nativos do Python que ignoram o bit de sinal?"
  ### Módulo: JFloat - Construtores e Conversões Primitivas (#37)

- **Data:** 19/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JFloat.__init__`, `JFloat.byteValue`, `JFloat.shortValue`, `JFloat.intValue`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como simular o truncamento de float para inteiros limitados a bytes e shorts em Python respeitando a especificação do Java 8?"

  ### Módulo: JFloat - Conversões e Semântica de Object (#38)

- **Data:** 20/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JFloat.hashCode`, `JFloat.equals`, `JFloat.compareTo`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como replicar a semântica de ordenação e tabelas hash da classe Float do Java 8 em Python, tratando a igualdade de NaN e diferenciação de zero negativo sem quebrar o linter?"
  
  ### Módulo: `JInteger` - Método: `valueOf`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @seu_usuario
* **Métodos Implementados/Auxiliados:** `JInteger.valueOf`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Unifique valueOf(int), valueOf(String) e valueOf(String, radix) do Java num único método estático em Python, simulando o IntegerCache (-128 a 127) com dicionário."
* **Observação:** Validei que valueOf(100) is valueOf(100) é True e valueOf(200) is valueOf(200) é False, replicando o IntegerCache do Java.

### Módulo: `JInteger` - Método: `decode`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @seu_usuario
* **Métodos Implementados/Auxiliados:** `JInteger.decode`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente decode(String) suportando sinal opcional e prefixos 0x/0X/# (hex) e zero líder (octal), retornando via valueOf para herdar o cache."
* **Observação:** Conferi decode("0x1A")==26, decode("-0x1A")==-26, decode("#1A")==26 e decode("010")==8 contra o javac.

### Módulo: JString - Núcleo Base (#52)

- **Data:** 20/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JString.__init__`, `JString.charAt`, `JString.hashCode`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como simular exatamente o algoritmo de hashCode da classe String do Java 8 em Python, garantindo que o overflow de inteiros de 32 bits assinalados funcione da mesma forma?"

### Módulo: `JFloat` - Método: `parseFloat, valueOf, toString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JFloat.parseFloat`, `JFloat.valueOf`, `JFloat.toString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente parseFloat(String) rejeitando '_' e aceitando sufixos f/F/d/D do Java, valueOf unificando float e String via dispatch, e toString unificando instância e estático com E maiúsculo fiel ao Java."
* **Observação:** A IA acelerou a escrita dos três métodos. Validei parseFloat("1.5f")==1.5, parseFloat("abc") lançando ValueError e toString(1.5)=="1.5". Conferi o dispatch de toString para chamada estática JFloat.toString(1.5).

### Módulo: `JFloat` - Método: `toHexString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JFloat.toHexString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente toHexString(float) coagindo para float32 e produzindo formato 0x<mantissa>p<exp> com zeros removidos da mantissa, fiel ao Java."
* **Observação:** Conferi toHexString(3.0)=="0x1.8p1" contra o javac.
### Módulo: `JFloat` - Método: `floatToIntBits, floatToRawIntBits, intBitsToFloat`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JFloat.floatToIntBits`, `JFloat.floatToRawIntBits`, `JFloat.intBitsToFloat`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente floatToIntBits e floatToRawIntBits para JFloat usando struct, documentando que em CPython ambos produzem o mesmo resultado para NaN pois struct canonicaliza 0x7fc00000."
* **Observação:** Validei floatToIntBits(1.0)==0x3f800000 e intBitsToFloat(0x3f800000)==1.0 contra o javac. Confirmei que NaN retorna 0x7fc00000 nos dois métodos.

### Módulo: `JFloat` - Método: `max, min, sum`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JFloat.max`, `JFloat.min`, `JFloat.sum`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente max(float, float), min(float, float) e sum(float, float) para JFloat, fiéis ao contrato Java."
* **Observação:** Métodos triviais; validei max(1.5, 2.5)==2.5, min(1.5, 2.5)==1.5 e sum(1.5, 2.5)==4.0.

### Módulo: `JString` - Método: `indexOf`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.indexOf`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Unifique indexOf(int ch), indexOf(int ch, int fromIndex), indexOf(String str) e indexOf(String str, int fromIndex) em um único método Python com dispatch por tipo via isinstance."
* **Observação:** Validei indexOf com char (int), string, fromIndex negativo (deve virar 0) e substring não encontrada (retorna -1).

### Módulo: `JString` - Método: `lastIndexOf`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.lastIndexOf`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Unifique as quatro sobrecargas de lastIndexOf em um único método Python com fromIndex=None, usando rfind() e replicando a semântica do Java de busca do fromIndex para trás."
* **Observação:** Validei lastIndexOf sem fromIndex (busca do final) e com fromIndex (busca para trás a partir da posição). Confirmei comportamento com char e substring.

### Módulo: `JString` - Método: `codePointAt, codePointBefore, codePointCount`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.codePointAt`, `JString.codePointBefore`, `JString.codePointCount`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente codePointAt(), codePointBefore() e codePointCount() para JString usando ord() do Python, documentando que Python usa UTF-32 sem surrogate pairs."
* **Observação:** Validei codePointAt(0) para ASCII e para caractere Unicode acima de U+FFFF. Confirmei que codePointCount retorna endIndex - beginIndex para strings sem surrogate pairs.

### Módulo: `JString` - Método: `offsetByCodePoints, getChars, getBytes`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.offsetByCodePoints`, `JString.getChars`, `JString.getBytes`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente offsetByCodePoints(), getChars() aceitando list como char[], e getBytes() unificando as duas sobrecargas via charsetName=None."
* **Observação:** Validei getBytes() com UTF-8 e charset inválido lançando LookupError. Confirmei getChars modificando a lista in-place corretamente.

### Módulo: `JString` - Método: `equals, equalsIgnoreCase, compareTo`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.equals`, `JString.equalsIgnoreCase`, `JString.compareTo`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente equals(), equalsIgnoreCase() e compareTo() para JString fiéis ao contrato Java SE 8, onde equals retorna False para qualquer objeto que não seja String."
* **Observação:** A IA acelerou a escrita. Validei que equals com str puro retorna False, fiel ao Java, e que compareTo replica a diferença de ord() do primeiro char divergente.

### Módulo: `JString` - Método: `compareToIgnoreCase, contentEquals, regionMatches`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JString.compareToIgnoreCase`, `JString.contentEquals`, `JString.regionMatches`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente compareToIgnoreCase(), contentEquals() aceitando str e JString como análogos de CharSequence, e regionMatches unificando as duas sobrecargas Java via ignoreCase=False como default."
* **Observação:** Validei regionMatches com toffset negativo, trecho além do tamanho e ignoreCase=True. Conferi contentEquals com JString e str puro.

### Módulo: `JString` - Métodos: `Utilitários Estáticos`
* **Data:** 21/06/2026
* **Desenvolvedor Responsável:** @rukaaah
* **Métodos Implementados/Auxiliados:** `valueOf`, `copyValueOf`, `format`, `join`
* **Ferramenta Utilizada:** Gemini
* **Prompt Representativo:**
  > "Como unificar as 9 sobrecargas do método estático String.valueOf do Java em Python sem violar o linter (F811), garantindo os retornos específicos para arrays de char e booleanos (true/false minúsculos)? Como adaptar o String.format e o String.join de forma idiomática utilizando as estruturas dinâmicas do Python (*args)?"