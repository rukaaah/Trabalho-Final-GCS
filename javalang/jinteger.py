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


class JInteger:
    # Constantes de limite e tamanho do tipo int em Java
    MAX_VALUE = 2147483647
    MIN_VALUE = -2147483648
    SIZE = 32
    BYTES = SIZE // 8

    # Adaptação idiomática para Python (justificada em docs/adaptacoes.md)
    TYPE = int

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