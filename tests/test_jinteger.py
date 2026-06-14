"""
Suíte de testes para a classe JInteger.

OBJETIVO:
Garantir que os ~40 métodos da classe wrapper Integer do Java SE 8
tenham o comportamento replicado corretamente no Python.

FLUXO (ADR-0004 - TDD / Test-First):
Esta suíte foi escrita ANTES da implementação de javalang/jinteger.py.
É esperado que TODOS os testes falhem inicialmente (RED). Cada
desenvolvedor deve implementar o necessário em javalang/jinteger.py
até que o(s) bloco(s) sob sua responsabilidade fiquem GREEN.

ORGANIZAÇÃO EM BLOCOS (REGRA GCS ANTI-ATALHO):
- Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
- Um commit não pode conter mais de 3 métodos de teste.
Os testes estão agrupados em blocos numerados por classe `Test*`. Cada
bloco contém poucos testes e pode ser usado como unidade de trabalho
para uma Issue/PR. Não é necessário implementar um bloco inteiro de
uma vez: respeite o limite de 3 métodos de teste por commit.

ADAPTAÇÕES:
Caso algum teste abaixo dependa de um método não implementável (ex.:
overloads de tipos primitivos distintos, Locale, etc.), a equipe deve
abrir uma Issue com label `decision`, registrar em docs/adaptacoes.md
e então remover/ajustar o teste correspondente via PR de decisão.
"""

import math

import pytest

from javalang.jinteger import JInteger


# ---------------------------------------------------------------------------
# BLOCO 1 - Constantes (MAX_VALUE, MIN_VALUE, SIZE, BYTES, TYPE)
# Issue sugerida: "JInteger - Constantes"
# ---------------------------------------------------------------------------
class TestJIntegerConstantes:
    def test_max_value(self):
        assert JInteger.MAX_VALUE == 2_147_483_647

    def test_min_value(self):
        assert JInteger.MIN_VALUE == -2_147_483_648

    def test_size_em_bits(self):
        assert JInteger.SIZE == 32

    def test_bytes(self):
        assert JInteger.BYTES == 4


# ---------------------------------------------------------------------------
# BLOCO 2 - Construtor e métodos de instância básicos
# Issue sugerida: "JInteger - Construtor e valores primitivos"
# ---------------------------------------------------------------------------
class TestJIntegerConstrutorEValores:
    def test_construtor_com_inteiro(self):
        numero = JInteger(10)
        assert numero.intValue() == 10

    def test_construtor_com_string(self):
        numero = JInteger("42")
        assert numero.intValue() == 42

    def test_double_value(self):
        numero = JInteger(10)
        assert numero.doubleValue() == 10.0

    def test_float_value(self):
        numero = JInteger(10)
        assert numero.floatValue() == 10.0

    def test_long_value(self):
        numero = JInteger(10)
        assert numero.longValue() == 10

    def test_short_value(self):
        numero = JInteger(10)
        assert numero.shortValue() == 10

    def test_byte_value(self):
        numero = JInteger(10)
        assert numero.byteValue() == 10


# ---------------------------------------------------------------------------
# BLOCO 3 - toString / valueOf
# Issue sugerida: "JInteger - Conversão para String"
# ---------------------------------------------------------------------------
class TestJIntegerToStringEValueOf:
    def test_to_string_instancia(self):
        numero = JInteger(123)
        assert numero.toString() == "123"

    def test_to_string_estatico(self):
        assert JInteger.toString(123) == "123"

    def test_to_string_negativo(self):
        assert JInteger.toString(-123) == "-123"

    def test_to_string_com_radix(self):
        assert JInteger.toString(255, 16) == "ff"

    def test_value_of_int(self):
        numero = JInteger.valueOf(42)
        assert isinstance(numero, JInteger)
        assert numero.intValue() == 42

    def test_value_of_string(self):
        numero = JInteger.valueOf("42")
        assert numero.intValue() == 42

    def test_value_of_string_com_radix(self):
        numero = JInteger.valueOf("ff", 16)
        assert numero.intValue() == 255


