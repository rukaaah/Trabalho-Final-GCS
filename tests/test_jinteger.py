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