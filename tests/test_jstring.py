"""
Suíte de testes para a classe JString.

OBJETIVO:
Validar o comportamento imutável e os ~60 métodos da classe String do Java SE 8.

O QUE TESTAR AQUI:
- Todos os tipos de construtores de JString.
- Acesso e tamanho (charAt, codePointAt, length).
- Buscas (indexOf, contains) e transformações (substring, replace).
- Regex (matches, split).
- Interações imutáveis (garantir que métodos não alteram a string original).

LEMBRETE DE ADAPTAÇÕES:
Se um teste falhar porque o Python trata strings de forma diferente do Java 
(ex: intern() ou charset), certifique-se de que a adaptação foi registrada
no README.md através de um PR de decisão.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""
from javalang.jstring import JString

def test_jstring_char_at():
    # TODO: Implementar teste
    pass

class TestJStringConstrutores:
    def test_construtor_vazio(self):
        s = JString()
        assert s.length() == 0

    def test_construtor_com_string_original(self):
        s = JString("ola")
        assert s.length() == 3

    def test_construtor_copia_valor(self):
        s = JString("teste")
        assert s.toCharArray() == ['t', 'e', 's', 't', 'e']

class TestJStringTamanhoEAcesso:
    def test_length_string_nao_vazia(self):
        s = JString("abcde")
        assert s.length() == 5

    def test_is_empty_string_vazia(self):
        s = JString("")
        assert s.isEmpty() is True

    def test_char_at_indice_valido(self):
        s = JString("hello")
        assert s.charAt(1) == 'e'
class TestJStringHashCode:
    def test_hash_code_consistente(self):
        a = JString("abc")
        b = JString("abc")
        assert a.hashCode() == b.hashCode()

class TestJStringMatchesEReplace:
    def test_matches_regex_simples(self):
        s = JString("abc123")
        assert s.matches(r"[a-z]+\d+") is True

    def test_replace_first(self):
        s = JString("aaa")
        assert s.replaceFirst("a", "b").toCharArray() == list("baa")

    def test_replace_all(self):
        s = JString("aaa")
        assert s.replaceAll("a", "b").toCharArray() == list("bbb")

class TestJStringSplit:
    def test_split_simples(self):
        s = JString("a,b,c")
        partes = s.split(",")
        assert [p.toCharArray() for p in partes] == [['a'], ['b'], ['c']]

    def test_split_com_limit(self):
        s = JString("a,b,c")
        partes = s.split(",", 2)
        assert len(partes) == 2

    def test_intern_mesmo_valor(self):
        a = JString("abc")
        b = JString("abc")
        assert a.intern() == b.intern()
class TestJStringIndexOfChar:
    def test_index_of_char(self):
        s = JString("hello")
        assert s.indexOf(ord('l')) == 2

    def test_index_of_char_from_index(self):
        s = JString("hello")
        assert s.indexOf(ord('l'), 3) == 3

    def test_index_of_nao_encontrado(self):
        s = JString("hello")
        assert s.indexOf(ord('z')) == -1

class TestJStringIndexOfString:
    def test_index_of_string(self):
        s = JString("hello world")
        other = JString("world")
        assert s.indexOf(other) == 6

    def test_index_of_string_from_index(self):
        s = JString("abcabc")
        other = JString("abc")
        assert s.indexOf(other, 1) == 3

    def test_last_index_of_char(self):
        s = JString("hello")
        assert s.lastIndexOf(ord('l')) == 3

class TestJStringLastIndexOf:
    def test_last_index_of_char_from_index(self):
        s = JString("hello")
        assert s.lastIndexOf(ord('l'), 2) == 2
        
class TestJStringCodePoint:
    def test_code_point_at(self):
        s = JString("abc")
        assert s.codePointAt(0) == ord('a')

    def test_code_point_before(self):
        s = JString("abc")
        assert s.codePointBefore(1) == ord('a')

    def test_code_point_count(self):
        s = JString("abc")
        assert s.codePointCount(0, 3) == 3

class TestJStringOffsetEGetChars:
    def test_offset_by_code_points(self):
        s = JString("abc")
        assert s.offsetByCodePoints(0, 2) == 2

    def test_get_chars(self):
        s = JString("hello")
        dst = [' '] * 5
        s.getChars(0, 5, dst, 0)
        assert dst == ['h', 'e', 'l', 'l', 'o']

class TestJStringGetBytes:
    def test_get_bytes_default(self):
        s = JString("abc")
        assert s.getBytes() == b'abc'
class TestJStringEquals:
    def test_equals_mesmo_conteudo(self):
        a = JString("abc")
        b = JString("abc")
        assert a.equals(b) is True

    def test_equals_ignore_case(self):
        a = JString("ABC")
        b = JString("abc")
        assert a.equalsIgnoreCase(b) is True

    def test_content_equals(self):
        a = JString("abc")
        b = JString("abc")
        assert a.contentEquals(b) is True

class TestJStringCompareTo:
    def test_compare_to_maior(self):
        a = JString("b")
        b = JString("a")
        assert a.compareTo(b) > 0

    def test_compare_to_ignore_case(self):
        a = JString("ABC")
        b = JString("abc")
        assert a.compareToIgnoreCase(b) == 0

class TestJStringRegionMatches:
    def test_region_matches_basico(self):
        a = JString("hello world")
        b = JString("world")
        assert a.regionMatches(6, b, 0, 5) is True

class TestJStringSubSequenceECase:
    def test_sub_sequence(self):
        s = JString("hello world")
        assert s.subSequence(6, 11).toCharArray() == list("world")

    def test_to_lower_case(self):
        s = JString("HELLO")
        assert s.toLowerCase().toCharArray() == list("hello")

    def test_to_upper_case(self):
        s = JString("hello")
        assert s.toUpperCase().toCharArray() == list("HELLO")

class TestJStringTrimEConcat:
    def test_trim_remove_espacos(self):
        s = JString("  hello  ")
        assert s.trim().toCharArray() == list("hello")

    def test_concat(self):
        a = JString("hello")
        b = JString(" world")
        assert a.concat(b).toCharArray() == list("hello world")

    def test_replace_char(self):
        s = JString("hello")
        assert s.replace('l', 'L').toCharArray() == list("heLLo")

class TestJStringReplaceSequence:
    def test_replace_char_sequence(self):
        s = JString("hello world")
        assert s.replace(JString("world"), JString("there")).toCharArray() == list("hello there")
