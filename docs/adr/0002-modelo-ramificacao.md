# ADR 0002: Modelo de Ramificação e Integração

## Sobre este documento
Este arquivo é um Registro de Decisão Arquitetural (ADR). Ele documenta o fluxo de controle de versão que a equipe deve seguir estritamente.
**Responsável pela manutenção:** Gerente de Configuração, [Angelo Antônio](https://github.com/angelo-acds).

## Status
Aceito

## Contexto
A disciplina de GCS exige rastreabilidade total entre o código produzido e as tarefas planejadas, proibindo o desenvolvimento direto na branch principal após o término do setup inicial. A equipe precisava escolher um modelo de ramificação que suportasse integração contínua frequente e garantisse revisões de código obrigatórias antes da submissão final.

## Decisão
A equipe adota estritamente o **GitHub Flow** com restrições adicionais de GCS:
1. A branch `main` é tratada como um ambiente protegido. Nenhuma alteração pode ser feita diretamente nela sem aprovação prévia.
2. Todo novo desenvolvimento (funcionalidade, correção, documentação) deve ocorrer em uma ramificação temporária criada a partir da `main`, utilizando prefixos semânticos (`feature/`, `fix/`, `docs/`, `chore/`).
3. A mesclagem de código só ocorrerá através de Pull Requests.
4. Todo Pull Request exigirá obrigatoriamente a aprovação em todos os testes automatizados da CI e a revisão de pelo menos um outro membro da equipe.
5. A aprovação e mesclagem (merge) final das Pull Requests na branch `main` é de responsabilidade exclusiva do Mantenedor / Gerente de Configuração, garantindo a integridade e rastreabilidade das baselines.

## Consequências
* Mitiga o risco de quebras de código na versão entregável do projeto.
* Garante que as restrições anti-atalho de limite de commits sejam validadas antes da mesclagem.
* Aumenta a carga de trabalho de revisão da equipe, exigindo comunicação constante.