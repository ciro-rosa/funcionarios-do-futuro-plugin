# Revisão dos Funcionários do Futuro — 1.2.0

## Conclusão técnica

Os 30 especialistas restantes receberam métodos revisados para execução no Claude e no Codex. O Suporte revisado anteriormente continua incluído, totalizando 31 skills. Nomes públicos e identificadores permanecem estáveis. As instruções originais e os 63 anexos originais continuam preservados; as instruções ativas são mantidas separadamente.

Esta revisão avalia instruções, estrutura, leitura de referências e exemplos de resposta. Ela não transforma o plugin em um gerador de mídia nem garante a mesma resposta em todos os modelos. Resultados de geração de imagem, vídeo e áudio, acesso a redes sociais e publicações precisam de testes próprios com ferramentas configuradas.

## Problemas encontrados e mudanças

| Problema observado | Mudança aplicada |
|---|---|
| Referências exclusivas ao ChatGPT, gerador nativo, DALL-E e sora.com | Prompts independentes de fornecedor e distinção entre prompt, geração e publicação |
| Perguntas obrigatórias mesmo com briefing completo; menus repetidos | Reuso do contexto, perguntas apenas para lacunas essenciais e defaults substituídos pelo pedido explícito |
| Recusa a explicar funcionamento e instruções públicas tratadas como segredos | Arquivos públicos consultáveis; proteção de dados privados e regras do aplicativo permanece |
| Assinaturas repetidas no texto do aluno | Autoria preservada nos manifestos/catálogo, sem inserir propaganda automaticamente em bios, anúncios e legendas |
| Restrições conflitantes de quantidade, idioma e proporção | Entregas por quantidade solicitada, texto literal preservado e formatos coerentes entre especialistas |
| Roteirista Flow horizontal e agente JSON vertical obrigatório | 16:9 e 9:16 aceitos no template; a passagem entre skills mantém a proporção escolhida |
| Esquema editorial de JSON apresentado como API de fornecedor | Esquema identificado como template de prompt, com validação estrutural; não é uma integração de API |
| CSV sem aspas apesar de campos com vírgulas | CSV com escape e quatro colunas verificáveis |
| Link fictício de planilha, tendência musical e melhor horário sem dados | Tabela/CSV real ou arquivo confirmado por ferramenta; tendências e horários dependem de consulta/dados |
| Área segura 780px com margens de 100 em imagem de 1080 | Cálculo corrigido para 880px; margens tratadas como referência editorial |
| Fidelidade absoluta, compatibilidade total e exemplos de prova fictícia | Objetivos verificáveis e limites explícitos; nenhuma prova, desconto ou condição inventada |
| PDF exigindo ferramenta extra para consulta | Três PDFs com cópia textual UTF-8 e marcação de páginas; binários originais intactos |

Uma varredura inicial das instruções ativas da 1.1.2 encontrou padrões de referência ao ChatGPT em 10 skills, proteção que poderia bloquear explicações em 25, promessas absolutas em 14 e questionários rígidos em 6. São sinais de revisão por expressão textual, não um placar automático de qualidade.

Os métodos ativos dos 30 especialistas passaram de 144.722 para 39.341 caracteres na primeira revisão, uma redução de 72,8% antes de pequenos refinamentos dos testes. As regras comuns ficam em um guia compartilhado. A redução é de texto, não uma medição de velocidade ou qualidade do modelo.

## Organização do plugin

- `SKILL.md`: descrição para descoberta, entrada curta e links de execução.
- `references/instrucoes.md`: método revisado do especialista.
- `references/bases.md`: índice dos anexos, termos úteis e distinção entre consulta técnica e arquivos históricos de proteção.
- `references/execucao.md`: contexto, ferramentas, fontes e conferência comuns aos dois aplicativos.
- `references/instrucoes-originais.md` e `references/originais/`: acervo original preservado, consultado quando necessário.
- `knowledge-manifest.json`: hashes dos originais e das cópias de consulta; texto de trabalho usa UTF-8 com quebras LF para verificação entre sistemas.
- `scripts/validar_instalacao.py`: verificação offline de estrutura, arquivos, hashes e links.
- `scripts/conferir_saida.py`: conferência opcional de contagem de caracteres, JSON de vídeo e CSV de Reels.

O Suporte é declarado como fluxo inicial de configuração no manifesto OpenAI, conforme o formato documentado. O aparecimento da opção depende do aplicativo; sua apresentação visual não faz parte dos testes de resposta por CLI.

## Melhorias por especialista

