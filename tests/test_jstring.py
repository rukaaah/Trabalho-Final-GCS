"""
Suíte de testes para a classe JString.

OBJETIVO:
Validar o comportamento imutável e os ~60 métodos da classe String do
Java SE 8.

FLUXO (ADR-0004 - TDD / Test-First):
Esta suíte foi escrita ANTES da implementação de javalang/jstring.py.
É esperado que TODOS os testes falhem inicialmente (RED). Cada
desenvolvedor deve implementar o necessário em javalang/jstring.py até
que o(s) bloco(s) sob sua responsabilidade fiquem GREEN.

ORGANIZAÇÃO EM BLOCOS (REGRA GCS ANTI-ATALHO):
- Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
- Um commit não pode conter mais de 3 métodos de teste.
Os testes estão agrupados em blocos numerados por classe `Test*`. Cada
bloco contém poucos testes e pode ser usado como unidade de trabalho
para uma Issue/PR. Não é necessário implementar um bloco inteiro de
uma vez: respeite o limite de 3 métodos de teste por commit.

LEMBRETE DE ADAPTAÇÕES:
Se um teste falhar porque o Python trata strings de forma diferente do
Java (ex.: intern(), StringBuffer/StringBuilder, Locale em
toUpperCase/toLowerCase, conforme ADR-0003), abra uma Issue com label
`decision`, registre em docs/adaptacoes.md e ajuste/remova o teste
correspondente via PR de decisão.
"""

import pytest

from javalang.jstring import JString


# ---------------------------------------------------------------------------
# BLOCO 1 - Construtores
# Issue sugerida: "JString - Construtores"
# ---------------------------------------------------------------------------
class TestJStringConstrutores:
    def test_construtor_vazio(self):
        texto = JString()
        assert texto.toString() == ""

    def test_construtor_com_string(self):
        texto = JString("abc")
        assert texto.toString() == "abc"

    def test_construtor_copia_outra_jstring(self):
        original = JString("abc")
        copia = JString(original)
        assert copia.toString() == "abc"
        assert copia.equals(original) is True

    def test_construtor_com_lista_de_caracteres(self):
        texto = JString(["a", "b", "c"])
        assert texto.toString() == "abc"


# ---------------------------------------------------------------------------
# BLOCO 2 - Acesso e tamanho (charAt, length, isEmpty, codePointAt)
# Issue sugerida: "JString - Acesso e tamanho"
# ---------------------------------------------------------------------------
class TestJStringAcessoETamanho:
    def test_length(self):
        assert JString("abc").length() == 3

    def test_length_string_vazia(self):
        assert JString("").length() == 0

    def test_char_at(self):
        assert JString("abc").charAt(1) == "b"

    def test_char_at_indice_invalido_lanca_exception(self):
        with pytest.raises(IndexError):
            JString("abc").charAt(10)

    def test_is_empty_true(self):
        assert JString("").isEmpty() is True

    def test_is_empty_false(self):
        assert JString("abc").isEmpty() is False

    def test_code_point_at(self):
        assert JString("A").codePointAt(0) == 65


# ---------------------------------------------------------------------------
# BLOCO 3 - Comparação e igualdade (equals, equalsIgnoreCase, compareTo)
# Issue sugerida: "JString - Comparação e igualdade"
# ---------------------------------------------------------------------------
class TestJStringComparacao:
    def test_equals_strings_iguais(self):
        assert JString("abc").equals(JString("abc")) is True

    def test_equals_strings_diferentes(self):
        assert JString("abc").equals(JString("abd")) is False

    def test_equals_ignore_case(self):
        assert JString("ABC").equalsIgnoreCase(JString("abc")) is True

    def test_compare_to_ordem_lexicografica(self):
        assert JString("a").compareTo(JString("b")) < 0
        assert JString("b").compareTo(JString("a")) > 0
        assert JString("a").compareTo(JString("a")) == 0

    def test_compare_to_ignore_case(self):
        assert JString("ABC").compareToIgnoreCase(JString("abc")) == 0

    def test_hash_code_consistente(self):
        assert JString("abc").hashCode() == JString("abc").hashCode()


# ---------------------------------------------------------------------------
# BLOCO 4 - Busca (indexOf, lastIndexOf, contains, startsWith, endsWith)
# Issue sugerida: "JString - Busca"
# ---------------------------------------------------------------------------
class TestJStringBusca:
    def test_index_of_encontrado(self):
        assert JString("hello world").indexOf("world") == 6

    def test_index_of_nao_encontrado(self):
        assert JString("hello world").indexOf("xyz") == -1

    def test_index_of_com_from_index(self):
        assert JString("abcabc").indexOf("a", 1) == 3

    def test_last_index_of(self):
        assert JString("abcabc").lastIndexOf("a") == 3

    def test_contains_true(self):
        assert JString("hello world").contains("world") is True

    def test_starts_with(self):
        assert JString("hello world").startsWith("hello") is True

    def test_ends_with(self):
        assert JString("hello world").endsWith("world") is True


