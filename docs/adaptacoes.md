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
### Módulo JFloat
*(Nenhuma adaptação registrada até o momento)*

### Módulo JString
*(Nenhuma adaptação registrada até o momento)*