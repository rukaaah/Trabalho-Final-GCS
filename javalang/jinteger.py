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
    def reverse(i: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        bin_invertido = bin(i_unsigned)[2:].zfill(32)[::-1]
        resultado = int(bin_invertido, 2)

        if resultado & 0x80000000:  
            return resultado - 0x100000000 
        return resultado

    @staticmethod
    def reverseBytes(i: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        b0 = (i_unsigned & 0x000000FF) << 24
        b1 = (i_unsigned & 0x0000FF00) << 8
        b2 = (i_unsigned & 0x00FF0000) >> 8
        b3 = (i_unsigned & 0xFF000000) >> 24
        resultado = b0 | b1 | b2 | b3

        if resultado & 0x80000000:  
            return resultado - 0x100000000
        return resultado
    
    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
