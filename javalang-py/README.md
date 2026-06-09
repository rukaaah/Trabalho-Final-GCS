# Javalang-py (GCS 2026.1)

Repositório destinado ao Trabalho Prático da disciplina de Gerência de Configuração de Software (GCS 2026.1) da Universidade Federal de Mato Grosso do Sul (UFMS).

**Objetivo:** Implementar em Python as classes `String`, `Integer` e `Float` da especificação Java SE 8, replicando o contrato público (construtores, métodos de instância e estáticos) e documentando as adaptações necessárias.

O princípio orientador deste projeto é: *"o código é o pretexto; a prática de GCS é o objeto da avaliação"*.

---

## 👥 Equipe e Papéis

Conforme estabelecido no processo de GCS do projeto, a equipe de 3 a 6 alunos possui seus papéis formais distribuídos da seguinte forma:

| Papel | Responsável (GitHub) | Atribuições |
| :--- | :--- | :--- |
| **Mantenedor** | [Pedro Cremonini](https://github.com/rukaaah) | Cria o repositório, configura proteção de branch, aprova merges em `main`, cria releases e tags. Garante a integridade das baselines. |
| **Gerente de Configuração** | [Angelo Antônio](https://github.com/angelo-acds) | Mantém atualizados os documentos de itens de configuração, ADRs e adaptações. Conduz a auditoria interna ao final. |
| **Engenheiro de Qualidade** | [Yan Victor Gomes](https://github.com/GomesYV) | Configura e mantém a CI, garante cobertura mínima dos testes, revisa PRs sob a ótica de qualidade e regressão. |
| **Desenvolvedores** | [Gabriel Mattos](https://github.com/GabrielMattosA), [Jonathan do Amaral](https://github.com/JhonnPA) | Implementam as classes. Cada desenvolvedor é dono de pelo menos um conjunto de métodos formalmente atribuído via issue. |
| **Relator** | [Cleiton Pinheiro](https://github.com/Ton-07) | Produz os relatórios de status a cada baseline e o relatório final. Sintetiza o trabalho para a apresentação. |

*(Nota: Os papéis definem responsabilidade, não exclusividade. Todos os membros da equipe revisam PRs uns dos outros).*

---

## 💻 Setup Local (Para Desenvolvedores)

Para garantir que todos utilizem as mesmas versões de dependências e ferramentas de qualidade (`pytest`, `ruff`, `coverage`), siga o fluxo abaixo para configurar seu ambiente local usando o `pyproject.toml`.

### 1. Clonar o Repositório
```bash
git clone [git@github.com:rukaaah/Trabalho-Final-GCS.git](git@github.com:rukaaah/Trabalho-Final-GCS.git)

cd javalang-py
```

### 2. Criar o Ambiente Virtual

Crie um ambiente virtual isolado para não conflitar com as bibliotecas da sua máquina:

```bash
python -m venv venv
```

### 3. Ativar o Ambiente Virtual

* **No Windows:**

```bash
venv\Scripts\activate
```
*   **No Linux / macOS:**
```bash
source venv/bin/activate
```
*(Você saberá que deu certo quando aparecer um `(venv)` no início da linha do terminal).*

### 4. Instalar Dependências (Modo Dev)
Com o ambiente ativado, instale o projeto localmente junto com todas as ferramentas de desenvolvimento e testes:
```bash
pip install -e ".[dev]"
```

Para confirmar se a instalação foi bem-sucedida, rode:

```bash
pytest --version
```

---

## ⚙️ Fluxo de Trabalho (GitHub Flow)

A equipe adota estritamente o GitHub Flow:

1. A branch `main` é protegida e nenhum commit direto nela é permitido após o primeiro sprint.


2. Toda alteração não-trivial nasce em uma **Issue**.


3. O desenvolvimento ocorre em uma branch específica (`feature/`, `fix/`, `docs/`, etc.).


4. A integração é feita via **Pull Request (PR)**, exigindo aprovação de pelo menos um membro além do autor e aprovação documentada antes de ser mesclada.



---

## ⚠️ Adaptações Documentadas

(Atenção equipe: De acordo com a especificação, os métodos do Java que não puderem ser implementados devem ser explicitamente listados abaixo, com aprovação prévia via Issue e Pull Request).

### Template para Não-Implementação

*(Use o formato abaixo para adicionar novas adaptações)*

**Método:** `Assinatura completa do método conforme a especificação Java`

* **Motivo da não-implementação:** `[Descrever se foi restrição da linguagem, dependência de tipo inexistente, comportamento indefinido em Python, ou decisão da equipe justificada]`

* **Alternativa Proposta:** `[Descrever como o comportamento equivalente pode ser obtido em código Python idiomático, quando aplicável]`


### Registro de Adaptações

*A ser preenchido durante os sprints de desenvolvimento de JInteger, JFloat e JString.*

```

```