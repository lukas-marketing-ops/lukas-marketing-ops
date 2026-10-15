from kh import *
from build_a import N, divider, person, IMG


# =====================================================================================
def s05(D):
    divider(D, 5, 'Lösung &\nWert', N('Wertversprechen, Lösungsarchitektur, Optionen und Empfehlung.',
                                       'Immer vom Kundennutzen her argumentieren, nicht von der Leistung.',
                                       'Kernlogik: Problem → Lösung → messbarer Nutzen → Empfehlung.'))
    s = D.slide('content', 'Unser Versprechen: Mehr Kapazität in kürzerer Zeit – ohne Compliance-Risiko',
                'Lösung & Wert | Wertversprechen', key='valueprop',
                notes=N('Kernbotschaft der Lösungspräsentation – eine Folie, die hängen bleibt.', 'Versprechen und Belege kundenspezifisch formulieren.',
                        'Der Satz links muss auch ohne Folie funktionieren – als Elevator Pitch.'))
    rect(s, L, 1.5, 5.6, 4.3, fill=BLUE)
    label(s, L + 0.35, 1.8, 5, 'Unser Versprechen', color=WHITE)
    text(s, L + 0.35, 2.15, 4.9, 3.0, 'Wir bringen Ihre neue Linie sechs Monate früher in die validierte Produktion – mit einem Team, das Planung, Umsetzung und Qualifizierung verantwortet.',
         size=22, color=WHITE)
    xr = 6.5; wr = R - xr
    pp = [('–6 Monate', 'Time-to-Market durch parallele Planung und Qualifizierung'),
          ('100 %', 'Annex-1-konformes Design von Anfang an'),
          ('1 Team', 'eine Verantwortung über alle Phasen – keine Übergabeverluste')]
    for i, (a, b) in enumerate(pp):
        y = 1.5 + i * 1.45
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.15, 2.6, 0.7, a, size=30, color=BLUE)
        text(s, xr + 2.8, y + 0.22, wr - 2.8, 0.9, b, size=14, anchor='t')

    s = D.slide('content', 'Value Proposition Canvas: Unsere Leistungen lösen die drei größten Pains',
                'Lösung & Wert | Value Proposition Canvas', key='vpc',
                notes=N('Strukturierte Herleitung des Wertversprechens (Workshop oder Angebot).', 'Kundenprofil aus Discovery füllen, dann Leistungen zuordnen.',
                        'Jeder Pain Reliever muss auf einen konkreten Pain zeigen – sonst streichen.'))
    cw = (W - 0.9) / 2
    for side, (lab, boxes, xs) in enumerate([('Unser Leistungsversprechen', [('Leistungen', ['Facility Design', 'CQV-Management', 'MES-Integration']),
                                                                              ('Pain Reliever', ['Parallelisierte Planung', 'Annex-1-Expertise', 'Ein Verantwortlicher']),
                                                                              ('Gain Creator', ['Benchmark-Wissen', 'Wiederverwendbare Templates', 'Befähigung Ihres Teams'])], L),
                                             ('Kundenprofil [Kunde]', [('Kundenaufgaben', ['Kapazität ausbauen', 'Inspektion bestehen', 'Budget einhalten']),
                                                                       ('Pains', ['Knappe interne Ressourcen', 'Unklare Anforderungen', 'Schnittstellen-Chaos']),
                                                                       ('Gains', ['Früherer Marktzugang', 'Planbare Kosten', 'Stabiler Betrieb'])], L + cw + 0.9)]):
        label(s, xs, 1.45, cw, lab, color=BLUE)
        for j, (h, b) in enumerate(boxes):
            bw = (cw - 0.4) / 3
            x = xs + j * (bw + 0.2)
            f = BLUE if (side == 0 and j == 1) or (side == 1 and j == 1) else LSAND
            c = WHITE if f == BLUE else BLACK
            rect(s, x, 1.8, bw, 3.95, fill=f)
            text(s, x + 0.2, 2.0, bw - 0.4, 0.4, h, size=15, color=c)
            text(s, x + 0.2, 2.5, bw - 0.4, 3.0, bl(b, sa=8), size=12, color=c)
    oval(s, L + cw + 0.15, 3.45, 0.6, fill=WHITE, line=BLUE, lw=1.5)
    icon(s, 'swap_horiz', L + cw + 0.27, 3.57, 0.36, BLUE)
    sowhat(s, 'Der Fit entsteht dort, wo unsere Pain Reliever die Pains des Kunden direkt adressieren (blau).')

    s = D.slide('content', 'Die Lösung verbindet fünf Ebenen zu einem integrierten Zielbild',
                'Lösung & Wert | Lösungsarchitektur', key='architecture',
                notes=N('Gesamtbild der Lösung – zeigt Vollständigkeit und Integration.', 'Module je Ebene an den Lösungsumfang anpassen; Projekt-Scope blau markieren.'))
    layers = [('Strategie & Governance', ['Kapazitätsstrategie', 'Investitionsplanung', 'Projekt-Governance']),
              ('Prozesse & Organisation', ['Soll-Prozesse', 'Rollen & Schichtmodell', 'Schulungskonzept']),
              ('Technologie & Anlagen', ['Isolator-Linie', 'Reinraum & HVAC', 'Medienversorgung']),
              ('Daten & Systeme', ['MES / eBR', 'LIMS-Schnittstelle', 'Datenplattform'])]
    lw_ = 2.9; x0 = L + lw_ + 0.15; mw = (R - 1.25 - x0 - 2 * 0.15) / 3
    for i, (h, mods) in enumerate(layers):
        y = 1.5 + i * 1.08
        rect(s, L, y, lw_, 0.92, fill=SAND, content=h, size=14, anchor='m', margin=(0.2, 0.05, 0.1, 0.05))
        for j, m in enumerate(mods):
            hi = (i, j) in [(1, 0), (2, 0), (3, 0)]
            rect(s, x0 + j * (mw + 0.15), y, mw, 0.92, fill=BLUE if hi else None, line=None if hi else STONE,
                 content=m, size=13, color=WHITE if hi else BLACK, anchor='m', align='c')
    tb = rect(s, R - 1.1, 1.5, 1.1, 4.16, fill=BLACK)
    t = text(s, 0, 0, 4.16, 0.5, 'Qualität & Compliance (GMP, Data Integrity)', size=13, color=WHITE, align='c', anchor='m')
    t.rotation = 270; t.left = I(R - 1.1 + 0.55 - 2.08); t.top = I(1.5 + 2.08 - 0.25)
    rect(s, L, 5.9, 0.22, 0.22, fill=BLUE); text(s, L + 0.32, 5.86, 4, 0.3, 'Im Projektumfang', size=11)
    rect(s, L + 2.4, 5.9, 0.22, 0.22, line=STONE); text(s, L + 2.72, 5.86, 4, 0.3, 'Optional / Folgeprojekt', size=11)

    s = D.slide('content', 'Vier Module – einzeln buchbar und aufeinander aufbauend',
                'Lösung & Wert | Leistungsmodule', key='modules',
                notes=N('Modularer Leistungsbaukasten – erleichtert den Einstieg mit kleinem Budget.', 'Dauer und Ergebnisse je Modul anpassen.',
                        'Land-and-Expand: Mit Modul 1 starten, Ergebnisse liefern, dann erweitern.'))
    mods = [('Modul 1', 'Assessment', '4–6 Wochen', ['Ist-Analyse und Benchmark', 'Potenzialbewertung', 'Priorisierte Roadmap'], 'Basis'),
            ('Modul 2', 'Konzept', '8–12 Wochen', ['Zielbild und Layout', 'URS und Lastenheft', 'Business Case'], 'Empfohlen'),
            ('Modul 3', 'Umsetzung', '9–18 Monate', ['Vergabe und Bauleitung', 'CQV und Validierung', 'Inbetriebnahme'], 'Empfohlen'),
            ('Modul 4', 'Befähigung', 'laufend', ['Schulung und Coaching', 'Hypercare', 'KPI-Monitoring'], 'Optional')]
    cw = (W - 3 * 0.3) / 4
    for i, (m, h, d, b, tag) in enumerate(mods):
        x = L + i * (cw + 0.3)
        f = BLUE if i == 1 else LSAND
        c = WHITE if f == BLUE else BLACK
        rect(s, x, 1.5, cw, 4.25, fill=f)
        label(s, x + 0.25, 1.75, cw - 0.5, m, color=WHITE if f == BLUE else BLUE)
        text(s, x + 0.25, 2.05, cw - 0.5, 0.45, h, size=22, color=c)
        text(s, x + 0.25, 2.6, cw - 0.5, 0.3, d, size=12, color=WHITE if f == BLUE else DGRAY)
        hline(s, x + 0.25, 3.05, cw - 0.5, WHITE if f == BLUE else STONE, 0.75)
        text(s, x + 0.25, 3.2, cw - 0.5, 1.6, bl(b, sa=6), size=12, color=c)
        rrect(s, x + 0.25, 5.1, 1.35, 0.32, fill=WHITE if f == BLUE else None, line=None if f == BLUE else BLUE, radius=0.16,
              content=tag, size=10, color=BLUE, align='c', anchor='m', margin=0)
        if i < 3:
            icon(s, 'arrow_forward', x + cw + 0.04, 3.45, 0.22, TAUPE)
    sowhat(s, 'Modul 1 liefert in sechs Wochen eine belastbare Entscheidungsgrundlage – bei überschaubarem Budget.')

    s = D.slide('content', 'Werttreiberbaum: Drei Hebel liefern € 4,1 Mio. Ergebnisbeitrag pro Jahr',
                'Lösung & Wert | Werttreiberbaum', 'Quelle: Analyse [Kunde]; Werte illustrativ', key='valuetree', sticker_='Illustrativ',
                notes=N('Übersetzt operative Hebel in finanzielle Wirkung – für CFO und Geschäftsführung.', 'Werte aus dem Business Case übernehmen; Summen prüfen.',
                        'Jeder Blattknoten braucht einen messbaren KPI und einen Owner beim Kunden.'))
    shape(s, SH.RECTANGLE, L, 3.05, 2.4, 1.2, fill=BLUE, content=[{'t': 'EBIT-Effekt p. a.', 'size': 12}, {'t': '€ 4,1 Mio.', 'size': 22}], color=WHITE, anchor='m')
    drv = [('Umsatz', '€ 2,4 Mio.', [('Zusätzliche Kapazität', '+18 % Ausbringung', '€ 1,8 Mio.'), ('Früherer Marktzugang', '–6 Monate', '€ 0,6 Mio.')]),
           ('Kosten', '€ 1,2 Mio.', [('Weniger Ausschuss', '–1,5 pp', '€ 0,7 Mio.'), ('Kürzere Freigabe', '–40 % Durchlaufzeit', '€ 0,5 Mio.')]),
           ('Kapital', '€ 0,5 Mio.', [('Geringerer Bestand', '–12 Tage Reichweite', '€ 0,5 Mio.')])]
    ys = [1.45, 3.15, 4.85]
    for i, (d, v, leaves) in enumerate(drv):
        y = ys[i]
        arrow(s, L + 2.4, 3.65, L + 3.0, y + 0.45, color=STONE)
        shape(s, SH.RECTANGLE, L + 3.0, y + 0.1, 2.4, 0.75, fill=SAND, content=[{'t': d, 'size': 13}, {'t': v, 'size': 15, 'color': BLUE}], anchor='m')
        for j, (lt, k, e) in enumerate(leaves):
            yy = y + j * 0.82 - (0.0 if len(leaves) > 1 else -0.1)
            arrow(s, L + 5.4, y + 0.47, L + 6.0, yy + 0.33, color=STONE)
            shape(s, SH.RECTANGLE, L + 6.0, yy, 3.4, 0.66, line=STONE, content=lt, size=13, anchor='m')
            text(s, L + 9.6, yy, 1.6, 0.66, k, size=12, anchor='m', color=DGRAY)
            text(s, L + 11.2, yy, 1.4, 0.66, e, size=14, anchor='m', color=BLUE, align='r')
    label(s, L + 9.6, 1.15, 1.6, 'KPI', color=DGRAY); label(s, L + 11.2, 1.15, 1.4, 'Effekt p. a.', color=DGRAY, align='r')

    s = D.slide('content', 'Der Nutzen ist messbar: Vier KPIs belegen den Projekterfolg',
                'Lösung & Wert | Nutzen und Tracking', 'Werte illustrativ; Zielwerte mit [Kunde] abstimmen', key='kpis', sticker_='Illustrativ',
                notes=N('Verbindet Nutzenversprechen mit einer Messlogik – Grundlage für Erfolgsmessung und Referenz.',
                        'KPIs, Baseline und Messmethode mit dem Kunden vereinbaren.',
                        'Ohne Baseline kein Nachweis: Baseline vor Projektstart messen und dokumentieren.'))
    k = [('+12 pp', 'OEE Linie 3', '54 % → 66 %', 'MES-Auswertung, monatlich'),
         ('–40 %', 'Freigabe-Durchlaufzeit', '18 → 11 Tage', 'QA-Tracking, je Charge'),
         ('–6 Mon.', 'Time-to-Market', 'Go-live Q3 statt Q1', 'Meilensteinplan'),
         ('€ 4,1 Mio.', 'EBIT-Effekt p. a.', 'ab Jahr 2', 'Controlling, quartalsweise')]
    cw = (W - 3 * 0.3) / 4
    for i, (a, b, c, m) in enumerate(k):
        x = L + i * (cw + 0.3)
        rect(s, x, 1.5, cw, 2.6, fill=BLUE if i == 3 else LSAND)
        col = WHITE if i == 3 else BLUE
        text(s, x + 0.25, 1.75, cw - 0.5, 0.8, a, size=34, color=col)
        text(s, x + 0.25, 2.65, cw - 0.5, 0.35, b, size=15, color=WHITE if i == 3 else BLACK)
        text(s, x + 0.25, 3.05, cw - 0.5, 0.35, c, size=12, color=WHITE if i == 3 else DGRAY)
        label(s, x, 4.35, cw, 'Messung', color=DGRAY)
        hline(s, x, 4.65, cw, STONE, 0.5)
        text(s, x, 4.75, cw, 0.6, m, size=12)
    sowhat(s, 'Die vier KPIs werden ab Projektstart im Steering Committee berichtet – Erfolg wird so für alle sichtbar.')

    s = D.slide('content', 'Vom papierbasierten Betrieb zur integrierten, datengestützten Produktion',
                'Lösung & Wert | Ist und Soll', key='asis_tobe',
                notes=N('Vorher-Nachher-Vergleich für Lösungs- oder Abschlusspräsentation.', 'Dimensionen und Aussagen anpassen; maximal fünf Zeilen.'))
    dims = [('Dokumentation', 'Papierchargenprotokolle, manuelle Prüfung', 'Elektronischer Batch Record, Review by Exception'),
            ('Rüsten', 'Ø 7 Stunden, abhängig von Einzelpersonen', 'Standardisiert, Ø 3 Stunden, SMED-Methodik'),
            ('Freigabe', 'Ø 18 Tage, sequenziell', 'Ø 11 Tage, parallelisiert'),
            ('Daten', 'Insellösungen, Excel-Auswertungen', 'Integrierte Plattform, Echtzeit-KPIs'),
            ('Compliance', 'Reaktiv nach Inspektionen', 'Proaktiv, Contamination Control Strategy')]
    label(s, L + 2.3, 1.45, 4.5, 'Heute', color=DGRAY); label(s, L + 7.3, 1.45, 5.0, 'Zielbild [Jahr]', color=BLUE)
    for i, (d, a, b) in enumerate(dims):
        y = 1.8 + i * 0.8
        text(s, L, y, 2.2, 0.68, d, size=14, anchor='m')
        rect(s, L + 2.3, y, 4.5, 0.68, fill=LSAND, content=a, size=12, anchor='m', margin=(0.15, 0.03, 0.1, 0.03))
        icon(s, 'arrow_forward', L + 6.92, y + 0.22, 0.25, BLUE)
        rect(s, L + 7.3, y, R - L - 7.3, 0.68, fill=BLUE, content=b, size=12, color=WHITE, anchor='m', margin=(0.15, 0.03, 0.1, 0.03))

    s = D.slide('content', 'Drei Optionen – Option B bietet das beste Verhältnis von Nutzen und Risiko',
                'Lösung & Wert | Optionen', 'Werte illustrativ', key='options', sticker_='Illustrativ',
                notes=N('Optionsvergleich vor der Empfehlung – zeigt, dass Alternativen geprüft wurden.', 'Optionen und Kennzahlen anpassen; empfohlene Option blau.',
                        'Immer mindestens drei Optionen zeigen – inklusive „Nichts tun“ oder Minimallösung.'))
    opts = [('Option A', 'Ertüchtigung Bestandslinie', ['Investition € 6 Mio.', 'Kapazität +15 %', 'Umsetzung 9 Monate'], 'Geringe Investition, aber Lücke ab [Jahr] bleibt'),
            ('Option B', 'Neue Isolator-Linie + Ertüchtigung', ['Investition € 18 Mio.', 'Kapazität +60 %', 'Umsetzung 20 Monate'], 'Schließt Lücke dauerhaft, gestaffeltes Risiko'),
            ('Option C', 'Externe Fertigung (CDMO)', ['Keine CAPEX', 'Kapazität flexibel', 'Transfer 12 Monate'], 'Abhängigkeit und höhere Stückkosten')]
    cw = (W - 2 * 0.3) / 3
    for i, (o, h, b, v) in enumerate(opts):
        x = L + i * (cw + 0.3)
        hi = i == 1
        f = BLUE if hi else LSAND; c = WHITE if hi else BLACK
        rect(s, x, 1.5, cw, 4.3, fill=f)
        label(s, x + 0.3, 1.75, cw - 0.6, 'Empfohlen' if hi else o, color=WHITE if hi else BLUE)
        text(s, x + 0.3, 2.05, cw - 0.6, 0.4, o, size=22, color=c)
        text(s, x + 0.3, 2.55, cw - 0.6, 0.6, h, size=14, color=c)
        hline(s, x + 0.3, 3.25, cw - 0.6, WHITE if hi else STONE, 0.75)
        text(s, x + 0.3, 3.4, cw - 0.6, 1.2, bl(b, sa=6), size=13, color=c)
        text(s, x + 0.3, 4.85, cw - 0.6, 0.8, v, size=12, color=c, italic=True)

    s = D.slide('content', 'Option B erfüllt fünf von sechs Kriterien am besten',
                'Lösung & Wert | Bewertungsmatrix', 'Bewertung: Workshop mit [Kunde], [Datum]', key='evaluation',
                notes=N('Transparente, gewichtete Bewertung der Optionen.', 'Kriterien und Gewichte vorab mit dem Kunden abstimmen; Harvey Balls 0–4.',
                        'Gewichte vor der Bewertung festlegen – sonst wirkt die Matrix konstruiert.'))
    crit = [('Strategischer Fit', '25 %', [2, 4, 2]), ('Investition', '20 %', [4, 2, 4]), ('Time-to-Market', '20 %', [3, 3, 2]),
            ('Umsetzungsrisiko', '15 %', [3, 3, 1]), ('Skalierbarkeit', '10 %', [1, 4, 3]), ('Compliance', '10 %', [2, 4, 3])]
    x0 = L + 4.2; cw = 2.4
    for j, o in enumerate(['Option A', 'Option B', 'Option C']):
        if j == 1:
            rect(s, x0 + j * cw, 1.4, cw, 4.45, fill=LBLUE)
        text(s, x0 + j * cw, 1.5, cw, 0.3, o, size=14, color=BLUE, align='c')
    text(s, L + 2.9, 1.5, 1.2, 0.3, 'Gewicht', size=12, color=DGRAY, align='c')
    hline(s, L, 1.9, W, BLACK, 1)
    for i, (c, wgt, sc) in enumerate(crit):
        y = 2.0 + i * 0.55
        text(s, L, y, 2.8, 0.5, c, size=13, anchor='m')
        text(s, L + 2.9, y, 1.2, 0.5, wgt, size=13, anchor='m', align='c', color=DGRAY)
        for j, q in enumerate(sc):
            harvey(s, x0 + j * cw + cw / 2 - 0.17, y + 0.08, 0.34, q)
        hline(s, L, y + 0.53, W, STONE, 0.5)
    y = 2.0 + 6 * 0.55 + 0.08
    text(s, L, y, 2.8, 0.45, 'Gewichteter Score', size=14, anchor='m')
    for j, v in enumerate(['2,7', '3,3', '2,5']):
        text(s, x0 + j * cw, y, cw, 0.45, v, size=18, align='c', anchor='m', color=BLUE if j == 1 else BLACK)

    s = D.slide('content', 'Wir empfehlen Option B und bitten um Freigabe der Phase 1',
                'Lösung & Wert | Empfehlung', key='recommendation',
                notes=N('Abschluss der Lösungsargumentation mit klarer Bitte (Call to Action).', 'Entscheidung, Budget und Termin konkret benennen.',
                        'Die Bitte gehört in den Titel – Entscheider sollen wissen, was von ihnen erwartet wird.'))
    rect(s, L, 1.5, 5.6, 4.3, fill=BLUE)
    label(s, L + 0.35, 1.8, 5, 'Unsere Empfehlung', color=WHITE)
    text(s, L + 0.35, 2.15, 4.9, 2.2, 'Option B umsetzen und Phase 1 (Konzept, € [xxx] Tsd.) bis [Datum] freigeben.', size=22, color=WHITE)
    rrect(s, L + 0.35, 4.95, 3.3, 0.48, fill=YELLOW, radius=0.24, content='Entscheidung bis [TT.MM.JJJJ]', size=13, color=BLACK, align='c', anchor='m', margin=0)
    xr = 6.5; wr = R - xr
    label(s, xr, 1.5, wr, 'Warum wir das empfehlen')
    rs = [('Schließt die Kapazitätslücke dauerhaft', '+60 % Kapazität ab [Jahr], skalierbar für Biologika'),
          ('Wirtschaftlich überzeugend', 'Payback 2,8 Jahre, Kapitalwert € 4,8 Mio.'),
          ('Risiko beherrschbar', 'Gestaffelte Umsetzung mit Entscheidungsgates nach jeder Phase')]
    for i, (h, b) in enumerate(rs):
        y = 1.9 + i * 1.25
        icon(s, 'check_circle', xr, y, 0.42, BLUE)
        text(s, xr + 0.6, y, wr - 0.6, 0.35, h, size=16)
        text(s, xr + 0.6, y + 0.4, wr - 0.6, 0.6, b, size=13, color=DGRAY)