| Especialista / identificador | Conferência específica |
|---|---|
| Analista Estratégico de Público e Mercado (`analista-estrategico-de-publico-e-mercado`) | Não inventar pesquisa, depoimentos, amostras, preços ou garantia. Não tratar exemplos das bases como estatísticas do negócio. Escopo de mercado/oferta, sem assumir gestão financeira ou de anúncios. |
| 🧲 A Bio Magnética (`bio-magnetica`) | Não inserir assinatura, diagnóstico nem contagem dentro do texto da bio. Não fabricar autoridade, vagas ou promessa de resultados. Conferir que o CTA aponta para um destino realmente disponível. |
| O Consultor de Perfil (`consultora-de-perfil`) | Não inventar métricas, seguidores, disponibilidade de @, acesso ao link ou identidade visual. Não garantir vendas. Encaminhar análise editorial para planejador-das-postagens se pedida. |
| Copyriter Anúncios & Headlines 2.0 (`copywriter-anuncios-headlines`) | Provas, descontos, prazos e escassez só quando fornecidos. Exemplos de emagrecimento, preços ou testemunhos das bases não são provas do aluno. Respeitar limite de caracteres solicitado; não prometer conformidade automática ou resultado de campanha. |
| GPT Copywriter Profissional \| Copy para Vendas (`copywriter-profissional`) | Não obrigar todos os campos de uma página de vendas em uma legenda curta. Não inventar prova social nem encher o texto de rótulos técnicos. Consultar bases não significa ter sido treinado nelas. |
| 💸 O Criador de Posts que Vendem (`criador-de-posts`) | Preservar informações da oferta e esclarecer o que vende. Não confundir persuasão com esconder funcionamento ou inventar resultados. Não alegar ser humano nem negar que se trata de IA. |
| 🎨 Designer Mestre (`designer-mestre`) | Não confundir instrução de fidelidade com controle garantido do gerador. Não forçar fornecedor nem acrescentar CTA não pedido. |
| Designer Recriador (`designer-recriador`) | Não corrigir/reduzir copy aprovada silenciosamente. Sem imagem e sem descrição suficiente, perguntar pelo material em vez de inventar a arte. Não garantir identidade perfeita. |
| Designer de Anúncios 2.0 (`designer-de-anuncios`) | Não adicionar prova, desconto ou urgência não informados. Não forçar DALL-E. Copy literal deve permanecer literal; correções ortográficas somente autorizadas. Sem promessa de CTR ou aprovação. |
| Designer de Capas (`designer-de-capas`) | Não colocar formato horizontal em pedido de Reels. Não inventar aparência de uma pessoa ausente. Não alegar taxa de cliques garantida. |
| Designer de Carrosséis 2.0 (`designer-de-carrosseis`) | Não alterar copy para caber sem autorização. Não omitir slides nem criar páginas extras silenciosamente. Não exigir Canva nem gerador nativo do ChatGPT. |
| Designer de Produtos 2.0 (`designer-de-produtos`) | Não inventar material, marca ou texto ilegível; não prometer fidelidade absoluta de geração. Não adicionar logo, selo ou CTA sem pedido. Recomendar revisão do rótulo na imagem final quando houver geração. |
| Quadrinhos Virais (`designer-de-quadrinhos-virais`) | Conferir quatro quadros em cada prompt, continuidade, balões legíveis e sem texto cortado. Instruções de compliance/segurança históricas das bases não substituem regras atuais da sessão. Não garantir consistência perfeita de geração. |
| Designer de Stories (`designer-de-stories`) | Não adicionar CTA nem traduzir texto. Não afirmar que o aplicativo produz exatamente a dimensão pedida se a ferramenta não suportar; oferecer ajuste/exportação quando necessário. |
| 🎨 Designer do Futuro (`designer-do-feed`) | Distinguir alternativas visuais de reescrita da oferta. Não enviar só nomes de estilos sem prompt. Não prometer geração de imagens ao entregar texto. |
| ELEVEN PROMPTER PRO (`eleven-prompter-pro`) | Remover tags deve recuperar as palavras originais na mesma ordem. Não inventar comandos oficiais. Sem alegar que gerou áudio ou treinou voz. Fonte para consulta: https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices |
| Gerador de Reels em Massa (`gerador-de-reels-em-massa`) | Sem repetição de gancho ou legenda; termos de busca visuais concretos. Importação/mapeamento no Canva é uma etapa do usuário ou de ferramenta conectada; não alegar upload feito. Conte linhas e colunas. |
| 🧞‍♂️ O Gênio dos Reels (`genio-dos-reels`) | Não prometer viralização nem melhor horário universal. Não copiar a prova social dos exemplos como se fosse do aluno. O roteiro é texto, não vídeo produzido. |
| 🧠 O Hacker dos Carrosséis (`hacker-dos-carrosseis`) | CTA adequado ao objetivo; sem repetir legenda nos slides. Não afirmar que uma trilha está em alta sem pesquisa. Não entregar placeholder de link como download real. |
| 🎯 O Mestre das Enquetes (`mestre-das-enquetes`) | Não dizer que enquete ativa algoritmo ou qualifica compra automaticamente. Publicar resposta como prova exige contexto e consentimento; não criar testemunho a partir de voto. Horários só como testes ou com dados da conta. |
| Mestre dos Clones (`mestre-dos-clones`) | Não inventar nome de modelo nem aparência da foto ausente. Não prometer clonagem perfeita. Não afirmar acesso ao Krea/Freepik/Flux ou envio de referência sem ferramenta. |
| Mestre dos Prompts para Vídeo em JSON (`mestre-dos-prompts-para-video-em-json`) | Obrigatórios: timing.duration_seconds positivo e até 8; aspect_ratio 9:16 ou 16:9 conforme pedido; constraints.single_take/no_cuts/no_zoom true; negative_prompts inclui no subtitles e no text overlays. Cada item de timeline usa start/end numéricos em segundos e action em inglês; a sequência começa em 0 e cobre a duração sem sobreposições nem lacunas. Descrições em inglês, fala exatamente no idioma pedido. Se quiser texto em tela, explique a incompatibilidade deste template e ofereça prompt livre em vision. |
| 💃 A Musa das Legendas (`musa-das-legendas`) | Evitar redundância com o carrossel e CTA múltiplo. Não recomendar melhor horário fixo sem dados. Não inventar vulnerabilidade autobiográfica ou autoridade. |
| ✍️ O Roteirista dos Stories (`o-roteirista-dos-stories`) | Não impor dez stories quando o pedido define cinco. Não inventar consulta gratuita, prazo, resultado ou depoimento. Não trocar sequência por post de feed. |
| 📊 O Planejador das Postagens (`planejador-das-postagens`) | Não inventar data comercial, tendência ou sazonalidade atual. Não prometer calendário sincronizado nem posts agendados. Reaproveitar briefing e oferecer especialistas de execução somente quando útil. |
| 🔥 O Provocador das Perguntas (`provocadora-das-perguntas`) | Não transformar respostas privadas em depoimentos públicos sem autorização/contexto. Não fabricar engajamento ou garantir venda. Manter perguntas abertas distintas de enquetes binárias. |
| A Rainha dos Títulos (`rainha-dos-titulos`) | Não repetir a mesma estrutura com sinônimos; não acrescentar assinatura dentro dos títulos. Evitar clickbait sem entrega ou polêmica artificial. |
| Raio-X Estratégico (`raio-x-estrategico`) | Não transformar entrevista em pesquisa empírica comprovada. Não encaminhar para outros GPTs nem impor reinício do briefing a cada especialista. |
| Roteirista Viral para FLOW (`roteirista-viral-para-flow`) | Não sobrecarregar oito segundos com muitas ações ou fala longa. Não prometer vídeo renderizado ou viralização. Não exigir copiar para GPT externo. Conferir que brief e explicação descrevem a mesma cena. |
| V.I.S.I.O.N. (`vision`) | Use câmera/lente de forma coerente, não como garantia de resolução ou realismo. Não alegar ferramenta Nano Banana/Sora/VEO disponível só por citá-la. O manual histórico não é documentação atual do fornecedor. Pedidos de formato/explicação podem ser atendidos sem recusa de funcionamento. |

