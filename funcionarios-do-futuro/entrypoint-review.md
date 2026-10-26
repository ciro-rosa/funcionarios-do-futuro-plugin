# Revisão da entrada Funcionários — versão 1.3.0

A skill `funcionarios` substitui `suporte-24-horas` como entrada de produção de conteúdo. São 30 especialistas mais uma central, preservando as 31 instruções originais e as 63 associações de bases. Os hashes das bases e instruções originais foram comparados com a versão 1.2.0; os métodos ativos dos outros 30 especialistas continuam idênticos.

## Casos executados em 26 de outubro de 2026

Foram produzidas cinco respostas no Codex CLI e cinco no Claude Code: saudação, texto de carrossel de seis slides, plano de três posts com briefing existente, combinação de texto e direção visual de três slides 4:5 e diagnóstico de Filename too long. O caso combinado também foi repetido isoladamente nos dois ambientes, totalizando 12 respostas nesta rodada final. A seleção dos especialistas ficou a cargo da central; os testes indicam explicitamente usar a central e não medem sua ativação implícita em pedidos arbitrários.

As respostas foram revisadas pelo assistente: os pedidos de produção receberam entregas na mesma conversa, o planejamento reutilizou o briefing, e o caso combinado consultou os métodos de carrossel e design, preservando a proporção e o CTA. Os caminhos das fontes consultadas foram conferidos. Isso não constitui avaliação por alunos reais nem garantia de qualidade editorial em toda resposta.

## Atalho e instalação

O comando `/funcionarios oi` foi executado com sucesso no Claude Code, carregando a versão candidata pelo mecanismo nativo de plugin. Em conflito com outro comando, use `/funcionarios-do-futuro:funcionarios`. A lista de skills e a frase “Use Funcionários do Futuro” são as entradas documentadas para o Codex; não se promete comando de barra idêntico nos dois aplicativos.

## Observações e limites

- Uma primeira resposta da confeitaria sugeriu garantia de data sem confirmação. A instrução da central foi reforçada e o conjunto repetido; a rodada final não incluiu essa garantia.
- No lote final do Claude, o caso combinado trouxe “aulas individuais, online”, dados presentes em outro caso do lote, mas ausentes naquele pedido. A repetição isolada nos dois aplicativos não incluiu essa oferta. Casos em lote podem compartilhar contexto; as afirmações específicas do negócio ainda exigem conferência editorial.
- Na repetição isolada do Claude, a copy usou a generalização “quase todo adulto”; recomenda-se suavizar antes de publicar. No Codex, uma quebra de linha dentro de uma célula pode exigir ajuste na apresentação da tabela.
- O teste do atalho curto verifica invocação e resposta inicial; a consulta aos métodos e às bases foi verificada nos testes de produção completos.
- Não foram geradas ou publicadas imagens, vídeos, áudios ou posts. Os 60 testes dos especialistas registrados no estudo da versão 1.2.0 não foram repetidos nesta alteração da central.
