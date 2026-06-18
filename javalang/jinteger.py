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

_DIGITOS = "0123456789abcdefghijklmnopqrstuvwxyz"

def _para_base_assinada(valor, radix):
    # conversor generico para base 2-36, preservando o sinal (usado por toString(int, radix))
    if valor == 0:
        return "0"
    negativo = valor < 0
    valor = abs(valor)
    digitos = []
    while valor > 0:
        valor, resto = divmod(valor, radix)
        digitos.append(_DIGITOS[resto])
    resultado = "".join(reversed(digitos))
    return "-" + resultado if negativo else resultado

def _bits_sem_sinal_32(valor):
    # trata o valor como o padrao de bits de 32 bits sem sinal (semantica unsigned do java)
    return valor & 0xFFFFFFFF

class JInteger:
    # Constantes de limite e tamanho do tipo int em Java
    MAX_VALUE = 2147483647    
    MIN_VALUE = -2147483648   
    SIZE = 32   
    BYTES = SIZE // 8
    
    # Adaptação idiomática para Python (justificada em docs/adaptacoes.md)
    TYPE = int

    def toString(self, radix=10):
        # unifica toString(int) e toString(int, radix) estaticos
        # python permite argumento default; java precisa de sobrecargas para o mesmo efeito
        valor = self._valor if isinstance(self, JInteger) else self
        if radix < 2 or radix > 36:
            # java: radix invalido (fora de MIN_RADIX..MAX_RADIX) -> fallback silencioso p/ base 10
            radix = 10
        if radix == 10:
            return str(valor)
        return _para_base_assinada(valor, radix)

    def toBinaryString(self):
        # java: trata o int como bits sem sinal de 32 bits (NAO preserva sinal, diferente de toString)
        valor = self._valor if isinstance(self, JInteger) else self
        return bin(_bits_sem_sinal_32(valor))[2:]

    def __init__(self, value):
        """
        Construtor correspondente a Integer(int value).
        Armazena o valor recebido sem impor a faixa de 32 bits por decisão de design.
        """
        self._valor = value
