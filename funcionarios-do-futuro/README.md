# Funcionários do Futuro

Plugin de Ciro Rosa com 31 skills para Instagram, copywriting, design, pesquisa, planejamento e prompts de vídeo.

Peça “use o suporte 24 horas para escolher meu especialista” ou indique diretamente uma skill. O [catálogo](references/catalogo.md) lista todas elas.

## Instalar no Claude

No Claude, abra Personalizar/Customize → Plugins e use o upload de plugin personalizado com o ZIP deste pacote. O arquivo `.claude-plugin/plugin.json` está na raiz do ZIP, junto de `skills/`.

Para testar no Claude Code sem instalação permanente:

```powershell
claude --plugin-dir "C:\caminho\funcionarios-do-futuro"
```

Para instalação permanente pelo marketplace local, extraia `funcionarios-do-futuro-marketplace.zip` e execute:

```powershell
claude plugin marketplace add "C:\caminho\funcionarios-do-futuro-marketplace"
claude plugin install funcionarios-do-futuro@funcionarios-do-futuro-local
```

Exemplos de comandos no Claude Code: `/funcionarios-do-futuro:suporte-24-horas`, `/funcionarios-do-futuro:raio-x-estrategico` e `/funcionarios-do-futuro:vision`.

## Instalar no Codex

O pacote contém `plugin.json` portátil e `.codex-plugin/plugin.json` de compatibilidade. Se a interface oferecer upload de plugin personalizado, use o mesmo ZIP. Para distribuição local por marketplace, mantenha a estrutura do workspace ou baixe o ZIP `funcionarios-do-futuro-marketplace.zip`, extraia e registre a pasta extraída:

```powershell
codex plugin marketplace add "C:\caminho\funcionarios-do-futuro-marketplace"
codex plugin add funcionarios-do-futuro@funcionarios-do-futuro-local
```

Abra Plugins no aplicativo Codex, selecione a fonte “Funcionários do Futuro”, instale o plugin e inicie uma conversa nova. As opções disponíveis de instalação podem variar com a versão do aplicativo.

## Pedidos de exemplo

- Use raio-x-estrategico para criar meu briefing.
- Use hacker-dos-carrosseis para planejar um carrossel e designer-de-carrosseis para sua direção visual.
- Use copywriter-anuncios-headlines para criar três anúncios.
- Use vision para criar um prompt de vídeo.
- Use mestre-dos-prompts-para-video-em-json para um vídeo vertical de até oito segundos.

## Bases e limites

Os nomes e as instruções integrais das 31 skills foram coletados dos editores da conta do autor. Os 63 anexos foram exportados diretamente dos GPTs e conferidos com os manifestos SHA256. Nenhuma base está pendente. Consulte [o relatório de migração](migration-report.md).

Cada skill preserva as instruções originais em `references/instrucoes-originais.md` e os arquivos de conhecimento intactos em `references/originais/`. As versões de trabalho ficam separadas. Nomes técnicos de pastas usam caracteres compatíveis com Claude e Codex; os nomes originais dos GPTs e anexos são preservados no conteúdo e no catálogo.

O plugin gera textos, estratégias, direção visual e prompts. Geração de imagens, vídeos, áudio e pesquisa dependem das ferramentas e serviços disponíveis no aplicativo. As skills não incluem logins ou créditos desses serviços.

Sora e VEO 3 como skills separadas foram excluídos por decisão do autor; use V.I.S.I.O.N (`vision`).

## Documentação dos formatos

- [Plugins da OpenAI](https://developers.openai.com/plugins/build/plugins)
- [Plugins do Claude](https://code.claude.com/docs/en/plugins)

O código, instruções e bases pertencem aos seus respectivos titulares. Nenhuma licença de redistribuição adicional é concedida por este empacotamento.
