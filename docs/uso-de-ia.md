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

### Módulo: `JString` - Método: `Exemplo`
* **Data:** 10/06/2026
* **Desenvolvedor Responsável:** @exemplo
* **Métodos Implementados/Auxiliados:** `JString.codePointBefore(int)`
* **Ferramenta Utilizada:** Gemini
* **Prompt Representativo:**
  > "Preciso implementar o método codePointBefore do Java em Python. Como o Python lida com surrogate pairs em strings unicode internamente comparado ao char do Java?"

### Módulo: `JInteger` - Método: `Conversões (long/float) e Integer(String s)`
* **Data:** 17/06/2026
* **Desenvolvedor Responsável:** @JhonnPA
* **Métodos Implementados/Auxiliados:** `JInteger.longValue`, `JInteger.floatValue`, `JInteger.__init__` (Integer(String s))
* **Ferramenta Utilizada:** `Claude (Anthropic)`
* **Prompt Representativo:**
  > "Para JInteger, implemente longValue() (widening), floatValue() coagindo para float de 32 bits como o (float) do Java, e estenda o __init__ para aceitar str (Integer(String s)), fazendo passar os testes da QA."
* **Observação:** Uso da IA apenas para agilizar. Conferi as asserções da QA (string "42" == int 42, floatValue de 10 == 10.0) e entendo por que floatValue coage para 32 bits.