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
