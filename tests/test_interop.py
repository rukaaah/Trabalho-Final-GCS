"""
Suíte de testes de Interoperabilidade (Interop).

OBJETIVO:
Garantir que JString, JInteger e JFloat funcionem perfeitamente juntas,
assim como no ecossistema Java. A avaliação foca na integração harmoniosa.

FLUXO (ADR-0004 - TDD / Test-First):
Estes testes só farão sentido a partir do Sprint 3 (Baseline v0.3),
quando mais de uma classe já estiver implementada. Até então, é
esperado que toda esta suíte falhe (RED) por ImportError/AttributeError
- isso é aceitável e intencional, servindo de guia para a integração.

ORGANIZAÇÃO EM BLOCOS (REGRA GCS ANTI-ATALHO):
- Um Pull Request NÃO pode conter mais do que 7 casos de teste implementados.
- Um commit não pode conter mais de 3 métodos de teste.

ADAPTAÇÕES:
Caso `JString.format` não suporte todos os especificadores testados
abaixo, a equipe deve registrar a limitação em docs/adaptacoes.md via
PR de decisão, ajustando os testes correspondentes.
"""

import math

from javalang.jfloat import JFloat
from javalang.jinteger import JInteger
from javalang.jstring import JString


# ---------------------------------------------------------------------------
# BLOCO 1 - Conversão de JInteger/JFloat para JString
# Issue sugerida: "Interop - valueOf/toString para JString"
# ---------------------------------------------------------------------------
class TestInteropConversaoParaString:
    def test_string_value_of_jinteger(self):
        numero = JInteger(42)
        resultado = JString.valueOf(numero.intValue())
        assert resultado.toString() == "42"

    def test_string_value_of_jfloat(self):
        numero = JFloat(3.14)
        resultado = JString.valueOf(numero.floatValue())
        assert resultado.toString() == "3.14"

    def test_jinteger_to_string_igual_a_jstring_value_of(self):
        numero = JInteger(100)
        assert numero.toString() == JString.valueOf(100).toString()


# ---------------------------------------------------------------------------
# BLOCO 2 - Parsing de JString para JInteger/JFloat
# Issue sugerida: "Interop - parseInt/parseFloat a partir de JString"
# ---------------------------------------------------------------------------
class TestInteropParsing:
    def test_parse_int_a_partir_de_jstring(self):
        texto = JString("123")
        numero = JInteger.parseInt(texto.toString())
        assert numero == 123

    def test_parse_float_a_partir_de_jstring(self):
        texto = JString("3.14")
        numero = JFloat.parseFloat(texto.toString())
        assert math.isclose(numero, 3.14, rel_tol=1e-6)

    def test_round_trip_jinteger_para_jstring_e_volta(self):
        original = JInteger(2024)
        texto = JString.valueOf(original.intValue())
        reconstruido = JInteger.parseInt(texto.toString())
        assert reconstruido == original.intValue()


# ---------------------------------------------------------------------------
# BLOCO 3 - Formatação combinada (JString.format recebendo JInteger/JFloat)
# Issue sugerida: "Interop - JString.format com múltiplos tipos"
# ---------------------------------------------------------------------------
class TestInteropFormatacao:
    def test_format_combinando_inteiro_e_float(self):
        idade = JInteger(30)
        altura = JFloat(1.75)
        resultado = JString.format(
            "Idade: %d, Altura: %.2f", idade.intValue(), altura.floatValue()
        )
        assert resultado.toString() == "Idade: 30, Altura: 1.75"

    def test_format_com_jstring_dentro(self):
        nome = JString("Maria")
        resultado = JString.format("Nome: %s", nome.toString())
        assert resultado.toString() == "Nome: Maria"
