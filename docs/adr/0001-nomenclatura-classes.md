# ADR 0001: Nomenclatura das Classes e Métodos

## Sobre este documento
Este arquivo é um Registro de Decisão Arquitetural (ADR). Ele documenta uma escolha técnica definitiva feita pela equipe.
**Responsável pela manutenção:** Gerente de Configuração, [Angelo Antônio](https://github.com/angelo-acds).


## Status
Aceito


## Contexto
O objetivo do projeto é recriar as classes `String`, `Integer` e `Float` do Java em Python. No entanto, Python já possui palavras reservadas e tipos embutidos nativos (built-ins) com funções semelhantes, como `int`, `float` e `str`. Além disso, o padrão de nomenclatura de métodos da comunidade Python (PEP 8) exige `snake_case`, enquanto o contrato da especificação Java SE 8 exige `camelCase`.


## Decisão
1. **Nome das Classes:** Para evitar sombreamento (shadowing) de palavras reservadas e conflitos no interpretador Python, as classes implementadas pela equipe receberão o prefixo "J". Assim, os módulos e classes serão nomeados como `JString`, `JInteger` e `JFloat`.

2. **Nome dos Métodos:** Para preservar estritamente o contrato público do Java SE 8, a nomenclatura original dos métodos será mantida em `camelCase` (exemplo: `parseInt`, `charAt`, `compareToIgnoreCase`).

3. O linter (Ruff/Flake8) foi configurado no `pyproject.toml` para ignorar o erro de nomenclatura `N802` e `N803`, permitindo o uso do `camelCase` sem falhar a Integração Contínua (CI).


## Consequências
* Garante a compatibilidade visual e estrutural com a especificação Java solicitada.
* Evita bugs de sobreposição de funções nativas do Python.
* Quebra o padrão PEP 8 intencionalmente, o que está documentado e justificado para fins de avaliação.