# ---------------------------------------------------------------------------
# BLOCO 5 - Transformações (substring, concat, replace, trim)
# Issue sugerida: "JString - Transformações básicas"
# ---------------------------------------------------------------------------
class TestJStringTransformacoes:
    def test_substring_com_um_argumento(self):
        assert JString("hello world").substring(6).toString() == "world"

    def test_substring_com_dois_argumentos(self):
        assert JString("hello world").substring(0, 5).toString() == "hello"

    def test_concat(self):
        original = JString("hello")
        resultado = original.concat(JString(" world"))
        assert resultado.toString() == "hello world"
        # Garante imutabilidade: original não é alterada
        assert original.toString() == "hello"

    def test_replace_caractere(self):
        assert JString("hello").replace("l", "L").toString() == "heLLo"

    def test_trim(self):
        assert JString("  hello  ").trim().toString() == "hello"

    def test_strip(self):
        assert JString("  hello  ").strip().toString() == "hello"


# ---------------------------------------------------------------------------
# BLOCO 6 - Alteração de caixa (toUpperCase, toLowerCase)
# Issue sugerida: "JString - Alteração de caixa (ver ADR-0003)"
# ---------------------------------------------------------------------------
class TestJStringCaixa:
    def test_to_upper_case(self):
        assert JString("hello").toUpperCase().toString() == "HELLO"

    def test_to_lower_case(self):
        assert JString("HELLO").toLowerCase().toString() == "hello"

    def test_to_upper_case_nao_altera_original(self):
        original = JString("hello")
        original.toUpperCase()
        assert original.toString() == "hello"


# ---------------------------------------------------------------------------
# BLOCO 7 - Regex (matches, split, replaceAll)
# Issue sugerida: "JString - Regex"
# ---------------------------------------------------------------------------
class TestJStringRegex:
    def test_matches_true(self):
        assert JString("12345").matches(r"\d+") is True

    def test_matches_false(self):
        assert JString("abc").matches(r"\d+") is False

    def test_split_simples(self):
        partes = JString("a,b,c").split(",")
        assert [p.toString() for p in partes] == ["a", "b", "c"]

    def test_split_com_regex(self):
        partes = JString("a1b22c").split(r"\d+")
        assert [p.toString() for p in partes] == ["a", "b", "c"]

    def test_replace_all(self):
        resultado = JString("a1b2c3").replaceAll(r"\d", "")
        assert resultado.toString() == "abc"


# ---------------------------------------------------------------------------
# BLOCO 8 - valueOf (conversões estáticas a partir de outros tipos)
# Issue sugerida: "JString - valueOf"
# ---------------------------------------------------------------------------
class TestJStringValueOf:
    def test_value_of_int(self):
        assert JString.valueOf(123).toString() == "123"

    def test_value_of_float(self):
        assert JString.valueOf(1.5).toString() == "1.5"

    def test_value_of_bool(self):
        assert JString.valueOf(True).toString() == "true"

    def test_value_of_char_array(self):
        assert JString.valueOf(["a", "b", "c"]).toString() == "abc"


# ---------------------------------------------------------------------------
# BLOCO 9 - Conversão para array de caracteres (toCharArray) e formatação
# Issue sugerida: "JString - toCharArray e format"
# ---------------------------------------------------------------------------
class TestJStringArrayEFormatacao:
    def test_to_char_array(self):
        assert JString("abc").toCharArray() == ["a", "b", "c"]

    def test_format_com_placeholder_de_string(self):
        resultado = JString.format("Olá, %s!", "Mundo")
        assert resultado.toString() == "Olá, Mundo!"

    def test_format_com_placeholder_numerico(self):
        resultado = JString.format("Valor: %d", 42)
        assert resultado.toString() == "Valor: 42"


# ---------------------------------------------------------------------------
# BLOCO 10 - Imutabilidade geral
# Issue sugerida: "JString - Garantias de imutabilidade"
# ---------------------------------------------------------------------------
class TestJStringImutabilidade:
    def test_substring_nao_altera_original(self):
        original = JString("hello world")
        original.substring(0, 5)
        assert original.toString() == "hello world"

    def test_replace_nao_altera_original(self):
        original = JString("hello")
        original.replace("l", "L")
        assert original.toString() == "hello"

    def test_trim_nao_altera_original(self):
        original = JString("  hello  ")
        original.trim()
        assert original.toString() == "  hello  "
