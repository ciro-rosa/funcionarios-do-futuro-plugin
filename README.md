# Funcionários do Futuro

Assistente de IA de Ciro Rosa para planejar e produzir conteúdo, com 30 especialistas que ele seleciona conforme a tarefa. São 31 skills: a central **Funcionários** e os especialistas.

As instruções de execução foram revisadas para Claude e Codex. Os nomes, as instruções originais e as 63 bases originais permanecem preservados. [Veja o estudo e a cobertura dos testes](funcionarios-do-futuro/review-report.md).

[Veja a revisão e os testes da central Funcionários na versão 1.3.0](funcionarios-do-futuro/entrypoint-review.md).

## Claude e Cowork

Em **Personalizar / Customize → Plugins → Adicionar → Adicionar marketplace**, escolha a opção de repositório e informe:

```text
https://github.com/ciro-rosa/funcionarios-do-futuro-plugin
```

Abra o marketplace **Funcionários do Futuro**, selecione o plugin e instale.

## Claude Code

Execute na conversa do Claude Code:

```text
/plugin marketplace add ciro-rosa/funcionarios-do-futuro-plugin
/plugin install funcionarios-do-futuro@funcionarios-do-futuro
```

Depois, use `/funcionarios` e conte o que precisa produzir. Se houver conflito com outro comando, use `/funcionarios-do-futuro:funcionarios`.

## Codex

Execute no terminal:

```shell
codex plugin marketplace add ciro-rosa/funcionarios-do-futuro-plugin
codex plugin add funcionarios-do-futuro@funcionarios-do-futuro
```

No aplicativo, o plugin aparece na fonte **Funcionários do Futuro**. Inicie uma conversa nova após instalar.

## Acesso ao repositório

Se o repositório for privado, a conta GitHub usada na instalação precisa ter acesso a ele. Em instalações pelo terminal, autentique o GitHub no computador antes de adicionar o marketplace. O plugin não inclui credenciais de nenhum serviço externo.

## Começar a usar

Você não precisa escolher um especialista. Conte sobre seu negócio e o que precisa produzir:

> Use Funcionários do Futuro. Tenho uma confeitaria e quero um carrossel de 6 slides para divulgar bolos por encomenda, com CTA para o WhatsApp.

O assistente escolhe os métodos, aproveita o briefing da conversa e entrega o conteúdo. Quando faltar uma informação essencial, ele pergunta. Você também pode chamar um especialista diretamente.

No Claude Code, a entrada curta é `/funcionarios` (testada no Claude Code), com `/funcionarios-do-futuro:funcionarios` como alternativa se houver conflito de nomes. No Codex, peça **“Use Funcionários do Futuro”** ou selecione a skill **funcionarios** na lista de skills. O comando de barra é específico do Claude Code; não é um comando de terminal.

Na versão 1.3.0, a skill `suporte-24-horas` passou a se chamar `funcionarios`. A ajuda de instalação e as bases originais continuam incluídas na central. Quem usava o comando antigo deve atualizar e usar o novo.

- “Use Funcionários do Futuro para me ajudar a produzir conteúdo para meu negócio.”
- “Use raio-x-estrategico para montar meu briefing.”
- “Use hacker-dos-carrosseis para planejar um carrossel.”
- “Use vision para criar um prompt de vídeo.”

[Veja todas as 31 skills](funcionarios-do-futuro/references/catalogo.md).

## Conteúdo incluído

O pacote preserva os nomes e as instruções originais dos GPTs, além de 63 anexos de conhecimento associados aos especialistas. Cada skill inclui os originais e as adaptações necessárias ao ambiente de execução.

Pesquisa, geração de imagens, vídeos e áudio dependem das ferramentas disponíveis na sessão e dos serviços configurados pelo usuário.

## Atualizar

No Claude Code, use `/plugin marketplace update funcionarios-do-futuro` e a opção de atualizar o plugin no painel Plugins. Pelo terminal:

```shell
claude plugin marketplace update funcionarios-do-futuro
claude plugin update funcionarios-do-futuro@funcionarios-do-futuro
```

No terminal do Codex:

```shell
codex plugin marketplace upgrade funcionarios-do-futuro
codex plugin add funcionarios-do-futuro@funcionarios-do-futuro
```

Reabra o aplicativo ou a conversa para carregar a revisão. O painel do Claude/Cowork pode oferecer seu próprio fluxo de atualização.

## Conferir os arquivos

O plugin inclui `knowledge-manifest.json` e o verificador opcional `scripts/validar_instalacao.py`. Se tiver Python, execute a partir da pasta do plugin:

```shell
python scripts/validar_instalacao.py
```

Ele confere os 31 especialistas, hashes das 63 bases, instruções, links e caminhos sem acessar a rede. Usar o plugin não exige Python; as ferramentas auxiliares são opcionais.

## Documentação das plataformas

- [Marketplaces no Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Instalação no Claude Code](https://code.claude.com/docs/en/discover-plugins)
- [Plugins e marketplaces no Codex](https://developers.openai.com/plugins/build/plugins)

As instruções e bases pertencem aos respectivos titulares. Este repositório não concede licença adicional de redistribuição.
