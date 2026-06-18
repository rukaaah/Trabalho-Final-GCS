"""
Módulo de testes para a classe JInteger.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.

ESCOPO DESTE ARQUIVO (Issue #11 - feat/jinteger-base):
Cobre apenas as constantes estáticas (MAX_VALUE, MIN_VALUE, SIZE, BYTES,
TYPE) e o construtor primário Integer(int value). Demais métodos
(conversões, parsing, bitwise, etc.) serão cobertos em PRs/blocos
seguintes (Issues #12, #13, ...), cada um adicionando seus próprios
testes a este mesmo arquivo.

FLUXO (conforme Issue #11):
QA escreve estes testes nesta branch (feat/jinteger-base) e os sobe
SEM abrir Pull Request. O Dev então implementa javalang/jinteger.py
nesta mesma branch até os testes ficarem GREEN, e juntos abrem o PR
final referenciando Closes #11.
"""

from javalang.jinteger import JInteger


class TestJIntegerConstantes:
    def test_max_value(self):
        assert JInteger.MAX_VALUE == 2_147_483_647

    def test_min_value(self):
        assert JInteger.MIN_VALUE == -2_147_483_648

    def test_size_em_bits(self):
        assert JInteger.SIZE == 32


class TestJIntegerConstantesParte2:
    def test_bytes(self):
        assert JInteger.BYTES == 4

    def test_type_existe(self):
        # No Java, Integer.TYPE referencia a classe primitiva int.
        # Em Python validamos que o atributo existe e aponta para o tipo builtin.
        assert JInteger.TYPE is int


class TestJIntegerConstrutor:
    def test_construtor_aceita_inteiro(self):
        numero = JInteger(10)
        assert numero is not None

    def test_construtor_guarda_valor_internamente(self):
        # Correção contra falso positivo sugerida no Code Review:
        # Verifica se o valor passado (0) foi realmente injetado e armazenado.
        numero = JInteger(0)
        assert getattr(numero, '_valor', None) == 0


class TestJIntegerBitCountESignum:
    def test_bit_count(self):
        assert JInteger.bitCount(7) == 3

    def test_signum_positivo(self):
        assert JInteger.signum(10) == 1

    def test_signum_negativo(self):
        assert JInteger.signum(-10) == -1


class TestJIntegerHighestELowestOneBit:
    def test_highest_one_bit(self):
        assert JInteger.highestOneBit(10) == 8

    def test_lowest_one_bit(self):
        assert JInteger.lowestOneBit(10) == 2
class TestJIntegerCompareUnsigned:
    def test_compare_unsigned_ambos_positivos(self):
        assert JInteger.compareUnsigned(10, 5) > 0

    def test_compare_unsigned_negativo_eh_maior_como_unsigned(self):
        assert JInteger.compareUnsigned(-1, 5) > 0


class TestJIntegerDivideERemainderUnsigned:
    def test_divide_unsigned_valores_positivos(self):
        assert JInteger.divideUnsigned(10, 3) == 3

    def test_remainder_unsigned_valores_positivos(self):
        assert JInteger.remainderUnsigned(10, 3) == 1

    def test_divide_unsigned_por_zero_lanca_exception(self):
        import pytest
        with pytest.raises(ArithmeticError):
            JInteger.divideUnsigned(10, 0)
class TestJIntegerAritmeticaBasica:
    def test_sum(self):
        assert JInteger.sum(2, 3) == 5

    def test_max(self):
        assert JInteger.max(2, 3) == 3

    def test_min(self):
        assert JInteger.min(2, 3) == 2


class TestJIntegerCompareEstatico:
    def test_compare_maior(self):
        assert JInteger.compare(10, 5) > 0

    def test_compare_menor(self):
        assert JInteger.compare(5, 10) < 0

    def test_compare_igual(self):
        assert JInteger.compare(5, 5) == 0
class TestJIntegerToStringComRadix:
    def test_to_string_decimal(self):
        assert JInteger.toString(123) == "123"

    def test_to_string_negativo(self):
        assert JInteger.toString(-123) == "-123"

    def test_to_string_com_radix(self):
        assert JInteger.toString(255, 16) == "ff"


