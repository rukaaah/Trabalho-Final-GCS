"""
Módulo de testes para a classe JInteger.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.

ESCOPO DESTE ARQUIVO (Issue #12 - feat/jinteger-conversoes):
Cobre o construtor alternativo Integer(String s) e os métodos de
conversão numérica primitiva (byteValue, shortValue, intValue,
longValue, floatValue).

ATENÇÃO (conforme a Issue #12):
Java diferencia rigorosamente byte, short, int e long; Python tem um
único tipo int. Os testes abaixo cobrem apenas o comportamento normal
(valores dentro da faixa correspondente). Casos de limite/overflow
(ex.: um valor maior que o limite de um byte sendo convertido via
byteValue()) dependem de uma decisão de equipe ainda não tomada sobre
simular overflow ou não - essa decisão deve ser registrada em
docs/adaptacoes.md antes de testes desses casos-limite serem
adicionados.

FLUXO (conforme Issue #12):
QA escreve estes testes nesta branch (feat/jinteger-conversoes) e os
sobe SEM abrir Pull Request. O Dev então implementa javalang/jinteger.py
nesta mesma branch até os testes ficarem GREEN, e juntos abrem o PR
final referenciando Closes #12.
"""

from javalang.jinteger import JInteger


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
