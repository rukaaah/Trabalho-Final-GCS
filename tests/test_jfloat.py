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
from javalang.jfloat import JFloat

def test_jfloat_is_nan():
    # TODO: Implementar teste com casos de borda do IEEE 754
    pass
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
