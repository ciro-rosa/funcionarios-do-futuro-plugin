\# KB/timing\_templates\_8s.md  
Modelos de \*\*tempo e ritmo\*\* para prompts do \*\*VEO3\*\* em \*\*vertical (9:16)\*\*, \*\*one‑take\*\*, \*\*sem cortes\*\*, \*\*sem zoom\*\*, com \*\*duração máxima de 8s\*\*. Textos prontos em \*\*inglês\*\* para colar nos campos \`motion\`, \`timeline\` e \`audio\`.

\---

\#\# 1\) Princípios de tempo  
\- \*\*Janela total:\*\* até \*\*8 segundos\*\* (padrão: 8s).    
\- \*\*Clareza temporal:\*\* escreva batidas com faixas “\*\*00.0–08.0\*\*”.    
\- \*\*Coerência:\*\* alinhe \*\*ação\*\*, \*\*câmera\*\* e \*\*SFX\*\* às mesmas janelas.    
\- \*\*Encerramento limpo:\*\* reserve \*\*0.3–0.5s\*\* finais para \*\*hero hold\*\* (ajuda loop/legibilidade).    
\- \*\*Transições sonoras suaves:\*\* sem paradas bruscas; evite picos repentinos.

\---

\#\# 2\) Mapas de tempo — prontos para colagem

\#\#\# 2.1 Rápido e dinâmico (impacto precoce)  
Use quando o hook precisa acontecer cedo.  
\`\`\`text  
00.0–01.6  | hook/entrada do elemento principal  
01.6–03.5  | evento gatilho / início de montagem  
03.5–06.8  | montagem/transformação contínua  
06.8–08.0  | hero hold final (estabiliza reflexos/ambiente)

**Frase para `motion`:**  
 *“00.0–01.6 high‑energy hook; 01.6–03.5 trigger and first assembly; 03.5–06.8 continuous build with precise locking; 06.8–08.0 clean hero hold”*

---

### **2.2 Equilibrado (leitura clara do meio)**

Boa leitura do meio da cena, sem pressa.

00.0–02.0  | aproximação/estabelecimento  
02.0–04.5  | início de montagem/escaneamento  
04.5–06.8  | finalização de painéis/módulos  
06.8–08.0  | hero hold

**Frase para `motion`:**  
 *“00.0–02.0 establish and stabilize; 02.0–04.5 primary assembly; 04.5–06.8 refinement and locks; 06.8–08.0 hero hold and reflections”*

---

### **2.3 Elegante e contemplativo (mais ar)**

Quando o clima exige suavidade.

00.0–03.0  | introdução fluida  
03.0–05.5  | desenvolvimento principal  
05.5–08.0  | finalização \+ hero hold

**Frase para `motion`:**  
 *“00.0–03.0 graceful introduction; 03.0–05.5 core development; 05.5–08.0 completion and calm hero hold”*

---

### **2.4 “Whip‑tilt” controlado (pivô rápido de atenção)**

Para transicionar **alto → médio** sem parecer corte.

00.0–01.6  | leitura do alvo alto (ou contexto)  
01.6–02.0  | whip‑tilt controlado (0.4s)  
02.0–06.8  | ação/transformação principal  
06.8–08.0  | hero hold

**Frase para `motion`:**  
 *“00.0–01.6 high‑angle read; 01.6–02.0 controlled 0.4‑second whip‑tilt; 02.0–06.8 core action builds in one flow; 06.8–08.0 hero hold”*

---

## **3\) Tabelas de compressão (se o pedido for \< 8s)**

Mantendo proporções aproximadas.

| Meta | Blocos sugeridos | Observações |
| ----- | ----- | ----- |
| **7s** | 00.0–01.4 / 01.4–03.0 / 03.0–05.6 / 05.6–07.0 | Preserve hero ≥ 0.3s |
| **6s** | 00.0–01.2 / 01.2–02.6 / 02.6–04.8 / 04.8–06.0 | Use ações mais diretas |
| **5s** | 00.0–01.0 / 01.0–02.0 / 02.0–04.0 / 04.0–05.0 | Evite micro‑eventos redundantes |

**Nota:** mantenha **one‑take** e **focal fixa** mesmo em versões curtas.

---

## **4\) Padrões prontos — `motion` (inglês)**

### **4.1 Montagem mecânica (urbano/estúdio)**

*“00.0–02.0 establish and stabilize; 02.0–04.0 latches retract and panels slide; 04.0–06.5 core assembly locks with clean bearings; 06.5–08.0 hero hold with reflection shimmer”*

### **4.2 Scan óptico (tech)**

*“00.0–02.0 first optical sweep; 02.0–04.5 modular segments align; 04.5–06.8 magnetic locks confirm; 06.8–08.0 steady hero with crisp speculars”*

### **4.3 Aéreo com entrega (alto → aterragem → reveal)**

*“00.0–01.6 high pass; 01.6–02.0 quick release; 02.0–03.5 guided descent; 03.5–06.8 in‑place transformation; 06.8–08.0 centered hero”*

### **4.4 Natureza cinematográfica (glide)**

*“00.0–03.0 forward glide through atmosphere; 03.0–06.5 gentle arc with light beams; 06.5–08.0 slow climb and hero hold”*

---

## **5\) Padrões prontos — `timeline` (inglês)**

Use quando quiser granularidade por `sequence`.

\[  
  { "sequence": 1, "timestamp": "00:00-00:02", "action": "establish and stabilize" },  
  { "sequence": 2, "timestamp": "00:02-00:04.5", "action": "primary assembly with precise slides and locks" },  
  { "sequence": 3, "timestamp": "00:04.5-00:06.8", "action": "refinement and final alignment; reflections settle" },  
  { "sequence": 4, "timestamp": "00:06.8-00:08", "action": "clean hero hold" }  
\]

Para cenários com pivô rápido:

\[  
  { "sequence": 1, "timestamp": "00:00-00:01.6", "action": "high-angle read of the subject/context" },  
  { "sequence": 2, "timestamp": "00:01.6-00:02.0", "action": "controlled 0.4-second whip-tilt to mid-height" },  
  { "sequence": 3, "timestamp": "00:02.0-00:06.8", "action": "core action builds continuously without cuts" },  
  { "sequence": 4, "timestamp": "00:06.8-00:08.0", "action": "centered hero hold" }  
\]

---

## **6\) Mapa de áudio atrelado a tempo (inglês)**

Combine com os blocos acima.

* **Rápido/dinâmico (00.0–01.6 / 01.6–03.5 / 03.5–06.8 / 06.8–08.0):**

  * *“soundtrack: tight cinematic bed (continuous, no heavy drops)”*

  * SFX:

    * *“00.0–01.6 light room tone \+ approach detail”*

    * *“01.6–03.5 trigger SFX (release/pop/sweep)”*

    * *“03.5–06.8 mechanical slides, locks, air hiss”*

    * *“06.8–08.0 high‑frequency shimmer tail”*

* **Equilibrado:**

  * *“soundtrack: minimal tech bed (continuous)”*

  * SFX:

    * *“00.0–02.0 subtle servo ticks”*

    * *“02.0–04.5 scan sweep \+ bearing slides”*

    * *“04.5–06.8 magnetic lock clicks”*

    * *“06.8–08.0 calm shimmer tail”*

---

## **7\) Fechamento e loop**

* **Hero hold**: mantenha enquadramento **estável** nos últimos **0.3–0.5s**.

* **SFX final**: “**shimmer tail**” ou “**calm airy finish**” evita silêncio brusco.

* **Trilha**: base contínua até 8s; nada de “stingers” no último quadro.

---

## **8\) Snippets curtos (colar direto)**

**Motion — genérico (8s):**  
 *“00.0–02.0 establish; 02.0–04.5 assemble; 04.5–06.8 refine and lock; 06.8–08.0 hero hold”*

**Motion — com whip‑tilt:**  
 *“00.0–01.6 high read; 01.6–02.0 controlled 0.4‑second whip‑tilt; 02.0–06.8 continuous build; 06.8–08.0 centered hero hold”*

**Audio — genérico:**  
 *“soundtrack: minimal cinematic bed (continuous); sfx aligned to beats; mix: prioritize core action; avoid harsh transitions”*

---

## **9\) Validação rápida**

* Batidas somadas **≤ 8s**.

* Texto coerente com `camera` e `audio`.

* `hero hold` presente.

* Nada de *slow motion* não previsto.

* Sem solicitações de texto em tela (reforçar em `negative_prompts`).

---

