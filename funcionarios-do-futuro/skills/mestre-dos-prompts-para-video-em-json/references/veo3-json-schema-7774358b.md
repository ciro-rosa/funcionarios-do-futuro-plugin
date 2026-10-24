\# KB/veo3\_json\_schema.md  
Guia de referência rápida do \*\*formato JSON\*\* para prompts do \*\*VEO3\*\*, com exemplos mínimos e regras de validação. Este arquivo serve como base para o agente gerar saídas consistentes.

\---

\#\# 1\) Regras Globais  
\- \*\*Idioma do prompt:\*\* sempre \*\*inglês\*\*.    
\- \*\*Narração (se houver):\*\* exatamente no \*\*idioma solicitado\*\* pela pessoa usuária.    
\- \*\*Sem legendas / sem texto em tela:\*\* proibir explicitamente em \`negative\_prompts\`.    
\- \*\*Duração:\*\* \*\*≤ 8 segundos\*\* (padrão: 8s).    
\- \*\*Aspect ratio:\*\* \*\*vertical obrigatório\*\* → \`"aspect\_ratio": "9:16"\`.    
\- \*\*Estilo de filmagem padrão:\*\* \*\*one‑take\*\*, \*\*no cuts\*\*, \*\*no zoom\*\*, \*\*fixed focal\*\*.    
\- \*\*JSON estrito:\*\* sem comentários, chaves e strings entre aspas, sem vírgulas finais.

\---

\#\# 2\) Conjunto de Chaves (use somente o necessário)  
\*\*Obrigatórias (recomendadas na maioria dos casos):\*\*  
\- \`mode\`: \`"text\_to\_video"\` ou \`"frame\_to\_video"\`.  
\- \`name\`: título curto.  
\- \`aspect\_ratio\`: sempre \`"9:16"\`.  
\- \`description\`: uma frase clara com a ação; \*\*sem on‑screen text\*\*.  
\- \`camera\` \*\*ou\*\* \`camera\_setup\`: descreve \*\*um\*\* movimento contínuo de 8s.  
\- \`timing\`: objeto com \`duration\_seconds\` (≤ 8\) e \`fps\` (ex.: 24).

\*\*Altamente úteis:\*\*  
\- \`style\`: tom visual (ex.: \*cinematic, ultra‑realistic, tech minimal\*).  
\- \`lighting\`: clima de luz.  
\- \`environment\`: cenário, sem dependências externas.  
\- \`elements\`: lista dos itens que precisam aparecer.  
\- \`motion\` \*\*ou\*\* \`timeline\`: batidas temporais (0–8s) em texto.  
\- \`audio\`: \`soundtrack\`, \`sfx\` e, se solicitado, \`narration\`.  
\- \`constraints\`: regras de filmagem e técnica (one‑take, no cuts, no zoom, focal).  
\- \`negative\_prompts\`: bloqueios consistentes.  
\- \`ending\`: composição do quadro final.  
\- \`keywords\`: palavras‑chave curtas.

\*\*Específicas de \`frame\_to\_video\`:\*\*  
\- \`reference\_assets\`: ex.: \`{ "initial\_frame": "ATTACHED\_IMAGE\_0" }\`    
  (pode incluir \`product\_packshot\`, \`logo\_description\` se necessário).

\---

\#\# 3\) Campos — Definições e Formatos

\#\#\# 3.1 \`mode\`  
\`\`\`json  
"mode": "text\_to\_video"

ou

"mode": "frame\_to\_video"

### **3.2 `name`**

Texto curto e objetivo.

### **3.3 `aspect_ratio`**

"aspect\_ratio": "9:16"

### **3.4 `description`**

* 1–2 frases no **presente** descrevendo a ação.

* **Não** incluir texto em tela ou legendas.

### **3.5 `camera` / `camera_setup`**

Descrever **um único** movimento contínuo, com verbos concretos. Ex.:  
 `"one continuous 8-second arc at mid-height; fixed focal length; no cuts; no zoom"`

### **3.6 `lighting`**

Definição clara de key/fill/haze ou clima geral (ex.: *golden hour with soft sky fill; subtle atmospheric haze*).

### **3.7 `environment`**

Cenário sucinto, sem dependências externas.

### **3.8 `elements`**

Lista objetiva dos objetos/entidades relevantes.

### **3.9 `motion` ou `timeline`**

* **`motion`**: parágrafo curto com **janelas temporais**.

* **`timeline`**: lista com `sequence`, `timestamp`, `action`, `audio` (quando convier).

### **3.10 `audio`**

Estrutura recomendada:

"audio": {  
  "soundtrack": "short description (continuous)",  
  "sfx": \[  
    "0.0–X: \<layer 1\>",  
    "X–Y: \<layer 2\>"  
  \]  
}

**Narração (opcional, somente se pedida):**

"narration": {  
  "language": "pt-BR",  
  "text": "Texto curto adequado ao tempo.",  
  "mix": "keep narration clear, slightly above ambience"  
}

### **3.11 `constraints`**

Regras técnicas explícitas:

"constraints": {  
  "single\_take": true,  
  "no\_cuts": true,  
  "no\_zoom": true,  
  "fixed\_focal\_length\_mm": 35  
}

Campos adicionais úteis: `safe_margins_percent`, `avoid_edge_cropping`, `transform_in_place`.

### **3.12 `negative_prompts`**

Manter um núcleo estável para evitar deriva:

"negative\_prompts": \[  
  "no text overlays",  
  "no subtitles",  
  "no shaky handheld",  
  "no auto zoom"  
\]

### **3.13 `ending`**

Descrever claramente a composição do último quadro (posição do sujeito, luz, reflexos).

### **3.14 `keywords`**

Tags curtas (3–10 itens) ajudam a consolidar o tom.

### **3.15 `timing`**

"timing": { "duration\_seconds": 8, "fps": 24 }

Nunca exceder 8s.

### **3.16 `reference_assets` (somente `frame_to_video`)**

"reference\_assets": {  
  "initial\_frame": "ATTACHED\_IMAGE\_0"  
}

Outros campos possíveis: `"product_packshot"`, `"logo_description"` (se necessário sintetizar).

---

## **4\) Regras de Validação**

* `aspect_ratio` **obrigatoriamente** `"9:16"`.

* `timing.duration_seconds` **≤ 8** (padrão: 8).

* **Movimento único** na câmera; evitar instruções contraditórias.

* `audio`: coerente com as batidas de `motion`/`timeline`.

* `negative_prompts` **sempre** inclui `"no text overlays"` e `"no subtitles"`.

* JSON estrito: aspas duplas, sem vírgulas finais, sem comentários.

* Tamanho total da resposta do agente **≤ 8.000 caracteres** (incluindo espaços).

---

## **5\) Exemplos Mínimos**

### **5.1 `text_to_video` — vertical one‑take (mínimo)**

{  
  "mode": "text\_to\_video",  
  "name": "Urban Mirror Reveal",  
  "aspect\_ratio": "9:16",  
  "style": "cinematic, ultra-realistic, fast",  
  "description": "A single-take vertical shot tracks a dynamic urban setup as a compact structure unfolds into a sleek mirror-clad form—clean, precise, and debris-free.",  
  "camera": "one continuous 8-second arc at mid-height; fixed focal length; no cuts; no zoom",  
  "lighting": "late-afternoon sun with soft sky fill; subtle haze for depth",  
  "environment": "busy avenue median with patterned sidewalks and trees",  
  "elements": \["compact crate", "mechanical latches", "mirror panels"\],  
  "motion": "00.0–02.0 approach and stabilize; 02.0–04.0 crate opens; 04.0–06.5 panels slide and lock; 06.5–08.0 clean hero hold",  
  "audio": {  
    "soundtrack": "tight cinematic bed (continuous)",  
    "sfx": \[  
      "0.0–2.0 light urban tone",  
      "2.0–6.5 hydraulic whirs, precise clicks",  
      "6.5–8.0 soft shimmer on reflections"  
    \]  
  },  
  "constraints": { "single\_take": true, "no\_cuts": true, "no\_zoom": true, "fixed\_focal\_length\_mm": 35 },  
  "negative\_prompts": \["no text overlays", "no subtitles", "no shaky handheld", "no auto zoom"\],  
  "ending": "hero frame: mirror surface stabilized, reflections gliding cleanly",  
  "keywords": \["8s one-take", "9:16", "urban", "mirror"\],  
  "timing": { "duration\_seconds": 8, "fps": 24 }  
}

### **5.2 `frame_to_video` — com frame inicial (mínimo)**

{  
  "mode": "frame\_to\_video",  
  "name": "Tech Studio Scan",  
  "aspect\_ratio": "9:16",  
  "reference\_assets": { "initial\_frame": "ATTACHED\_IMAGE\_0" },  
  "style": "CGI photoreal, clean studio",  
  "description": "From the attached frame, a precision scan passes across the object, assembling a refined vertical form in one continuous move.",  
  "camera\_setup": "one continuous 8-second push-orbit; fixed focal; no cuts; no zoom",  
  "lighting": "cool studio key with soft rim; controlled reflections",  
  "environment": "minimal tech studio floor with subtle volumetrics",  
  "elements": \["object on plinth", "optical scan head", "modular panels"\],  
  "timeline": \[  
    { "sequence": 1, "timestamp": "00:00-00:08", "continuous\_shot": true, "action": "scan crosses, components slide and lock; final pose stabilizes", "audio": "soft electronic bed, gentle servo ticks, quiet shimmer at the end" }  
  \],  
  "negative\_prompts": \["no text overlays", "no subtitles", "no auto zoom"\],  
  "ending": "clean hero vertical pose with neat reflections",  
  "timing": { "duration\_seconds": 8, "fps": 24 }  
}

---

## **6\) Padrões de Texto (úteis para colagem)**

* **Câmera:** *“one continuous 8‑second ; fixed focal length; no cuts; no zoom”*

* **Luz:** *“golden hour with soft sky fill; subtle atmospheric haze”*

* **Áudio (base):** *“tight cinematic bed (continuous)”*

* **SFX (exemplos):** *“hydraulic whirs, precise latch clicks, glass panel slides, soft shimmer”*

* **Negativos fixos:** *“no text overlays”, “no subtitles”, “no shaky handheld”, “no auto zoom”*

---

## **7\) Erros Comuns a Evitar**

* Exceder **8s** de duração.

* Omitir `"aspect_ratio": "9:16"`.

* Misturar múltiplos movimentos de câmera contraditórios.

* Incluir **texto em tela** ou **legendas** por engano.

* Descrever sons sem alinhar às janelas de tempo.

* JSON inválido (vírgulas finais, aspas faltando).

---

## **8\) Procedimento de Validação Final**

1. Confirmar **inglês** no prompt (narration apenas se pedida, na língua solicitada).

2. Verificar `aspect_ratio: "9:16"` e `duration_seconds ≤ 8`.

3. Garantir **one‑take**, **no cuts**, **no zoom**.

4. Garantir `negative_prompts` com **“no text overlays”** e **“no subtitles”**.

5. Conferir coerência entre `motion`/`timeline` e `audio`.

6. Revisar se o texto total da resposta do agente **≤ 8.000 caracteres**.

---

