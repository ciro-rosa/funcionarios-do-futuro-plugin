\# KB/camera\_move\_recipes.md  
Biblioteca de \*\*movimentos de câmera\*\* para VEO3 — vertical \*\*16:9\*\*, \*\*one‑take\*\*, \*\*no cuts\*\*, \*\*no zoom\*\*, \*\*fixed focal\*\*. Textos prontos em \*\*inglês\*\* para colar em \`camera\` / \`camera\_setup\` e guias de tempo para \*\*até 8s\*\*.

\---

\#\# 1\) Princípios essenciais (aplicar em todos os prompts)  
\- \*\*Vertical only:\*\* \`aspect\_ratio: "16:9"\`.  
\- \*\*Tomada única:\*\* descreva \*\*um\*\* caminho contínuo (sem cortes).  
\- \*\*Sem zoom:\*\* declare \*\*fixed focal length\*\* (ex.: 35 mm).  
\- \*\*Estabilidade:\*\* prefira “stabilized tracking”; se usar \*\*whip‑tilt\*\*/\*\*whip‑pan\*\*, limite a 0.3–0.6 s.  
\- \*\*Safe area:\*\* mantenha sujeito dentro de \*\*10–15%\*\* das bordas (sem crop automático).  
\- \*\*Velocidade:\*\* combine o ritmo do movimento com as batidas de \`motion\`/\`timeline\`.  
\- \*\*Foco:\*\* por padrão não faça focus pulls; se necessário, declare \*\*no focus pulls\*\*.

\---

\#\# 2\) Frases prontas (colar em \`camera\` ou \`camera\_setup\`)  
\> Em inglês; escolha \*\*uma\*\* e adapte.

1\. \*\*Mid‑Height Arc\*\*  
   \- \*“one continuous 8‑second mid‑height arc; fixed focal length; no cuts; no zoom; stabilized vertical framing”\*  
2\. \*\*Push‑Orbit\*\*  
   \- \*“one continuous 8‑second push‑orbit at mid‑height; fixed focal length; no cuts; no zoom; gentle parallax”\*  
3\. \*\*Lateral Dolly \+ Gentle Rise\*\*  
   \- \*“one continuous 8‑second lateral dolly with a gentle crane rise; fixed focal length; no cuts; no zoom”\*  
4\. \*\*Tracking Glide (Forward)\*\*  
   \- \*“one continuous 8‑second forward tracking glide; fixed focal length; no cuts; no zoom; subject kept within safe margins”\*  
5\. \*\*Crane‑Down to Hero\*\*  
   \- \*“one continuous 8‑second crane‑down settling into a centered hero; fixed focal length; no cuts; no zoom”\*  
6\. \*\*Whip‑Tilt High‑to‑Low (controlado)\*\*  
   \- \*“one continuous 8‑second move with a single 0.4‑second whip‑tilt from high angle to mid‑height; fixed focal length; no cuts; no zoom”\*  
7\. \*\*Parallax Strafe\*\*  
   \- \*“one continuous 8‑second parallax strafe keeping the subject centered; fixed focal length; no cuts; no zoom”\*  
8\. \*\*Overhead to Three‑Quarters\*\*  
   \- \*“one continuous 8‑second move from near‑overhead to three‑quarters view; fixed focal length; no cuts; no zoom”\*  
9\. \*\*Orbit‑Settle\*\*  
   \- \*“one continuous 8‑second half‑orbit that settles to a centered hero; fixed focal length; no cuts; no zoom”\*  
10\. \*\*Locked Hero (Micro Drift)\*\*  
    \- \*“one continuous 8‑second locked hero with subtle micro drift for depth; fixed focal length; no cuts; no zoom”\*

\---

\#\# 3\) Receitas por contexto (com tempos até 8s)

\#\#\# 3.1 Sobrevoo alto → entrega dinâmica (helicóptero/queda controlada)  
\- \*\*Câmera (colar):\*\* \*“one continuous 8‑second up‑angle track with a brief 0.4‑second whip‑tilt to ground level; fixed focal length; no cuts; no zoom”\*  
\- \*\*Ritmo sugerido:\*\*  
  \- \*\*00.0–01.6:\*\* up‑angle tracking do alvo \*\*alto\*\*.  
  \- \*\*01.6–02.0:\*\* whip‑tilt controlado para o ponto de queda.  
  \- \*\*02.0–03.6:\*\* descida guiada/posicionamento.  
  \- \*\*03.6–06.8:\*\* transformação \*\*in place\*\*.  
  \- \*\*06.8–08.0:\*\* settle em hero vertical.

\#\#\# 3.2 Estúdio tecnológico (scan/assembly)  
\- \*\*Câmera:\*\* \*“one continuous 8‑second push‑orbit at mid‑height; fixed focal; no cuts; no zoom”\*  
\- \*\*Ritmo:\*\*  
  \- \*\*00.0–02.0:\*\* início do push com primeiro scan.  
  \- \*\*02.0–04.5:\*\* módulos deslizam/encaixam.  
  \- \*\*04.5–06.8:\*\* refinamento, painéis finais.  
  \- \*\*06.8–08.0:\*\* hero posicionado e reflexos estáveis.

\#\#\# 3.3 Natureza cinematográfica (glide sobre cenário)  
\- \*\*Câmera:\*\* \*“one continuous 8‑second forward tracking glide with gentle crane rise; fixed focal; no cuts; no zoom”\*  
\- \*\*Ritmo:\*\*  
  \- \*\*00.0–03.0:\*\* glide sobre o primeiro plano.  
  \- \*\*03.0–06.5:\*\* arco suave com elementos atmosféricos.  
  \- \*\*06.5–08.0:\*\* leve subida e hero final.

\#\#\# 3.4 Praça/avenida urbana (reveal estruturado)  
\- \*\*Câmera:\*\* \*“one continuous 8‑second half‑orbit settling to a centered hero; fixed focal; no cuts; no zoom”\*  
\- \*\*Ritmo:\*\*  
  \- \*\*00.0–02.0:\*\* aproximação lateral.  
  \- \*\*02.0–04.0:\*\* meia órbita para leitura de volume.  
  \- \*\*04.0–06.5:\*\* montagem/ação principal.  
  \- \*\*06.5–08.0:\*\* hero central, reflexos limpos.

\---

\#\# 4\) Padrões de tempo (use o que convém)  
\- \*\*Rápido/dinâmico:\*\* \`00.0–01.6\`, \`01.6–03.2\`, \`03.2–06.8\`, \`06.8–08.0\`  
\- \*\*Equilibrado:\*\* \`00.0–02.0\`, \`02.0–04.0\`, \`04.0–06.5\`, \`06.5–08.0\`  
\- \*\*Lento/elegante:\*\* \`00.0–03.0\`, \`03.0–05.5\`, \`05.5–08.0\`

\> Ajuste o texto de \`motion\`/\`timeline\` para bater com o padrão escolhido.

\---

\#\# 5\) DO / DON’T (succinto)  
\*\*FAZER\*\*  
\- Definir \*\*um\*\* caminho claro e contínuo.  
\- Declarar \*\*fixed focal length\*\* e \*\*no zoom\*\*.  
\- Amarrar batidas de câmera ao \`motion\`/\`timeline\`.  
\- Manter o sujeito dentro da \*\*safe area\*\*.

\*\*EVITAR\*\*  
\- Misturar múltiplos movimentos conflitantes.  
\- Usar “zoom in/out” (o modelo tende a exagerar).  
\- Trocar de altura/ângulo sem transição coerente.  
\- Deixar a câmera “caçando” o alvo (handheld look).

\---

\#\# 6\) Minibloco para colar (genérico, vertical)  
Use como base em \`camera\`:  
\- \*“one continuous 8‑second mid‑height arc; fixed focal length; no cuts; no zoom; stabilized vertical framing; subject kept within safe margins”\*

E variação para whip‑tilt controlado:  
\- \*“one continuous 8‑second move with a single 0.4‑second whip‑tilt from high angle to mid‑height; fixed focal length; no cuts; no zoom; stabilized vertical framing”\*

\---

\#\# 7\) Erros comuns e correção  
\- \*\*Drift de horizonte/auto‑nível:\*\* reafirme “stabilized vertical framing; do not auto‑level the horizon”.  
\- \*\*Zoom indesejado:\*\* reforçar “no zoom; fixed focal length”.  
\- \*\*Cortes invisíveis:\*\* repetir “one continuous 8‑second move; no cuts”.  
\- \*\*Sujeito fora de quadro:\*\* citar “subject kept within safe margins; avoid edge cropping”.

\---

