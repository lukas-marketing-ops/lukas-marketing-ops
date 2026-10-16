# Design-Skills – Übersicht & Aufruf in Claude

Alle bereits installierten Skills mit Design-Bezug, gruppiert nach Einsatzzweck.
**Aufruf:** In Claude (claude.ai, Desktop, Claude Code) einfach den Slash-Befehl tippen, z. B. `/canva:edit-design`, oder die Aufgabe in natürlicher Sprache beschreiben – Claude wählt den passenden Skill automatisch.

> Stand: 16.10.2026 · Quelle: installierte Plugins `adobe-for-creativity`, `canva`, `design`, `marketing` + Anthropic-Skills

---

## 1. Visuelle Assets erstellen (Präsentationen, Flyer, Social, Print)

| Slash-Befehl | Was er macht | B2B-Pharma-Use-Case | Benötigt |
|---|---|---|---|
| `/adobe-for-creativity:adobe-design-from-template` | Design aus Adobe-Express-Template: Flyer, Poster, Social Posts, Präsentationen, Visitenkarten, Einladungen | Event-Einladung Fachkongress, LinkedIn-Post zu Whitepaper | Adobe-Connector |
| `/adobe-for-creativity:adobe-design-to-pdf` | Template anpassen → druckfertiges PDF / Share-Link | One-Pager für Messe, Sales-Leave-Behind | Adobe-Connector |
| `/adobe-for-creativity:adobe-create-pdfs-from-data` | InDesign-Datenmerge: CSV + Template → personalisierte PDFs | Personalisierte Angebots-/Zertifikats-PDFs je Account | Adobe-Connector |
| `/canva:bulk-create` | Eine Canva-Designvorlage pro Datenzeile (CSV/Tabelle) | ABM: personalisierte Visuals pro Zielaccount | Canva-Connector |
| `/anthropic-skills:canvas-design` | Originale Poster/Visuals als PNG/PDF | Key-Visual für Thought-Leadership-Kampagne | – |
| `/anthropic-skills:carousel-builder` | LinkedIn/Instagram-Carousel: Slide-Copy, Cover-Lines, Caption | C-Level-Carousel zu Regulatory-Trends | – |
| `/anthropic-skills:pptx` | PowerPoint-Decks erstellen/bearbeiten | Pitch-Deck, QBR-Präsentation | – |

## 2. Bestehende Designs bearbeiten & anpassen

| Slash-Befehl | Was er macht | B2B-Pharma-Use-Case | Benötigt |
|---|---|---|---|
| `/canva:edit-design` | Texte, Bilder, Formatierung in Canva-Design ändern | Deck auf neuen Kunden umlabeln, übersetzen | Canva-Connector |
| `/canva:implement-feedback` | Kommentare von Reviewern lesen & umsetzen | MLR-/Legal-Feedback einarbeiten | Canva-Connector |
| `/canva:resize-for-social-media` | Ein Design → FB, IG, LinkedIn-Formate | Kampagnen-Visual für alle Kanäle | Canva-Connector |
| `/adobe-for-creativity:adobe-create-social-variations` | Bild/Video plattformgerecht zuschneiden | Webinar-Teaser für LinkedIn + YouTube | Adobe-Connector |
| `/adobe-for-creativity:adobe-resize-photos-and-videos` | Exakte Pixelmaße / Seitenverhältnisse | Banner für Fachportal-Werbeplätze | Adobe-Connector |
| `/adobe-for-creativity:adobe-batch-edit-photos` | Einheitlicher Look über viele Fotos | Event-Fotos konsistent aufbereiten | Adobe-Connector |
| `/adobe-for-creativity:adobe-retouch-portraits` | Portraits im Batch retuschieren | Team-/Expert-Headshots für Website | Adobe-Connector |
| `/adobe-for-creativity:adobe-edit-quick-cut` | Highlight-Cut aus Video | Kongress-/Webinar-Sizzle-Reel | Adobe-Connector |

## 3. Qualitätssicherung, Brand & Feedback

