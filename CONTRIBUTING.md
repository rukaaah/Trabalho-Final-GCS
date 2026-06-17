# Guia de Contribuição (GCS 2026.1)

Este documento define as regras obrigatórias para qualquer contribuição ao repositório Javalang-py. O cumprimento destas diretrizes será avaliado na nota final.

## 1. Regras de Ouro (Anti-Atalho)

* O histórico não pode ser concentrado em uma janela de 72 horas antes da entrega final.
* O uso de *force push* na branch `main` é estritamente proibido.
* A aprovação de Pull Requests pelo próprio autor (auto-aprovação) é vedada.
* A utilização das credenciais de um colega sem consentimento expresso via issue é considerada falta grave.
* **Limite por Commit:** Um commit não pode conter mais do que 3 métodos ou casos de testes implementados.
* **Limite por Pull Request:** Uma PR não pode conter mais do que 7 métodos ou casos de testes implementados.

## 2. Modelo de Ramificação

O repositório adota o **GitHub Flow** com restrições adicionais de GCS, conforme a [ADR 0002](docs/adr/0002-modelo-ramificacao.md).

* A branch `main` é estritamente protegida. Nenhuma alteração pode ser feita diretamente nela.
* As branches de desenvolvimento devem possuir nomes descritivos com prefixos claros, como `feature/nome-da-feature`, `fix/nome-do-bug` ou `docs/nome-da-documentacao`.
* A mesclagem de código ocorre exclusivamente via Pull Request, exigindo aprovação da CI e revisão de pares.

## 3. Fluxo de Desenvolvimento (TDD/Test-First)

Seguimos a metodologia **Test-Driven Development (TDD)**, conforme definido na ADR 0004:

1. **Ciclo RED:** O Engenheiro de Qualidade (QA) inicia a funcionalidade escrevendo os testes automatizados baseados na especificação Java SE 8.
2. **Ciclo GREEN:** O desenvolvedor implementa o código estritamente necessário para fazer os testes passarem.
3. **Bloqueio:** O desenvolvimento lógico não deve ser iniciado sem que a suíte de testes correspondente já esteja presente na branch.

## 4. Controle de Mudanças (Issues)

* Toda mudança não-trivial deve nascer primeiramente em uma Issue.
* As descrições das issues devem seguir os **Templates Oficiais** configurados no repositório (Feature, Bug ou Decision).
* Toda issue deve receber *labels* apropriadas (`feature`, `bug`, `docs`, `decision`, `good-first-issue`, `refactor`).
* A issue deve ser atribuída a um responsável (*assignee*) e vinculada a um *milestone* correspondente à baseline atual.

## 5. Padrões de Commit

Os commits devem ser semânticos e obrigatoriamente referenciar a issue de origem.

* **Prefixos Aceitos:** `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`.
* **Exemplo de Mensagem Correta:** `feat: add JString.substring(int) refs #14`.

## 6. Fluxo de Pull Requests (PRs)

* A abertura de um PR acionará automaticamente o nosso **Template de Pull Request**. O autor é obrigado a preencher o checklist de regras anti-atalho e referenciar a issue (ex: `Closes #N`).
* O autor deve fornecer um resumo do impacto da mudança, listando arquivos modificados, testes adicionados e se há quebra de contrato.
* O *code review* exige a ocorrência de discussão técnica registrada nos comentários.
* A integração contínua (CI) executará o linter (`ruff`) e os testes (`pytest`). Todos os *checks* devem passar (verde) antes do *merge*.

## 7. Uso de Inteligência Artificial

A utilização de IA generativa para auxílio na implementação técnica é permitida, contanto que seja estritamente declarada.

* Toda assistência de IA deve ser registrada no arquivo `docs/uso-de-ia.md`.
* O registro deve conter a listagem dos métodos auxiliados e os prompts representativos utilizados.
* O desenvolvedor permanece inteiramente responsável por explicar oralmente o código sob seu nome.

---

## 8. Comandos Locais de Teste e Linter

Antes de enviar qualquer commit ou abrir um Pull Request, os desenvolvedores devem rodar as verificações localmente utilizando o ambiente virtual configurado via `pyproject.toml`.

1. Certifique-se de que o ambiente virtual está ativado (`source venv/bin/activate` no Linux/Mac ou `venv\Scripts\activate` no Windows).
2. Para verificar a formatação e as regras de sintaxe, execute:
`ruff check .`
3. Para executar a suíte de testes e validar o comportamento das classes, execute:
`pytest`

## 9. Padrões Específicos de Python Adotados

As decisões técnicas abaixo foram oficializadas para garantir conformidade com a especificação Java SE 8:

* **Nomenclatura (ADR 0001):** Adotamos o padrão `camelCase` para métodos das classes `JString`, `JInteger` e `JFloat`. Esta é uma violação intencional da PEP 8 para preservar a paridade com a API Java. O linter está configurado para ignorar os alertas `N802` e `N803`.
* **Tratamento de Locale (ADR 0003):** Métodos que exigem instâncias de `Locale` como parâmetro não serão implementados devido à falta de correspondência direta no Python. Estas assinaturas devem ser registradas obrigatoriamente em `docs/adaptacoes.md`.

## 10. Gestão de Conflitos

Eventuais conflitos de sincronização devem ser resolvidos localmente na branch de trabalho utilizando prioritariamente o comando `git merge main`. É responsabilidade do desenvolvedor garantir que a branch esteja atualizada antes de solicitar a revisão. Pelo menos três casos de conflitos reais enfrentados pela equipe devem ser documentados para auditoria de GCS.