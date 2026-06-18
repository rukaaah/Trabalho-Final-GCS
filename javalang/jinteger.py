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

    @staticmethod
    def bitCount(i: int) -> int:
        return bin(i & 0xFFFFFFFF).count('1')
    
    @staticmethod
    def signum(i: int) -> int:
        if i < 0:
            return -1
        elif i > 0:
            return 1
        else:
            return 0

    @staticmethod   
    def highestOneBit(i: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        if i_unsigned == 0:
            return 0
        
        posicao = i_unsigned.bit_length() - 1
        resultado = 1 << posicao

        if resultado & 0x80000000:
            return resultado - 0x100000000
        return resultado
    
    @staticmethod
    def lowestOneBit(i: int) -> int:
        resultado = i & -i
        resultado_32 = resultado & 0xFFFFFFFF
        if resultado_32 == 0:
            return 0
        if resultado_32 & 0x80000000:
            return resultado_32 - 0x100000000
        return resultado_32
    
    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
