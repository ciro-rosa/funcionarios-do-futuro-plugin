\# KB/audio\_sfx\_catalog.md  
Catálogo de \*\*trilhas e SFX\*\* para prompts do \*\*VEO3\*\* em \*\*vertical (16:9)\*\*, \*\*one‑take\*\*, \*\*sem cortes\*\*, \*\*sem zoom\*\*, \*\*até 8s\*\*. Textos prontos em \*\*inglês\*\* para colar no campo \`audio\` do JSON.

\---

\#\# 1\) Fundamentos de áudio (aplicar em qualquer cena)  
\- \*\*Sem legendas / sem texto em tela.\*\* Reforçar em \`negative\_prompts\`: \`"no text overlays"\`, \`"no subtitles"\`.  
\- \*\*Duração ≤ 8s.\*\* Trilhas e SFX devem respeitar janelas temporais do \`motion\`/\`timeline\`.  
\- \*\*Camadas recomendadas:\*\*  
  1\) \*\*Soundtrack\*\* (base contínua e discreta).    
  2\) \*\*SFX primário\*\* (ação central: mecânico, queda, montagem, escaneamento).    
  3\) \*\*SFX de textura\*\* (micro detalhes: cliques, flutter, shimmer).    
  4\) \*\*Ambiência\*\* (cidade, natureza, salão) em baixo nível.  
\- \*\*Mix (princípios):\*\* a base \*\*não\*\* deve encobrir SFX; reduzir levemente a base durante eventos chave; transições \*\*suaves\*\* (sem cortes sonoros bruscos); evitar “stingers” exagerados se não estiverem previstos.

Minibloco base (colar e ajustar):  
\> \*\*\`"soundtrack": "tight cinematic bed (continuous, no drops)", "sfx": \["time-windowed layers aligned to on-screen action"\], "mix": "prioritize core SFX; ambience restrained; avoid harsh transitions"\`\*\*

\---

\#\# 2\) Padrões de trilha (frases prontas)  
Use uma por prompt; mantenha breve e clara.

\- \*\*Cinematic Pulse (rápido/dinâmico):\*\*    
  \*“tight cinematic pulse (continuous, no heavy drops)”\*  
\- \*\*Tech Minimal (estúdio/assembly):\*\*    
  \*“minimal tech bed with soft pulses and airy highs (no risers)”\*  
\- \*\*Ambient Natural (floresta/dunas/água):\*\*    
  \*“natural ambient bed (subtle wind and space), calming and continuous”\*  
\- \*\*Neon Night (urbano noturno):\*\*    
  \*“restrained neon synth bed with steady tempo and clean low end”\*  
\- \*\*Silence‑plus‑Texture (hero estático):\*\*    
  \*“ultra‑subtle tonal bed; focus on micro‑textures and room tone”\*

\---

\#\# 3\) Blocos SFX por contexto (tabelas de uso rápido)

\#\#\# 3.1 Aéreo / Queda controlada / Paraquedas  
\- \*\*Vocabulário:\*\* \*rotor thump\*, \*Doppler pass\*, \*quick‑release clack\*, \*air rush\*, \*parachute pop\*, \*canopy snap‑open\*, \*fabric flutter\*, \*riser tension\*, \*controlled touchdown thud\*, \*cable whip\*.    
\- \*\*Template (colar):\*\*  
\`\`\`json  
{  
  "soundtrack": "tight cinematic pulse (continuous, no heavy drops)",  
  "sfx": \[  
    "0.0–1.6: distant rotor thump with light Doppler; urban room tone",  
    "1.6–2.0: quick-release clack, air rush; parachute pop and canopy snap-open",  
    "2.0–3.5: fabric flutter with riser tension; wind-shear whoosh",  
    "3.5–3.8: contained landing thud; short cable whip upward",  
    "3.8–6.8: hydraulic whirs, precise servo clicks, panel slides",  
    "6.8–8.0: soft shimmer as reflections settle; rotor recedes"  
  \],  
  "mix": "keep rotor impactful but elegant; foreground mechanical details; ambience restrained"  
}

### **3.2 Estúdio tecnológico / Montagem óptica**

* **Vocabulário:** *servo ticks*, *precision actuators*, *linear slides*, *optical scan sweep*, *lidar ticks*, *electromagnetic lock*, *air hiss*, *micro‑latch click*, *clean bearings*.

* **Template:**

{  
  "soundtrack": "minimal tech bed with soft pulses (continuous)",  
  "sfx": \[  
    "0.0–2.0: subtle room tone; faint servo ticks",  
    "2.0–4.5: optical scan sweep with lidar ticks; linear slides on clean bearings",  
    "4.5–6.8: micro-latch clicks; magnetic lock confirmations; soft air hiss",  
    "6.8–8.0: delicate shimmer tail; bed remains steady"  
  \],  
  "mix": "prioritize scan and mechanical clarity; avoid harsh highs; no risers"  
}

### **3.3 Natureza cinematográfica / Voo rasante**

* **Vocabulário:** *soft wind*, *leaf rustle*, *pollen motes*, *distant waterfall haze*, *river glint*, *avian calls (very low)*.

* **Template:**

{  
  "soundtrack": "natural ambient bed (subtle wind and space), continuous",  
  "sfx": \[  
    "0.0–3.0: soft wind and leaf rustle; distant waterfall haze",  
    "3.0–6.5: gentle whoosh from forward glide; occasional water glint sparkle",  
    "6.5–8.0: ambience calms; subtle airy tail"  
  \],  
  "mix": "keep ambience low; emphasize spatial depth; no abrupt changes"  
}

### **3.4 Urbano premium / Neon noturno**

* **Vocabulário:** *city room tone*, *light traffic whoosh*, *distant horn blur*, *LED hum (very low)*, *mirror shimmer high‑freq.*

* **Template:**

{  
  "soundtrack": "restrained neon synth bed (steady tempo)",  
  "sfx": \[  
    "0.0–2.0: city room tone with soft traffic whoosh",  
    "2.0–6.5: mechanical assembly clicks/slides (if any)",  
    "6.5–8.0: high-frequency shimmer as reflections settle"  
  \],  
  "mix": "preserve clean low end; avoid crowd chatter; keep horns distant"  
}

### **3.5 Gelo → Salão (morph controlado)**

* **Vocabulário:** *frost crackles*, *pressure creak*, *crystalline shatter*, *particle tinks*, *mirror strip power‑up hum*, *electrical fizz*.

* **Template:**

{  
  "soundtrack": "subtle cinematic bed that warms slightly over time",  
  "sfx": \[  
    "0.0–1.2: cold room tone with faint frost crackles",  
    "1.2–2.2: pressure creak and low air swell",  
    "2.2–2.6: crystalline shatter with airy whoosh; brief tinkle tail",  
    "2.6–5.8: delicate particle tinks; assembly clicks",  
    "3.2–7.0: light power-up hum; gentle electrical fizz from mirror strips",  
    "7.0–8.0: reflection shimmer settles to calm"  
  \],  
  "mix": "keep shatter impactful but refined; foreground particle detail; smooth bed"  
}

---

## **4\) Narração (opcional e somente se pedida)**

* **Idioma:** exatamente o que a pessoa solicitou.

* **Extensão:** curta o suficiente para caber em 8s.

* **Mistura:** clara, levemente acima da ambiência, sem competir com SFX principais.

* **Nunca** converter em legendas ou texto em tela.

**Snippet para colar:**

"narration": {  
  "language": "\<e.g., pt-BR | en-US | es-ES\>",  
  "text": "\<short line requested by the user\>",  
  "mix": "keep narration clear and slightly above ambience; do not overpower key SFX"  
}

---

## **5\) Negativos relacionados a áudio (copiar para `negative_prompts`)**

* `"no text overlays"`, `"no subtitles"`

* `"no harsh stingers"`, `"no jump cuts in audio"`

* `"no auto ducking artifacts"`, `"no pumping"`

* `"no crowd chatter foreground"`

* `"no heavy distortion"`, `"no clipping"`

* `"no exaggerated reverb tails"`

---

## **6\) Padrões de janela temporal (até 8s)**

Use conforme o ritmo do `motion`:

* **Rápido:** `00.0–01.6`, `01.6–03.5`, `03.5–06.8`, `06.8–08.0`

* **Equilibrado:** `00.0–02.0`, `02.0–04.5`, `04.5–06.8`, `06.8–08.0`

* **Elegante:** `00.0–03.0`, `03.0–05.5`, `05.5–08.0`

---

## **7\) Validação rápida (antes de enviar)**

* Soundtrack contínua, **sem quedas dramáticas** fora do planejado.

* SFX **alinhados às batidas** e com prioridade clara na mix.

* Ambiência **baixa** e coerente com o cenário.

* Narração apenas se requerida, no idioma pedido, **sem legendas**.

* `negative_prompts` inclui bloqueios de texto/legendas e artefatos de áudio.

* Tudo cabe em **≤ 8s** e o JSON permanece compacto.

---

