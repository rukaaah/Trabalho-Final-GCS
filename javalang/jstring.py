"""
Módulo contendo a implementação da classe JString.

Esta classe reproduz o contrato público da especificação da classe String
do Java SE 8. É fundamental garantir que as instâncias desta classe se
comportem como imutáveis, assim como no Java.

Aviso aos Desenvolvedores:
- Mantenha a nomenclatura original em camelCase (ex: charAt, substring).
- Métodos que dependem de construtos específicos do Java (como StringBuffer
  ou intern) devem ter suas adaptações documentadas no README.md.

REGRA GCS ANTI-ATALHO:
Um Pull Request NÃO pode conter mais do que 7 casos de testes implementados.
Faça PRs curtos e frequentes!
Um commit não pode conter mais de 3 métodos de teste.
"""

class JString:
    # ==========================================
    # NÚCLEO BASE E CONSTRUTORES (Issue 1 e 2)
    # ==========================================
    def __init__(self, original: object = ""):
        # TODO (Issue 2): Expandir construtor para lidar com byte[], char[], int[] (CodePoints) e StringBuilder
        if isinstance(original, JString):
            self._valor = str(getattr(original, '_valor'))
        else:
            self._valor = str(original)

    def length(self) -> int:
        return len(self._valor)
    
    def isEmpty(self) -> bool:
        return len(self._valor) == 0

    def charAt(self, index: int) -> str:
        if index < 0 or index >= len(self._valor):
            raise IndexError(f"String index out of range: {index}")
        return self._valor[index]
    
    def toCharArray(self) -> list:
        return list(self._valor)

    def hashCode(self) -> int:
        h = 0
        for char in self._valor:
            h = (31 * h + ord(char)) & 0xFFFFFFFF
            
        if h >= 0x80000000:
            h -= 0x100000000
        return h

    # ==========================================
    # COMPARAÇÕES E IGUALDADE (Issue 3)
    # (Ex: equals, compareTo, regionMatches)
    # ==========================================
    # TODO: Implementações da Issue 3 aqui


    # ==========================================
    # UNICODE E CODIFICAÇÃO (Issue 4)
    # (Ex: codePointAt, getBytes, getChars)
    # ==========================================
    # TODO: Implementações da Issue 4 aqui


    # ==========================================
    # BUSCA BASE (Issue 5)
    # (Ex: indexOf e lastIndexOf parte 1)
    # ==========================================
    # TODO: Implementações da Issue 5 aqui
    def indexOf(self, search, fromIndex: int = 0) -> int:
        # unifica indexOf(int ch), indexOf(int ch, int fromIndex),
        # indexOf(String str) e indexOf(String str, int fromIndex)
        # java nao tem sobrecarga unica — python resolve via dispatch por tipo
        if fromIndex < 0:
            fromIndex = 0
        if isinstance(search, int):
            # busca por codepoint (char)
            alvo = chr(search)
        else:
            alvo = search._valor if isinstance(search, JString) else search
        resultado = self._valor.find(alvo, fromIndex)
        return resultado
    
    def lastIndexOf(self, search, fromIndex: int = None) -> int:
        # unifica lastIndexOf(int ch), lastIndexOf(int ch, int fromIndex),
        # lastIndexOf(String str) e lastIndexOf(String str, int fromIndex)
        if isinstance(search, int):
            alvo = chr(search)
        else:
            alvo = search._valor if isinstance(search, JString) else search
        if fromIndex is None:
            # sem fromIndex: busca do final da string
            return self._valor.rfind(alvo)
        # com fromIndex: busca a partir de fromIndex em direcao ao inicio
        # java: lastIndexOf com fromIndex busca da posicao fromIndex para tras
        return self._valor.rfind(alvo, 0, fromIndex + len(alvo))


    # ==========================================
    # EXTRAÇÃO E BUSCA COMPLEMENTAR (Issue 6)
    # (Ex: substring, startsWith, contains)
    # ==========================================
    # TODO: Implementações da Issue 6 aqui


    # ==========================================
    # TRANSFORMAÇÕES E FORMATAÇÃO (Issue 7)
    # (Ex: toLowerCase, trim, replace, concat)
    # ==========================================
    # TODO: Implementações da Issue 7 aqui


    # ==========================================
    # REGEX, SPLITS E INTERN (Issue 8)
    # (Ex: matches, split, replaceAll, intern)
    # ==========================================
    # TODO: Implementações da Issue 8 aqui


    # ==========================================
    # UTILITÁRIOS ESTÁTICOS (Issue 9)
    # (Ex: valueOf, format, join)
    # ==========================================
    # TODO: Implementações da Issue 9 aqui