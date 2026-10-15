# Körber Slide Library 2026 – Pharma Consulting

## Standard deck (English, v2.0) – recommended

`Koerber_Slide_Library_2026_EN.pptx`: 184 content-neutral template slides in Körber 2025 CI (placeholders such as *Headline*, *[Name]* and *00%* instead of example content), 23 chapters in three parts – **winning the project** (basics, company introduction, customer situation, buying center, solution, business case, approach, proposal, references), **delivering the project** (kick-off, analysis, processes, target picture & roadmap, validation & compliance, implementation & change, project steering, workshops) and **growing the account & toolbox** (account management, frameworks, charts, closing, appendix, toolkit). Google Material Symbols as icons; every slide has English speaker notes (USE / ADAPT / TIP). Clickable contents on slide 3, storyline builder for 12 meeting types on slide 4. Preview: `Koerber_Slide_Library_2026_EN_Preview.pdf`. Rebuild: `cd generator && python3 build_en.py` (content in `en.py` … `en4.py`).

## Deutsche Fassung mit Beispielinhalten (v1.0)

Eine Folienbibliothek mit 150 Folien im Körber-CI für Kundentermine und Leadprojekte. Sie basiert auf dem offiziellen **Körber-2025-Master** (Layouts, Logo, Fußzeile, Klassifizierung) und ersetzt die v7-Vorlage.

| Datei | Inhalt |
|---|---|
| `Koerber_Slide_Library_2026.pptx` | Die Bibliothek, editierbar, mit 17 PowerPoint-Abschnitten |
| `Koerber_Slide_Library_2026_Vorschau.pdf` | PDF-Vorschau (LibreOffice-Rendering, Schrift kann minimal abweichen) |
| `generator/` | Python-Skripte, mit denen die Bibliothek erzeugt wird |

## Aufbau

| Kapitel | Folien | Zweck |
|---|---|---|
| 00 Einstieg | 1–5 | Nutzung, klickbares Inhaltsverzeichnis, Storyline-Baukasten, Storytelling-Regeln |
| 01 Titel & Agenda | 6–13 | Deckblätter, Agenda, Ziele, Teilnehmende |
| 02 Über uns | 14–25 | Portfolio, Kompetenzen, Ökosystem, Differenzierung, Team |
| 03 Markt & Kundenverständnis | 26–36 | Trends, SCR, Issue Tree, Hypothesen, Reifegrad, Benchmark |
| 04 Buying Center | 37–44 | Rollen, Stakeholder, Beziehungen, Nutzenargumente, Discovery-Fragen |
| 05 Lösung & Wert | 45–55 | Wertversprechen, Architektur, Module, Werttreiber, Optionen, Empfehlung |
| 06 Business Case | 56–62 | NPV, Cashflow, Wertbrücke, Kosten des Nichthandelns, Sensitivität, Szenarien |
| 07 Vorgehen & Plan | 63–74 | Phasen, Gantt, Meilensteine, Stage-Gate, Organisation, RACI, Governance |
| 08 Prozesse & Abläufe | 75–83 | Prozesslandkarte, Swimlane, SIPOC, Prozessschritt, Wertstrom, Soll-Prozess |
| 09 Referenzen | 84–91 | Case Studies, Referenzmatrix, Logos, Zitat |
| 10 Angebot | 92–100 | Scope, Pakete, Honorar, Zahlungsplan, Mutual Action Plan |
| 11 Projektsteuerung | 101–113 | Auftrag, OKR, Status, Steering Committee, Risiken, Entscheidung, Change Request |
| 12 Account-Management | 114–122 | Account-Plan, Whitespace, Pipeline, QBR, Health Score |
| 13 Frameworks | 123–130 | SWOT, Five Forces, Priorisierung, Wertkette, TAM/SAM/SOM, Ishikawa |
| 14 Diagramme | 131–138 | Native, editierbare Diagramme im Körber-Stil |
| 15 Abschluss | 139–145 | Kernaussagen, nächste Schritte, Kontakt, Disclaimer |
| 16 Toolkit | 146–150 | Raster, Farben, Bausteine, 117 Icons |

## Designregeln (für alle neuen Folien)

- **Action Title:** ein vollständiger Satz mit der Aussage, höchstens 76 Zeichen (24 pt, Master).
- **Tracker-Zeile:** „Kapitel | Thema“ im Untertitel-Platzhalter.
- **Raster:** Inhalt von 1,45" bis 5,80"; „So what“-Box immer bei 5,98"; Spaltenabstand 0,3".
- **Farbe:** Blau nur für die eine Hervorhebung, Warmgrau für Flächen und Vergleichswerte, Gelb nur für Call to Action, Amber und Orange nur für Status.
- **Sticker:** „Illustrativ“ / „Intern“ kennzeichnet Beispielwerte bzw. interne Folien – vor dem Kundentermin entfernen.
- **[Eckige Klammern]** sind Platzhalter.
- Jede Folie hat in den **Sprechernotizen** Hinweise zu Einsatz, Anpassung und einen Tipp.

## Neu generieren

```bash
pip install python-pptx lxml pillow
cd generator
KOERBER_TEMPLATE=/pfad/zu/Körber_2025.pptx python3 build.py Koerber_Slide_Library_2026.pptx
```

Inhalte werden in `build_a.py` (Kapitel 00–04), `build_b.py` (05–09) und `build_c.py` (10–16) gepflegt. Die Bausteine (Farben, Karten, Chevrons, Tabellen, Diagramme, Icons) liegen in `kh.py`. Inhaltsverzeichnis und Storyline-Baukasten werden mit den Foliennummern automatisch befüllt.
