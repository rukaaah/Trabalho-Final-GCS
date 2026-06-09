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

O repositório adota o **GitHub Flow**.

* Nenhum commit direto na branch `main` é permitido após a finalização do primeiro sprint (Setup).
* As branches de desenvolvimento devem possuir nomes descritivos com prefixos claros, como `feature/nome-da-feature`, `fix/nome-do-bug` ou `docs/nome-da-documentacao`.

> **Aviso de Atualização Pendente:** A formalização deste modelo de ramificação está aguardando a aprovação da equipe na issue correspondente à **ADR 0002**. Após a aprovação, esta seção deverá referenciar diretamente o documento finalizado em `docs/adr/0002-modelo-ramificacao.md`.

## 3. Controle de Mudanças (Issues)

* Toda mudança não-trivial deve nascer primeiramente em uma Issue.
* As descrições das issues devem seguir os **Templates Oficiais** configurados no repositório (Feature, Bug ou Decision).
* Toda issue deve receber *labels* apropriadas (`feature`, `bug`, `docs`, `decision`, `good-first-issue`, `refactor`).
* A issue deve ser atribuída a um responsável (*assignee*) e vinculada a um *milestone* correspondente à baseline atual.

## 4. Padrões de Commit

Os commits devem ser semânticos e obrigatoriamente referenciar a issue de origem.

* **Prefixos Aceitos:** `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`.
* **Exemplo de Mensagem Correta:** `feat: add JString.substring(int) refs #14`.

## 5. Fluxo de Pull Requests (PRs)

* A abertura de um PR acionará automaticamente o nosso **Template de Pull Request**. O autor é obrigado a preencher o checklist de regras anti-atalho e referenciar a issue (ex: `Closes #N`).
* O autor deve fornecer um resumo do impacto da mudança, listando arquivos modificados, testes adicionados e se há quebra de contrato.
* O *code review* exige a ocorrência de discussão técnica registrada nos comentários.
* A integração contínua (CI) executará o linter (`ruff`) e os testes (`pytest`). Todos os *checks* devem passar (verde) antes do *merge*.

## 6. Uso de Inteligência Artificial

A utilização de IA generativa para auxílio na implementação técnica é permitida, contanto que seja estritamente declarada.

* Toda assistência de IA deve ser registrada no arquivo `docs/uso-de-ia.md`.
* O registro deve conter a listagem dos métodos auxiliados e os prompts representativos utilizados.
* O desenvolvedor permanece inteiramente responsável por explicar oralmente o código sob seu nome.

---

## 7. Comandos Locais de Teste e Linter

Antes de enviar qualquer commit ou abrir um Pull Request, os desenvolvedores devem rodar as verificações localmente utilizando o ambiente virtual configurado via `pyproject.toml`.

1. Certifique-se de que o ambiente virtual está ativado (`source venv/bin/activate` no Linux/Mac ou `venv\Scripts\activate` no Windows).
2. Para verificar a formatação e as regras de sintaxe, execute:
`ruff check .`
3. Para executar a suíte de testes e validar o comportamento das classes, execute:
`pytest`

## 8. Padrões Específicos de Python Adotados (Aguardando ADRs)

> **Aviso de Atualização Pendente:** A equipe está em processo de votação/discussão das seguintes Regras Arquiteturais. O texto abaixo **deverá ser modificado e atualizado** pelo Gerente de Configuração assim que os respectivos PRs de decisão forem aprovados:

* **Nomenclatura (Aguardando ADR 0001):** Se aprovada, documentar aqui que a equipe decidiu violar a PEP 8 e adotar o padrão `camelCase` para métodos, ignorando os alertas do Ruff (N802 e N803), a fim de manter o contrato visual do Java SE 8.
* **Tratamento de Locale (Aguardando ADR 0003):** Se aprovada, documentar aqui que métodos que dependem de instâncias de `Locale` não serão implementados e devem ser direcionados diretamente para o catálogo do arquivo `docs/adaptacoes.md`.

## 9. Gestão de Conflitos

[INSERIR: Acordo da equipe sobre como lidar com rebase, mesclagem e os "pelo menos três conflitos reais" obrigatórios descritos na disciplina. Esta seção deverá ser preenchida via PR em sprints futuros.]