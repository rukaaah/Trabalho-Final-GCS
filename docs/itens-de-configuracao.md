# Itens de Configuração do Projeto

## Sobre este documento

Este documento é de manutenção obrigatória e de responsabilidade do **Gerente de Configuração**, [Angelo Antonio](https://github.com/angelo-acds), da equipe. Seu objetivo é identificar, catalogar e rastrear o estado de todos os artefatos essenciais que compõem o repositório deste projeto.

De acordo com as regras estabelecidas para a disciplina, este catálogo deve conter, no mínimo, a identificação dos seguintes elementos:
* Os três módulos de classe principais (`JString`, `JInteger`, `JFloat`) e suas respectivas suítes de testes.
* Os documentos de decisões arquiteturais (ADRs).
* A documentação de adaptações técnicas (`README.md` e `docs/adaptacoes.md`).
* A configuração de Integração Contínua (CI) localizada em `.github/workflows/`.

Para garantir a rastreabilidade correta, cada item de configuração deve listar os seguintes atributos vitais: **responsável, formato, periodicidade de mudança e dependências**.

---
## Catálogo de Itens

*(Atenção Gerente de Configuração: Preencha os nomes dos responsáveis designados para cada módulo e mantenha esta tabela atualizada conforme o projeto avança pelas baselines).*

### 1. Infraestrutura e Documentação

| Item de Configuração | Arquivo (Caminho) | Responsável | Formato | Periodicidade de Mudança | Dependências |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Configuração de CI | `.github/workflows/ci.yml` | Engenheiro de Qualidade | YAML | Baixa (Apenas em setup e ajustes) | Nenhuma |
| Decisões Arquiteturais | `docs/adr/` | Gerente de Configuração | Markdown | Média (Conforme novos impasses surgem) | Nenhuma |
| Adaptações Documentadas | `docs/adaptacoes.md` / `README.md` | Gerente de Configuração | Markdown | Média (Atualizado a cada classe adaptada) | Módulos de Classe |
| Plano de Implementação | `docs/plano-implementacao.md` | Gerente de Configuração | Markdown | Baixa | Decisões Arquiteturais |

### 2. Código Fonte e Testes

| Item de Configuração | Arquivo (Caminho) | Responsável | Formato | Periodicidade de Mudança | Dependências |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Classe JInteger | `javalang/jinteger.py` | [Inserir Nome] | Python | Alta (Foco na Baseline v0.2) | Nenhuma |
| Testes JInteger | `tests/test_jinteger.py` | [Inserir Nome] | Python | Alta (Acompanha a classe) | Classe JInteger |
| Classe JFloat | `javalang/jfloat.py` | [Inserir Nome] | Python | Alta (Foco na Baseline v0.3) | Classe JInteger (Interoperabilidade) |
| Testes JFloat | `tests/test_jfloat.py` | [Inserir Nome] | Python | Alta (Acompanha a classe) | Classe JFloat |
| Classe JString | `javalang/jstring.py` | [Inserir Nome] | Python | Alta (Foco na Baseline v0.4) | JInteger e JFloat |
| Testes JString | `tests/test_jstring.py` | [Inserir Nome] | Python | Alta (Acompanha a classe) | Classe JString |
| Interoperabilidade | `tests/test_interop.py` | [Inserir Nome] | Python | Média (A partir da Baseline v0.3) | JString, JInteger, JFloat |