# =====================================================================================
def s06(D):
    divider(D, 6, 'Business\nCase', N('Wirtschaftlichkeit: Kapitalwert, Payback, Sensitivitäten, Szenarien.',
                                        'Zahlen mit dem Controlling des Kunden validieren.',
                                        'Business Case gemeinsam mit dem Kunden rechnen – dann verteidigt er ihn intern selbst.'))
    s = D.slide('content', 'Die Investition amortisiert sich in 2,8 Jahren',
                'Business Case | Zusammenfassung', 'Quelle: Business-Case-Modell [Version]; Werte illustrativ', key='bc_summary', sticker_='Illustrativ',
                notes=N('One-Pager für die Investitionsentscheidung.', 'Zahlen aus dem Excel-Modell übernehmen.'))
    cw = (W - 0.5) / 2
    for side, (lab, rows, tot) in enumerate([('Investition (einmalig)', [('Anlagen und Technik', '€ 11,2 Mio.'), ('Bau und Reinraum', '€ 4,1 Mio.'),
                                                                          ('Engineering und CQV', '€ 2,7 Mio.')], '€ 18,0 Mio.'),
                                             ('Nutzen (p. a. ab Jahr 2)', [('Zusätzlicher Deckungsbeitrag', '€ 4,9 Mio.'), ('Kosteneinsparungen', '€ 1,2 Mio.'),
                                                                           ('Kapitalbindung', '€ 0,5 Mio.')], '€ 6,6 Mio.')]):
        x = L + side * (cw + 0.5)
        label(s, x, 1.5, cw, lab, color=BLUE)
        hline(s, x, 1.82, cw, BLACK)
        for i, (a, b) in enumerate(rows):
            y = 1.9 + i * 0.45
            text(s, x, y, cw - 1.6, 0.4, a, size=13, anchor='m'); text(s, x + cw - 1.6, y, 1.6, 0.4, b, size=13, anchor='m', align='r')
            hline(s, x, y + 0.43, cw, STONE, 0.5)
        y = 1.9 + 3 * 0.45 + 0.05
        text(s, x, y, cw - 1.6, 0.4, 'Summe', size=14, anchor='m'); text(s, x + cw - 1.6, y, 1.6, 0.4, tot, size=14, anchor='m', align='r', color=BLUE)
    k = [('€ 4,8 Mio.', 'Kapitalwert (NPV, 8 % WACC)'), ('2,8 Jahre', 'Amortisationsdauer'), ('24 %', 'Interner Zinsfuß (IRR)')]
    cw3 = (W - 2 * 0.3) / 3
    for i, (a, b) in enumerate(k):
        x = L + i * (cw3 + 0.3)
        rect(s, x, 3.95, cw3, 1.85, fill=BLUE if i == 0 else LSAND)
        text(s, x + 0.3, 4.15, cw3 - 0.6, 0.8, a, size=34, color=WHITE if i == 0 else BLUE)
        text(s, x + 0.3, 5.05, cw3 - 0.6, 0.4, b, size=13, color=WHITE if i == 0 else BLACK)

    s = D.slide('content', 'Ab dem dritten Jahr ist der kumulierte Cashflow positiv',
                'Business Case | Cashflow-Verlauf', 'Quelle: Business-Case-Modell; € Mio.; Werte illustrativ', key='bc_cashflow', sticker_='Illustrativ',
                notes=N('Visualisiert Investitionsphase und Break-even.', 'Diagramm per Rechtsklick > „Daten bearbeiten“ anpassen; negative Werte grau.'))
    vals = [-6.0, -14.5, -10.8, -4.2, 2.4, 9.0, 15.6]
    bar(s, L, 1.4, 8.3, 4.4, ['2026', '2027', '2028', '2029', '2030', '2031', '2032'], [('Kumulierter Cashflow', vals)],
        fmt='0.0', point_colors=[STONE if v < 0 else BLUE for v in vals], gap=50, size=12).category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    xr = 9.2; wr = R - xr
    kpi(s, xr, 1.6, wr, '€ –14,5 Mio.', 'Maximaler Mittelbedarf (2027)', bigsize=28)
    kpi(s, xr, 3.2, wr, 'Q3 2029', 'Break-even (kumuliert)', bigsize=28)
    sowhat(s, 'Der Mittelbedarf ist auf zwei Jahre begrenzt – ab 2029 finanziert sich die Linie selbst.')

    s = D.slide('content', 'Vom Nutzen zum Kapitalwert: Mehr Kapazität trägt 55 % des Bruttonutzens',
                'Business Case | Wertbrücke', 'Quelle: Business-Case-Modell; Barwerte in € Mio.; Werte illustrativ', key='bc_waterfall', sticker_='Illustrativ',
                notes=N('Wasserfall zeigt, woher der Wert kommt.', 'Werte in der Tabelle des Diagramms anpassen: Spalten „Summe“, „Zunahme“, „Abnahme“; „Basis“ bleibt unsichtbar.',
                        'Einfacher: Werte im Skript ändern und neu generieren (siehe Toolkit).'))
    waterfall(s, L, 1.4, W, 4.4, ['Kapazität', 'Time-to-Market', 'Kosten', 'Kapital', 'Bruttonutzen', 'Betriebskosten', 'Investition', 'Kapitalwert'],
              [14.2, 3.6, 5.8, 2.1, 25.7, -2.9, -18.0, 4.8], totals=[4, 7], size=12, colors=[None, BLUE, STONE, BLACK])
    sowhat(s, 'Der Kapazitätsgewinn allein deckt fast 80 % der Investition – die übrigen Hebel machen den Case robust.')

    s = D.slide('content', 'Jeder Monat Verzögerung kostet rund € 0,6 Mio. Deckungsbeitrag',
                'Business Case | Kosten des Nichthandelns', 'Quelle: Business-Case-Modell; Werte illustrativ', key='costofdelay', sticker_='Illustrativ',
                notes=N('Erzeugt Dringlichkeit – stärkstes Argument gegen „Wir warten noch“.', 'Monatlichen Deckungsbeitrag aus dem Modell einsetzen.',
                        'Gegen Ende der Präsentation zeigen, direkt vor der Entscheidungsbitte.'))
    bar(s, L, 1.4, 7.6, 4.4, ['3 Monate', '6 Monate', '9 Monate', '12 Monate'], [('Entgangener Deckungsbeitrag', [1.8, 3.6, 5.4, 7.2])],
        fmt='"€ "0.0" Mio."', highlight=[3], gap=60, size=12)
    disturber(s, 9.4, 1.8, [{'t': '€ 0,6 Mio.', 'size': 24}, {'t': 'pro Monat Verzögerung', 'size': 12}], d=2.6)
    text(s, 8.7, 4.7, 4.2, 1.0, 'Hinzu kommen Vertragsstrafen und Marktanteilsverluste, die hier nicht quantifiziert sind.', size=12, color=DGRAY)
    sowhat(s, 'Nicht zu entscheiden ist auch eine Entscheidung – mit dem höchsten Preis.')

    s = D.slide('content', 'Der Business Case bleibt auch bei ungünstigen Annahmen positiv',
                'Business Case | Sensitivitätsanalyse', 'Quelle: Business-Case-Modell; Kapitalwert in € Mio., Basis 4,8; Werte illustrativ', key='tornado', sticker_='Illustrativ',
                notes=N('Tornado-Diagramm: Welche Annahme bewegt das Ergebnis am stärksten?', 'Spannweiten (±) je Treiber im Modell berechnen und eintragen.',
                        'Die zwei größten Balken sind die Annahmen, die gemeinsam mit dem Kunden validiert werden müssen.'))
    cats = ['Absatzmenge ±20 %', 'Preis ±10 %', 'Investition ±15 %', 'Ramp-up ±3 Monate', 'Betriebskosten ±10 %']
    ch = bar(s, L, 1.4, 8.4, 4.4, cats, [('Negativ', [-4.1, -2.9, -2.4, -1.6, -0.9]), ('Positiv', [4.1, 2.9, 2.4, 1.2, 0.9])],
             kind='bar', fmt='+0.0;-0.0', colors=[STONE, BLUE], overlap=100, gap=40, size=12, legend='b')
    ch.category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
    xr = 9.3; wr = R - xr
    label(s, xr, 1.5, wr, 'Lesart')
    text(s, xr, 1.85, wr, 3.5, bl(['Selbst bei –20 % Absatz bleibt der Kapitalwert positiv (€ 0,7 Mio.)',
                                   'Absatz und Preis sind die kritischen Annahmen',
                                   'Beide werden mit Vertrieb und Marketing von [Kunde] validiert'], sa=10), size=13)

    s = D.slide('content', 'Drei Szenarien: Kapitalwert zwischen € 0,9 und 8,1 Mio.',
                'Business Case | Szenarien', 'Quelle: Business-Case-Modell; Werte illustrativ', key='scenarios', sticker_='Illustrativ',
                notes=N('Szenarioanalyse für die Investitionsentscheidung.', 'Annahmen je Szenario dokumentieren und mit dem Kunden abstimmen.'))
    rows = [['Annahme', 'Konservativ', 'Basis', 'Optimistisch'],
            ['Absatzwachstum p. a.', '4 %', '7 %', '10 %'],
            ['Auslastung im Zieljahr', '65 %', '78 %', '85 %'],
            ['Ramp-up-Dauer', '12 Monate', '9 Monate', '6 Monate'],
            ['Investition', '€ 20,7 Mio.', '€ 18,0 Mio.', '€ 17,1 Mio.'],
            [('Kapitalwert (NPV)', {'bold': False}), ('€ 0,9 Mio.', {'size': 16}), ('€ 4,8 Mio.', {'size': 16, 'color': WHITE, 'fill': BLUE}), ('€ 8,1 Mio.', {'size': 16})],
            ['Payback', '4,6 Jahre', '2,8 Jahre', '2,1 Jahre']]
    table(s, L, 1.5, W, rows, colw=[4, 2.8, 2.8, 2.8], rowh=0.55, size=13, aligns=['l', 'c', 'c', 'c'], fills={(r, 2): LBLUE for r in range(1, 7) if r != 5})
    sowhat(s, 'Auch im konservativen Szenario ist der Kapitalwert positiv – das Risiko liegt im Timing, nicht im Grundsatz.')


