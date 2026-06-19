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
