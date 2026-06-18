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

### Módulo: `JInteger` - Constantes e Construtor (Issue #11)
* **Data:** 16/06/2026
* **Desenvolvedor Responsável:** @GomesYV
* **Métodos Implementados/Auxiliados:** Testes de `JInteger.MAX_VALUE`, `MIN_VALUE`, `SIZE`, `BYTES`, `TYPE` e do construtor `Integer(int value)`.
* **Ferramenta Utilizada:** Claude (Anthropic)
* **Prompt Representativo:**
  > "Escreva os testes em pytest para as constantes estáticas e o construtor primário da classe JInteger, cobrindo o contrato da Issue #11, em blocos de até 3 testes por commit, seguindo o fluxo TDD descrito (testes em RED, sem abrir PR contra a main)."

  ### Módulo: JInteger - Métodos: Reversão de Bits e Bytes

- **Data:** 18/06/2026
- **Desenvolvedor Responsável:** @GabrielMattosA
- **Métodos Implementados/Auxiliados:** `JInteger.reverse` e `JInteger.reverseBytes`
- **Ferramenta Utilizada:** Gemini
- **Prompt Representativo:**
  "Como implementar os métodos de espelhamento binário reverse e inversão de endianness reverseBytes do Java 8 em Python garantindo o estouro para signed int de 32 bits?"