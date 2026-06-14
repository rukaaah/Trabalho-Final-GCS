"""
Suíte de testes para a classe JFloat.

OBJETIVO:
Garantir que os ~35 métodos da classe Float do Java SE 8, incluindo o
comportamento do padrão IEEE 754, funcionem corretamente.

FLUXO (ADR-0004 - TDD / Test-First):
Esta suíte foi escrita ANTES da implementação de javalang/jfloat.py.
É esperado que TODOS os testes falhem inicialmente (RED). Cada
desenvolvedor deve implementar o necessário em javalang/jfloat.py até
que o(s) bloco(s) sob sua responsabilidade fiquem GREEN.

ORGANIZAÇÃO EM BLOCOS (REGRA GCS ANTI-ATALHO):
- Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
- Um commit não pode conter mais de 3 métodos de teste.
Os testes estão agrupados em blocos numerados por classe `Test*`. Cada
bloco contém poucos testes e pode ser usado como unidade de trabalho
para uma Issue/PR. Não é necessário implementar um bloco inteiro de
uma vez: respeite o limite de 3 métodos de teste por commit.

ADAPTAÇÕES:
Python usa `float` de 64 bits (double) nativamente; a especificação
Float do Java é de 32 bits. Caso a equipe decida não simular a
precisão de 32 bits para todos os métodos, essa decisão deve ser
registrada em docs/adaptacoes.md (via Issue com label `decision`) e
os testes abaixo ajustados via PR de decisão.
"""

import math

import pytest

from javalang.jfloat import JFloat


# ---------------------------------------------------------------------------
# BLOCO 1 - Constantes IEEE 754
# Issue sugerida: "JFloat - Constantes"
# ---------------------------------------------------------------------------
class TestJFloatConstantes:
    def test_positive_infinity(self):
        assert JFloat.POSITIVE_INFINITY == math.inf

    def test_negative_infinity(self):
        assert JFloat.NEGATIVE_INFINITY == -math.inf

    def test_nan_e_nan(self):
        assert math.isnan(JFloat.NaN)

    def test_max_value(self):
        # Maior valor finito representável em float de 32 bits (IEEE 754)
        assert math.isclose(JFloat.MAX_VALUE, 3.4028235e38, rel_tol=1e-6)

    def test_min_value_positivo(self):
        # Menor valor positivo (subnormal) representável em float de 32 bits
        assert JFloat.MIN_VALUE > 0

    def test_size_em_bits(self):
        assert JFloat.SIZE == 32


# ---------------------------------------------------------------------------
# BLOCO 2 - Construtor e métodos de instância básicos
# Issue sugerida: "JFloat - Construtor e valores primitivos"
# ---------------------------------------------------------------------------
class TestJFloatConstrutorEValores:
    def test_construtor_com_float(self):
        numero = JFloat(3.14)
        assert math.isclose(numero.floatValue(), 3.14, rel_tol=1e-6)

    def test_construtor_com_string(self):
        numero = JFloat("3.14")
        assert math.isclose(numero.floatValue(), 3.14, rel_tol=1e-6)

    def test_double_value(self):
        numero = JFloat(2.5)
        assert numero.doubleValue() == 2.5

    def test_int_value_trunca_decimais(self):
        numero = JFloat(9.7)
        assert numero.intValue() == 9

    def test_long_value_trunca_decimais(self):
        numero = JFloat(9.7)
        assert numero.longValue() == 9


# ---------------------------------------------------------------------------
# BLOCO 3 - Verificações IEEE 754 (isNaN, isInfinite)
# Issue sugerida: "JFloat - Verificações isNaN e isInfinite"
# ---------------------------------------------------------------------------
class TestJFloatVerificacoes:
    def test_is_nan_instancia_com_nan(self):
        numero = JFloat(JFloat.NaN)
        assert numero.isNaN() is True

    def test_is_nan_instancia_com_numero_normal(self):
        numero = JFloat(1.0)
        assert numero.isNaN() is False

    def test_is_nan_estatico(self):
        assert JFloat.isNaN(float("nan")) is True
        assert JFloat.isNaN(1.0) is False

    def test_is_infinite_instancia(self):
        numero = JFloat(JFloat.POSITIVE_INFINITY)
        assert numero.isInfinite() is True

    def test_is_infinite_estatico(self):
        assert JFloat.isInfinite(math.inf) is True
        assert JFloat.isInfinite(1.0) is False

    def test_is_finite_estatico(self):
        assert JFloat.isFinite(1.0) is True
        assert JFloat.isFinite(math.inf) is False
        assert JFloat.isFinite(float("nan")) is False


