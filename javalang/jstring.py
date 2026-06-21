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
    def codePointAt(self, index: int) -> int:
        # java: retorna o codepoint unicode na posicao index
        # python: ord() ja retorna codepoint correto sem surrogate pairs
        if index < 0 or index >= len(self._valor):
            raise IndexError(f"String index out of range: {index}")
        return ord(self._valor[index])

    def codePointBefore(self, index: int) -> int:
        # java: retorna o codepoint unicode antes da posicao index
        if index < 1 or index > len(self._valor):
            raise IndexError(f"String index out of range: {index - 1}")
        return ord(self._valor[index - 1])

    def codePointCount(self, beginIndex: int, endIndex: int) -> int:
        # java: conta codepoints no intervalo [beginIndex, endIndex)
        # python: sem surrogate pairs, equivale ao numero de caracteres do slice
        if beginIndex < 0 or endIndex > len(self._valor) or beginIndex > endIndex:
            raise IndexError("String index out of range")
        return endIndex - beginIndex
    
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int:
        # java: retorna o indice deslocado por codePointOffset codepoints a partir de index
        # python: sem surrogate pairs, deslocamento equivale a soma direta de indices
        resultado = index + codePointOffset
        if resultado < 0 or resultado > len(self._valor):
            raise IndexError("String index out of range")
        return resultado

    def getChars(self, srcBegin: int, srcEnd: int, dst: list, dstBegin: int) -> None:
        # java: copia chars de [srcBegin, srcEnd) para dst a partir de dstBegin
        # python: dst deve ser uma list mutavel (analogo ao char[] do java)
        if srcBegin < 0 or srcEnd > len(self._valor) or srcBegin > srcEnd:
            raise IndexError("String index out of range")
        for i, ch in enumerate(self._valor[srcBegin:srcEnd]):
            dst[dstBegin + i] = ch

    def getBytes(self, charsetName: str = None) -> bytes:
        # unifica getBytes() e getBytes(String charsetName)
        # java: UnsupportedEncodingException -> python: LookupError em charset invalido
        if charsetName is None:
            return self._valor.encode("utf-8")
        try:
            return self._valor.encode(charsetName)
        except LookupError:
            raise LookupError(f"Charset nao suportado: '{charsetName}'")

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
    def subSequence(self, beginIndex: int, endIndex: int):
        # java: retorna CharSequence. Aqui retornamos uma nova JString (análogo idiomático)
        if beginIndex < 0 or endIndex < 0 or endIndex > len(self._valor) or beginIndex > endIndex:
            raise IndexError("String index out of range")
        return JString(self._valor[beginIndex:endIndex])

    def toLowerCase(self) -> 'JString':
        return JString(self._valor.lower())

    def toUpperCase(self) -> 'JString':
        return JString(self._valor.upper())

    def trim(self) -> 'JString':
        # java: remove caracteres com valor <= ' ' (\u0020)
        # python: strip() remove caracteres de espaço em branco por padrão
        # (A diferença de comportamento foi documentada em docs/adaptacoes.md)
        return JString(self._valor.strip())

    def concat(self, str_) -> 'JString':
        outro = str_._valor if isinstance(str_, JString) else str(str_)
        return JString(self._valor + outro)

    def replace(self, target, replacement) -> 'JString':
        # unifica replace(char oldChar, char newChar) e 
        # replace(CharSequence target, CharSequence replacement)
        if isinstance(target, int):
            t = chr(target)
        else:
            t = target._valor if isinstance(target, JString) else str(target)
            
        if isinstance(replacement, int):
            r = chr(replacement)
        else:
            r = replacement._valor if isinstance(replacement, JString) else str(replacement)
            
        return JString(self._valor.replace(t, r))


    # ==========================================
    # REGEX, SPLITS E INTERN (Issue 8)
    # (Ex: matches, split, replaceAll, intern)
    # ==========================================
    # TODO: Implementações da Issue 8 aqui
    def matches(self, regex: str) -> bool:
        # java: retorna True se a string inteira bate com o regex
        # re.fullmatch exige correspondencia completa, identico ao java
        import re as _re
        return _re.fullmatch(regex, self._valor) is not None

    def replaceFirst(self, regex: str, replacement: str) -> 'JString':
        # java: substitui apenas a primeira ocorrencia do regex
        import re as _re
        return JString(_re.sub(regex, replacement, self._valor, count=1))

    def replaceAll(self, regex: str, replacement: str) -> 'JString':
        # java: substitui todas as ocorrencias do regex
        import re as _re
        return JString(_re.sub(regex, replacement, self._valor))
    
    def __eq__(self, other):
        if isinstance(other, JString):
            return self._valor == other._valor
        if isinstance(other, str):
            return self._valor == other
        return False
    
    def split(self, regex: str, limit: int = 0) -> list:
        # unifica split(String regex) e split(String regex, int limit)
        # java: limit=0 remove trailing empty strings; limit<0 preserva; limit>0 limita partes
        import re as _re
        if limit > 0:
            partes = _re.split(regex, self._valor, maxsplit=limit - 1)
        elif limit < 0:
            partes = _re.split(regex, self._valor)
        else:
            # limit=0: remove strings vazias do final (comportamento padrao do java)
            partes = _re.split(regex, self._valor)
            while partes and partes[-1] == "":
                partes.pop()
        return [JString(p) for p in partes]

    def intern(self) -> 'JString':
        # java: retorna referencia do pool de strings da JVM
        # python: sys.intern() nao se aplica a objetos customizados; CPython nao tem pool equivalente
        # retorna self como stub — ver docs/adaptacoes.md
        return self


    # ==========================================
    # UTILITÁRIOS ESTÁTICOS (Issue 9)
    # (Ex: valueOf, format, join)
    # ==========================================
    # TODO: Implementações da Issue 9 aqui