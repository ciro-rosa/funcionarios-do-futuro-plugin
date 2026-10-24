# Guia atual para alunos

Este guia orienta o plugin atual. Os três anexos originais do suporte são históricos; os links antigos de GPTs e os especialistas separados de Sora/VEO nesses anexos foram substituídos pelo catálogo do plugin.

## Instalar no Claude Code

Na conversa do Claude Code, execute separadamente:

```text
/plugin marketplace add ciro-rosa/funcionarios-do-futuro-plugin
```

```text
/plugin install funcionarios-do-futuro@funcionarios-do-futuro
```

Feche e abra o Claude Code. Comece com `/funcionarios-do-futuro:suporte-24-horas`.

## Instalar no Codex

No terminal do computador com o Codex instalado, execute separadamente:

```shell
codex plugin marketplace add ciro-rosa/funcionarios-do-futuro-plugin
```

```shell
codex plugin add funcionarios-do-futuro@funcionarios-do-futuro
```

Na próxima conversa ou turno com o catálogo atualizado, peça: “Use o Suporte 24 horas dos Funcionários do Futuro para me ajudar.” Se a lista não aparecer, abra uma conversa nova ou reabra o aplicativo.

## Claude pelo painel de plugins

Se a versão da conta oferecer adicionar um marketplace de repositório, informe `https://github.com/ciro-rosa/funcionarios-do-futuro-plugin` e instale o plugin. As telas e permissões variam. Não instrua o aluno a digitar os comandos do Claude Code numa conversa comum do Claude. Se não houver painel compatível, indique o guia do repositório e confirme a versão do aplicativo antes de orientar outro método.

## Atualizar uma instalação existente

No Claude Code, atualize o marketplace com `/plugin marketplace update funcionarios-do-futuro` e use o painel de plugins para atualizar o plugin. Pelo terminal, o equivalente é `claude plugin marketplace update funcionarios-do-futuro`, seguido de `claude plugin update funcionarios-do-futuro@funcionarios-do-futuro`. Reabra o Claude Code para aplicar.

No terminal do Codex, execute `codex plugin marketplace upgrade funcionarios-do-futuro` e depois `codex plugin add funcionarios-do-futuro@funcionarios-do-futuro`. Confirme a versão informada pelo comando e reabra a conversa ou o aplicativo para atualizar o catálogo.

## Começar e continuar

- Briefing: “Use raio-x-estrategico dos Funcionários do Futuro para entender meu negócio e criar meu briefing.”
- Carrossel: “Use hacker-dos-carrosseis dos Funcionários do Futuro para criar um carrossel de sete slides sobre [tema]. Meu público é [público].”
- Anúncios: “Use copywriter-anuncios-headlines dos Funcionários do Futuro para criar três anúncios da minha [oferta].”
- Vídeo: “Use vision dos Funcionários do Futuro para criar um prompt de vídeo vertical de oito segundos sobre [cena].”
- Sequência: “Agora use designer-de-carrosseis para preparar a direção visual desse carrossel, mantendo o briefing.”

O modelo executa as instruções do especialista. Os arquivos de conhecimento são consultados conforme a tarefa, sem necessidade de o aluno reenviar os anexos do plugin.

## Erros frequentes

- **Filename too long no Windows:** a versão 1.1.1 encurtou os arquivos. Se a primeira adição do marketplace falhou, repita a adição para buscar a versão corrigida e depois instale. Se o marketplace já estiver registrado no Claude Code, atualize com `/plugin marketplace update funcionarios-do-futuro`; siga a opção de atualização do plugin no painel e reabra o aplicativo. Não peça para apagar pastas ou alterar o registro do Windows como primeira medida.
- **Skill não aparece:** confirme que o plugin foi instalado e está habilitado, reabra o aplicativo ou abra uma conversa nova, e tente o nome completo `funcionarios-do-futuro:suporte-24-horas` ou o pedido em linguagem natural.
- **Comando codex não reconhecido:** é um problema de instalação ou PATH da CLI. Confirme se o aluno está usando o aplicativo ou o terminal e consulte a documentação oficial para sua versão; não presuma que o plugin foi instalado.
- **MCP precisa autenticar:** verifique o nome do servidor; este plugin não inclui MCP. Só oriente conexão de um serviço externo se a tarefa precisar dele.
- **Não gerou imagem/vídeo/áudio:** verifique se há ferramenta de geração disponível. O prompt produzido pela skill pode ser usado no serviço escolhido pelo aluno, sujeito ao acesso e aos limites desse serviço.
- **Cobrança ou acesso ao curso:** indique apenas o canal oficial já recebido pelo aluno; o plugin não consulta pagamentos nem matrículas.

## Fontes públicas

- Guia de instalação e catálogo: https://github.com/ciro-rosa/funcionarios-do-futuro-plugin
- Catálogo completo no GitHub: https://github.com/ciro-rosa/funcionarios-do-futuro-plugin/blob/main/funcionarios-do-futuro/references/catalogo.md
- Índice das bases do suporte: https://github.com/ciro-rosa/funcionarios-do-futuro-plugin/blob/main/funcionarios-do-futuro/skills/suporte-24-horas/references/bases.md
- Migração dos GPTs: https://help.openai.com/pt-br/articles/20001519-custom-gpt-retirement-and-migration-faq
- Claude Code: https://code.claude.com/docs/en/discover-plugins
- Codex: https://developers.openai.com/plugins/build/plugins

Para cronogramas, planos, menus e preços, confira a fonte oficial atual ou o aviso da conta; este guia não fixa essas informações.
