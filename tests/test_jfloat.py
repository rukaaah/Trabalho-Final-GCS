"""
Suíte de testes para a classe JFloat.

OBJETIVO:
Garantir que os ~35 métodos da classe Float do Java SE 8, incluindo o 
comportamento do padrão IEEE 754, funcionem corretamente.

O QUE TESTAR AQUI:
- Verificações IEEE 754 (isNaN, isInfinite, isFinite).
- Tratamento de limites (POSITIVE_INFINITY, NEGATIVE_INFINITY, NaN).
- Conversão Binária (floatToIntBits).
- Operações de comparação.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""
import math
from javalang.jfloat import JFloat

def test_jfloat_is_nan():
    # TODO: Implementar teste com casos de borda do IEEE 754
    pass

class TestJFloatConstantes:
    def test_positive_infinity(self):
        assert JFloat.POSITIVE_INFINITY == math.inf

    def test_negative_infinity(self):
        assert JFloat.NEGATIVE_INFINITY == -math.inf

    def test_nan_e_nan(self):
        assert math.isnan(JFloat.NaN)

class TestJFloatIsNaN:
    def test_is_nan_instancia_com_nan(self):
        numero = JFloat(float('nan'))
        assert numero.isNaN() is True

    def test_is_nan_estatico(self):
        assert JFloat.isNaN(float('nan')) is True


class TestJFloatIsInfiniteECompare:
    def test_is_infinite_instancia(self):
        numero = JFloat(math.inf)
        assert numero.isInfinite() is True

    def test_is_finite_valor_normal(self):
        assert JFloat.isFinite(1.0) is True
class TestJFloatConstrutores:
    def test_construtor_com_float(self):
        numero = JFloat(3.14)
        assert numero is not None

    def test_construtor_guarda_valor_internamente(self):
        numero = JFloat(1.5)
        assert getattr(numero, '_valor', None) is not None

    def test_construtor_com_string(self):
        numero = JFloat("3.14")
        assert numero is not None

class TestJFloatConversoesParte1:
    def test_int_value_trunca(self):
        numero = JFloat(3.9)
        assert numero.intValue() == 3

    def test_int_value_negativo_trunca(self):
        numero = JFloat(-3.9)
        assert numero.intValue() == -3

    def test_byte_value_dentro_da_faixa(self):
        numero = JFloat(100.7)
        assert numero.byteValue() == 100


class TestJFloatConversoesParte2:
    def test_short_value_dentro_da_faixa(self):
        numero = JFloat(1000.5)
        assert numero.shortValue() == 1000

class TestJFloatConversoesAltas:
    def test_long_value(self):
        numero = JFloat(3.9)
        assert numero.longValue() == 3

    def test_float_value(self):
        numero = JFloat(1.5)
        assert math.isclose(numero.floatValue(), 1.5, rel_tol=1e-6)

    def test_double_value(self):
        numero = JFloat(1.5)
        assert math.isclose(numero.doubleValue(), 1.5, rel_tol=1e-6)

class TestJFloatHashCodeEEquals:
    def test_hash_code_consistente(self):
        a = JFloat(1.5)
        b = JFloat(1.5)
        assert a.hashCode() == b.hashCode()

    def test_equals_mesmo_valor(self):
        assert JFloat(1.5).equals(JFloat(1.5)) is True

    def test_equals_nan_retorna_true(self):
        assert JFloat(float('nan')).equals(JFloat(float('nan'))) is True


class TestJFloatCompareTo:
    def test_compare_to_maior(self):
        assert JFloat(2.0).compareTo(JFloat(1.0)) > 0

