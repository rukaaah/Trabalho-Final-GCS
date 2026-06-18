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

### Módulo JFloat
*(Nenhuma adaptação registrada até o momento)*

### Módulo JString
*(Nenhuma adaptação registrada até o momento)*