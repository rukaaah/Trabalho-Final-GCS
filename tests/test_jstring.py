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
import pytest
# from javalang.jstring import JString

def test_jstring_char_at():
    # TODO: Implementar teste
    pass