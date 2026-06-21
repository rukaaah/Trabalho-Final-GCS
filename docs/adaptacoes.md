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
**Assinatura do Método:** `public static String toString(int i)` / `public static String toString(int i, int radix)`
* **Motivo da não-implementação:** Python não suporta sobrecarga de métodos; as duas assinaturas não podem existir como métodos estáticos distintos com o mesmo nome.
* **Alternativa Proposta:** método único `toString(self, radix=10)`, unificando via argumento default e dispatch híbrido instância/estático (`isinstance(self, JInteger)`). Conversão para base arbitrária (2–36) implementada manualmente, via divisão sucessiva, já que Python só converte nativamente em base 2/8/10/16. Radix fora de `[2, 36]` recebe fallback silencioso para base 10, replicando o comportamento documentado do Java.

**Assinatura do Método:** `public static String toBinaryString(int i)` / `public static String toOctalString(int i)` / `public static String toHexString(int i)`
* **Motivo da não-implementação:** `bin()`/`oct()`/`hex()` do Python incluem prefixos (`0b`/`0o`/`0x`) que o Java não usa, e convertem o valor **com sinal**, enquanto o Java trata o `int` como padrão de bits **sem sinal** de 32 bits (ex.: `toBinaryString(-1)` produz 32 uns, não `"-1"`).
* **Alternativa Proposta:** mascaramento com `& 0xFFFFFFFF` antes da conversão (válido porque o `int` do Python representa negativos em complemento de dois "infinito"), com o prefixo removido via slice `[2:]`.

**Assinatura do Método:** `public static final Class<Integer> TYPE`
* **Motivo da não-implementação:** `TYPE` referencia o objeto `Class` do primitivo `int`. Python não possui tipos primitivos nem um `Class<T>` equivalente para eles.
* **Alternativa Proposta:** `TYPE = int` (o builtin), análogo idiomático que aponta para o tipo usado internamente pela classe. Não é um `Class<Integer>`; é a aproximação possível na linguagem.

**Assinatura do Método:** `public Integer(int value)` / `public Integer(String s) throws NumberFormatException`
* **Motivo da não-implementação:** Python não suporta sobrecarga de métodos; as duas assinaturas não podem coexistir como construtores distintos com o mesmo nome.
* **Alternativa Proposta:** `__init__` único com dispatch por tipo (`isinstance(value, str)`), delegando a conversão de string para `int(value)`. A faixa de 32 bits não é imposta — decisão da equipe, já que o `int` do Python é de precisão arbitrária.

### Contagem e Análise de Bits

- **Assinatura do Método:** `public static int bitCount(int i)`, `public static int signum(int i)`, `public static int highestOneBit(int i)` e `public static int lowestOneBit(int i)`
- **Motivo da não-implementação:** Em Java, inteiros em complemento de dois possuem tamanho estrito de 32 bits. O Python possui precisão arbitrária onde números negativos estendem os bits de sinal indefinidamente para a esquerda, alterando o comportamento natural de funções de contagem (`bin().count('1')`) e de isolamento de extremidades de bits.
- **Alternativa Proposta:** Apliquei a máscara bitwise `& 0xFFFFFFFF` para simular o comportamento de truncamento binário de 32 bits. Nos métodos de isolamento de bit único (`highestOneBit` e `lowestOneBit`), após extrair o bit correspondente usando propriedades matemáticas (`bit_length()` e `i & -i`), verifiquei se o bit de sinal (`0x80000000`) está ativo para converter o valor de volta ao formato signed esperado pelo Java.
Aritmética Unsigned

- **Assinatura do Método:** `public static int compareUnsigned(int x, int y)`, `public static int divideUnsigned(int dividend, int divisor)` e `public static int remainderUnsigned(int dividend, int divisor)`
- **Motivo da não-implementação:** O comportamento nativo de divisão, resto e comparação no Python considera o sinal dos operandos e precisão infinita. No Java SE 8, esses métodos interpretam os padrões de bits de inteiros com sinal de 32 bits como inteiros estritamente positivos antes de computar o resultado.
- **Alternativa Proposta:** Adotei o uso sistemático da máscara bitwise `& 0xFFFFFFFF` em todas as entradas de dados. Isso força o truncamento e a conversão dos números (especialmente os negativos) para o intervalo positivo equivalente de 32 bits antes de realizar as operações aritméticas (`//`, `%` e operadores lógicos). Tratei manualmente o divisor igual a zero lançando `ZeroDivisionError` para se alinhar à expectativa de `ArithmeticError` da suíte de testes.
### Operações e Comparações Básicas

