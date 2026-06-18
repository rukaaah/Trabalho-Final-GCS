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
### JInteger.doubleValue()
Assinatura Java: 

                    public double doubleValue()
Situação: widening exato int->double; double do Python (53 bits de mantissa)
representa qualquer int de 32 bits sem perda de precisão, diferente do
floatValue() (32 bits), que exige coerção via struct.

### JInteger.toString()
Assinatura Java: 

                public String toString()
Situação: implementado retornando a representação decimal com sinal (str(valor)).

### JInteger.hashCode()
Assinatura Java: 

                public int hashCode()
Situação: implementado retornando o valor int encapsulado, exatamente como
Integer.hashCode() no Java (não é um hash derivado, é o próprio valor).

### JInteger.equals(Object)
Assinatura Java: 
    
                public boolean equals(Object obj)
Situação: implementado fielmente ao Java — retorna True apenas se o outro objeto
for instância de JInteger com o mesmo valor encapsulado. Não há coerção com int
puro (JInteger(5).equals(5) é False, assim como em Java).

### JInteger.compareTo(Integer)
Assinatura Java: 

                public int compareTo(Integer anotherInteger)
Situação: implementado via comparação numérica direta, retornando -1/0/1 segundo
o sinal da diferença, equivalente a Integer.compare(this.value, other.value).

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