# =====================================================================================
def s07(D):
    divider(D, 7, 'Vorgehen\n& Plan', N('Projektvorgehen, Zeitplan, Organisation, Governance.',
                                          'Phasen, Termine und Rollen projektspezifisch anpassen.',
                                          'Das Vorgehen zeigt, dass wir das Projekt beherrschen – konkret statt generisch.'))
    s = D.slide('content', 'In fünf Phasen von der Analyse zur validierten Anlage',
                'Vorgehen & Plan | Phasenmodell', key='phases',
                notes=N('Überblick über das Projektvorgehen.', 'Phasen, Dauer und Ergebnisse anpassen.',
                        'Ergebnisse als Substantive formulieren („Freigegebenes Basic Design“) – sie sind die Basis für Zahlungsmeilensteine.'))
    ph = ['Analyse', 'Konzept', 'Engineering', 'Realisierung', 'Qualifizierung']
    chevrons(s, ph, L + 1.8, 1.45, W - 1.8, 0.6, size=13)
    rows = [('Dauer', ['6 Wochen', '3 Monate', '5 Monate', '8 Monate', '4 Monate']),
            ('Leitfrage', ['Wo stehen wir, was ist möglich?', 'Wie sieht die Lösung aus?', 'Wie bauen wir sie?', 'Wie setzen wir um?', 'Funktioniert alles GMP-konform?']),
            ('Ergebnis', ['Potenzialanalyse, Roadmap', 'Zielbild, URS, Business Case', 'Basic & Detail Design', 'Installierte Anlage', 'Qualifizierte Anlage, Freigabe'])]
    cw = (W - 1.8 - 4 * 0.06) / 5
    hts = [0.5, 1.2, 1.2]
    y = 2.2
    for j, (lab, vals) in enumerate(rows):
        hline(s, L, y, W, STONE, 0.5)
        label(s, L, y + 0.12, 1.7, lab, color=BLUE if j == 2 else DGRAY)
        for i, v in enumerate(vals):
            x = L + 1.8 + i * (cw + 0.06)
            if j == 2:
                rect(s, x, y + 0.08, cw, hts[j] - 0.16, fill=LSAND)
            text(s, x + 0.12, y + 0.08, cw - 0.24, hts[j] - 0.16, v, size=13, anchor='m' if j != 1 else 't')
        y += hts[j]
    sowhat(s, 'Jede Phase endet mit einem freigegebenen Ergebnis – Sie behalten jederzeit die Kontrolle über Budget und Umfang.')

    s = D.slide('content', 'Phase 1 Analyse: In sechs Wochen zur belastbaren Entscheidungsgrundlage',
                'Vorgehen & Plan | Phasendetail', key='phasedetail',
                notes=N('Detaillierung einer Phase – für Angebot oder Kick-off.', 'Für jede Phase duplizieren; Phase im Chevron oben markieren.'))
    chevrons(s, ['Analyse', 'Konzept', 'Engineering', 'Realisierung', 'Qualifizierung'], L, 1.45, W, 0.45, active=0, size=11)
    cols = [('Ziele', 'target', ['Transparenz über Ist-Zustand', 'Quantifiziertes Potenzial', 'Priorisierte Handlungsfelder']),
            ('Aktivitäten', 'checklist', ['Interviews (8–10)', 'Datenanalyse 12 Monate', 'Vor-Ort-Begehung', 'Benchmark-Abgleich']),
            ('Ergebnisse', 'description', ['Analysebericht', 'Potenzial in € und KPIs', 'Roadmap mit Quick Wins']),
            ('Ihre Mitwirkung', 'groups', ['Ansprechpartner je Bereich', 'Datenbereitstellung', '2 Workshops à 3 h'])]
    cw = (W - 3 * 0.3) / 4
    for i, (h, ic, b) in enumerate(cols):
        x = L + i * (cw + 0.3)
        colhead(s, x, 2.2, cw, None, h, bl(b, sa=6), icon_=ic, hsize=18, bsize=13, bh=2.0)
    rect(s, L, 5.25, W, 0.55, fill=LSAND)
    text(s, L + 0.25, 5.25, W - 0.5, 0.55, [{'t': [('Dauer  ', {'color': BLUE}), ('6 Wochen    ', {}), ('Team  ', {'color': BLUE}), ('2 Berater, 1 Experte    ', {}),
                                                    ('Gate  ', {'color': BLUE}), ('Steering Committee am [Datum]', {})]}], size=13, anchor='m')

    s = D.slide('content', 'Projektplan: Go-live der neuen Linie im September 2027',
                'Vorgehen & Plan | Gantt', 'Stand: [Datum]', key='gantt',
                notes=N('Zeitplan auf Monatsebene für Angebot, Kick-off und Steering Committee.', 'Balken per Drag & Drop verschieben; kritischer Pfad blau.',
                        'Maximal 10–12 Zeilen; Details gehören in den Projektplan, nicht auf die Folie.'))
    months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    text(s, L + 3.0, 1.38, 9.6, 0.25, '2027', size=11, color=BLUE)
    rows = [('Analyse', 0, 1.5, 'hl'), ('Konzept & URS', 1.5, 3.5, 'hl'), ('Gate: Investitionsfreigabe', 3.5, 0, 'ms'),
            ('Basic & Detail Design', 3.5, 6.5, 'hl'), ('Vergabe & Lieferung', 5, 8, 'bar'), ('Installation', 7, 9, 'hl'),
            ('IQ / OQ', 8.5, 10, 'hl'), ('Go-live', 8.75, 0, 'ms'), ('PQ & Prozessvalidierung', 9.5, 11.5, 'bar'), ('Schulung & Hypercare', 9, 12, 'bar')]
    gantt(s, L, 1.6, W, rows, months, lab_w=3.0, rowh=0.41)
    rect(s, L, 6.25, 0.3, 0.16, fill=BLUE); text(s, L + 0.4, 6.2, 2, 0.25, 'Kritischer Pfad', size=10)
    rect(s, L + 2.0, 6.25, 0.3, 0.16, fill=STONE); text(s, L + 2.4, 6.2, 2, 0.25, 'Weitere Aktivitäten', size=10)
    shape(s, SH.DIAMOND, L + 4.3, 6.21, 0.22, 0.22, fill=BLACK); text(s, L + 4.62, 6.2, 2, 0.25, 'Meilenstein', size=10)

    s = D.slide('content', 'Sechs Meilensteine markieren den Weg zur Marktfreigabe',
                'Vorgehen & Plan | Meilensteine', key='milestones',
                notes=N('Meilenstein-Zeitstrahl für Management-Präsentationen.', 'Termine und Beschreibungen anpassen; erreichte Meilensteine gefüllt.'))
    ms = [('Q4 2026', 'Projektstart', 'Kick-off und Analyse'), ('Q1 2027', 'Investitionsfreigabe', 'Business Case genehmigt'),
          ('Q2 2027', 'Design Freeze', 'Detail Design freigegeben'), ('Q3 2027', 'Installation', 'Mechanical Completion'),
          ('Q4 2027', 'Go-live', 'Erste GMP-Charge'), ('Q1 2028', 'Marktfreigabe', 'Behördliche Zulassung')]
    y0 = 3.55; cw = W / 6
    hline(s, L, y0, W, BLACK, 1.25)
    for i, (d, h, b) in enumerate(ms):
        x = L + i * cw
        done = i < 2
        oval(s, x + 0.02, y0 - 0.15, 0.3, fill=BLUE if done else WHITE, line=BLUE, lw=1.75)
        up = i % 2 == 0
        if up:
            text(s, x, 1.65, cw - 0.15, 0.45, d, size=22, color=BLUE)
            text(s, x, 2.2, cw - 0.15, 0.35, h, size=14)
            text(s, x, 2.55, cw - 0.15, 0.6, b, size=12, color=DGRAY)
        else:
            text(s, x, 3.9, cw - 0.15, 0.45, d, size=22, color=BLUE)
            text(s, x, 4.45, cw - 0.15, 0.35, h, size=14)
            text(s, x, 4.8, cw - 0.15, 0.6, b, size=12, color=DGRAY)
    dot(s, L, 6.27, 0.18, BLUE); text(s, L + 0.28, 6.22, 1.5, 0.3, 'Erreicht', size=10)
    oval(s, L + 1.3, 6.27, 0.18, fill=WHITE, line=BLUE, lw=1.5); text(s, L + 1.58, 6.22, 1.5, 0.3, 'Geplant', size=10)

    s = D.slide('content', 'Nach jeder Phase entscheidet ein Gate über das weitere Vorgehen',
                'Vorgehen & Plan | Stage-Gate', key='stagegate',
                notes=N('Zeigt Risikobegrenzung durch Entscheidungspunkte – überzeugt CFO und Einkauf.', 'Gate-Kriterien projektspezifisch festlegen.'))
    phs = ['Analyse', 'Konzept', 'Engineering', 'Realisierung']
    gates = [('Gate 1', ['Potenzial > € 2 Mio.', 'Sponsor bestätigt']), ('Gate 2', ['Business Case positiv', 'CAPEX genehmigt']),
             ('Gate 3', ['Design Freeze', 'Budget ±10 %']), ('Gate 4', ['IQ/OQ bestanden', 'Freigabe QA'])]
    pw = (W - 4 * 0.55) / 4
    for i, p in enumerate(phs):
        x = L + i * (pw + 0.55)
        rect(s, x, 1.6, pw, 0.6, fill=BLUE if i == 0 else SAND, content=p, size=14, color=WHITE if i == 0 else BLACK, align='c', anchor='m')
        gx = x + pw + 0.1
        shape(s, SH.DIAMOND, gx, 1.6, 0.6 - 0.25, 0.6, fill=BLACK)
        g, crit = gates[i]
        label(s, x, 2.55, pw + 0.5, g + ' – Kriterien', color=BLUE)
        hline(s, x, 2.85, pw + 0.45, STONE, 0.5)
        text(s, x, 2.95, pw + 0.4, 1.4, bl(crit, sa=6), size=13)
    rect(s, L, 4.5, W, 1.3, fill=LSAND)
    text(s, L + 0.3, 4.6, W - 0.6, 1.1, [{'t': 'Am Gate entscheidet das Steering Committee:', 'size': 14, 'sa': 6},
                                         {'t': [('Go  ', {'color': BLUE}), ('nächste Phase starten   ', {}), ('Hold  ', {'color': BLUE}),
                                                ('Nacharbeit mit neuem Termin   ', {}), ('Stop  ', {'color': BLUE}), ('Projekt beenden, Ergebnisse sichern', {})], 'size': 13}])

    s = D.slide('content', 'Vier Workshops binden Ihre Experten gezielt und zeitsparend ein',
                'Vorgehen & Plan | Workshop-Konzept', key='workshops',
                notes=N('Zeigt, wie und wann der Kunde eingebunden wird – reduziert Sorge um Ressourcenbindung.', 'Workshops, Teilnehmende und Dauer anpassen.'))
    ws = [('W1', 'Zielbild', 'Woche 2', 'Ziele, Anforderungen und Erfolgskriterien abstimmen', 'Sponsor, Produktion, QA'),
          ('W2', 'Ist-Analyse', 'Woche 4', 'Ergebnisse der Analyse validieren, Hypothesen prüfen', 'Fachbereiche'),
          ('W3', 'Lösungsoptionen', 'Woche 6', 'Optionen bewerten und priorisieren', 'Kernteam, Finanzen'),
          ('W4', 'Roadmap', 'Woche 8', 'Umsetzungsplan und Business Case verabschieden', 'Steering Committee')]
    cw = (W - 3 * 0.3) / 4
    for i, (n_, h, wk, z, t) in enumerate(ws):
        x = L + i * (cw + 0.3)
        oval(s, x, 1.5, 0.8, fill=BLUE, content=n_, size=16, color=WHITE, align='c', anchor='m', margin=0)
        text(s, x + 0.95, 1.55, cw - 0.95, 0.35, h, size=18)
        text(s, x + 0.95, 1.95, cw - 0.95, 0.3, wk, size=12, color=DGRAY)
        hline(s, x, 2.55, cw, BLACK)
        label(s, x, 2.7, cw, 'Ziel'); text(s, x, 3.0, cw, 0.9, z, size=13)
        label(s, x, 4.0, cw, 'Teilnehmende'); text(s, x, 4.3, cw, 0.6, t, size=13)
        label(s, x, 4.9, cw, 'Dauer'); text(s, x, 5.2, cw, 0.4, '3 Stunden', size=13)
        if i < 3:
            icon(s, 'arrow_forward', x + cw + 0.03, 1.77, 0.24, TAUPE)
    sowhat(s, 'Rund 12 Stunden Workshop-Zeit je Experte – mehr Einbindung ist nicht nötig, weniger gefährdet die Akzeptanz.')

    s = D.slide('content', 'Tandem-Projektleitung sichert Entscheidungsfähigkeit auf beiden Seiten',
                'Vorgehen & Plan | Projektorganisation', key='org',
                notes=N('Projektorganisation für Angebot und Kick-off.', 'Namen und Workstreams eintragen.',
                        'Tandem (Kunde + Körber) auf jeder Ebene vermeidet Entscheidungsstau.'))
    rect(s, 3.67, 1.45, 6.0, 0.75, fill=BLUE, content=[{'t': 'Steering Committee', 'size': 15}, {'t': '[Sponsor Kunde], [Körber Executive]', 'size': 11}], color=WHITE, align='c', anchor='m')
    vline(s, 6.67, 2.2, 0.35, STONE)
    rect(s, 4.17, 2.55, 2.4, 0.8, fill=SAND, content=[{'t': 'Projektleitung Kunde', 'size': 13}, {'t': '[Name]', 'size': 11}], align='c', anchor='m')
    rect(s, 6.77, 2.55, 2.4, 0.8, fill=SAND, content=[{'t': 'Projektleitung Körber', 'size': 13}, {'t': '[Name]', 'size': 11}], align='c', anchor='m')
    rect(s, 10.0, 2.55, 2.97, 0.8, line=STONE, content=[{'t': 'PMO', 'size': 13}, {'t': 'Planung, Reporting, Risiken', 'size': 11}], align='c', anchor='m')
    hline(s, 9.17, 2.95, 0.83, STONE)
    vline(s, 6.67, 3.35, 0.4, STONE)
    wsn = ['Facility & Process', 'CQV', 'MES & Daten', 'Organisation']
    cw = (W - 3 * 0.25) / 4
    hline(s, L + cw / 2, 3.75, W - cw, STONE)
    for i, w_ in enumerate(wsn):
        x = L + i * (cw + 0.25)
        vline(s, x + cw / 2, 3.75, 0.3, STONE)
        rect(s, x, 4.05, cw, 1.75, line=STONE)
        label(s, x + 0.2, 4.2, cw - 0.4, 'Workstream %d' % (i + 1))
        text(s, x + 0.2, 4.5, cw - 0.4, 0.35, w_, size=15)
        text(s, x + 0.2, 4.95, cw - 0.4, 0.8, 'Lead Kunde: [Name]\nLead Körber: [Name]', size=11, color=DGRAY)
    sowhat(s, 'Jede Rolle ist doppelt besetzt – Entscheidungen fallen dort, wo das Wissen sitzt.')

    s = D.slide('content', 'Klare Verantwortlichkeiten: RACI für die zentralen Ergebnisse',
                'Vorgehen & Plan | RACI-Matrix', key='raci',
                notes=N('Verantwortungsmatrix für Kick-off und Projekthandbuch.', 'Ergebnisse und Rollen anpassen. Je Zeile genau ein „A“.'))
    roles = ['Sponsor', 'PL Kunde', 'PL Körber', 'QA', 'Produktion', 'Einkauf']
    deliv = [('Projektauftrag', 'A R C C I I'), ('User Requirements (URS)', 'I A R C C I'), ('Basic Design', 'I A R C C I'),
             ('Vergabeentscheidung', 'A R C I C R'), ('Qualifizierungsplan', 'I C R A C I'), ('Freigabe Go-live', 'A C C R C I')]
    data = [['Ergebnis'] + roles] + [[d] + v.split() for d, v in deliv]
    tb = table(s, L, 1.5, W, data, colw=[3.6] + [1.5] * 6, rowh=0.52, size=13, aligns=['l'] + ['c'] * 6)
    for r in range(1, len(data)):
        for c in range(1, 7):
            v = data[r][c]
            cell = tb.cell(r, c)
            if v in ('A', 'R'):
                cell.fill.solid(); setc(cell.fill.fore_color, BLUE if v == 'A' else LBLUE)
                fill_tf(cell.text_frame, v, size=13, color=WHITE if v == 'A' else BLUE, align='c')
    text(s, L, 5.4, W, 0.3, [{'t': [('R ', {'color': BLUE}), ('Responsible – führt aus    ', {}), ('A ', {'color': BLUE}), ('Accountable – entscheidet    ', {}),
                                     ('C ', {'color': BLUE}), ('Consulted – wird gefragt    ', {}), ('I ', {'color': BLUE}), ('Informed – wird informiert', {})]}], size=11)

    s = D.slide('content', 'Drei Gremien mit festen Rhythmen steuern das Projekt',
                'Vorgehen & Plan | Governance', key='governance',
                notes=N('Steuerungs- und Kommunikationsstruktur.', 'Gremien, Teilnehmende und Rhythmen anpassen.'))
    rows = [['Gremium', 'Teilnehmende', 'Rhythmus', 'Zweck', 'Format'],
            ['Steering Committee', 'Sponsor, Geschäftsführung, PL', 'Monatlich, 60 Min.', 'Entscheidungen, Eskalationen, Gates', 'Statusbericht, Entscheidungsvorlage'],
            ['Projektleitungsrunde', 'PL Kunde, PL Körber, PMO', 'Wöchentlich, 45 Min.', 'Fortschritt, Risiken, Ressourcen', 'Status-Dashboard'],
            ['Workstream-Meeting', 'Workstream-Teams', 'Wöchentlich, 30 Min.', 'Operative Abstimmung', 'Aufgabenliste'],
            ['Daily Stand-up', 'Team vor Ort (Realisierung)', 'Täglich, 15 Min.', 'Tagesplanung, Hindernisse', 'Board']]
    table(s, L, 1.5, W, rows, colw=[2.4, 3.0, 2.0, 3.0, 2.6], rowh=0.7, size=13, bold_first_col=False)
    sowhat(s, 'Entscheidungen fallen im Steering Committee – alle anderen Gremien bereiten vor und setzen um.')

    s = D.slide('content', 'Annahmen und Mitwirkungsleistungen schaffen Planungssicherheit',
                'Vorgehen & Plan | Annahmen und Mitwirkung', key='assumptions',
                notes=N('Grundlage für Angebot und Vertrag – reduziert spätere Nachträge.', 'Projektspezifisch ergänzen; mit Vertragsanlage abgleichen.'))
    cw = (W - 0.5) / 2
    for i, (h, ic, items) in enumerate([('Unsere Annahmen', 'fact_check', ['Projektstart spätestens [Datum]', 'Bestehende Gebäudestruktur wird genutzt',
                                                                          'Maximal zwei Produktformate', 'Entscheidungen innerhalb von 10 Arbeitstagen', 'Arbeitssprache Deutsch und Englisch']),
                                        ('Ihre Mitwirkung', 'groups', ['Benannte Projektleitung (50 % Kapazität)', 'Zugang zu Daten, Systemen und Anlagen',
                                                                       'Fachexperten für Workshops (ca. 2 Tage/Monat)', 'Freigaben durch QA innerhalb der Fristen', 'Arbeitsplätze für das Körber-Team vor Ort'])]):
        x = L + i * (cw + 0.5)
        icon(s, ic, x, 1.5, 0.45, BLUE)
        text(s, x + 0.65, 1.55, cw - 0.65, 0.4, h, size=18)
        hline(s, x, 2.15, cw, BLACK)
        for j, it in enumerate(items):
            y = 2.3 + j * 0.62
            num(s, x, y + 0.03, j + 1, 0.36, filled=False, size=11)
            text(s, x + 0.55, y, cw - 0.6, 0.45, it, size=14, anchor='m')

    s = D.slide('content', 'Die ersten 90 Tage: Schnelle Ergebnisse schaffen Momentum',
                'Vorgehen & Plan | 30-60-90-Tage-Plan', key='plan90',
                notes=N('Zeigt Tempo und frühe Ergebnisse – stark in Kick-off und Angebot.', 'Aktivitäten und Quick Wins anpassen.'))
    cols = [('Tag 1–30', 'Verstehen', ['Kick-off und Interviews', 'Datenanalyse', 'Baseline der KPIs'], 'Quick Win: Rüst-Standard Linie 3'),
            ('Tag 31–60', 'Gestalten', ['Zielbild und Optionen', 'Workshops mit Fachbereichen', 'Business Case'], 'Quick Win: Freigabe-Checkliste'),
            ('Tag 61–90', 'Entscheiden', ['Roadmap verabschieden', 'Investitionsantrag', 'Start Umsetzung'], 'Ergebnis: Freigabe Phase 2')]
    cw = (W - 2 * 0.3) / 3
    for i, (d, h, b, q) in enumerate(cols):
        x = L + i * (cw + 0.3)
        rect(s, x, 1.5, cw, 0.9, fill=BLUE if i == 2 else SAND)
        text(s, x + 0.25, 1.55, cw - 0.5, 0.4, d, size=12, color=WHITE if i == 2 else DGRAY, anchor='m')
        text(s, x + 0.25, 1.88, cw - 0.5, 0.45, h, size=20, color=WHITE if i == 2 else BLACK)
        text(s, x + 0.25, 2.65, cw - 0.5, 1.6, bl(b, sa=8), size=14)
        rect(s, x, 4.6, cw, 0.9, fill=LSAND)
        icon(s, 'bolt', x + 0.2, 4.83, 0.42, BLUE)
        text(s, x + 0.75, 4.6, cw - 0.9, 0.9, q, size=13, anchor='m')