- **Assinatura do Método:** `public static int sum(int a, int b)`, `public static int max(int a, int b)`, `public static int min(int a, int b)` e `public static int compare(int x, int y)`
- **Motivo da não-implementação:** Não houve impedimento linguístico. O Python possui funções built-in equivalentes (`sum`, `max`, `min`) e operadores relacionais diretos que tornam a transposição de contrato simples e direta.
- **Alternativa Proposta:** Os métodos foram mapeados utilizando as funções nativas do Python. Para o método `compare`, foi estruturada uma condicional simples para replicar fielmente o retorno binário/ternário (`-1`, `1`, `0`) esperado pelo contrato do Java SE 8.
### Formatação Unsigned

- **Assinatura do Método:** `public static String toUnsignedString(int i)` e `public static String toUnsignedString(int i, int radix)`
- **Motivo da não-implementação:** No Java, inteiros possuem limite rígido de 32 bits, onde números negativos utilizam complemento de dois. Ao formatar como unsigned, esses bits são lidos como valores estritamente positivos. O Python possui inteiros de precisão arbitrária, mantendo o sinal negativo nativamente independente do tamanho.
- **Alternativa Proposta:** Aplicamos a máscara bitwise `& 0xFFFFFFFF` para truncar o valor nos 32 bits inferiores, simulando perfeitamente o comportamento do Java SE 8 para números negativos, e convertemos o resultado para a base desejada (`radix`) usando divisões sucessivas.
# Adaptacões de Linguagem

### Métodos Unsigned

- **Assinatura do Método:** `public static int parseUnsignedInt(String s)` e `public static int parseUnsignedInt(String s, int radix)`
- **Motivo da não-implementação:** Em Java, os tipos primitivos possuem tamanho fixo de 32 bits, e o método `parseUnsignedInt` trata os bits para representar valores estritamente positivos (de 0 a 4294967295). O Python não possui suporte nativo a tipos unsigned ou limite rígido de bits em inteiros (precisão arbitrária), o que tornaria o comportamento padrão indefinido em relação ao contrato do Java.
- **Alternativa Proposta:** Implementamos uma validação manual dentro do método em Python para interceptar strings que comecem com o sinal de menos (`-`) e lançar um `ValueError`, simulando estritamente a restrição e o comportamento do Java SE 8.

---

### Sobrecarga de Métodos

- **Assinatura do Método:** `public static int parseInt(String s)` e `public static int parseInt(String s, int radix)`
- **Motivo da não-implementação:** O Java utiliza sobrecarga de métodos (overloading) para permitir duas assinaturas com o mesmo nome mas número de argumentos diferentes. O Python não suporta sobrecarga de métodos nativamente em sua estrutura de classes.
- **Alternativa Proposta:** Unificamos as assinaturas utilizando argumentos opcionais idiomáticos do Python (`radix: int = 10`), atingindo o mesmo comportamento de forma limpa e tratando dinamicamente o intervalo do radix entre 2 e 36.
**Assinatura do Método:** `public byte byteValue()` / `public short shortValue()`
* **Motivo da não-implementação:** Python não possui os primitivos `byte` (8 bits) e `short` (16 bits); existe um único `int` de precisão arbitrária.
* **Alternativa Proposta:** Mascaramento dos bits baixos (`& 0xFF` / `& 0xFFFF`) com reinterpretação em complemento de dois, replicando o estreitamento `(byte)(int)value` / `(short)(int)value` da JLS 5.1.3.

**Assinatura do Método:** `public float floatValue()`
* **Motivo da não-implementação:** o `float` do Python é IEEE 754 de 64 bits (double); Java retorna precisão simples de 32 bits.
* **Alternativa Proposta:** coerção explícita para precisão simples via `struct.pack/unpack(">f", ...)`.

**Assinatura do Método:** `public Integer(String s) throws NumberFormatException`
* **Motivo da não-implementação:** Python não suporta sobrecarga; esta assinatura não pode coexistir com `Integer(int value)` como construtor separado.
* **Alternativa Proposta:** unificada no mesmo `__init__` via dispatch por tipo (`isinstance(value, str)`), delegando a conversão a `int(value)`.

### Zeros e Rotação de Bits

- **Assinatura do Método:** `public static int numberOfLeadingZeros(int i)`, `public static int numberOfTrailingZeros(int i)`, `public static int rotateLeft(int i, int distance)` e `public static int rotateRight(int i, int distance)`
- **Motivo da não-implementação:** Em Java, operações bitwise ocorrem num espaço rígido de 32 bits em complemento de dois. No Python, inteiros possuem precisão arbitrária (tamanho dinâmico), fazendo com que um bit-shift para a esquerda (`<<`) cresça o número infinitamente em vez de rotacionar os bits excedentes de volta para o início.
- **Alternativa Proposta:** Apliquei a máscara `& 0xFFFFFFFF` para isolar os 32 bits. Na contagem de zeros à esquerda, usamos `32 - i.bit_length()`. Nas rotações, Apliquei o módulo `% 32` na distância para garantir a ciclicidade e combinamos máscaras de deslocamento composto (`(val << dist) | (val >> (32 - dist))`). Ao final, se o bit `0x80000000` estiver ativo, subtraímos `0x100000000` para converter o número de volta para o formato signed (com sinal) exigido pelo Java SE 8.

