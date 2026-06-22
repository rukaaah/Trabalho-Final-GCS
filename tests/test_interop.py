"""
Suíte de testes de Interoperabilidade (Interop).

OBJETIVO:
Garantir que JString, JInteger e JFloat funcionem perfeitamente juntas,
assim como no ecossistema Java. A avaliação foca na integração harmoniosa.

O QUE TESTAR AQUI:
- Conversão de JInteger e JFloat para JString (String.valueOf, toString).
- Parsing de JString para JInteger/JFloat (Integer.parseInt, Float.parseFloat).
- Operações de formatação (String.format recebendo instâncias das outras classes).

ATENÇÃO:
Estes testes só farão sentido a partir do Sprint 3 (Baseline v0.3), quando
mais de uma classe já estiver implementada.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""
import pytest
from javalang.jinteger import JInteger
from javalang.jfloat import JFloat
from javalang.jstring import JString

def test_conversao_cruzada():
    # TODO: Implementar testes que conectam as 3 classes
    pass

class TestInteropParsingEIgualdade:
    @pytest.mark.xfail(reason="JInteger.parseInt nao aceita JString diretamente, so str puro - gap conhecido refs #92")
    def test_parse_int_recebendo_jstring_radix_hex(self):
        s = JString("ff")
        assert JInteger.parseInt(s, 16) == 255

    def test_jstring_equals_isolamento_de_tipo(self):
        s = JString("123")
        i = JInteger(123)
        assert s.equals(i) is False

    @pytest.mark.xfail(reason="JString.concat imprime endereco de memoria ao inves do valor formatado - gap conhecido refs #92")
    def test_jstring_concat_recebendo_jinteger(self):
        s = JString("valor: ")
        i = JInteger(42)
        assert s.concat(i).toCharArray() == list("valor: 42")

class TestInteropFormatacaoEBusca:
    def test_jinteger_to_string_formatacao_limpa(self):
        i = JInteger(42)
        assert i.toString() == "42"

    def test_jfloat_to_string_formatacao_limpa(self):
        f = JFloat(3.14)
        assert f.toString() == "3.14"

    @pytest.mark.xfail(reason="JString.contains nao reconhece JInteger como argumento de busca - gap conhecido refs #92")
    def test_jstring_contains_recebendo_jinteger(self):
        s = JString("valor: 42")
        i = JInteger(42)
        assert s.contains(i) is True

class TestInteropJoin:
    @pytest.mark.xfail(reason="JString.join imprime endereco de memoria para tipos nao-JString - gap conhecido refs #92")
    def test_join_com_lista_mista(self):
        partes = [JString("a"), JInteger(1), JFloat(2.5)]
        resultado = JString.join(JString("-"), *partes)
        assert resultado.toCharArray() == list("a-1-2.5")
