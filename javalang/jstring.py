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

def _unwrap(obj):
    if hasattr(obj, '_valor'):
        return str(obj._valor)
    if hasattr(obj, 'toString'):
        try:
            return str(obj.toString())
        except:
            pass
    return str(obj) if obj is not None else ""


class JString:
    # ==========================================
    # NÚCLEO BASE E CONSTRUTORES (Issue 1 e 2)
    # ==========================================
    def __init__(self, *args):
        if not args:
            self._valor = ""
            return

        primeiro = args[0]

        # Suporte da Issue 1 (Núcleo Base)
        if isinstance(primeiro, JString):
            self._valor = str(getattr(primeiro, '_valor'))
            return

        # Suporte da Issue 2: byte[] com slices e charsets
        if isinstance(primeiro, (bytes, bytearray)):
            if len(args) == 2 and isinstance(args[1], str):
                charset = args[1].lower()
                self._valor = primeiro.decode(charset)
            elif len(args) == 3 and isinstance(args[1], int) and isinstance(args[2], int):
                offset, length = args[1], args[2]
                self._valor = primeiro[offset:offset+length].decode('utf-8')
            else:
                self._valor = primeiro.decode('utf-8')
            return

        # Suporte da Issue 2: char[] e char[] com offset/count
        if isinstance(primeiro, list):
            if len(args) == 3 and isinstance(args[1], int) and isinstance(args[2], int):
                offset, count = args[1], args[2]
                lista_fatiada = primeiro[offset:offset+count]
            else:
                lista_fatiada = primeiro

            # Diferencia Code Points usando o primeiro elemento
            if lista_fatiada and isinstance(lista_fatiada[0], int):
                self._valor = "".join(chr(cp) for cp in lista_fatiada)
            else:
                self._valor = "".join(str(ch) for ch in lista_fatiada)
            return

        # Suporte da Issue 2: StringBuilder
        if type(primeiro).__name__ == "StringBuilder":
            raise NotImplementedError("Conversão direta de StringBuilder não suportada em Python. Use concatenação ou .join().")

        # Fallback padrão
        self._valor = str(primeiro)
        
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
    # ==========================================
    def equals(self, anObject):
        if isinstance(anObject, JString):
            return self._valor == anObject._valor
        if isinstance(anObject, str):
            return self._valor == anObject
        return False

    def equalsIgnoreCase(self, anotherString):
        outro = anotherString._valor if isinstance(anotherString, JString) else anotherString
        return self._valor.lower() == outro.lower()
    
    def compareTo(self, anotherString):
        outro = anotherString._valor if isinstance(anotherString, JString) else anotherString
        if self._valor == outro:
            return 0
        for c1, c2 in zip(self._valor, outro):
            if c1 != c2:
                return ord(c1) - ord(c2)
        return len(self._valor) - len(outro)
    
    def compareToIgnoreCase(self, str_):
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
        if isinstance(cs, JString):
            return self._valor == cs._valor
        if isinstance(cs, str):
            return self._valor == cs
        return False
    
    def regionMatches(self, toffset, other, ooffset, len_, ignoreCase=False):
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
    # ==========================================
    def codePointAt(self, index: int) -> int:
        if index < 0 or index >= len(self._valor):
            raise IndexError(f"String index out of range: {index}")
        return ord(self._valor[index])

    def codePointBefore(self, index: int) -> int:
        if index < 1 or index > len(self._valor):
            raise IndexError(f"String index out of range: {index - 1}")
        return ord(self._valor[index - 1])

    def codePointCount(self, beginIndex: int, endIndex: int) -> int:
        if beginIndex < 0 or endIndex > len(self._valor) or beginIndex > endIndex:
            raise IndexError("String index out of range")
        return endIndex - beginIndex
    
    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int:
        resultado = index + codePointOffset
        if resultado < 0 or resultado > len(self._valor):
            raise IndexError("String index out of range")
        return resultado

    def getChars(self, srcBegin: int, srcEnd: int, dst: list, dstBegin: int) -> None:
        if srcBegin < 0 or srcEnd > len(self._valor) or srcBegin > srcEnd:
            raise IndexError("String index out of range")
        for i, ch in enumerate(self._valor[srcBegin:srcEnd]):
            dst[dstBegin + i] = ch

    def getBytes(self, charsetName: str = None) -> bytes:
        if charsetName is None:
            return self._valor.encode("utf-8")
        try:
            return self._valor.encode(charsetName)
        except LookupError:
            raise LookupError(f"Charset nao suportado: '{charsetName}'")

    # ==========================================
    # BUSCA BASE (Issue 5)
    # ==========================================
    def indexOf(self, search, fromIndex: int = 0) -> int:
        if fromIndex < 0:
            fromIndex = 0
        if isinstance(search, int):
            alvo = chr(search)
        else:
            alvo = search._valor if isinstance(search, JString) else search
        resultado = self._valor.find(alvo, fromIndex)
        return resultado
    
    def lastIndexOf(self, search, fromIndex: int = None) -> int:
        if isinstance(search, int):
            alvo = chr(search)
        else:
            alvo = search._valor if isinstance(search, JString) else search
        if fromIndex is None:
            return self._valor.rfind(alvo)
        return self._valor.rfind(alvo, 0, fromIndex + 1)

    # ==========================================
    # EXTRAÇÃO E BUSCA COMPLEMENTAR (Issue 6)
    # ==========================================
    def contains(self, s) -> bool:
        if s is None:
            raise TypeError("NullPointerException")
        alvo = _unwrap(s)
        return alvo in self._valor

    def startsWith(self, prefix, toffset: int = 0) -> bool:
        pref = prefix._valor if isinstance(prefix, JString) else str(prefix)
        if toffset < 0 or toffset > len(self._valor):
            return False
        return self._valor.startswith(pref, toffset)

    def endsWith(self, suffix) -> bool:
        suf = suffix._valor if isinstance(suffix, JString) else str(suffix)
        return self._valor.endswith(suf)

    def substring(self, beginIndex: int, endIndex: int = None) -> 'JString':
        if endIndex is None:
            endIndex = len(self._valor)
            
        if beginIndex < 0 or endIndex > len(self._valor) or beginIndex > endIndex:
            raise IndexError("String index out of range")
            
        return JString(self._valor[beginIndex:endIndex])

    # ==========================================
    # TRANSFORMAÇÕES E FORMATAÇÃO (Issue 7)
    # ==========================================
    def subSequence(self, beginIndex: int, endIndex: int):
        if beginIndex < 0 or endIndex < 0 or endIndex > len(self._valor) or beginIndex > endIndex:
            raise IndexError("String index out of range")
        return JString(self._valor[beginIndex:endIndex])

    def toLowerCase(self) -> 'JString':
        return JString(self._valor.lower())

    def toUpperCase(self) -> 'JString':
        return JString(self._valor.upper())

    def trim(self) -> 'JString':
        return JString(self._valor.strip())

    def concat(self, str_) -> 'JString':
        if str_ is None:
            raise TypeError("NullPointerException")
        outro = _unwrap(str_)
        return JString(self._valor + outro)

    def replace(self, target, replacement) -> 'JString':
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
    # ==========================================
    def matches(self, regex: str) -> bool:
        import re as _re
        return _re.fullmatch(regex, self._valor) is not None

    def replaceFirst(self, regex: str, replacement: str) -> 'JString':
        import re as _re
        return JString(_re.sub(regex, replacement, self._valor, count=1))

    def replaceAll(self, regex: str, replacement: str) -> 'JString':
        import re as _re
        return JString(_re.sub(regex, replacement, self._valor))
    
    def __eq__(self, other):
        if isinstance(other, JString):
            return self._valor == other._valor
        if isinstance(other, str):
            return self._valor == other
        return False
    
    def split(self, regex: str, limit: int = 0) -> list:
        import re as _re
        if limit > 0:
            partes = _re.split(regex, self._valor, maxsplit=limit - 1)
        elif limit < 0:
            partes = _re.split(regex, self._valor)
        else:
            partes = _re.split(regex, self._valor)
            while partes and partes[-1] == "":
                partes.pop()
        return [JString(p) for p in partes]

    def intern(self) -> 'JString':
        return self

    # ==========================================
    # UTILITÁRIOS ESTÁTICOS (Issue 9)
    # ==========================================
    @staticmethod
    def valueOf(value) -> 'JString':
        if value is None:
            return JString("null")
        if isinstance(value, bool):
            return JString("true" if value else "false")
        if isinstance(value, list):
            return JString("".join(str(c) for c in value))
        return JString(str(value))

    @staticmethod
    def copyValueOf(data: list) -> 'JString':
        return JString.valueOf(data)

    @staticmethod
    def format(format_str, *args) -> 'JString':
        f_str = format_str._valor if isinstance(format_str, JString) else str(format_str)
        
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args_list = args[0]
        else:
            args_list = args
            
        args_formatados = tuple(
            a._valor if isinstance(a, JString) else a for a in args_list
        )
        return JString(f_str % args_formatados)

    @staticmethod
    def join(delimiter, *elements) -> 'JString':
        if delimiter is None:
            raise TypeError("NullPointerException")
            
        delim = _unwrap(delimiter)
        
        if len(elements) == 1 and isinstance(elements[0], (list, tuple, set)):
            lista_elementos = elements[0]
        else:
            lista_elementos = elements
            
        str_elements = []
        for el in lista_elementos:
            if el is None:
                str_elements.append("null")
            else:
                str_elements.append(_unwrap(el))
                
        return JString(delim.join(str_elements))