# =====================================================================================
def s08(D):
    divider(D, 8, 'Prozesse &\nAbläufe', N('Standardisierte Darstellung von Prozessen: Landkarte, Swimlane, SIPOC, Prozessschritt, Wertstrom, Soll-Prozess, Entscheidungslogik, KPIs.',
                                             'Immer dieselben Formen verwenden: Prozessschritt = Rechteck, Entscheidung = Raute, Wartezeit = Dreieck.',
                                             'Einheitliche Prozessdarstellung ist der größte Hebel für ein professionelles Gesamtbild über Projekte hinweg.'))
    s = D.slide('content', 'Prozesslandkarte: Zwölf Prozesse auf drei Ebenen',
                'Prozesse | Prozesslandkarte', key='processmap',
                notes=N('Einstieg in jede Prozessanalyse – zeigt den Gesamtkontext.', 'Prozesse anpassen; untersuchte Prozesse blau markieren.'))
    label(s, L, 1.45, 3, 'Managementprozesse', color=DGRAY)
    mp = ['Strategie & Planung', 'Qualitätsmanagement', 'Risikomanagement']
    mw = (W - 2 * 0.2) / 3
    for i, m in enumerate(mp):
        rect(s, L + i * (mw + 0.2), 1.75, mw, 0.65, fill=SAND, content=m, size=13, align='c', anchor='m')
    label(s, L, 2.7, 3, 'Kernprozesse', color=BLUE)
    chevrons(s, ['Beschaffung', 'Herstellung', 'Abfüllung', 'Prüfung & Freigabe', 'Distribution'], L, 3.0, W, 1.1, active=[2, 3], size=14)
    label(s, L, 4.4, 3, 'Unterstützungsprozesse', color=DGRAY)
    sp_ = ['Instandhaltung', 'IT / OT', 'Personal & Schulung', 'Engineering']
    sw = (W - 3 * 0.2) / 4
    for i, m in enumerate(sp_):
        rect(s, L + i * (sw + 0.2), 4.7, sw, 0.65, fill=SAND, content=m, size=13, align='c', anchor='m')
    rect(s, L, 5.6, 0.22, 0.22, fill=BLUE); text(s, L + 0.32, 5.56, 4, 0.3, 'Im Fokus der Analyse', size=11)

    s = D.slide('content', 'Chargenfreigabe heute: Vier Bereiche, elf Übergaben, 18 Tage',
                'Prozesse | Swimlane (Ist)', 'Quelle: Prozessaufnahme [Kunde], [Datum]', key='swimlane',
                notes=N('Ablauf über Abteilungsgrenzen – macht Übergaben und Wartezeiten sichtbar.', 'Lanes = Organisationseinheiten; Schritte als Rechtecke, Engpässe blau.',
                        'Übergaben zählen: Jede Lane-Grenze ist ein Risiko für Wartezeit und Fehler.'))
    lanes = ['Produktion', 'QC-Labor', 'QA', 'Logistik']
    lh = 1.0; lx = L + 1.7; y0 = 1.45
    for i, ln in enumerate(lanes):
        y = y0 + i * lh
        rect(s, L, y, 1.6, lh - 0.06, fill=SAND, content=ln, size=13, anchor='m')
        rect(s, lx, y, R - lx, lh - 0.06, fill=LSAND)
    steps = [(0, 0, 'Charge abschließen', False), (1, 1, 'Muster prüfen', False), (0, 2, 'Protokoll prüfen', False), (2, 3, 'Review Protokoll', True),
             (1, 3, 'Prüfbericht', False), (2, 4, 'Abweichung bewerten', True), (2, 5, 'QP-Freigabe', False), (3, 6, 'Versand freigeben', False)]
    sw = 1.25; gap = (R - lx - 0.2 - 7 * sw) / 6 + sw
    pos = {}
    for k, (lane, col, t, hi) in enumerate(steps):
        x = lx + 0.1 + col * gap; y = y0 + lane * lh + 0.17
        rect(s, x, y, sw, lh - 0.4, fill=BLUE if hi else WHITE, line=None if hi else STONE, content=t, size=11, color=WHITE if hi else BLACK, align='c', anchor='m', margin=0.04)
        pos[k] = (x, y)
    for a, b in [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5, 6), (6, 7)]:
        xa, ya = pos[a]; xb, yb = pos[b]
        elbow(s, xa + sw, ya + (lh - 0.4) / 2, xb, yb + (lh - 0.4) / 2)
    sowhat(s, 'Review des Chargenprotokolls und Bewertung von Abweichungen verursachen zwei Drittel der Durchlaufzeit.')

    s = D.slide('content', 'SIPOC: Der Abfüllprozess vom Lieferanten bis zum Kunden',
                'Prozesse | SIPOC', key='sipoc',
                notes=N('Prozessabgrenzung zu Projektbeginn (Scope-Klärung).', 'Einträge je Spalte anpassen; 3–6 Einträge pro Spalte.'))
    cols = [('S', 'Supplier', ['Wirkstoffherstellung', 'Primärpackmittel-Lieferant', 'Medienversorgung']),
            ('I', 'Input', ['Bulk-Lösung', 'Vials, Stopfen', 'WFI, Reinstdampf', 'Herstellanweisung']),
            ('P', 'Process', ['Vorbereitung', 'Sterilfiltration', 'Abfüllung im Isolator', 'Verschließen', 'Inspektion']),
            ('O', 'Output', ['Gefüllte Vials', 'Chargenprotokoll', 'In-Prozess-Daten']),
            ('C', 'Customer', ['Verpackung', 'QA / QP', 'Patient (indirekt)'])]
    cw = (W - 4 * 0.2) / 5
    for i, (l_, h, items) in enumerate(cols):
        x = L + i * (cw + 0.2)
        hi = i == 2
        rect(s, x, 1.5, cw, 0.95, fill=BLUE if hi else SAND)
        text(s, x + 0.2, 1.55, 0.8, 0.85, l_, size=36, color=WHITE if hi else BLUE, anchor='m')
        text(s, x + 0.9, 1.55, cw - 1.0, 0.85, h, size=15, color=WHITE if hi else BLACK, anchor='m')
        for j, it in enumerate(items):
            y = 2.65 + j * 0.62
            rect(s, x, y, cw, 0.52, line=BLUE if hi else STONE, content=it, size=12, anchor='m', margin=(0.12, 0.02, 0.08, 0.02))
            if hi and j < len(items) - 1:
                icon(s, 'arrow_forward', x + cw / 2 - 0.08, y + 0.5, 0.0, BLUE) if False else None

    s = D.slide('content', 'Prozessschritt Chargenprüfung: Input, Aktivitäten und Output im Überblick',
                'Prozesse | Prozessschritt-Detail', key='processstep',
                notes=N('Standard-Steckbrief für einen Prozessschritt – für Prozesshandbücher und Soll-Konzepte.', 'Für jeden Prozessschritt duplizieren; Kopfzeile = Position im Prozess.',
                        'Gleicher Steckbrief für alle Schritte macht Prozessdokumentationen vergleichbar.'))
    chevrons(s, ['1 Vorbereitung', '2 Herstellung', '3 Abfüllung', '4 Chargenprüfung', '5 Freigabe'], L, 1.45, W, 0.45, active=3, size=11)
    blocks = [('Input', ['Chargenprotokoll (eBR)', 'Prüfergebnisse QC', 'Abweichungsberichte']),
              ('Aktivitäten', ['Vollständigkeit prüfen', 'Abweichungen bewerten', 'Trends auswerten', 'Prüfung dokumentieren']),
              ('Output', ['Geprüftes Protokoll', 'Freigabeempfehlung', 'CAPA bei Bedarf'])]
    bw = (W - 2 * 0.55) / 3
    for i, (h, it) in enumerate(blocks):
        x = L + i * (bw + 0.55)
        rect(s, x, 2.15, bw, 2.0, fill=BLUE if i == 1 else LSAND)
        label(s, x + 0.2, 2.3, bw - 0.4, h, color=WHITE if i == 1 else BLUE)
        text(s, x + 0.2, 2.6, bw - 0.4, 1.5, bl(it, sa=4), size=13, color=WHITE if i == 1 else BLACK)
        if i < 2:
            icon(s, 'arrow_forward', x + bw + 0.14, 3.0, 0.28, TAUPE)
    meta = [('Verantwortlich', 'QA Operations'), ('Systeme', 'MES, LIMS, QMS'), ('KPI', 'Review-Zeit je Charge (Ziel < 2 Tage)'), ('Risiken', 'Unvollständige Daten, Rückfragen')]
    mw = (W - 3 * 0.3) / 4
    for i, (a, b) in enumerate(meta):
        x = L + i * (mw + 0.3)
        hline(s, x, 4.45, mw, BLACK)
        label(s, x, 4.57, mw, a, color=DGRAY)
        text(s, x, 4.87, mw, 0.8, b, size=13)

    s = D.slide('content', 'Wertstrom: Nur 6 % der Durchlaufzeit sind wertschöpfend',
                'Prozesse | Wertstromanalyse', 'Quelle: Wertstromaufnahme [Kunde], [Datum]; Werte illustrativ', key='vsm', sticker_='Illustrativ',
                notes=N('Wertstromanalyse (VSM) – zeigt Verschwendung in Durchlaufzeit.', 'Prozesszeiten (PZ) und Wartezeiten je Schritt eintragen; Summen aktualisieren.',
                        'Wartezeiten als Dreieck, Prozessschritte als Rechteck – Standard-Symbolik beibehalten.'))
    steps = [('Herstellung', '1,0 d'), ('Abfüllung', '0,5 d'), ('QC-Prüfung', '2,0 d'), ('Protokoll-Review', '0,3 d'), ('QP-Freigabe', '0,1 d')]
    waits = ['2 d', '4 d', '6 d', '3 d']
    n_ = len(steps); bw = 1.75; gap = (W - n_ * bw) / (n_ - 1)
    for i, (h, pz) in enumerate(steps):
        x = L + i * (bw + gap)
        rect(s, x, 1.7, bw, 1.15, fill=SAND, content=[{'t': h, 'size': 13}, {'t': 'PZ ' + pz, 'size': 11, 'color': BLUE}], align='c', anchor='m')
        if i < n_ - 1:
            tx = x + bw + gap / 2 - 0.3
            tri = shape(s, SH.ISOSCELES_TRIANGLE, tx, 1.95, 0.6, 0.5, fill=ORANGE if waits[i] == '6 d' else STONE)
            text(s, tx - 0.3, 2.5, 1.2, 0.3, waits[i], size=12, align='c')
    # timeline ladder
    yb = 3.45
    xs = [L]
    for i in range(n_):
        x = L + i * (bw + gap)
        hline(s, x, yb + 0.45, bw, BLUE, 2.5)
        text(s, x, yb + 0.5, bw, 0.3, steps[i][1], size=11, align='c', color=BLUE)
        if i < n_ - 1:
            hline(s, x + bw, yb, gap, BLACK, 1.5)
            text(s, x + bw, yb - 0.32, gap, 0.3, waits[i], size=11, align='c')
            vline(s, x + bw, yb, 0.45, BLACK, 1.0); vline(s, x + bw + gap, yb, 0.45, BLACK, 1.0)
    k = [('18,9 Tage', 'Durchlaufzeit'), ('3,9 Tage', 'Prozesszeit'), ('6 %', 'Wertschöpfungsanteil')]
    for i, (a, b) in enumerate(k):
        x = L + i * 4.3
        kpi(s, x, 4.45, 3.9, a, b, bigsize=26)

    s = D.slide('content', 'Soll-Prozess: Fünf statt elf Schritte durch Review by Exception',
                'Prozesse | Ist- und Soll-Prozess', key='tobeprocess',
                notes=N('Gegenüberstellung Ist- und Soll-Prozess.', 'Entfallende Schritte grau mit Kreuz, neue Schritte blau.'))
    label(s, L, 1.45, 6, 'Ist-Prozess (11 Schritte, 18 Tage)', color=DGRAY)
    ist = ['Charge abschl.', 'Papier sammeln', 'Muster prüfen', 'Ergebnis übertragen', 'Protokoll prüfen', 'Rückfragen', 'Korrektur', 'Review QA', 'Abweichung', 'QP-Freigabe', 'Versand']
    keep = {0, 2, 7, 9, 10}
    bw = (W - 10 * 0.08) / 11
    for i, t in enumerate(ist):
        x = L + i * (bw + 0.08)
        f = SAND if i in keep else WHITE
        rect(s, x, 1.8, bw, 0.9, fill=f, line=None if i in keep else STONE, content=t, size=10, align='c', anchor='m', margin=0.03,
             color=BLACK if i in keep else DGRAY)
        if i not in keep:
            icon(s, 'cancel', x + bw / 2 - 0.13, 2.78, 0.26, TAUPE)
    label(s, L, 3.35, 4, 'Soll-Prozess (5 Schritte, 11 Tage)', color=BLUE)
    soll = [('Charge abschließen', False), ('Automatische Prüfung im MES', True), ('Musterprüfung QC', False), ('Review by Exception', True), ('QP-Freigabe & Versand', False)]
    bw2 = (W - 4 * 0.4) / 5
    for i, (t, new) in enumerate(soll):
        x = L + i * (bw2 + 0.4)
        rect(s, x, 3.7, bw2, 0.95, fill=BLUE if new else SAND, content=t, size=13, color=WHITE if new else BLACK, align='c', anchor='m')
        if i < 4:
            icon(s, 'arrow_forward', x + bw2 + 0.08, 4.04, 0.24, TAUPE)
    rect(s, L, 4.95, 0.22, 0.22, fill=BLUE); text(s, L + 0.32, 4.91, 3, 0.3, 'Neu / digitalisiert', size=11)
    icon(s, 'cancel', L + 2.6, 4.93, 0.24, TAUPE); text(s, L + 2.95, 4.91, 3, 0.3, 'Entfällt', size=11)
    sowhat(s, 'Digitale Prüfung im MES macht manuelle Übertragungen überflüssig – die Freigabe wird 40 % schneller.')

    s = D.slide('content', 'Abweichungsmanagement: Eindeutige Entscheidungslogik in drei Stufen',
                'Prozesse | Entscheidungslogik', key='flowchart',
                notes=N('Flussdiagramm mit Entscheidungen – für SOPs und Soll-Prozesse.', 'Standard-Symbole: Start/Ende = abgerundet, Schritt = Rechteck, Entscheidung = Raute.'))
    def box(x, y, t, kind='step', w=2.2, h=0.7):
        if kind == 'term':
            return rrect(s, x, y, w, h, fill=BLACK, radius=0.35, content=t, size=12, color=WHITE, align='c', anchor='m')
        if kind == 'dec':
            return shape(s, SH.DIAMOND, x, y, w, h + 0.5, fill=BLUE, content=t, size=11, color=WHITE, align='c', anchor='m', margin=0.05)
        return rect(s, x, y, w, h, fill=SAND, content=t, size=12, align='c', anchor='m')
    box(L, 1.65, 'Abweichung erkannt', 'term', 2.0)
    arrow(s, L + 2.0, 2.0, L + 2.5, 2.0)
    box(L + 2.5, 1.65, 'Erfassen und Sofortmaßnahmen')
    arrow(s, L + 4.7, 2.0, L + 5.2, 2.0)
    box(L + 5.2, 1.4, 'Produkt-\nqualität\nbetroffen?', 'dec', 2.2, 0.7)
    arrow(s, L + 7.4, 2.0, L + 8.0, 2.0); text(s, L + 7.45, 1.65, 0.6, 0.3, 'Nein', size=11)
    box(L + 8.0, 1.65, 'Minor: Dokumentieren, Trend', w=2.3)
    arrow(s, L + 10.3, 2.0, L + 10.8, 2.0)
    box(L + 10.8, 1.65, 'Abschluss', 'term', 1.8)
    arrow(s, L + 6.3, 2.6, L + 6.3, 3.2); text(s, L + 6.4, 2.7, 0.6, 0.3, 'Ja', size=11)
    box(L + 5.2, 3.2, 'Ursachenanalyse (Root Cause)', w=2.2)
    arrow(s, L + 6.3, 3.9, L + 6.3, 4.3)
    box(L + 5.2, 4.3, 'Kritisch für\nPatienten?', 'dec', 2.2, 0.7)
    arrow(s, L + 7.4, 4.9, L + 8.0, 4.9); text(s, L + 7.45, 4.55, 0.6, 0.3, 'Nein', size=11)
    box(L + 8.0, 4.55, 'Major: CAPA, QA-Freigabe', w=2.3)
    arrow(s, L + 5.2, 4.9, L + 4.7, 4.9); text(s, L + 4.75, 4.55, 0.4, 0.3, 'Ja', size=11)
    rect(s, L + 2.5, 4.55, 2.2, 0.7, fill=ORANGE, content='Critical: Sperren, Behörde informieren', size=11, align='c', anchor='m')
    elbow(s, L + 10.3, 4.9, L + 11.7, 2.35)

    s = D.slide('content', 'Fünf Prozess-KPIs machen den Fortschritt messbar',
                'Prozesse | KPI-Steckbrief', 'Quelle: [System]; Stand [Datum]', key='processkpi',
                notes=N('KPI-Definitionen für Prozessprojekte – Basis für Reporting und Dashboard.', 'Definition, Quelle und Owner mit dem Kunden abstimmen.',
                        'Jede KPI braucht Definition, Datenquelle, Rhythmus und Owner – sonst wird sie nicht gemessen.'))
    rows = [['KPI', 'Definition', 'Ist', 'Ziel', 'Quelle / Rhythmus', 'Owner'],
            ['Durchlaufzeit Freigabe', 'Chargenende bis QP-Freigabe (Tage)', '18', '11', 'MES, je Charge', 'Head of QA'],
            ['Right First Time', 'Chargen ohne Abweichung (%)', '82 %', '95 %', 'QMS, monatlich', 'Head of Production'],
            ['OEE Linie 3', 'Verfügbarkeit × Leistung × Qualität', '54 %', '66 %', 'MES, wöchentlich', 'Linienleitung'],
            ['Rüstzeit', 'Letzte Gutteil bis erste Gutteil (h)', '7,0', '3,0', 'MES, je Rüstvorgang', 'Linienleitung'],
            ['Offene CAPAs > 30 Tage', 'Anzahl überfälliger Maßnahmen', '14', '< 3', 'QMS, monatlich', 'QA Operations']]
    tb = table(s, L, 1.5, W, rows, colw=[2.4, 3.6, 1.0, 1.0, 2.4, 2.2], rowh=0.62, size=12, aligns=['l', 'l', 'c', 'c', 'l', 'l'])
    for r in range(1, 6):
        fill_tf(tb.cell(r, 3).text_frame, rows[r][3], size=13, color=BLUE, align='c')
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=13)


