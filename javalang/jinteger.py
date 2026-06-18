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
import struct as _struct # noqa: E402


def _para_int8(bits):
    # interpreta os 8 bits baixos como signed
    return bits - 256 if bits >= 128 else bits


def _para_int16(bits):
    # interpreta os 16 bits baixos como signed
    return bits - 65536 if bits >= 32768 else bits


def _para_float32(valor):
    # coage para precisão simples IEEE 754 (32 bits), como o (float) do Java
    return _struct.unpack(">f", _struct.pack(">f", valor))[0]


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
    @staticmethod
    def sum(a: int, b: int) -> int:
        # Implementação de soma básica
        return a + b
    @staticmethod
    def max(a: int, b: int) -> int:
        # Implementação de máximo básico
        return max(a, b)
    @staticmethod
    def min(a: int, b: int) -> int:
        # Implementação de mínimo básico
        return min(a, b)
    @staticmethod
    def compare(a: int, b: int) -> int:
        # Implementação de comparação básica
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0

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
    
    def toOctalString(self):
        valor = self._valor if isinstance(self, JInteger) else self
        return oct(_bits_sem_sinal_32(valor))[2:]

    def toHexString(self):
        valor = self._valor if isinstance(self, JInteger) else self
        return hex(_bits_sem_sinal_32(valor))[2:]
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
    def doubleValue(self):
        # java: (double) value -> widening exato; double tem mantissa suficiente para int de 32 bits
        return float(self._valor)
    
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
    
    def compareUnsigned(a: int, b: int) -> int:
        x_unsigned = a & 0xFFFFFFFF
        y_unsigned = b & 0xFFFFFFFF
        if x_unsigned < y_unsigned:
            return -1
        elif x_unsigned > y_unsigned:
            return 1
        else:
            return 0
    
    def divideUnsigned(dividend: int, divisor: int) -> int:
        dividend_unsigned = dividend & 0xFFFFFFFF
        divisor_unsigned = divisor & 0xFFFFFFFF
        if divisor_unsigned == 0:
            raise ZeroDivisionError("Divisão por zero")
        return dividend_unsigned // divisor_unsigned
    
    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int) -> int:
        dividend_unsigned = dividend & 0xFFFFFFFF
        divisor_unsigned = divisor & 0xFFFFFFFF
        if divisor_unsigned == 0:
            raise ZeroDivisionError("Divisão por zero")
        return dividend_unsigned % divisor_unsigned
    @staticmethod
    def numberOfLeadingZeros(i: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        if i_unsigned == 0:
            return 32
        return 32 - i_unsigned.bit_length()
    
    @staticmethod
    def numberOfTrailingZeros(i: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        if i_unsigned == 0:
            return 32
        lsb = i_unsigned & -i_unsigned
        return lsb.bit_length() - 1
    
    @staticmethod
    def rotateLeft(i: int, distance: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        distance = distance % 32
        if distance == 0:
            return i if i <= 0x7FFFFFFF else i - 0x100000000
        
        resultado = ((i_unsigned << distance) | (i_unsigned >> (32 - distance))) & 0xFFFFFFFF

        if resultado & 0x80000000:
            return resultado - 0x100000000
        return resultado
    
    @staticmethod
    def rotateRight(i: int, distance: int) -> int:
        i_unsigned = i & 0xFFFFFFFF
        distance = distance % 32
        if distance == 0:
            return i if i <= 0x7FFFFFFF else i - 0x100000000
        
        resultado = ((i_unsigned >> distance) | (i_unsigned << (32 - distance))) & 0xFFFFFFFF

        if resultado & 0x80000000:
            return resultado - 0x100000000
        return resultado
        
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
        if isinstance(value, str):
            self._valor = int(value)
        else:
            self._valor = value

    def intValue(self):
        # java: Integer.intValue() devolve o int encapsulado diretamente
        return self._valor

    def byteValue(self):
        # java: (byte) value -> 8 bits baixos como signed; trunca/faz wrap, nunca lança
        return _para_int8(self._valor & 0xFF)

    def shortValue(self):
        # java: (short) value -> 16 bits baixos como signed; trunca/faz wrap, nunca lança
        return _para_int16(self._valor & 0xFFFF)

    def longValue(self):
        # java: (long) value -> widening para long; numericamente idêntico
        return self._valor

    def floatValue(self):
        # java: (float) value -> widening para float de 32 bits (precisão simples)
        return _para_float32(self._valor)