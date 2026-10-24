# Método de execução

Cria JSON estruturado de prompt para vídeo curto em plano único. Use quando o pedido exige JSON; ideias de cenas são de roteirista-viral-para-flow e prompt livre é de vision.

## Contexto necessário

Cena/ação, duração, proporção, áudio e modo texto ou frame; mídia real se for frame_to_video.

## Método

Use um esquema editorial consistente, não alegue ser o schema oficial da API do fornecedor. Defaults: 8s, 9:16, um plano, sem cortes/zoom e sem legendas/texto em tela. Proporção horizontal 16:9 é aceita quando pedida para manter o fluxo do roteirista; não converta silenciosamente. Até 8s neste template; se pedirem maior duração, proponha cenas ou vision. Narração só quando solicitada, curta e no idioma pedido.

## Entrega

Um JSON estrito em bloco, sem comentários, válido em parser e até 8.000 caracteres por resposta; até três variantes se pedidas. Campos estáveis: mode, name, aspect_ratio, description, camera, lighting, environment, elements, timeline (início/fim em segundos), audio, constraints, negative_prompts, ending, timing. Para frame_to_video, reference_assets somente com uma referência real fornecida ou placeholder explicitamente solicitado. Não trate ATTACHED_IMAGE_0 como um arquivo existente.

## Conferência antes de responder

Obrigatórios: timing.duration_seconds positivo e até 8; aspect_ratio 9:16 ou 16:9 conforme pedido; constraints.single_take/no_cuts/no_zoom true; negative_prompts inclui no subtitles e no text overlays. Cada item de timeline usa start/end numéricos em segundos e action em inglês; a sequência começa em 0 e cobre a duração sem sobreposições nem lacunas. Descrições em inglês, fala exatamente no idioma pedido. Se quiser texto em tela, explique a incompatibilidade deste template e ofereça prompt livre em vision.

Estas instruções são a versão revisada para execução. Os originais estão preservados para consulta histórica, não precisam ser carregados para executar a tarefa.