# ---------------------------------------------------------------------------
# BLOCO 4 - parseInt
# Issue sugerida: "JInteger - parseInt"
# ---------------------------------------------------------------------------
class TestJIntegerParseInt:
    def test_parse_int_decimal(self):
        assert JInteger.parseInt("10") == 10

    def test_parse_int_negativo(self):
        assert JInteger.parseInt("-10") == -10

    def test_parse_int_com_radix_binario(self):
        assert JInteger.parseInt("1010", 2) == 10

    def test_parse_int_com_radix_hexadecimal(self):
        assert JInteger.parseInt("ff", 16) == 255

    def test_parse_int_invalido_lanca_exception(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("abc")

    def test_parse_int_string_vazia_lanca_exception(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("")


# ---------------------------------------------------------------------------
# BLOCO 5 - Comparação (compareTo, equals, hashCode)
# Issue sugerida: "JInteger - Comparação e igualdade"
# ---------------------------------------------------------------------------
class TestJIntegerComparacao:
    def test_compare_to_maior(self):
        assert JInteger(10).compareTo(JInteger(5)) > 0

    def test_compare_to_menor(self):
        assert JInteger(5).compareTo(JInteger(10)) < 0

    def test_compare_to_igual(self):
        assert JInteger(5).compareTo(JInteger(5)) == 0

    def test_equals_mesmo_valor(self):
        assert JInteger(5).equals(JInteger(5)) is True

    def test_equals_valor_diferente(self):
        assert JInteger(5).equals(JInteger(6)) is False

    def test_hash_code_consistente(self):
        assert JInteger(5).hashCode() == JInteger(5).hashCode()

    def test_compare_estatico(self):
        assert JInteger.compare(10, 5) > 0
        assert JInteger.compare(5, 10) < 0
        assert JInteger.compare(5, 5) == 0


# ---------------------------------------------------------------------------
# BLOCO 6 - Operações estáticas de aritmética (sum, max, min, signum)
# Issue sugerida: "JInteger - Operações aritméticas estáticas"
# ---------------------------------------------------------------------------
class TestJIntegerAritmeticaEstatica:
    def test_sum(self):
        assert JInteger.sum(2, 3) == 5

    def test_max(self):
        assert JInteger.max(2, 3) == 3

    def test_min(self):
        assert JInteger.min(2, 3) == 2

    def test_sum_com_negativos(self):
        assert JInteger.sum(-5, 3) == -2

    def test_signum_positivo(self):
        assert JInteger.signum(10) == 1

    def test_signum_negativo(self):
        assert JInteger.signum(-10) == -1

    def test_signum_zero(self):
        assert JInteger.signum(0) == 0


# ---------------------------------------------------------------------------
# BLOCO 7 - Operações bit a bit (bitCount, rotateLeft, rotateRight, etc.)
# Issue sugerida: "JInteger - Operações bit a bit"
# ---------------------------------------------------------------------------
class TestJIntegerBitwise:
    def test_bit_count(self):
        assert JInteger.bitCount(7) == 3  # 0b111

    def test_bit_count_zero(self):
        assert JInteger.bitCount(0) == 0

    def test_rotate_left(self):
        # 1 rotacionado 4 bits para a esquerda em um inteiro de 32 bits = 16
        assert JInteger.rotateLeft(1, 4) == 16

    def test_rotate_right(self):
        # 16 rotacionado 4 bits para a direita em um inteiro de 32 bits = 1
        assert JInteger.rotateRight(16, 4) == 1

    def test_highest_one_bit(self):
        assert JInteger.highestOneBit(10) == 8  # 0b1010 -> 0b1000

    def test_lowest_one_bit(self):
        assert JInteger.lowestOneBit(10) == 2  # 0b1010 -> 0b0010

    def test_number_of_leading_zeros(self):
        assert JInteger.numberOfLeadingZeros(1) == 31

    def test_number_of_trailing_zeros(self):
        assert JInteger.numberOfTrailingZeros(16) == 4

    def test_reverse(self):
        # Reverte os 32 bits de 1, resultando no bit mais significativo ligado
        assert JInteger.reverse(1) == JInteger.MIN_VALUE


# ---------------------------------------------------------------------------
# BLOCO 8 - Conversões de base (toBinaryString, toHexString, toOctalString)
# Issue sugerida: "JInteger - Conversão de bases numéricas"
# ---------------------------------------------------------------------------
class TestJIntegerConversaoDeBases:
    def test_to_binary_string(self):
        assert JInteger.toBinaryString(10) == "1010"

    def test_to_hex_string(self):
        assert JInteger.toHexString(255) == "ff"

    def test_to_octal_string(self):
        assert JInteger.toOctalString(8) == "10"

    def test_to_binary_string_negativo_representacao_32_bits(self):
        # Java representa números negativos em complemento de dois (32 bits)
        assert JInteger.toBinaryString(-1) == "1" * 32


# ---------------------------------------------------------------------------
# BLOCO 9 - Overflow e limites (comportamento de 32 bits com sinal)
# Issue sugerida: "JInteger - Comportamento de overflow (32 bits)"
# ---------------------------------------------------------------------------
class TestJIntegerOverflow:
    def test_max_value_mais_um_estoura_para_min_value(self):
        resultado = JInteger.sum(JInteger.MAX_VALUE, 1)
        assert resultado == JInteger.MIN_VALUE

    def test_min_value_menos_um_estoura_para_max_value(self):
        resultado = JInteger.sum(JInteger.MIN_VALUE, -1)
        assert resultado == JInteger.MAX_VALUE


# ---------------------------------------------------------------------------
# BLOCO 10 - decode e toUnsignedString
# Issue sugerida: "JInteger - decode e toUnsignedString"
# ---------------------------------------------------------------------------
class TestJIntegerDecodeEUnsigned:
    def test_decode_decimal(self):
        numero = JInteger.decode("123")
        assert numero.intValue() == 123

    def test_decode_hexadecimal_com_prefixo_0x(self):
        numero = JInteger.decode("0x1A")
        assert numero.intValue() == 26

    def test_decode_octal_com_prefixo_0(self):
        numero = JInteger.decode("010")
        assert numero.intValue() == 8

    def test_to_unsigned_string(self):
        assert JInteger.toUnsignedString(-1) == str(2**32 - 1)


# ---------------------------------------------------------------------------
# BLOCO 11 - Compatibilidade com tipos/operações nativas Python
# Issue sugerida: "JInteger - Compatibilidade com tipos nativos Python"
# ---------------------------------------------------------------------------
class TestJIntegerCompatibilidadeNativa:
    def test_str_retorna_representacao_decimal(self):
        numero = JInteger(7)
        assert str(numero) == "7"

    def test_double_value_compativel_com_math(self):
        numero = JInteger(16)
        assert math.sqrt(numero.doubleValue()) == 4.0
