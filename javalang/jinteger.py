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
    def parseInt(s: str, radix: int = 10) -> int:
        #Implementa os métodos parseInt com e sem radix
        if not (2 <= radix <= 36):
            raise ValueError(f"radix {radix} está fora do intervalo válido (2-36)")
        try:
            return int(s, radix)
        except ValueError:
            raise ValueError(f"Formato inválido: '{s}' com radix {radix}")
        
    @staticmethod
    def parseUnsignedInt(s: str, radix: int = 10) -> int:
        #Implementa os métodos parseUnsignedInt com e sem radix
        if not (2 <= radix <= 36):
            raise ValueError(f"radix {radix} está fora do intervalo válido (2-36)")
        s_clean =s.strip()
        if s_clean.startswith('-'):
            raise ValueError(f"Número negativo não permitido: '{s}'")
        try:
            return int(s_clean, radix)
        except ValueError:
            raise ValueError(f"Formato inválido: '{s}' com radix {radix}")

    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
