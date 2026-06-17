# ADR 0003: Tratamento de Dependências de Locale

## Sobre este documento
Este arquivo é um Registro de Decisão Arquitetural (ADR). Ele documenta como a equipe lidará com métodos da especificação Java que dependem de bibliotecas regionais ausentes no escopo atual.
**Responsável pela manutenção:** Gerente de Configuração, [Angelo Antônio](https://github.com/angelo-acds).

## Status
Aceito

## Contexto
Na especificação do Java SE 8, especificamente na classe `String`, existem métodos que dependem diretamente de configurações regionais ou de objetos externos para funcionar corretamente, como `toLowerCase(Locale locale)` ou `toUpperCase(Locale locale)`. O ecossistema Python lida com localização de maneira atrelada ao sistema operacional ou através de módulos distintos, sem correspondência direta ao objeto `Locale` da JVM.

## Decisão
1. A equipe não tentará recriar ou simular a classe `Locale` do Java, pois isso foge do escopo do trabalho.
2. Os métodos que dependem explicitamente de uma instância de `Locale` como parâmetro não serão implementados em sua totalidade.
3. Essas assinaturas específicas serão catalogadas no arquivo `docs/adaptacoes.md`.
4. Os métodos análogos que não recebem parâmetros (exemplo: `toLowerCase()` padrão) assumirão o comportamento padrão do Python para conversão unicode, que já é suficiente para as validações básicas requeridas pela especificação generalista.

## Consequências
* Reduz a complexidade desnecessária do projeto.
* Transfere o peso da avaliação para a documentação correta das adaptações, conforme exigido pelas regras da disciplina.