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
        # Em Python não há um equivalente direto (ver adaptação registrada
        # em docs/adaptacoes.md). Aqui validamos apenas que o atributo
        # existe e aponta para o tipo usado internamente pela classe.
        assert JInteger.TYPE is not None


class TestJIntegerConstrutor:
    def test_construtor_aceita_inteiro(self):
        numero = JInteger(10)
        assert numero is not None

    def test_construtor_guarda_valor_internamente(self):
        # Verifica apenas que a instância foi criada com sucesso a partir
        # de um int, sem depender de métodos de conversão (intValue, etc.),
        # que ainda não fazem parte do escopo desta issue.
        numero = JInteger(0)
        assert isinstance(numero, JInteger)

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