| Slash-Befehl | Was er macht | B2B-Pharma-Use-Case | Benötigt |
|---|---|---|---|
| `/canva:brand-check` | Design gegen Brand Kit prüfen (Farben, Fonts, Logo, Tonalität) | Agentur-Lieferungen vor Freigabe prüfen | Canva-Connector |
| `/canva:get-design-feedback` | Strukturiertes Design-Feedback (read-only) | Sales-Deck vor Kundentermin reviewen | Canva-Connector |
| `/design:design-critique` | Feedback zu Usability, Hierarchie, Konsistenz (Screenshot/Figma) | Landingpage-Entwurf kritisch prüfen | – (Figma optional) |
| `/design:accessibility-review` | WCAG-2.1-AA-Audit | Barrierefreiheit von Website/Portal | – |
| `/marketing:brand-review` | Content gegen Brand Voice & Guidelines prüfen | Tonalität C-Level-Content sicherstellen | – |
| `/adobe-for-creativity:adobe-document-review` | PDF smart highlighten (Risiken, Fristen, Zahlen) | Ausschreibungs-/RFP-Unterlagen sichten | Adobe-Connector |

## 4. Design-System, UX & Übergabe

| Slash-Befehl | Was er macht | B2B-Pharma-Use-Case | Benötigt |
|---|---|---|---|
| `/design:design-system` | Design-System auditieren, dokumentieren, erweitern | Corporate Design für Templates konsolidieren | – |
| `/design:design-handoff` | Dev-Handoff-Specs (Tokens, States, Breakpoints) | Briefing an Web-Agentur | – |
| `/design:ux-copy` | Microcopy, CTAs, Fehlermeldungen | CTA-Optimierung Demo-Request-Formular | – |
| `/design:user-research` | Research-Plan, Interviewleitfaden, Surveys | Buyer-Persona-Interviews mit Einkauf/QA | – |
| `/design:research-synthesis` | Research zu Insights & Empfehlungen verdichten | Win/Loss-Interviews auswerten | – |
| `/adobe-for-creativity:adobe-fonts` | Adobe Fonts finden, vergleichen, Vorschau | Schriftwahl für neue Content-Reihe | Adobe-Connector |

## 5. Hilfsfunktionen

| Slash-Befehl | Zweck |
|---|---|
| `/adobe-for-creativity:adobe` | Tour durch alle Adobe-Funktionen |
| `/adobe-for-creativity:adobe-anypdf` | PDF-Aufgaben (Komprimieren, Mergen, OCR, Konvertieren) |
| `/adobe-for-creativity:adobe-anypptx` | PDF → PowerPoint |
| `/pdf-viewer:annotate` · `/pdf-viewer:sign` | PDFs gemeinsam annotieren / signieren |

---

## Voraussetzungen

- **Canva-Skills** brauchen den verbundenen **Canva-Connector**, **Adobe-Skills** den **Adobe-for-creativity-Connector** (claude.ai → Einstellungen → Connectors).
- `/design:*` arbeitet ohne Connector; Figma, Notion, Slack etc. sind optionale Datenquellen.
- In **Claude-Code-Cloud-Sessions** blockiert die Netzwerk-Policy aktuell die Adobe-/Canva-/Figma-Server (403). Dort funktionieren nur die connector-freien Skills; für Canva/Adobe claude.ai oder die Desktop-App nutzen oder die Domains in der Environment-Netzwerkrichtlinie freigeben.

## Empfohlener Workflow (Content → Asset → Freigabe)

1. **Content:** `/marketing:draft-content` oder `/anthropic-skills:carousel-builder`
2. **Asset:** `/adobe-for-creativity:adobe-design-from-template` bzw. `/anthropic-skills:pptx`
3. **QA:** `/canva:brand-check` + `/design:accessibility-review`
4. **Ausspielung:** `/canva:resize-for-social-media` bzw. `/adobe-for-creativity:adobe-create-social-variations`

**Business-Impact:** Kürzere Time-to-Market für Kampagnen-Assets, konsistente Markenführung ohne Agentur-Schleifen, skalierbare Personalisierung (ABM) über Bulk-/Merge-Skills.
**KPI-Vorschlag:** Durchlaufzeit Briefing → freigegebenes Asset (Tage), Anzahl Korrekturschleifen pro Asset, Anteil Assets mit bestandenem Brand-Check.
