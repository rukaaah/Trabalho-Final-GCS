"""
Módulo contendo a implementação da classe JFloat.

Esta classe reproduz o contrato público da especificação da classe Float
do Java SE 8. Ela deve contemplar os cerca de 35 métodos previstos,
garantindo o comportamento adequado para números de ponto flutuante
conforme o padrão IEEE 754.

Aviso aos Desenvolvedores:
- Preste atenção aos limites e constantes especiais (NaN, POSITIVE_INFINITY,
  NEGATIVE_INFINITY).
- Mantenha a nomenclatura original em camelCase (ex: parseFloat, isNaN).

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""
import struct
import math

class JFloat:
    # ==========================================
    # CONSTANTES 
    # ==========================================
    NaN = float('nan')
    POSITIVE_INFINITY = float('inf')
    NEGATIVE_INFINITY = float('-inf')
    
    MAX_VALUE = 3.4028235e+38
    MIN_NORMAL = 1.17549435e-38
    MIN_VALUE = 1.4e-45
    
    SIZE = 32
    BYTES = 4
    
    # ==========================================
    # CONSTRUTORES E CONVERSÃO NUMÉRICA 
    # (Ex: __init__, byteValue, intValue, etc)
    # ==========================================
    def __init__(self, value):
        if isinstance(value, str):
            try:
                self._valor = float(value)
            except ValueError:
                raise ValueError(f"Texto inválido para conversão: '{value}'")
        elif isinstance(value, (int, float)):
            self._valor = float(value)
        else:
            raise TypeError("Tipo de dado inválido")
        
    def byteValue(self) -> int:
        val_int = int(self._valor)
        resultado = val_int & 0xFF
        if resultado & 0x80:
            return resultado - 0x100
        return resultado
    
    def shortValue(self) -> int:
        val_int = int(self._valor)
        resultado = val_int & 0xFFFF
        if resultado & 0x8000:
            return resultado - 0x10000
        return resultado
    
    def intValue(self) -> int:
        val_int = int(self._valor)
        resultado = val_int & 0xFFFFFFFF
        if resultado & 0x80000000:
            return resultado - 0x100000000
        return resultado
    
    # ==========================================
    # MÉTODOS DE OBJECT 
    # (Ex: hashCode, equals, toString)
    # ==========================================
    def longValue(self) -> int:
        val_int = int(self._valor)
        resultado = val_int & 0xFFFFFFFFFFFFFFFF
        if resultado & 0x8000000000000000:
            return resultado - 0x10000000000000000
        return resultado
    
    def floatValue(self) -> float:
        return self._valor
    
    def doubleValue(self) -> float:
        return self._valor
    
    def hashCode(self) -> int:
        return struct.unpack(">I", struct.pack(">f", self._valor))[0]
    
    @staticmethod
    def hashCode_static(value: float) -> int:
        return struct.unpack(">I", struct.pack(">f", value))[0]
    
    def equals(self, obj: object) -> bool:
        if not isinstance(obj, JFloat):
            return False
        
        bits_self = struct.unpack(">I", struct.pack(">f", self._valor))[0]
        bits_obj = struct.unpack(">I", struct.pack(">f", obj._valor))[0]
        return bits_self == bits_obj
    
    def compareTo(self, anotherFloat: 'JFloat') -> int:
        if not isinstance(anotherFloat, JFloat):
            raise TypeError("O argumento precisa ser um objeto JFloat")
            
        if math.isnan(self._valor):
            if math.isnan(anotherFloat._valor):
                return 0
            return 1
        if math.isnan(anotherFloat._valor):
            return -1
            
        if self._valor < anotherFloat._valor:
            return -1
        elif self._valor > anotherFloat._valor:
            return 1
            
        bits_self = struct.unpack('>I', struct.pack('>f', self._valor))[0]
        bits_obj = struct.unpack('>I', struct.pack('>f', anotherFloat._valor))[0]
        if bits_self < bits_obj:
            return -1
        elif bits_self > bits_obj:
            return 1
        return 0
    
    # ==========================================
    # VERIFICAÇÕES IEEE 754 E PARSING 
    # (Ex: isNaN, isInfinite, parseFloat)
    # ==========================================
    def isNaN(self, v=None) -> bool:
        if isinstance(self, (int, float)):
            return math.isnan(self)
        if v is not None:
            return math.isnan(v)
        return math.isnan(self._valor)
    
    def isInfinite(self, v=None) -> bool:
        if isinstance(self, (int, float)):
            return math.isinf(self)
        if v is not None:
            return math.isinf(v)
        return math.isinf(self._valor)
    
    @staticmethod
    def isInfinite_static(v: float) -> bool:   
        return math.isinf(v)

    @staticmethod
    def isFinite(f: float) -> bool:
        return math.isfinite(f)
    
    @staticmethod
    def compare(f1: float, f2: float) -> int:
        if math.isnan(f1):
            if math.isnan(f2):
                return 0
            return 1
        if math.isnan(f2):
            return -1
        
        if f1 < f2:
            return -1
        elif f1 > f2:
            return 1
        
        bits_f1 = struct.unpack('>I', struct.pack('>f', f1))[0]
        bits_f2 = struct.unpack('>I', struct.pack('>f', f2))[0]
        if bits_f1 < bits_f2:
            return -1
        elif bits_f1 > bits_f2:
            return 1
        return 0
    # ==========================================
    # CONVERSÃO BINÁRIA E ARITMÉTICA 
    # (Ex: floatToIntBits, compare, sum)
    # ==========================================
    @staticmethod
    def floatToIntBits(value):
        # java: canonicaliza NaN para 0x7fc00000 antes de extrair os bits
        # em CPython struct.pack(">f", nan) ja produz 0x7fc00000 — comportamento identico
        import struct as _s
        if value != value:  # NaN
            return 0x7fc00000
        return _s.unpack(">I", _s.pack(">f", value))[0]

    @staticmethod
    def floatToRawIntBits(value):
        # java: preserva o padrao de bits exato, sem canonicalizar NaN
        # em CPython o resultado e identico a floatToIntBits pois struct canonicaliza NaN
        import struct as _s
        return _s.unpack(">I", _s.pack(">f", value))[0]

    @staticmethod
    def intBitsToFloat(bits):
        # java: reconstroi um float32 a partir do padrao de bits de 32 bits
        import struct as _s
        return _s.unpack(">f", _s.pack(">I", bits))[0]
    
    @staticmethod
    def max(a, b):
        # java: Float.max(float, float) -> maior valor entre os dois
        return a if a >= b else b

    @staticmethod
    def min(a, b):
        # java: Float.min(float, float) -> menor valor entre os dois
        return a if a <= b else b

    @staticmethod
    def sum(a, b):
        # java: Float.sum(float, float) -> soma simples, equivalente a a + b
        return a + b
    pass