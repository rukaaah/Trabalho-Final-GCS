"""
Módulo contendo a implementação da classe JString.

Esta classe reproduz o contrato público da especificação da classe String
do Java SE 8. É fundamental garantir que as instâncias desta classe se
comportem como imutáveis, assim como no Java.

Aviso aos Desenvolvedores:
- Esta é a classe mais extensa, com cerca de 60 métodos. Dividam o trabalho
  formalmente através de Issues.
- Mantenha a nomenclatura original em camelCase (ex: charAt, substring).
- Métodos que dependem de construtos específicos do Java (como StringBuffer
  ou intern) devem ter suas adaptações documentadas no README.md.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""

class JString:
    def __init__(self):
        # TODO: Implementar múltiplas formas de construção
        pass

    # TODO: Implementar métodos de acesso, tamanho, comparação, busca e regex