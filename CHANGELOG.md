# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato baseia-se em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Unreleased] (Não Lançado)
*Equipe: Aqui ficarão as mudanças que a equipe está desenvolvendo na branch main antes de fechar a próxima tag.*

### Adicionado
- Setup e fragmentação massiva das issues para o núcleo de `JString` (Issues #52 a #61).

---

## [0.3.0] - Baseline Allocated JFloat - 2026-06-21

### Adicionado
- Implementação completa da classe `JFloat` lidando estritamente com o contrato Java SE 8.
- Adição de constantes e métodos de validação de estado IEEE 754 (`isNaN`, `isInfinite`, `isFinite`).
- Implementação de conversões numéricas (`byteValue`, `shortValue`, `intValue`, `longValue`, `doubleValue`) utilizando lógica de máscaras e complemento de dois manuais para simular overflow.
- Operações de Object (`equals`, `hashCode`, `compareTo`) e comparações estáticas (`compare`), além de conversões binárias (`floatToIntBits`), implementadas através do módulo nativo `struct` para garantir emulação de precisão de 32-bits e tratamento de `NaN`.
- Implementação dos métodos estáticos de parsing e formatação de strings (`parseFloat`, `valueOf`, `toString`, `toHexString`).
- Suíte de testes `test_jfloat.py` avaliando as limitações matemáticas e coerções primitivas.
- Relatório de Status v0.3 (`docs/relatorios/status-v0.3.md`).

### Modificado
- Atualização do `docs/adaptacoes.md` com justificativas técnicas avançadas sobre o comportamento de dupla precisão do CPython vs. Java e o uso massivo da biblioteca `struct`.
- Registro de auditoria atualizado para a resolução formal do segundo conflito de merge da equipe (Issue #65).

---

## [0.2.0] - Baseline Allocated JInteger - 2026-06-20

### Adicionado
- Implementação completa da classe `JInteger` (~40 métodos) em conformidade com o contrato Java SE 8.
- Extensa suíte de testes em `test_jinteger.py` cobrindo limites de 32-bits, operações bitwise, parsing e formatação em múltiplas bases.
- Simulação algorítmica do *IntegerCache* de -128 a 127 nativo da JVM.
- Relatório de Status v0.2 (`docs/relatorios/status-v0.2.md`).

### Modificado
- Ampla atualização do `docs/adaptacoes.md` detalhando decisões sobre bitmasks (`& 0xFFFFFFFF`), ausência de sobrecarga de métodos e uso de precisão arbitrária do Python.
- Atualização do `README.md` com a Ata de Resolução de Conflito de Merge para auditoria (Issue #62).
- Adição massiva de logs de *prompts* justificados e métodos implementados no arquivo `docs/uso-de-ia.md`.

---

## [0.1.0] - Baseline Functional - 2026-06-16

### Adicionado
- Estrutura base de diretórios e arquivos de configuração (`pyproject.toml`, `.gitignore`).
- Documentação inicial com definição formal de papéis da equipe no `README.md`.
- Regras de contribuição e restrições anti-atalho formalizadas no `CONTRIBUTING.md`.
- Templates de Issues (`feature`, `bug`, `decision`) e de Pull Request.
- Arquivo `docs/itens-de-configuracao.md` catalogando os artefatos base.
- Arquivo `docs/uso-de-ia.md` preparado para registro de prompts de Inteligência Artificial.
- Decisões Arquiteturais base criadas: ADR 0001 a 0004.
- Relatório de Status v0.1 (`docs/relatorios/status-v0.1.md`).