# =====================================================================================
def s09(D):
    divider(D, 9, 'Referenzen', N('Referenzen, Case Studies und Testimonials.',
                                   'Nur freigegebene Referenzen verwenden; ggf. anonymisieren („Top-20-Pharmaunternehmen“).',
                                   'Die beste Referenz ist die mit dem ähnlichsten Problem – nicht die mit dem größten Logo.'))
    s = D.slide('content', 'Ausgewählte Referenzen aus vergleichbaren Projekten',
                'Referenzen | Übersicht', 'Kundennamen nur mit Freigabe; sonst anonymisiert', key='refs',
                notes=N('Überblick über relevante Referenzen – Auswahl je Termin.', 'Sechs passende Referenzen wählen; Ergebnisse quantifizieren.'))
    refs = [('Big Pharma', 'Neue Isolator-Linie', 'Qualifizierung 9 Wochen vor Plan'), ('CDMO', 'OEE-Programm, 3 Standorte', '+18 % Ausbringung in 9 Monaten'),
            ('Biotech', 'Scale-up mAb-Produktion', 'Von Klinik zu Kommerz in 20 Monaten'), ('Generika', 'Rüstzeit-Reduktion', '–55 % Rüstzeit auf zwei Linien'),
            ('Big Pharma', 'MES-Rollout, 4 Werke', 'Papierlose Freigabe in 14 Monaten'), ('ATMP', 'Annex-1-Gap-Assessment', '0 kritische Beobachtungen bei Inspektion')]
    cw, chh = (W - 2 * 0.3) / 3, 2.05
    for i, (seg, h, r) in enumerate(refs):
        x = L + (i % 3) * (cw + 0.3); y = 1.5 + (i // 3) * (chh + 0.25)
        rect(s, x, y, cw, chh, fill=LSAND)
        rrect(s, x + 0.25, y + 0.25, 0.25 + 0.085 * len(seg), 0.3, fill=WHITE, line=BLUE, radius=0.15, content=seg, size=10, color=BLUE, align='c', anchor='m', margin=0)
        text(s, x + 0.25, y + 0.75, cw - 0.5, 0.4, h, size=16)
        text(s, x + 0.25, y + 1.25, cw - 0.5, 0.6, r, size=14, color=BLUE)

    s = D.slide('content', 'Case: Neue Isolator-Linie neun Wochen vor Plan qualifiziert',
                'Referenzen | Case Study', 'Kunde: Top-20-Pharmaunternehmen, Deutschland; Freigabe [Datum]', key='case1',
                notes=N('Standard-Case-Study als One-Pager.', 'Herausforderung, Vorgehen, Ergebnis – jeweils maximal drei Punkte; Bild aus Pictures Library.',
                        'Ergebnis zuerst nennen (im Titel) – Details nur für Interessierte.'))
    picture(s, IMG + 'image21.jpeg', 9.0, 1.45, R - 9.0, 4.35)
    blocks = [('Herausforderung', ['Kapazitätsengpass bei sterilen Injektabilia', 'Fester Launch-Termin', 'Erste Isolator-Linie am Standort']),
              ('Vorgehen', ['Parallelisierte Planung und CQV', 'Risikobasierte Qualifizierung', 'Tandem-Projektleitung']),
              ('Ergebnis', ['Qualifizierung 9 Wochen vor Plan', 'Budget eingehalten (–3 %)', 'Inspektion ohne kritische Beobachtung'])]
    bw = (9.0 - L - 0.3 - 2 * 0.25) / 3
    for i, (h, it) in enumerate(blocks):
        x = L + i * (bw + 0.25)
        f = BLUE if i == 2 else LSAND
        rect(s, x, 1.45, bw, 2.75, fill=f)
        label(s, x + 0.2, 1.65, bw - 0.4, h, color=WHITE if i == 2 else BLUE)
        text(s, x + 0.2, 1.98, bw - 0.4, 2.1, bl(it, sa=6), size=12, color=WHITE if i == 2 else BLACK)
    k = [('9 Wochen', 'früher qualifiziert'), ('–3 %', 'unter Budget'), ('0', 'kritische Beobachtungen')]
    for i, (a, b) in enumerate(k):
        kpi(s, L + i * (bw + 0.25), 4.45, bw, a, b, bigsize=26)

    s = D.slide('content', 'Case: OEE-Programm steigert die Ausbringung um 18 % in neun Monaten',
                'Referenzen | Case Study mit Ergebnissen', 'Kunde: Europäisches CDMO, 3 Standorte; Werte vor/nach Programm', key='case2',
                notes=N('Case Study mit quantifizierten Vorher-Nachher-Ergebnissen.', 'Diagrammdaten per „Daten bearbeiten“ anpassen.'))
    bar(s, L, 1.4, 7.4, 4.4, ['OEE', 'Verfügbarkeit', 'Leistung', 'Qualität'], [('Vorher', [0.52, 0.71, 0.78, 0.94]), ('Nachher', [0.63, 0.80, 0.83, 0.96])],
        fmt='0%', colors=[STONE, BLUE], gap=70, overlap=-10, legend='b', size=12)
    xr = 8.2; wr = R - xr
    label(s, xr, 1.5, wr, 'Was den Unterschied gemacht hat')
    for i, (h, b) in enumerate([('SMED-Workshops', 'Rüstzeiten auf allen Linien halbiert'), ('Shopfloor-Management', 'Tägliche KPI-Runden mit klaren Eskalationen'),
                                ('Datenbasis', 'Stillstandsgründe automatisch im MES erfasst')]):
        y = 1.9 + i * 1.25
        num(s, xr, y, i + 1, 0.42)
        text(s, xr + 0.6, y - 0.02, wr - 0.6, 0.35, h, size=16)
        text(s, xr + 0.6, y + 0.38, wr - 0.6, 0.6, b, size=13, color=DGRAY)

    s = D.slide('content', 'Case: Vom Konzept zur bestandenen Inspektion in 20 Monaten',
                'Referenzen | Case Study als Zeitstrahl', 'Kunde: Biotech-Unternehmen, Schweiz', key='case3',
                notes=N('Case Study als Projektreise – gut für komplexe, mehrphasige Projekte.', 'Meilensteine und Ergebnisse anpassen.'))
    ev = [('M0', 'Kick-off', 'Zielbild und Scope'), ('M3', 'Konzept', 'Modulare Anlage, Single-Use'), ('M8', 'Design Freeze', 'Detail Design abgeschlossen'),
          ('M14', 'Installation', 'Mechanical Completion in 6 Monaten'), ('M18', 'PQ', 'Prozessvalidierung'), ('M20', 'Inspektion', 'Ohne kritische Beobachtung')]
    y0 = 3.0; cw = W / 6
    rect(s, L, y0 - 0.06, W, 0.12, fill=SAND)
    rect(s, L, y0 - 0.06, W * 0.98, 0.12, fill=BLUE)
    for i, (m, h, b) in enumerate(ev):
        x = L + i * cw
        oval(s, x, y0 - 0.25, 0.5, fill=WHITE, line=BLUE, lw=2, content=m, size=9, color=BLUE, align='c', anchor='m', margin=0)
        text(s, x, y0 + 0.45, cw - 0.2, 0.35, h, size=14)
        text(s, x, y0 + 0.85, cw - 0.2, 0.6, b, size=12, color=DGRAY)
    label(s, L, 1.5, 4, 'Ausgangslage')
    text(s, L, 1.8, W, 0.6, 'Kommerzieller Launch eines monoklonalen Antikörpers erforderte eine neue Produktionsanlage – ohne eigene Engineering-Abteilung.', size=14)
    sowhat(s, '20 Monate vom Konzept zur Inspektion – rund 30 % schneller als der Branchendurchschnitt für vergleichbare Anlagen.')

    s = D.slide('content', 'Breite Erfahrung über alle Kundensegmente und Leistungsfelder',
                'Referenzen | Referenzmatrix', 'Anzahl Projekte seit [Jahr]; Werte illustrativ', key='refmatrix', sticker_='Illustrativ',
                notes=N('Zeigt die Breite der Erfahrung – besonders in Ausschreibungen.', 'Zahlen aus der Referenzdatenbank / CRM übernehmen.',
                        'Im CRM Referenzen nach Segment und Leistungsfeld taggen – dann ist diese Folie in Minuten aktualisiert.'))
    segs = ['Big Pharma', 'Biotech & ATMP', 'CDMO', 'Generika']
    svc = ['Facility & Process Design', 'GMP Compliance & CQV', 'Digitalisierung & MES', 'Supply Chain', 'Projektmanagement', 'Operational Excellence']
    vals = [[24, 11, 8, 6], [31, 14, 12, 9], [12, 4, 6, 3], [7, 3, 5, 6], [19, 8, 7, 4], [10, 2, 9, 11]]
    data = [['Leistungsfeld'] + segs] + [[svc[i]] + [str(v) for v in vals[i]] for i in range(6)]
    tb = table(s, L, 1.5, W, data, colw=[4.0] + [2.15] * 4, rowh=0.58, size=13, aligns=['l', 'c', 'c', 'c', 'c'])
    for r in range(1, 7):
        for c in range(1, 5):
            v = vals[r - 1][c - 1]
            f = BLUE if v >= 20 else (MBLUE if v >= 10 else (LBLUE if v >= 5 else None))
            if f:
                tb.cell(r, c).fill.solid(); setc(tb.cell(r, c).fill.fore_color, f)
            fill_tf(tb.cell(r, c).text_frame, str(v), size=13, color=WHITE if v >= 20 else BLACK, align='c')
    for i, (f, t) in enumerate([(BLUE, '≥ 20'), (MBLUE, '10–19'), (LBLUE, '5–9'), (WHITE, '< 5')]):
        rect(s, L + i * 1.4, 5.75, 0.22, 0.22, fill=f, line=STONE if f == WHITE else None); text(s, L + i * 1.4 + 0.3, 5.71, 1, 0.3, t, size=11)

    s = D.slide('content', 'Kunden, die uns vertrauen',
                'Referenzen | Kundenlogos', 'Logos nur mit Freigabe verwenden', key='logos', sticker_='Freigabe prüfen',
                notes=N('Logo-Wand für Erstgespräche.', 'Logos in Graustufen einsetzen; nur mit schriftlicher Freigabe.'))
    cw, chh = (W - 3 * 0.3) / 4, 1.2
    for i in range(12):
        x = L + (i % 4) * (cw + 0.3); y = 1.6 + (i // 4) * (chh + 0.3)
        rect(s, x, y, cw, chh, fill=LSAND, content='[Logo]', size=13, color=TAUPE, align='c', anchor='m')

    s = D.slide('quote', '„Körber hat unser Team befähigt, die Anlage drei Monate früher freizugeben.“', key='testimonial',
                notes=N('Kundenzitat als emotionaler Beleg.', 'Zitat, Name und Foto nur mit Freigabe; Foto per „Bild ändern“.'))
    {p.placeholder_format.idx: p for p in s.placeholders}[34].insert_picture(IMG + 'image29.jpeg')
    D.ph(s, 14, '[Vorname Name]\nHead of Manufacturing, [Kunde]')
