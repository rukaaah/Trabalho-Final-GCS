# Registro de Uso de Inteligência Artificial

Este documento serve como declaração obrigatória do uso de ferramentas de IA generativa (ChatGPT, Gemini, GitHub Copilot, etc.) como auxílio na implementação técnica deste projeto. 

Conforme as regras de GCS, a utilização de IA não exime o desenvolvedor da responsabilidade de explicar oralmente o código sob seu nome.

---

## 📋 Template de Registro
*(Desenvolvedor: Copie o bloco abaixo, preencha com suas informações e adicione no topo da seção de "Logs de Utilização" sempre que utilizar IA para gerar ou refatorar lógicas de métodos).*

### Módulo: `[Nome da Classe]` - Método: `[Nome do Método]`
* **Data:** DD/MM/2026
* **Desenvolvedor Responsável:** @[seu_usuario]
* **Métodos Implementados/Auxiliados:** `[Ex: JString.regionMatches]`
* **Ferramenta Utilizada:** `[Ex: ChatGPT / Gemini]`
* **Prompt Representativo:**
  > "[Cole aqui a essência ou a cópia exata do prompt que você enviou para a IA. Ex: 'Como posso simular o comportamento de offset de CodePoints do Java em Python 3.10 preservando a performance?']"

---

## 🗄️ Logs de Utilização

*(Adicione os novos registros abaixo desta linha)*
### Módulo: `JInteger` - Método: `toString(int, radix), toBinaryString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.toString` (estendido), `JInteger.toBinaryString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Unifique toString(int)/toString(int, radix) estáticos do Java usando argumento default em Python. Implemente um conversor genérico para base 2-36 e replique o fallback do Java para radix inválido (volta a base 10). Implemente toBinaryString tratando o valor como bits sem sinal de 32 bits."
* **Observação:** A IA acelerou a escrita do conversor de base. Validei manualmente o fallback de radix inválido (conferido contra o Javadoc) e o comportamento unsigned de toBinaryString(-1).

### Módulo: `JInteger` - Método: `toOctalString, toHexString`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.toOctalString`, `JInteger.toHexString`
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Implemente toOctalString e toHexString para JInteger, reaproveitando a lógica de bits sem sinal de 32 bits usada em toBinaryString."
* **Observação:** Conferi que toHexString(-1) retorna "ffffffff" e toOctalString(-1) retorna "37777777777", batendo com a saída real do javac.

### Módulo: `JInteger` - Constantes e Construtor (Issue #11)
* **Data:** 16/06/2026
* **Desenvolvedor Responsável:** @GomesYV
* **Métodos Implementados/Auxiliados:** Testes de `JInteger.MAX_VALUE`, `MIN_VALUE`, `SIZE`, `BYTES`, `TYPE` e do construtor `Integer(int value)`.
* **Ferramenta Utilizada:** Claude (Anthropic)
* **Prompt Representativo:**
  > "Escreva os testes em pytest para as constantes estáticas e o construtor primário da classe JInteger, cobrindo o contrato da Issue #11, em blocos de até 3 testes por commit, seguindo o fluxo TDD descrito (testes em RED, sem abrir PR contra a main)."