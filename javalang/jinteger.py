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
    def toUnsignedString(i: int, radix: int = 10) -> str:
        #Implementa os métodos toUnsignedString(int i) e toUnsignedString(int i, int radix) do Java
        if not(2 <= radix <= 36):
            raise ValueError(f"radix {radix} está fora do intervalo (2, 36)")
        valor_unsigned = i & 0xFFFFFFFF

        if radix == 10:
            return str(valor_unsigned)
        if valor_unsigned == 0:
            return "0"
        
        digitos = "0123456789abcdefghijklmnopqrstuvwxyz"
        resultado = []
        while valor_unsigned > 0:
            resultado.append(digitos[valor_unsigned % radix])
            valor_unsigned //= radix
        return "".join(reversed(resultado))
    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
