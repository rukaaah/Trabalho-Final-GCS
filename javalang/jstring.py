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
    def equals(self, anObject):
        # java: retorna True apenas se anObject for String com mesmo conteudo
        if isinstance(anObject, JString):
            return self._valor == anObject._valor
        if isinstance(anObject, str):
            return self._valor == anObject
        return False

    def equalsIgnoreCase(self, anotherString):
        # java: comparacao sem diferenciar maiusculas/minusculas
        outro = anotherString._valor if isinstance(anotherString, JString) else anotherString
        return self._valor.lower() == outro.lower()
    
    def compareTo(self, anotherString):
        # java: comparacao lexicografica; retorna diferenca do primeiro char divergente
        outro = anotherString._valor if isinstance(anotherString, JString) else anotherString
        if self._valor == outro:
            return 0
        for c1, c2 in zip(self._valor, outro):
            if c1 != c2:
                return ord(c1) - ord(c2)
        return len(self._valor) - len(outro)
    
    def compareToIgnoreCase(self, str_):
        # java: comparacao lexicografica sem diferenciar maiusculas/minusculas
        outro = str_._valor if isinstance(str_, JString) else str_
        a = self._valor.lower()
        b = outro.lower()
        if a == b:
            return 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                return ord(c1) - ord(c2)
        return len(a) - len(b)

    def contentEquals(self, cs):
        # java: compara com qualquer CharSequence (StringBuilder, StringBuffer, etc.)
        # python: aceita str e JString como analogos idiomaticos — ver docs/adaptacoes.md
        if isinstance(cs, JString):
            return self._valor == cs._valor
        if isinstance(cs, str):
            return self._valor == cs
        return False
    
    def regionMatches(self, toffset, other, ooffset, len_, ignoreCase=False):
        # unifica regionMatches(int,String,int,int) e regionMatches(bool,int,String,int,int)
        # python nao tem sobrecarga; ignoreCase=False como default cobre as duas assinaturas
        outro = other._valor if isinstance(other, JString) else other
        if toffset < 0 or ooffset < 0:
            return False
        if toffset + len_ > len(self._valor) or ooffset + len_ > len(outro):
            return False
        trecho_self = self._valor[toffset:toffset + len_]
        trecho_outro = outro[ooffset:ooffset + len_]
        if ignoreCase:
            return trecho_self.lower() == trecho_outro.lower()
        return trecho_self == trecho_outro


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