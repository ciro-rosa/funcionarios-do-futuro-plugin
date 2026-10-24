\# KB/negative\_prompts\_catalog.md  
Catálogo de \*\*negative prompts\*\* para VEO3 — focado em \*\*vertical (9:16)\*\*, \*\*one‑take\*\*, \*\*sem cortes\*\*, \*\*sem zoom\*\*, \*\*≤ 8s\*\*. Todos os itens estão prontos em \*\*inglês\*\* para colagem direta no campo \`negative\_prompts\` do JSON. Use apenas o que fizer sentido para o caso.

\---

\#\# 1\) Núcleo estável (usar na maioria dos prompts)  
\> Mantém o vídeo limpo, sem texto e sem comportamentos automáticos indesejados.  
\`\`\`json  
\[    
  "no subtitles",  
  "no on-screen captions",  
  "no lower-thirds",  
  "no watermarks",  
  "no timecode burns",  
  "no UI elements",  
  "no logo slates",

  "no cuts",  
  "no jump cuts",  
  "no zoom",  
  "no dolly zoom",  
  "no handheld shake",  
  "no focus hunting",  
  "no rack focus pulls",  
  "no auto reframing",  
  "no auto horizon leveling",

  "no auto exposure shifts",  
  "no auto white balance",  
  "no heavy bloom",  
  "no glare streaks",  
  "no banding on gradients",  
  "no vignetting",  
  "no color fringing",  
  "no blown-out highlights",  
  "no crushed blacks",

  "no letterboxing",  
  "no pillarboxing",  
  "no aspect ratio changes",  
  "no orientation auto-rotate"  
\]

---

## **2\) Câmera e composição**

Evita drift, cortes invisíveis e enquadramento ruim.

\[  
  "no shaky handheld",  
  "no rolling shutter artifacts",  
  "no micro jitter",  
  "no camera roll drift",  
  "no tilt breathing",  
  "no edge cropping of the main subject",  
  "no partial occlusion of the main subject",  
  "no subject popping in or teleporting",  
  "no speed ramps",  
  "no slow motion unless explicitly described"  
\]

---

## **3\) Iluminação e cor**

Mantém reflexos e highlights sob controle, sem flutuações.

\[  
  "no exposure pumping",  
  "no white balance drift",  
  "no harsh lens flares",  
  "no excessive bloom",  
  "no glare starbursts",  
  "no neon oversaturation",  
  "no muddy midtones",  
  "no washed-out colors",  
  "no color banding",  
  "no color cast drift"  
\]

---

## **4\) Materiais, superfícies e render**

Garante realismo de metal/vidro/pele/superfícies gloss.

\[  
  "no low-resolution textures",  
  "no texture stretching",  
  "no visible tiling",  
  "no jagged edges",  
  "no aliasing shimmer",  
  "no plastic look on metals",  
  "no fake reflections",  
  "no overdone motion blur on the subject",  
  "no DOF pulsing",  
  "no excessive film grain"  
\]

---

## **5\) Efeitos e partículas**

Evita exagero de FX e ruídos visuais.

\[  
  "no particle spam",  
  "no unrealistic smoke plumes",  
  "no chaotic sparks",  
  "no debris clouds",  
  "no confetti",  
  "no fog wall",  
  "no over-cranked FX simulations"  
\]

---

## **6\) Áudio (mapa rápido)**

Alinha o som a uma base limpa e sem cortes bruscos.

\[  
  "no text overlays",  
  "no subtitles",  
  "no harsh stingers",  
  "no jump cuts in audio",  
  "no pumping or aggressive auto ducking",  
  "no clipping or distortion",  
  "no crowd chatter foreground",  
  "no exaggerated reverb tails",  
  "no abrupt soundtrack stops"  
\]

---

## **7\) Verticalidade (9:16)**

Mantém consistência no formato.

\[  
  "no landscape framing",  
  "no rotation flips",  
  "no letterboxing",  
  "no pillarboxing",  
  "no auto-rotate prompts"  
\]

---

## **8\) Toggles criativos (use quando fizer sentido)**

Mecanismos para **evitar clichês** recorrentes quando indesejados.

\[  
  "no circular halos or energy rings around the subject",  
  "no zipper-like effects on surfaces",  
  "no hologram HUD overlays",  
  "no random glitch transitions",  
  "no bokeh shapes that distract from the subject",  
  "no cartoon outlines",  
  "no comic-book panels",  
  "no emoji graphics",  
  "no retro VHS filters"  
\]

---

## **9\) Contextos específicos — blocos prontos**

### **9.1 Aéreo / Paraquedas / Entrega dinâmica**

\[  
  "no low helicopter altitude framing",  
  "no unsafe proximity to traffic",  
  "no dust plumes into the street",  
  "no parachute tangling",  
  "no crate skidding out of footprint",  
  "no crowd close-ups",  
  "no chaotic wind artifacts"  
\]

### **9.2 Estúdio tecnológico / Montagem óptica**

\[  
  "no overcomplicated robot choreography",  
  "no laser beams through the camera",  
  "no UI floating labels",  
  "no overblown bloom on light panels",  
  "no oily fingerprints on glossy surfaces"  
\]

### **9.3 Natureza / Voo rasante**

\[  
  "no wildlife close-ups",  
  "no heavy fog banks",  
  "no rain curtains",  
  "no flying debris",  
  "no branch occlusions of the main subject"  
\]

### **9.4 Gelo → Salão (morph controlado)**

\[  
  "no violent shatter",  
  "no shards toward camera",  
  "no slippery floor hazards",  
  "no condensation obscuring the subject",  
  "no messy residue on final surfaces"  
\]

### **9.5 Neon urbano / Noite**

\[  
  "no flashing strobes",  
  "no glare streaks crossing the subject",  
  "no LED banding",  
  "no sign flicker artifacts",  
  "no crowd foreground silhouettes blocking the subject"  
\]

---

## **10\) Bloco mínimo (copiar e colar)**

Use como base em praticamente qualquer prompt; adicione itens específicos conforme o caso.

\[  
  "no text overlays",  
  "no subtitles",  
  "no cuts",  
  "no zoom",  
  "no handheld shake",  
  "no auto exposure shifts",  
  "no auto white balance",  
  "no heavy bloom",  
  "no glare streaks",  
  "no banding on gradients",  
  "no letterboxing",  
  "no pillarboxing",  
  "no orientation auto-rotate",  
  "no subject popping in or teleporting"  
\]

---

## **11\) Dicas de uso (curtas)**

* **Menos é mais:** inclua o **núcleo estável** e **2–5** negativos específicos do contexto.

* **Coerência:** negativos devem **combinar** com `camera`, `lighting`, `motion` e `audio`.

* **Evite redundância:** não repita termos idênticos em blocos diferentes.

* **Teste iterativo:** se o modelo insistir em um vício (ex.: “zoom”), **suba** a prioridade do negativo (“no zoom” \+ “fixed focal length; no digital zoom” em `camera`).

---