# ---------------------------------------------------------------------------
# BLOCO 4 - toString / valueOf
# Issue sugerida: "JFloat - Conversão para String"
# ---------------------------------------------------------------------------
class TestJFloatToStringEValueOf:
    def test_to_string_instancia(self):
        numero = JFloat(3.14)
        assert numero.toString() == "3.14"

    def test_to_string_estatico(self):
        assert JFloat.toString(3.14) == "3.14"

    def test_to_string_infinito(self):
        assert JFloat.toString(JFloat.POSITIVE_INFINITY) == "Infinity"

    def test_to_string_nan(self):
        assert JFloat.toString(JFloat.NaN) == "NaN"

    def test_value_of_float(self):
        numero = JFloat.valueOf(3.14)
        assert isinstance(numero, JFloat)
        assert math.isclose(numero.floatValue(), 3.14, rel_tol=1e-6)

    def test_value_of_string(self):
        numero = JFloat.valueOf("3.14")
        assert math.isclose(numero.floatValue(), 3.14, rel_tol=1e-6)


# ---------------------------------------------------------------------------
# BLOCO 5 - parseFloat
# Issue sugerida: "JFloat - parseFloat"
# ---------------------------------------------------------------------------
class TestJFloatParseFloat:
    def test_parse_float_decimal(self):
        assert math.isclose(JFloat.parseFloat("3.14"), 3.14, rel_tol=1e-6)

    def test_parse_float_negativo(self):
        assert math.isclose(JFloat.parseFloat("-3.14"), -3.14, rel_tol=1e-6)

    def test_parse_float_notacao_cientifica(self):
        assert math.isclose(JFloat.parseFloat("1.5e3"), 1500.0, rel_tol=1e-6)

    def test_parse_float_infinity(self):
        assert JFloat.parseFloat("Infinity") == math.inf

    def test_parse_float_nan(self):
        assert math.isnan(JFloat.parseFloat("NaN"))

    def test_parse_float_invalido_lanca_exception(self):
        with pytest.raises(ValueError):
            JFloat.parseFloat("abc")


# ---------------------------------------------------------------------------
# BLOCO 6 - Comparação (compareTo, equals, hashCode)
# Issue sugerida: "JFloat - Comparação e igualdade"
# ---------------------------------------------------------------------------
class TestJFloatComparacao:
    def test_compare_to_maior(self):
        assert JFloat(2.0).compareTo(JFloat(1.0)) > 0

    def test_compare_to_menor(self):
        assert JFloat(1.0).compareTo(JFloat(2.0)) < 0

    def test_compare_to_igual(self):
        assert JFloat(1.0).compareTo(JFloat(1.0)) == 0

    def test_equals_mesmo_valor(self):
        assert JFloat(1.0).equals(JFloat(1.0)) is True

    def test_equals_nan_e_nan_retorna_true(self):
        # Diferente de '==', Float.equals(NaN, NaN) é True no Java
        assert JFloat(JFloat.NaN).equals(JFloat(JFloat.NaN)) is True

    def test_compare_estatico(self):
        assert JFloat.compare(2.0, 1.0) > 0
        assert JFloat.compare(1.0, 2.0) < 0
        assert JFloat.compare(1.0, 1.0) == 0


# ---------------------------------------------------------------------------
# BLOCO 7 - max, min e sum estáticos
# Issue sugerida: "JFloat - Operações aritméticas estáticas"
# ---------------------------------------------------------------------------
class TestJFloatAritmeticaEstatica:
    def test_max(self):
        assert JFloat.max(1.0, 2.0) == 2.0

    def test_min(self):
        assert JFloat.min(1.0, 2.0) == 1.0

    def test_sum(self):
        assert JFloat.sum(1.5, 2.5) == 4.0

    def test_max_com_nan_retorna_nan(self):
        assert math.isnan(JFloat.max(1.0, JFloat.NaN))


# ---------------------------------------------------------------------------
# BLOCO 8 - Conversão Binária (floatToIntBits, intBitsToFloat)
# Issue sugerida: "JFloat - Conversão binária IEEE 754"
# ---------------------------------------------------------------------------
class TestJFloatConversaoBinaria:
    def test_float_to_int_bits_zero(self):
        assert JFloat.floatToIntBits(0.0) == 0

    def test_float_to_int_bits_um(self):
        # Representação IEEE 754 de 1.0f em 32 bits
        assert JFloat.floatToIntBits(1.0) == 0x3F800000

    def test_int_bits_to_float_um(self):
        assert JFloat.intBitsToFloat(0x3F800000) == 1.0

    def test_round_trip_float_int_bits(self):
        valor_original = 2.5
        bits = JFloat.floatToIntBits(valor_original)
        assert JFloat.intBitsToFloat(bits) == valor_original
