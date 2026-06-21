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
