# Método de execução

Prepara texto para narração com tags de entonação e pausas para ElevenLabs. Use para direção de voz mantendo as palavras do original; não gera áudio nem clona uma voz.

## Contexto necessário

Texto original, intenção/voz e modelo-alvo se conhecido.

## Método

Preserve palavras e ordem do original; adicione tags esparsas como [excited], [whispering] ou [sighs] quando adequadas à voz e modelo. Respeite tags existentes sem duplicação. Alterações de pontuação opcionais não podem mudar sentido; se o pedido for literal, acrescente apenas tags. Não expanda texto curto só para alcançar 250 caracteres. Não force efeitos sonoros em narração simples.

## Entrega

Texto pronto em bloco, com tags em colchetes. Diagnóstico curto e variações apenas quando solicitados. Sem prometer compatibilidade total: tags e desempenho dependem do modelo/voz; confirme documentação atual se precisar de recursos específicos.

## Conferência antes de responder

Remover tags deve recuperar as palavras originais na mesma ordem. Não inventar comandos oficiais. Sem alegar que gerou áudio ou treinou voz. Fonte para consulta: https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices

Estas instruções são a versão revisada para execução. Os originais estão preservados para consulta histórica, não precisam ser carregados para executar a tarefa.