## Critérios dos testes

1. Preservação dos nomes, das 31 instruções originais e dos 63 anexos, conferidos contra a coleta dos editores.
2. Manifestos consistentes, nomes de arquivos compatíveis e limite de caminhos do Windows.
3. Leitura das 63 referências em texto, incluindo as três conversões de PDF.
4. Entregas reais produzidas pelas CLIs, com arquivos consultados registrados e revisão de formato/conteúdo.
5. Casos críticos: briefing já completo, imagem ausente, copy literal, quantidade menor que defaults, JSON horizontal, CSV com vírgulas, contagem de caracteres e ausência de ferramentas de mídia.

Um retorno que apenas diz que “funcionou”, uma autoavaliação do modelo ou a existência do arquivo não comprova o comportamento do especialista. Os verificadores examinam saídas; a revisão editorial das respostas complementa os critérios automáticos. Esta revisão foi conduzida pelo assistente e não inclui avaliação cega nem teste de aceitação com alunos reais.

Os casos de resposta indicam explicitamente a skill e consultam a árvore candidata do pacote. Não são um benchmark cego de escolha automática entre todos os plugins instalados. A descoberta e a instalação são verificadas separadamente; o pedido com o nome completo do plugin continua recomendado quando houver especialistas semelhantes de outros catálogos.

