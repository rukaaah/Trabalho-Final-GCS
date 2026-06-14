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
  

### Módulo: `JInteger`, `JFloat`, `JString`, `Interop` - Suíte de Testes Base
* **Data:** 14/06/2026
* **Desenvolvedor Responsável:** @GomesYV
* **Métodos Implementados/Auxiliados:** Suíte completa de testes (tests/test_jinteger.py, tests/test_jfloat.py, tests/test_jstring.py, tests/test_interop.py) - aproximadamente 158 casos de teste cobrindo o contrato público das três classes, conforme a especificação Java SE 8.
* **Ferramenta Utilizada:** Claude (Anthropic)
* **Prompt Representativo:**
  > "Preciso de um arquivo de teste-base para os devs usarem como referência (TDD/Test-First conforme ADR-0004), cobrindo construtores, métodos de instância e estáticos das classes JInteger, JFloat e JString conforme a especificação Java SE 8, organizados em blocos pequenos compatíveis com as regras anti-atalho do projeto (máx. 7 testes por PR, máx. 3 por commit)."