### Reversão de Bits e Bytes

- **Assinatura do Método:** `public static int reverse(int i)` e `public static int reverseBytes(int i)`
- **Motivo da não-implementação:** O Python gerencia inteiros com tamanho dinâmico na memória. Operações de reversão de bits estruturais ou inversão de ordem de bytes (*endianness*) exigem delimitação estrita de palavra de máquina (32 bits), caso contrário, os bits seriam invertidos considerando tamanhos indefinidos ou preservando o sinal incorretamente.
- **Alternativa Proposta:** Para o método `reverse`, extraímos a string binária de 32 bits formatada com `zfill(32)`, invertemos a cadeia de caracteres nativamente e reconfiguramos o valor numérico. Para o `reverseBytes`, aplicamos máscaras de segmentação byte a byte (`0xFF`, `0xFF00`, etc.) combinadas com bit-shifts de reposicionamento simétrico. Em ambos os casos, validamos o bit `0x80000000` para restabelecer o sinal negativo em formato signed de 32 bits.

**Assinatura do Método:** `public static Integer valueOf(int i)` / `public static Integer valueOf(String s)` / `public static Integer valueOf(String s, int radix)`
* **Motivo da não-implementação:** Python não suporta sobrecarga; as três assinaturas não podem coexistir como métodos estáticos distintos com o mesmo nome.
* **Alternativa Proposta:** método único `valueOf(value, radix=None)` com dispatch por tipo. O cache do Java (`IntegerCache`, -128 a 127) foi simulado via dicionário no nível do módulo — `JInteger.valueOf(n) is JInteger.valueOf(n)` é `True` para `n` nessa faixa.

**Assinatura do Método:** `public static Integer decode(String nm)`
* **Motivo da não-implementação:** a gramática do Java rejeita convenções que o `int()` nativo do Python aceita (espaços, `_`, prefixos redundantes).
* **Alternativa Proposta:** implementado com helper de parsing estrito (`_parseInt_java`), suportando `0x`/`0X`/`#` (hex), zero líder (octal) e decimal. Retorna via `valueOf`, herdando o cache.

### Módulo JFloat
*(Nenhuma adaptação registrada até o momento)*
### Propriedades IEEE 754 e Validações de JFloat (#39)

- **Assinatura do Método:** `isNaN()`, `isNaN(float)`, `isInfinite()`, `isInfinite(float)`, `isFinite(float)` e `compare(float, float)`
- **Motivo da não-implementação:** O Python não aceita sobrecarga de métodos com escopos diferentes (instância vs estático) sob o mesmo identificador na classe. Adicionalmente, as avaliações de igualdade de ponto flutuante convencionais falham ao distinguir as representações binárias de sinal nos zeros (`0.0` e `-0.0`) exigidas pelo ecossistema Java.
- **Alternativa Proposta:** Customizamos as assinaturas estáticas adicionando o sufixo `_static`. No método de comparação primitiva `compare`, vinculamos as checagens explícitas do módulo `math` para isolamento prioritário de estados `NaN` combinadas à leitura estrutural de bits via `struct` para desempatar as ordens de magnitude dos limites de zero assinalado.
### Construtores e Conversões de JFloat (#37)

- **Assinatura do Método:** `Float(value)`, `byteValue()`, `shortValue()` e `intValue()`
- **Motivo da não-implementação:** O Python gerencia valores `float` nativos como dupla precisão de 64 bits (equivalente ao `double` do Java) e carece de suporte nativo a tipos de capacidade reduzida como `byte` (8-bit) e `short` (16-bit), além de não realizar sobrecarga de construtores.
- **Alternativa Proposta:** Desenvolvemos uma inicialização dinâmica baseada em checagem de tipos (`isinstance`). Emulamos o truncamento de ponto flutuante e o estouro posicionado de tipos de dados menores através de casts explicitados combinados a operações de máscaras bitwise (`& 0xFF`, `& 0xFFFF`, `& 0xFFFFFFFF`) seguidas de checagens de bit de sinal mais significativo para replicar fielmente o comportamento de estouro do Java SE 8.

### Módulo JString
*(Nenhuma adaptação registrada até o momento)*