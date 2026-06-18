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
