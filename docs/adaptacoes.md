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
## JInteger (java.lang.Integer, Java SE 8)
### Constantes de limite e tamanho
Assinatura Java:

                public static final int MAX_VALUE = 2147483647
                public static final int MIN_VALUE =
                -2147483648
                public static final int SIZE = 32
                public static final int BYTES = 4
Situação: implementadas como constantes de classe, valores idênticos ao Java.
Adaptação: o int do Python é de precisão arbitrária e não sofre overflow. As
constantes são informativas e não são aplicadas
automaticamente — JInteger não impõe a faixa de 32 bits.

### TYPE
Assinatura Java: public static final Class<Integer> TYPE
Motivo da não-implementação: TYPE referencia o objeto Class do primitivo int.
Python não possui tipos primitivos nem um Class<T> equivalente para eles.
Alternativa: TYPE = int, análogo idiomático que aponta para o tipo
usado internamente pela classe. Não é um Class<Integer>; é a aproximação
possível na linguagem.

### Construtores
Assinatura Java:

            public Integer(int value)
            public Integer(String s) throws NumberFormatException
Situação: Integer(int value) implementado, armazenando o valor recebido. A faixa
de 32 bits não é imposta — o int do Python é de precisão arbitrária.
Adaptação: Python não tem sobrecarga de métodos; os dois construtores não podem
coexistir como assinaturas distintas. Integer(String s) será unificado no mesmo
__init__ via dispatch por tipo na issue de parsing, delegando a parseInt.

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

### Módulo JFloat
*(Nenhuma adaptação registrada até o momento)*

### Módulo JString
*(Nenhuma adaptação registrada até o momento)*