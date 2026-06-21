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

class TestJFloatParseFloat:
    def test_parse_float_decimal(self):
        assert math.isclose(JFloat.parseFloat("3.14"), 3.14, rel_tol=1e-6)

    def test_parse_float_negativo(self):
        assert math.isclose(JFloat.parseFloat("-1.5"), -1.5, rel_tol=1e-6)

    def test_parse_float_invalido_lanca_exception(self):
        import pytest
        with pytest.raises(ValueError):
            JFloat.parseFloat("abc")

class TestJFloatValueOf:
    def test_value_of_float(self):
        numero = JFloat.valueOf(1.5)
        assert isinstance(numero, JFloat)

    def test_value_of_string(self):
        numero = JFloat.valueOf("1.5")
        assert math.isclose(numero.floatValue(), 1.5, rel_tol=1e-6)


class TestJFloatToString:
    def test_to_string_instancia(self):
        numero = JFloat(1.5)
        assert numero.toString() == "1.5"

    def test_to_string_estatico(self):
        assert JFloat.toString(1.5) == "1.5"
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

class TestJFloatToHexString:
    def test_to_hex_string_um(self):
        assert JFloat.toHexString(1.0) == "0x1.0p0"