class TestJIntegerFormatacaoBinariaOctal:
    def test_to_binary_string(self):
        assert JInteger.toBinaryString(10) == "1010"

    def test_to_octal_string(self):
        assert JInteger.toOctalString(8) == "10"


class TestJIntegerFormatacaoHex:
    def test_to_hex_string(self):
        assert JInteger.toHexString(255) == "ff"

    def test_to_binary_string_negativo_representacao_32_bits(self):
        assert JInteger.toBinaryString(-1) == "1" * 32
class TestJIntegerToUnsignedString:
    def test_to_unsigned_string_valor_positivo(self):
        assert JInteger.toUnsignedString(10) == "10"

    def test_to_unsigned_string_valor_negativo(self):
        assert JInteger.toUnsignedString(-1) == str(2**32 - 1)

    def test_to_unsigned_string_com_radix(self):
        assert JInteger.toUnsignedString(255, 16) == "ff"
class TestJIntegerDoubleValueEToString:
    def test_double_value(self):
        numero = JInteger(10)
        assert numero.doubleValue() == 10.0

    def test_to_string_valor_positivo(self):
        numero = JInteger(123)
        assert numero.toString() == "123"

    def test_to_string_valor_negativo(self):
        numero = JInteger(-123)
        assert numero.toString() == "-123"

class TestJIntegerHashCodeEEquals:
    def test_hash_code_consistente_para_mesmo_valor(self):
        a = JInteger(5)
        b = JInteger(5)
        assert a.hashCode() == b.hashCode()

    def test_equals_valor_diferente_retorna_false(self):
        assert JInteger(5).equals(JInteger(6)) is False

class TestJIntegerCompareTo:
    def test_compare_to_maior(self):
        assert JInteger(10).compareTo(JInteger(5)) > 0

    def test_compare_to_menor(self):
        assert JInteger(5).compareTo(JInteger(10)) < 0

class TestJIntegerParseInt:
    def test_parse_int_decimal(self):
        assert JInteger.parseInt("10") == 10

    def test_parse_int_negativo(self):
        assert JInteger.parseInt("-10") == -10

    def test_parse_int_com_radix(self):
        assert JInteger.parseInt("ff", 16) == 255


class TestJIntegerParseIntInvalido:
    def test_parse_int_string_invalida_lanca_exception(self):
        import pytest
        with pytest.raises(ValueError):
            JInteger.parseInt("abc")


class TestJIntegerParseUnsignedInt:
    def test_parse_unsigned_int_decimal(self):
        assert JInteger.parseUnsignedInt("10") == 10

    def test_parse_unsigned_int_com_radix(self):
        assert JInteger.parseUnsignedInt("ff", 16) == 255

    def test_parse_unsigned_int_string_invalida_lanca_exception(self):
        import pytest
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("-1")
class TestJIntegerConstrutorString:
    def test_construtor_string_resulta_no_mesmo_valor_que_int(self):
        a = JInteger("42")
        b = JInteger(42)
        assert a.intValue() == b.intValue()

    def test_construtor_string_negativa(self):
        numero = JInteger("-10")
        assert numero.intValue() == -10


class TestJIntegerConversoesParte1:
    def test_int_value(self):
        numero = JInteger(10)
        assert numero.intValue() == 10

    def test_long_value(self):
        numero = JInteger(10)
        assert numero.longValue() == 10

    def test_float_value(self):
        numero = JInteger(10)
        assert numero.floatValue() == 10.0


class TestJIntegerConversoesParte2:
    def test_byte_value_dentro_da_faixa(self):
        numero = JInteger(100)
        assert numero.byteValue() == 100

    def test_short_value_dentro_da_faixa(self):
        numero = JInteger(1000)
        assert numero.shortValue() == 1000


class TestJIntegerContagemDeZeros:
    def test_number_of_leading_zeros(self):
        assert JInteger.numberOfLeadingZeros(1) == 31

    def test_number_of_trailing_zeros(self):
        assert JInteger.numberOfTrailingZeros(16) == 4


class TestJIntegerRotacao:
    def test_rotate_left(self):
        assert JInteger.rotateLeft(1, 4) == 16

    def test_rotate_right(self):
        assert JInteger.rotateRight(16, 4) == 1

    def test_rotate_left_circular_passando_de_32_bits(self):
        assert JInteger.rotateLeft(1, 33) == JInteger.rotateLeft(1, 1)
