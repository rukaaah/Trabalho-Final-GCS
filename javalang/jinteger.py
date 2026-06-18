"""
Módulo contendo a implementação da classe JInteger.

Esta classe reproduz o contrato público da especificação da classe Integer
do Java SE 8 (wrapper). Ela deve contemplar os cerca de 40 métodos previstos,
incluindo constantes, construtores, conversões, parsing, operações bit a bit
e aritmética estática.

Aviso aos Desenvolvedores:
- Mantenha a nomenclatura original em camelCase (ex: parseInt, bitCount).
- Qualquer método que não puder ser implementado (por diferenças entre as
  linguagens) deve ser levado para discussão e registrado no README.md.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""
"""
Módulo da classe JInteger, representando o wrapper java.lang.Integer.
"""

class JInteger:
    # Constantes de limite e tamanho do tipo int em Java
    MAX_VALUE = 2147483647    
    MIN_VALUE = -2147483648   
    SIZE = 32   
    BYTES = SIZE // 8
    
    # Adaptação idiomática para Python (justificada em docs/adaptacoes.md)
    TYPE = int

    def doubleValue(self):
        # java: (double) value -> widening exato; double tem mantissa suficiente para int de 32 bits
        return float(self._valor)
    
    def toString(self):
        # java: Integer.toString() -> representação decimal com sinal
        return str(self._valor)
    
    def hashCode(self):
        # java: Integer.hashCode() devolve o proprio valor encapsulado, nao um hash derivado
        return self._valor
    
    def equals(self, other):
        # java: Integer.equals so retorna True se other for Integer com mesmo valor
        if not isinstance(other, JInteger):
            return False
        return self._valor == other._valor

    def compareTo(self, other):
        # java: Integer.compareTo -> negativo/zero/positivo por comparacao numerica
        return (self._valor > other._valor) - (self._valor < other._valor)
    
    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