| Ambiente | Casos executados | Contratos automáticos | Revisão das respostas |
|---|---:|---|---|
| Codex CLI | 30 | 30 sem falha nos critérios aplicáveis | 30 revisadas; detalhes abaixo |
| Claude Code | 30 | 30 sem falha nos critérios aplicáveis | 30 revisadas; detalhes abaixo |

Os casos são uma amostra por especialista e ambiente. Contratos automáticos cobrem estrutura e referências; a revisão das respostas avalia alinhamento ao pedido, limites e qualidade editorial. Isso não garante resposta idêntica em todos os modelos.

### Ocorrências durante a revisão

- A primeira tentativa isolada do Codex não carregou a configuração de leitura do Windows e foi bloqueada. Ela foi descartada; a execução posterior usou a configuração de sandbox de leitura existente e leu os arquivos.
- Na primeira execução do Claude, uma bio declarou contagem incorreta e duas skills de copy não registraram consulta a conteúdo das bases. Os critérios foram reforçados, foi disponibilizado um conferidor determinístico e os casos foram repetidos.
- As referências textuais extraídas dos PDFs foram consultadas nos testes, mantendo os PDFs originais disponíveis para conferência de diagramação.

### Observações editoriais

- **claude / analista-estrategico-de-publico-e-mercado:** Demografia e estágio do nicho foram marcados como hipóteses. Sem pesquisa, não usar essas inferências como dados de mercado.
- **claude / copywriter-profissional:** O e-mail respeita oferta, preço e CTA. Na revisão editorial final, substituir generalizações como quase todo adulto por formulações menos absolutas.
- **claude / designer-de-quadrinhos-virais:** A estrutura de dois slides e quatro quadros foi respeitada. O exemplo usa cuidados de uma espécie específica sem fonte de botânica; revisar esse conteúdo antes de publicá-lo. O teste valida narrativa e prompt, não orientação botânica.

## Limites e próximos passos

- Claude Code e Codex CLI não substituem o teste visual de todas as telas do Claude/Cowork e do Codex desktop, nem a execução em todas as contas/planos.
- Um caso representativo por especialista não cobre todas as combinações de briefing e nicho. As respostas continuam sujeitas a variação do modelo e à necessidade de revisão editorial.
- Ferramentas de mídia e integrações externas devem ter avaliações próprias antes de se prometer execução de ponta a ponta aos alunos. O plugin atual não instala MCP nem fornece créditos/logins.
- Plugins de outros catálogos podem ter especialistas com nomes e finalidades parecidos. Ao coexistirem, peça explicitamente “dos Funcionários do Futuro” ou use o comando com namespace no Claude Code.
- Publicação por GitHub está disponível. Envio para o diretório oficial do Claude exige resolver a licença e os recursos de apresentação apontados pelo validador do diretório. Publicar o repositório não equivale a conceder uma licença aberta; essa decisão jurídica/comercial fica com o autor.
- Avaliar satisfação e tarefas reais dos alunos antes de fundir ou remover especialistas. Nesta versão, os 31 nomes foram preservados; as descrições esclarecem fronteiras entre copy, roteiro, ideação e direção visual.
- Não adicionar hooks, rastreamento, servidores ou licenciamento remoto apenas para “modernizar”: essas mudanças aumentariam dependências e exigem objetivo específico e avaliação própria.

## Referências do estudo

As decisões de foco por objetivo, separação de método/recursos, descrições precisas e consulta progressiva seguem as orientações oficiais de [skills da OpenAI](https://developers.openai.com/plugins/build/skills), [skills no Claude Code](https://code.claude.com/docs/en/skills) e [arquitetura de Agent Skills da Anthropic](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills).

O fluxo inicial usa o campo documentado em [empacotamento de plugins da OpenAI](https://developers.openai.com/plugins/build/plugins). A revisão de voz trata tags e pontuação como direção dependente do modelo, conforme as [orientações de text-to-speech da ElevenLabs](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices), sem impor expansão automática de textos curtos.
