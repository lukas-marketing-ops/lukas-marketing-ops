from kh import *
from kh import _strip_style
from build_a import N, divider, person, IMG


# =====================================================================================
def s10(D):
    divider(D, 10, 'Angebot', N('Angebotspräsentation: Umfang, Pakete, Honorar, Zahlungsplan, Fahrplan zur Beauftragung.',
                                 'Zahlen mit dem kaufmännischen Angebot abgleichen.',
                                 'Preis nie ohne Nutzen zeigen – Business Case vorher präsentieren.'))
    s = D.slide('content', 'Unser Angebot auf einen Blick: In 20 Monaten zur validierten Linie',
                'Angebot | Zusammenfassung', 'Details: Angebot Nr. [xxx] vom [Datum]', key='offer',
                notes=N('Executive Summary des Angebots – erste Folie der Angebotspräsentation.', 'Alle vier Felder aus dem schriftlichen Angebot übernehmen.'))
    blocks = [('Ihre Ausgangslage', 'search', 'Kapazitätslücke ab [Jahr], Annex-1-Anpassungen an der Bestandslinie erforderlich.'),
              ('Unser Leistungsumfang', 'checklist', 'Planung, Projektmanagement und CQV für die neue Isolator-Linie (Phasen 1–5).'),
              ('Ihr Ergebnis', 'flag', 'Validierte, Annex-1-konforme Linie mit +60 % Kapazität – Go-live September 2027.'),
              ('Ihre Investition', 'euro', 'Honorar € 1,24 Mio. zzgl. Reisekosten, zahlbar nach abgenommenen Meilensteinen.')]
    cw = (W - 0.3) / 2; chh = 1.95
    for i, (h, ic, b) in enumerate(blocks):
        x = L + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.3)
        f = BLUE if i == 2 else LSAND
        rect(s, x, y, cw, chh, fill=f)
        icon(s, ic, x + 0.3, y + 0.3, 0.45, WHITE if f == BLUE else BLUE)
        text(s, x + 1.0, y + 0.3, cw - 1.3, 0.4, h, size=18, color=WHITE if f == BLUE else BLACK)
        text(s, x + 1.0, y + 0.8, cw - 1.3, 1.0, b, size=14, color=WHITE if f == BLUE else BLACK)

    s = D.slide('content', 'Klarer Leistungsumfang: Was enthalten ist – und was nicht',
                'Angebot | Scope', key='scope',
                notes=N('Scope-Abgrenzung – verhindert Missverständnisse und Nachträge.', 'Mit Leistungsbeschreibung im Angebot abgleichen.',
                        'Out-of-Scope aktiv ansprechen – das schafft Vertrauen.'))
    cw = (W - 0.5) / 2
    for i, (h, ic, col, items) in enumerate([('Im Leistungsumfang', 'check_circle', BLUE, ['Konzept, Basic und Detail Design', 'Ausschreibung und Vergabeunterstützung',
                                                                                            'Projekt- und Terminmanagement', 'CQV inkl. Protokolle und Berichte', 'Schulung des Betriebspersonals']),
                                             ('Nicht im Leistungsumfang', 'cancel', TAUPE, ['Lieferung von Anlagen und Equipment', 'Bauleistungen und Genehmigungsplanung',
                                                                                            'Prozessvalidierung der Produkte', 'Behördliche Zulassungsverfahren', 'Betrieb nach Hypercare'])]):
        x = L + i * (cw + 0.5)
        rect(s, x, 1.5, cw, 0.7, fill=BLUE if i == 0 else SAND, content=h, size=16, color=WHITE if i == 0 else BLACK, anchor='m', margin=(0.25, 0, 0.1, 0))
        for j, it in enumerate(items):
            y = 2.4 + j * 0.62
            icon(s, ic, x + 0.05, y + 0.06, 0.34, col)
            text(s, x + 0.55, y, cw - 0.6, 0.46, it, size=14, anchor='m')
            hline(s, x, y + 0.55, cw, STONE, 0.5)
    sowhat(s, 'Optionale Leistungen (z. B. Prozessvalidierung) können jederzeit per Change Request ergänzt werden.')

    s = D.slide('content', 'Drei Pakete – das Paket „Umsetzung“ bietet das beste Verhältnis',
                'Angebot | Leistungspakete', 'Preise netto zzgl. Reisekosten; Werte illustrativ', key='packages', sticker_='Illustrativ',
                notes=N('Paketauswahl (Good-Better-Best) – lenkt die Diskussion von „ob“ zu „welches“.', 'Leistungen und Preise anpassen; empfohlenes Paket in der Mitte.',
                        'Das mittlere Paket wird am häufigsten gewählt – dort die Empfehlung platzieren.'))
    feats = ['Analyse und Zielbild', 'Konzept und Business Case', 'Detail Design', 'Projektmanagement', 'CQV-Management', 'Hypercare (3 Monate)']
    packs = [('Konzept', '€ 240 Tsd.', [1, 1, 0, 0, 0, 0]), ('Umsetzung', '€ 1,24 Mio.', [1, 1, 1, 1, 1, 0]), ('Komplett', '€ 1,45 Mio.', [1, 1, 1, 1, 1, 1])]
    x0 = L + 4.0; cw = (R - x0 - 2 * 0.2) / 3
    for j, (n_, p, inc) in enumerate(packs):
        x = x0 + j * (cw + 0.2)
        hi = j == 1
        rect(s, x, 1.45, cw, 4.4, fill=LBLUE if hi else LSAND)
        rect(s, x, 1.45, cw, 1.2, fill=BLUE if hi else SAND)
        if hi:
            label(s, x + 0.2, 1.55, cw - 0.4, 'Empfohlen', color=WHITE)
        text(s, x + 0.2, 1.8, cw - 0.4, 0.4, n_, size=18, color=WHITE if hi else BLACK)
        text(s, x + 0.2, 2.2, cw - 0.4, 0.4, p, size=15, color=WHITE if hi else BLUE)
        for i, v in enumerate(inc):
            y = 2.85 + i * 0.5
            if v:
                icon(s, 'check_circle', x + cw / 2 - 0.15, y + 0.06, 0.3, BLUE)
            else:
                hline(s, x + cw / 2 - 0.1, y + 0.21, 0.2, STONE, 1)
    for i, f in enumerate(feats):
        y = 2.85 + i * 0.5
        text(s, L, y, 3.9, 0.42, f, size=13, anchor='m')
        hline(s, L, y + 0.46, R - L, STONE, 0.5)

    s = D.slide('content', 'Honorarübersicht: € 1,24 Mio. über fünf Phasen',
                'Angebot | Honorar', 'Tagessätze gemäß Rahmenvertrag; Werte illustrativ', key='fees', sticker_='Illustrativ',
                notes=N('Transparente Honoraraufstellung je Phase.', 'Werte aus der Kalkulation übernehmen; Summen prüfen.'))
    rows = [['Phase', 'Leistungen', 'Personentage', 'Honorar', 'Abrechnung'],
            ['1 Analyse', 'Ist-Analyse, Potenzial, Roadmap', '120', '€ 156 Tsd.', 'Festpreis'],
            ['2 Konzept', 'Zielbild, URS, Business Case', '180', '€ 234 Tsd.', 'Festpreis'],
            ['3 Engineering', 'Basic und Detail Design', '260', '€ 325 Tsd.', 'Festpreis'],
            ['4 Realisierung', 'Projekt- und Baumanagement', '220', '€ 275 Tsd.', 'Nach Aufwand'],
            ['5 Qualifizierung', 'CQV, Protokolle, Berichte', '200', '€ 250 Tsd.', 'Nach Aufwand'],
            [('Gesamt', {'color': BLUE}), '', ('980', {'color': BLUE}), ('€ 1.240 Tsd.', {'color': BLUE}), '']]
    table(s, L, 1.5, W, rows, colw=[2.4, 4.6, 1.8, 1.9, 1.9], rowh=0.58, size=13, aligns=['l', 'l', 'r', 'r', 'l'])
    sowhat(s, '60 % des Honorars sind als Festpreis kalkuliert – das gibt Ihnen Budgetsicherheit in den Planungsphasen.')

    s = D.slide('content', 'Senior-Expertise dort, wo Entscheidungen fallen',
                'Angebot | Aufwand nach Rolle', 'Personentage je Phase; Werte illustrativ', key='effort', sticker_='Illustrativ',
                notes=N('Zeigt den Team-Mix je Phase – Argument gegen „zu teuer“ und „zu junior“.', 'Diagrammdaten per „Daten bearbeiten“ anpassen.'))
    bar(s, L, 1.4, 8.3, 4.4, ['Analyse', 'Konzept', 'Engineering', 'Realisierung', 'Qualifizierung'],
        [('Partner / Experte', [30, 40, 30, 20, 25]), ('Senior Consultant', [50, 80, 120, 100, 85]), ('Consultant', [40, 60, 110, 100, 90])],
        stacked=True, colors=[BLUE, TAUPE, STONE], legend='b', gap=60, size=12)
    xr = 9.2; wr = R - xr
    kpi(s, xr, 1.6, wr, '15 %', 'Anteil Partner und Experten', bigsize=30)
    kpi(s, xr, 3.2, wr, '45 %', 'Anteil Senior Consultants', bigsize=30)
    sowhat(s, 'In Analyse und Konzept ist der Senior-Anteil am höchsten – dort entstehen 80 % der Kostenwirkung.')

    s = D.slide('content', 'Zahlungsplan: 80 % der Vergütung sind an Ergebnisse gekoppelt',
                'Angebot | Zahlungsplan', 'Werte illustrativ', key='payment', sticker_='Illustrativ',
                notes=N('Meilensteinbasierter Zahlungsplan – reduziert wahrgenommenes Risiko.', 'Meilensteine und Anteile mit dem Vertrag abgleichen.'))
    ms = [('Auftrag', '20 %', 'Bei Beauftragung'), ('M1', '15 %', 'Abnahme Analysebericht'), ('M2', '20 %', 'Freigabe Business Case'),
          ('M3', '20 %', 'Design Freeze'), ('M4', '15 %', 'Mechanical Completion'), ('M5', '10 %', 'Abschluss Qualifizierung')]
    cw = W / 6; y0 = 3.1
    hline(s, L, y0, W, BLACK, 1.25)
    for i, (m, p, b) in enumerate(ms):
        x = L + i * cw
        oval(s, x, y0 - 0.2, 0.4, fill=BLUE if i else BLACK)
        text(s, x, 1.6, cw - 0.2, 0.7, p, size=32, color=BLUE)
        text(s, x, 2.35, cw - 0.2, 0.3, m, size=14)
        text(s, x, y0 + 0.4, cw - 0.25, 0.6, b, size=12)
    rect(s, L, 4.4, W, 1.4, fill=LSAND)
    text(s, L + 0.3, 4.55, W - 0.6, 1.1, bl(['Zahlungsziel 30 Tage nach Rechnungsstellung', 'Leistungen nach Aufwand: monatliche Abrechnung mit Leistungsnachweis',
                                             'Reisekosten nach Aufwand, maximal [x] % des Honorars'], sa=4), size=13)

    s = D.slide('content', 'Kommerzielle Rahmenbedingungen im Überblick',
                'Angebot | Konditionen', 'Es gelten die Allgemeinen Geschäftsbedingungen von Körber [Gesellschaft]', key='terms',
                notes=N('Konditionen-Übersicht für Einkauf und Rechtsabteilung.', 'Mit Rechtsabteilung und Vertragsentwurf abstimmen.'))
    terms = [('description', 'Vertragsmodell', 'Dienstvertrag mit Festpreis-Anteilen je Phase'), ('calendar_month', 'Laufzeit', '[Monat JJJJ] bis [Monat JJJJ]'),
             ('swap_horiz', 'Änderungen', 'Change-Request-Verfahren mit Freigabe durch das Steering Committee'), ('payments', 'Reisekosten', 'Nach Aufwand gemäß Reiserichtlinie'),
             ('shield', 'Haftung', 'Gemäß AGB, begrenzt auf [x] % des Auftragswerts'), ('lock', 'Vertraulichkeit', 'Gegenseitige Geheimhaltungsvereinbarung (NDA)')]
    cw = (W - 2 * 0.3) / 3; chh = 2.0
    for i, (ic, h, b) in enumerate(terms):
        x = L + (i % 3) * (cw + 0.3); y = 1.5 + (i // 3) * (chh + 0.3)
        card(s, x, y, cw, chh, h, b, icon_=ic, hsize=16, bsize=13)

    s = D.slide('content', 'Gemeinsamer Fahrplan bis zum Projektstart am [Datum]',
                'Angebot | Mutual Action Plan', 'Stand: [Datum]', key='map_plan',
                notes=N('Mutual Action Plan – gemeinsamer Plan bis zur Unterschrift; macht den Entscheidungsprozess transparent.',
                        'Schritte mit dem Kunden abstimmen und im CRM als nächste Schritte hinterlegen.',
                        'Ein MAP verkürzt Sales Cycles messbar, weil Verzögerungen sofort sichtbar werden.'))
    rows = [['Schritt', 'Verantwortlich', 'Termin', 'Status'],
            ['Angebotspräsentation', 'Körber', '[TT.MM.]', ''], ['Klärung offener Fragen Einkauf', '[Kunde] Einkauf, Körber', '[TT.MM.]', ''],
            ['Referenzgespräch mit Bestandskunde', 'Körber', '[TT.MM.]', ''], ['Business Case Validierung mit Controlling', '[Kunde] CFO, Körber', '[TT.MM.]', ''],
            ['Freigabe Investitionsausschuss', '[Kunde] Geschäftsführung', '[TT.MM.]', ''], ['Vertragsunterzeichnung', 'Beide', '[TT.MM.]', ''],
            ['Kick-off', 'Beide', '[TT.MM.]', '']]
    tb = table(s, L, 1.5, W, rows, colw=[5.2, 3.8, 1.6, 2.0], rowh=0.52, size=13)
    st = ['g', 'g', 'y', 'n', 'n', 'n', 'n']
    for r in range(1, 8):
        rag(s, L + W * (10.6 / 12.6) + 0.15, 1.5 + r * 0.52 + 0.16, st[r - 1])
        text(s, L + W * (10.6 / 12.6) + 0.45, 1.5 + r * 0.52, 1.5, 0.52, {'g': 'Erledigt', 'y': 'In Arbeit', 'n': 'Offen'}[st[r - 1]], size=12, anchor='m')


# =====================================================================================
def s11(D):
    divider(D, 11, 'Projekt-\nsteuerung', N('Folien für laufende Leadprojekte: Auftrag, Status, Steering Committee, Risiken, Entscheidungen, Abschluss.',
                                             'Wöchentlich bzw. monatlich aktualisieren; Format nicht verändern.',
                                             'Gleiches Statusformat in allen Projekten macht Projekte für Kunden und Management vergleichbar.'))
    s = D.slide('content', 'Projektauftrag [Projektname] auf einen Blick',
                'Projektsteuerung | Projektauftrag', 'Freigegeben durch [Sponsor] am [Datum]', key='charter',
                notes=N('Project Charter für das Kick-off.', 'Alle Felder ausfüllen; vom Sponsor freigeben lassen.'))
    f = [('Ziel', 'Kapazität der sterilen Abfüllung um 60 % erhöhen – Annex-1-konform', True), ('Sponsor', '[Name, Funktion]', False),
         ('Im Umfang', 'Neue Isolator-Linie, Ertüchtigung Linie 3, MES-Anbindung', False), ('Nicht im Umfang', 'Gebäudeerweiterung, Produkttransfers', False),
         ('Ergebnisse', 'Qualifizierte Linie, Betriebsdokumentation, geschultes Personal', False), ('Budget', '€ 18,0 Mio. CAPEX, € 1,24 Mio. Beratung', False),
         ('Zeitrahmen', 'Oktober 2026 bis September 2027', False), ('Erfolgskriterien', 'Go-live im Termin, Budget ±5 %, keine kritische Beobachtung', True)]
    cw = (W - 0.3) / 2; chh = 0.95
    for i, (h, b, hi) in enumerate(f):
        x = L + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.15)
        rect(s, x, y, cw, chh, fill=BLUE if hi else LSAND)
        label(s, x + 0.2, y + 0.15, cw - 0.4, h, color=WHITE if hi else BLUE)
        text(s, x + 0.2, y + 0.42, cw - 0.4, 0.5, b, size=14, color=WHITE if hi else BLACK)

    s = D.slide('content', 'Drei Ziele mit messbaren Schlüsselergebnissen',
                'Projektsteuerung | Ziele und Key Results', 'Stand: [Datum]', key='okr',
                notes=N('Ziele und Key Results mit Fortschritt – für Steering Committee.', 'Fortschrittsbalken: Breite des blauen Balkens anpassen.'))
    okr = [('Kapazität sichern', [('Linie qualifiziert bis 09/2027', 0.55), ('Ausbringung +60 %', 0.2)]),
           ('Compliance gewährleisten', [('Annex-1-Gap-Schließung', 0.8), ('CCS dokumentiert', 0.6)]),
           ('Betrieb befähigen', [('40 Mitarbeitende geschult', 0.3), ('SOPs freigegeben', 0.45)])]
    for i, (o, krs) in enumerate(okr):
        y = 1.5 + i * 1.45
        hline(s, L, y, W, BLACK)
        oval(s, L, y + 0.2, 0.55, fill=BLUE, content='O%d' % (i + 1), size=13, color=WHITE, align='c', anchor='m', margin=0)
        text(s, L + 0.75, y + 0.2, 3.6, 0.55, o, size=17, anchor='m')
        for j, (k, p) in enumerate(krs):
            yy = y + 0.15 + j * 0.6
            text(s, L + 4.6, yy, 3.6, 0.45, k, size=13, anchor='m')
            rect(s, L + 8.4, yy + 0.15, 3.3, 0.16, fill=SAND)
            rect(s, L + 8.4, yy + 0.15, 3.3 * p, 0.16, fill=BLUE)
            text(s, L + 11.85, yy, 0.75, 0.45, '%d %%' % round(p * 100), size=13, anchor='m', align='r')

    s = D.slide('content', 'Status KW [xx]: Im Plan – Entscheidung zur MES-Schnittstelle nötig',
                'Projektsteuerung | Statusbericht', 'Berichtszeitraum: [TT.MM.] – [TT.MM.]', key='status',
                notes=N('Wöchentlicher Status-One-Pager – immer gleiches Format.', 'Gesamtstatus, Fortschritt und vier Felder aktualisieren.',
                        'Der Titel sagt Status und die eine Sache, die das Management wissen muss.'))
    rect(s, L, 1.5, 3.4, 4.3, fill=LSAND)
    label(s, L + 0.25, 1.7, 3, 'Gesamtstatus')
    oval(s, L + 0.25, 2.05, 0.6, fill=BLUE)
    text(s, L + 1.0, 2.05, 2.2, 0.6, 'Im Plan', size=20, anchor='m')
    for i, (k, st) in enumerate([('Termine', 'g'), ('Budget', 'g'), ('Qualität', 'g'), ('Ressourcen', 'y')]):
        y = 2.95 + i * 0.4
        rag(s, L + 0.25, y + 0.07, st); text(s, L + 0.6, y, 2.5, 0.35, k, size=13, anchor='m')
    label(s, L + 0.25, 4.65, 3, 'Fortschritt')
    rect(s, L + 0.25, 5.0, 2.9, 0.2, fill=WHITE); rect(s, L + 0.25, 5.0, 2.9 * 0.48, 0.2, fill=BLUE)
    text(s, L + 0.25, 5.25, 2.9, 0.3, '48 % (Plan: 50 %)', size=12)
    x0 = L + 3.7; cw = (R - x0 - 0.3) / 2; chh = 2.0
    boxes = [('Erreicht', bl(['Basic Design freigegeben', 'Lieferant Isolator beauftragt', 'Risikoanalyse abgeschlossen'], sa=3), LSAND),
             ('Nächste Schritte', bl(['Detail Design HVAC', 'FAT-Planung', 'Schulungskonzept'], sa=3), LSAND),
             ('Top-Risiken', bl(['Lieferzeit Isolator (+4 Wochen)', 'Verfügbarkeit QA-Ressourcen'], sa=3), LSAND),
             ('Entscheidungsbedarf', bl(['Schnittstelle MES–ERP: Middleware vs. Direktanbindung (bis [Datum])'], sa=3), BLUE)]
    for i, (h, b, f_) in enumerate(boxes):
        x = x0 + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.3)
        c = WHITE if f_ == BLUE else BLACK
        rect(s, x, y, cw, chh, fill=f_)
        label(s, x + 0.2, y + 0.2, cw - 0.4, h, color=WHITE if f_ == BLUE else BLUE)
        text(s, x + 0.2, y + 0.5, cw - 0.4, chh - 0.6, b, size=13, color=c)

    s = D.slide('content', 'Vier Workstreams: Drei im Plan, MES-Integration gefährdet',
                'Projektsteuerung | Steering-Committee-Dashboard', 'Stand: [Datum]', key='steerco',
                notes=N('Dashboard für das Steering Committee.', 'Ampeln (Kreise) umfärben: Blau = im Plan, Gelb = gefährdet, Orange = kritisch.',
                        'Gelb und Orange immer mit Maßnahme und Owner im Kommentar.'))
    rows = [['Workstream', 'Lead', 'Termine', 'Budget', 'Qualität', 'Trend', 'Kommentar / Maßnahme'],
            ['Facility & Process', '[Name]', '', '', '', '', 'Basic Design freigegeben'],
            ['CQV', '[Name]', '', '', '', '', 'Qualifizierungsplan in Review'],
            ['MES & Daten', '[Name]', '', '', '', '', 'ERP-Schnittstelle offen – Entscheidung SteerCo'],
            ['Organisation', '[Name]', '', '', '', '', 'Schulungskonzept im Entwurf']]
    tb = table(s, L, 1.5, W, rows, colw=[2.4, 1.6, 1.1, 1.1, 1.1, 1.0, 4.3], rowh=0.7, size=13, aligns=['l', 'l', 'c', 'c', 'c', 'c', 'l'])
    st = [['g', 'g', 'g'], ['g', 'g', 'y'], ['y', 'r', 'g'], ['g', 'g', 'g']]
    tr = ['trending_up', 'arrow_forward', 'trending_down', 'arrow_forward']
    xs = [L + W * sum([2.4, 1.6, 1.1, 1.1, 1.1, 1.0, 4.3][:k]) / 12.6 for k in range(8)]
    for r in range(4):
        y = 1.5 + 0.7 * (r + 1)
        for c in range(3):
            rag(s, (xs[2 + c] + xs[3 + c]) / 2 - 0.12, y + 0.23, st[r][c], 0.24)
        icon(s, tr[r], (xs[5] + xs[6]) / 2 - 0.15, y + 0.2, 0.3, BLUE if r != 2 else ORANGE)
    legend_rag(s, L, 5.3)

    s = D.slide('content', 'Meilensteine: Zwei erreicht, einer mit zwei Wochen Verzug',
                'Projektsteuerung | Meilenstein-Tracker', 'Stand: [Datum]', key='mstracker',
                notes=N('Meilensteinverfolgung Plan vs. Prognose.', 'Prognosetermine wöchentlich aktualisieren; Abweichung in Tagen.'))
    rows = [['Meilenstein', 'Plan', 'Prognose / Ist', 'Abweichung', 'Status'],
            ['M1 Analysebericht abgenommen', '15.11.2026', '13.11.2026', '–2 Tage', 'Erreicht'],
            ['M2 Business Case freigegeben', '31.01.2027', '31.01.2027', '0', 'Erreicht'],
            ['M3 Design Freeze', '30.04.2027', '14.05.2027', '+14 Tage', 'Gefährdet'],
            ['M4 Mechanical Completion', '31.07.2027', '31.07.2027', '0', 'Im Plan'],
            ['M5 Go-live', '30.09.2027', '30.09.2027', '0', 'Im Plan']]
    tb = table(s, L, 1.5, W, rows, colw=[4.4, 1.9, 2.2, 1.8, 2.3], rowh=0.62, size=13, aligns=['l', 'c', 'c', 'c', 'l'])
    m = {'Erreicht': 'g', 'Gefährdet': 'y', 'Im Plan': 'n'}
    for r in range(1, 6):
        stt = rows[r][4]
        rag(s, L + W * (10.3 / 12.6) + 0.12, 1.5 + r * 0.62 + 0.21, m[stt])
        fill_tf(tb.cell(r, 4).text_frame, '      ' + stt, size=13, anchor='m')
        if rows[r][3].startswith('+'):
            fill_tf(tb.cell(r, 3).text_frame, rows[r][3], size=13, color=ORANGE, align='c')
    sowhat(s, 'Der Verzug bei M3 wird durch Parallelisierung der HVAC-Planung aufgeholt – M5 ist nicht gefährdet.')

    s = D.slide('content', 'Budget: 46 % verbraucht bei 48 % Fortschritt',
                'Projektsteuerung | Budgetverlauf', 'Quelle: Projektcontrolling; kumuliert in € Tsd.; Werte illustrativ', key='budget', sticker_='Illustrativ',
                notes=N('Budget-Burn-down: Plan vs. Ist vs. Prognose.', 'Diagrammdaten monatlich aktualisieren.'))
    months = ['Okt', 'Nov', 'Dez', 'Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep']
    plan = [60, 150, 260, 390, 500, 620, 740, 850, 960, 1060, 1160, 1240]
    ist = [55, 140, 240, 370, 470, 570, None, None, None, None, None, None]
    prog = [None, None, None, None, None, 570, 690, 800, 910, 1020, 1130, 1220]
    cd = CategoryChartData(); cd.categories = months
    cd.add_series('Plan', plan); cd.add_series('Ist', ist); cd.add_series('Prognose', prog)
    gf = s.shapes.add_chart(XCT.LINE, I(L), I(1.4), I(8.6), I(4.4), cd)
    ch = gf.chart; ch.font.size = Pt(12)
    from pptx.enum.dml import MSO_LINE
    for i, (ser, c, d) in enumerate(zip(ch.plots[0].series, [STONE, BLUE, BLUE], [None, None, MSO_LINE.DASH])):
        ser.format.line.fill.solid(); setc(ser.format.line.color, c); ser.format.line.width = Pt(2.5)
        ser.smooth = False
        if d: ser.format.line.dash_style = d
    va = ch.value_axis; va.has_major_gridlines = True
    va.major_gridlines.format.line.color.rgb = RGBColor.from_string(HEX['grid']); va.format.line.fill.background()
    va.tick_labels.font.size = Pt(11)
    ch.category_axis.tick_labels.font.size = Pt(11); ch.category_axis.major_tick_mark = XL_TICK_MARK.NONE
    ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
    xr = 9.5; wr = R - xr
    kpi(s, xr, 1.6, wr, '€ 570 Tsd.', 'Ist-Kosten (46 % des Budgets)', bigsize=26)
    kpi(s, xr, 3.0, wr, '€ –20 Tsd.', 'Prognose zum Projektende vs. Plan', bigsize=26)
    sowhat(s, 'Das Projekt liegt leicht unter Budget – die Prognose zum Projektende beträgt € 1.220 Tsd.')

    s = D.slide('content', 'Zwei Risiken erfordern Maßnahmen vor dem Design Freeze',
                'Projektsteuerung | Risikomatrix', 'Stand: [Datum]', key='riskmatrix',
                notes=N('Risikomatrix (Eintrittswahrscheinlichkeit × Auswirkung).', 'Nummerierte Kreise in die passende Zelle verschieben; Liste rechts pflegen.'))
    gx0, gy0, cs = L + 0.6, 1.45, 1.42
    heat = [[AMBER, ORANGE, ORANGE], [SAND, AMBER, ORANGE], [LSAND, SAND, AMBER]]
    for r in range(3):
        for c in range(3):
            rect(s, gx0 + c * (cs + 0.05), gy0 + r * (cs + 0.05), cs, cs, fill=heat[r][c])
    text(s, gx0, gy0 + 3 * (cs + 0.05) + 0.05, 3 * cs, 0.3, 'Eintrittswahrscheinlichkeit →', size=11, align='r')
    tb = text(s, 0, 0, 3 * cs, 0.35, 'Auswirkung →', size=11, align='r')
    tb.rotation = 270; tb.left = I(gx0 - 0.4 - 1.5 * cs); tb.top = I(gy0 + 1.5 * cs - 0.17)
    rs = [(1, 2, 0), (2, 1, 0), (3, 1, 1), (4, 0, 2), (5, 2, 2)]
    for n_, c, r in rs:
        num(s, gx0 + c * (cs + 0.05) + cs / 2 - 0.22, gy0 + r * (cs + 0.05) + cs / 2 - 0.22, n_, 0.44, filled=n_ <= 2, color=BLACK if n_ <= 2 else BLACK)
    xr = 6.0; wr = R - xr
    items = [('Lieferverzug Isolator', 'Alternativer Lieferslot, Pönale', True), ('Fehlende QA-Kapazität', 'Externe Unterstützung ab [Monat]', True),
             ('Schnittstelle MES–ERP', 'Entscheidung SteerCo [Datum]', False), ('Kostensteigerung HVAC', 'Festpreisangebot einholen', False),
             ('Personalfluktuation', 'Wissensdokumentation, Stellvertretung', False)]
    for i, (h, m_, hi) in enumerate(items):
        y = 1.5 + i * 0.86
        num(s, xr, y + 0.08, i + 1, 0.38, filled=hi, color=BLACK)
        text(s, xr + 0.55, y, wr - 0.55, 0.32, h, size=14)
        text(s, xr + 0.55, y + 0.34, wr - 0.55, 0.35, 'Maßnahme: ' + m_, size=12, color=DGRAY)
        if i < 4:
            hline(s, xr + 0.55, y + 0.78, wr - 0.55, STONE, 0.5)

    s = D.slide('content', 'Risiko-Log: Maßnahmen, Verantwortliche und Termine',
                'Projektsteuerung | Risiko-Log', 'Stand: [Datum]', key='risklog',
                notes=N('Detailliertes Risikoregister als Anhang zum Statusbericht.', 'Zeilen ergänzen; Bewertung W × A (1–3).'))
    rows = [['#', 'Risiko', 'W', 'A', 'Score', 'Maßnahme', 'Owner', 'Termin'],
            ['1', 'Lieferverzug Isolator', '3', '3', '9', 'Alternativer Lieferslot, Pönale vereinbaren', '[Name]', '[TT.MM.]'],
            ['2', 'Fehlende QA-Kapazität', '2', '3', '6', 'Externe Unterstützung beauftragen', '[Name]', '[TT.MM.]'],
            ['3', 'Schnittstelle MES–ERP', '2', '2', '4', 'Entscheidungsvorlage für SteerCo', '[Name]', '[TT.MM.]'],
            ['4', 'Kostensteigerung HVAC', '1', '3', '3', 'Festpreisangebot einholen', '[Name]', '[TT.MM.]'],
            ['5', 'Personalfluktuation', '3', '1', '3', 'Wissensdokumentation, Stellvertretung', '[Name]', '[TT.MM.]']]
    tb = table(s, L, 1.5, W, rows, colw=[0.5, 3.0, 0.6, 0.6, 0.9, 4.2, 1.4, 1.4], rowh=0.6, size=13, aligns=['l', 'l', 'c', 'c', 'c', 'l', 'l', 'l'])
    for r in range(1, 6):
        v = int(rows[r][4]); c = tb.cell(r, 4)
        c.fill.solid(); setc(c.fill.fore_color, ORANGE if v >= 6 else (AMBER if v >= 4 else SAND))
        fill_tf(c.text_frame, str(v), size=13, align='c')
    text(s, L, 5.3, W, 0.3, 'W = Wahrscheinlichkeit, A = Auswirkung (je 1 = gering bis 3 = hoch); Score = W × A', size=11, color=DGRAY)

    s = D.slide('content', 'Entscheidungsvorlage: Schnittstelle MES–ERP über Middleware umsetzen',
                'Projektsteuerung | Entscheidungsvorlage', 'Vorlage für Steering Committee am [Datum]', key='decision',
                notes=N('Standardformat für Entscheidungen im Steering Committee.', 'Frage, Optionen, Empfehlung und Auswirkungen ausfüllen.',
                        'Vorab mit den Entscheidern abstimmen – im Gremium wird nur noch bestätigt.'))
    rect(s, L, 1.5, W, 0.7, fill=LSAND)
    text(s, L + 0.25, 1.5, W - 0.5, 0.7, [{'t': [('Entscheidungsfrage:  ', {'color': BLUE}), ('Wie binden wir das MES an das ERP-System an?', {})]}], size=15, anchor='m')
    opts = [('Option A', 'Direktanbindung', ['Kosten € 80 Tsd.', '6 Wochen', 'Hohe Abhängigkeit bei ERP-Updates'], False),
            ('Option B', 'Middleware', ['Kosten € 120 Tsd.', '8 Wochen', 'Wiederverwendbar für weitere Werke'], True)]
    cw = 4.0
    for i, (o, h, b, hi) in enumerate(opts):
        x = L + i * (cw + 0.3)
        rect(s, x, 2.45, cw, 3.35, fill=BLUE if hi else LSAND)
        label(s, x + 0.25, 2.65, cw - 0.5, o + (' – empfohlen' if hi else ''), color=WHITE if hi else BLUE)
        text(s, x + 0.25, 2.95, cw - 0.5, 0.4, h, size=18, color=WHITE if hi else BLACK)
        text(s, x + 0.25, 3.5, cw - 0.5, 2.0, bl(b, sa=6), size=13, color=WHITE if hi else BLACK)
    xr = L + 2 * cw + 0.7; wr = R - xr
    label(s, xr, 2.5, wr, 'Auswirkungen der Empfehlung')
    for i, (a, b) in enumerate([('Termin', '+2 Wochen, ohne Einfluss auf Go-live'), ('Budget', '+€ 40 Tsd. aus Projektreserve'), ('Nutzen', 'Rollout auf Werk 2 spart ca. € 60 Tsd.')]):
        y = 2.85 + i * 0.75
        hline(s, xr, y, wr, STONE, 0.5)
        text(s, xr, y + 0.08, 1.2, 0.6, a, size=13, color=BLUE)
        text(s, xr + 1.2, y + 0.08, wr - 1.2, 0.6, b, size=13)
    rrect(s, xr, 5.3, wr, 0.5, fill=YELLOW, radius=0.25, content='Bitte: Freigabe Option B', size=13, align='c', anchor='m', margin=0)

    s = D.slide('content', 'Change Request 07: Zusätzliches Format verlängert Phase 3 um 3 Wochen',
                'Projektsteuerung | Change Request', 'CR-Nr. [07]; eingereicht am [Datum] von [Name]', key='changerequest',
                notes=N('Standardformat für Änderungsanträge.', 'Alle Felder ausfüllen; Freigabe im Steering Committee.'))
    left = [('Beschreibung', 'Integration eines dritten Vial-Formats (2R) in das Linienkonzept'),
            ('Begründung', 'Neues Produkt im Portfolio ab 2028; Nachrüstung später deutlich teurer'),
            ('Empfehlung', 'Annehmen – Mehrkosten durch Vermeidung späterer Umbauten gedeckt')]
    for i, (h, b) in enumerate(left):
        y = 1.5 + i * 1.12
        hline(s, L, y, 6.6, BLACK)
        label(s, L, y + 0.12, 6.6, h)
        text(s, L, y + 0.42, 6.6, 0.65, b, size=14)
    xr = 7.4; wr = R - xr
    label(s, xr, 1.5, wr, 'Auswirkungen')
    for i, (k, v, st) in enumerate([('Termin', '+3 Wochen Phase 3; Go-live unverändert', 'y'), ('Kosten', '+€ 85 Tsd. Beratung, +€ 0,4 Mio. CAPEX', 'y'),
                                    ('Qualität', 'Keine negative Auswirkung', 'g'), ('Risiko', 'Gering – Format bereits validiert bei Lieferant', 'g')]):
        y = 1.85 + i * 0.75
        rect(s, xr, y, wr, 0.65, fill=LSAND)
        rag(s, xr + 0.2, y + 0.23, st)
        text(s, xr + 0.55, y, 1.2, 0.65, k, size=13, anchor='m')
        text(s, xr + 1.75, y, wr - 1.9, 0.65, v, size=12, anchor='m')
    for i, t in enumerate(['Freigabe PL Kunde', 'Freigabe PL Körber', 'Freigabe SteerCo']):
        x = L + i * 4.3
        hline(s, x, 5.55, 3.9, BLACK)
        text(s, x, 5.6, 3.9, 0.3, t + ' / Datum', size=11, color=DGRAY)

    s = D.slide('content', 'Lessons Learned: Drei Erkenntnisse für künftige Projekte',
                'Projektsteuerung | Lessons Learned', 'Workshop mit Projektteam am [Datum]', key='lessons',
                notes=N('Retrospektive am Projektende oder nach Meilensteinen.', 'Mit Team erarbeiten; Erkenntnisse in Wissensdatenbank übernehmen.'))
    cols = [('thumb_up', 'Was gut lief', ['Tandem-Projektleitung', 'Frühe Einbindung der QA', 'Wöchentliche Entscheidungsrunde']),
            ('build', 'Was wir verbessern', ['Lieferanten früher einbinden', 'Datenzugang vor Projektstart klären', 'Ressourcenplanung QA']),
            ('school', 'Was wir übernehmen', ['Standard-Templates für CQV', 'Risikobasierter Qualifizierungsansatz', 'Change-Request-Prozess'])]
    cw = (W - 2 * 0.5) / 3
    for i, (ic, h, b) in enumerate(cols):
        x = L + i * (cw + 0.5)
        colhead(s, x, 1.5, cw, None, h, bl(b, sa=8), icon_=ic, hsize=20, bsize=14, bh=2.2)
    sowhat(s, 'Die frühe Einbindung der QA hat die Qualifizierung um sechs Wochen verkürzt – künftig Standard in allen Projekten.')

    s = D.slide('content', 'Projektabschluss: Alle Ziele erreicht, Übergabe an den Betrieb erfolgt',
                'Projektsteuerung | Abschluss', 'Abschlussbericht vom [Datum]', key='closure',
                notes=N('Abschlussfolie für das letzte Steering Committee – Basis für die Referenz.', 'Ziel- und Ist-Werte eintragen; Übergabepunkte prüfen.',
                        'Direkt im Anschluss Referenzfreigabe und Zufriedenheitsbefragung anstoßen.'))
    rows = [['Ziel', 'Soll', 'Ist', ''],
            ['Go-live', '30.09.2027', '23.09.2027', ''], ['Budget', '€ 18,0 Mio.', '€ 17,6 Mio.', ''],
            ['Kapazität', '+60 %', '+62 %', ''], ['Inspektion', '0 kritische', '0 kritische', '']]
    table(s, L, 1.5, 7.2, rows, colw=[2.2, 2.0, 2.0, 1.0], rowh=0.62, size=14, aligns=['l', 'c', 'c', 'c'])
    for r in range(1, 5):
        icon(s, 'check_circle', L + 6.45, 1.5 + r * 0.62 + 0.15, 0.32, BLUE)
    xr = 8.1; wr = R - xr
    rect(s, xr, 1.5, wr, 3.65, fill=LSAND)
    label(s, xr + 0.25, 1.7, wr - 0.5, 'Übergabe an den Betrieb')
    for i, t in enumerate(['Betriebsdokumentation', 'SOPs freigegeben', 'Personal geschult', 'Ersatzteilkonzept', 'Hypercare bis [Datum]']):
        y = 2.05 + i * 0.6
        icon(s, 'task_alt', xr + 0.25, y + 0.05, 0.3, BLUE)
        text(s, xr + 0.7, y, wr - 0.9, 0.4, t, size=14, anchor='m')
    sowhat(s, 'Projekt eine Woche vor Plan und 2 % unter Budget abgeschlossen.')


# =====================================================================================
def s12(D):
    divider(D, 12, 'Account-\nmanage-\nment', N('Account-Planung, Whitespace, Pipeline, Quartalsreview, Kundengesundheit.',
                                               'Daten aus dem CRM übernehmen; überwiegend interne Folien.',
                                               'Diese Folien machen den Beitrag von Marketing und Vertrieb zum Umsatz sichtbar.'))
    s = D.slide('content', 'Account-Plan [Kunde] 2027: Umsatz von € 1,2 auf 2,0 Mio. steigern',
                'Account-Management | Account-Plan (intern)', 'Quelle: CRM, Stand [Datum]', key='accountplan', sticker_='Intern',
                notes=N('Account-Plan auf einer Seite für Key Accounts.', 'Felder jährlich erstellen, quartalsweise aktualisieren.',
                        'Umsatzziel, Whitespace und Stakeholder-Lücken gehören zusammen – sonst bleibt der Plan Wunschdenken.'))
    k = [('€ 1,2 Mio.', 'Umsatz 2026'), ('€ 2,0 Mio.', 'Ziel 2027'), ('€ 3,4 Mio.', 'Pipeline (ungewichtet)'), ('4 von 6', 'Buying-Center-Rollen abgedeckt')]
    cw = (W - 3 * 0.3) / 4
    for i, (a, b) in enumerate(k):
        x = L + i * (cw + 0.3)
        rect(s, x, 1.5, cw, 1.3, fill=BLUE if i == 1 else LSAND)
        text(s, x + 0.2, 1.6, cw - 0.4, 0.6, a, size=26, color=WHITE if i == 1 else BLUE)
        text(s, x + 0.2, 2.25, cw - 0.4, 0.4, b, size=12, color=WHITE if i == 1 else BLACK)
    cols = [('Strategische Ziele', ['Rahmenvertrag Engineering', 'Zweiter Standort (Werk B)', 'Executive-Beziehung CFO']),
            ('Wachstumsfelder', ['Digitalisierung & MES', 'Annex-1-Assessments', 'OEE-Programm']),
            ('Aktivitäten Q1–Q2', ['Executive-Dinner mit COO', 'Benchmark-Workshop', 'Referenzbesuch Werk X'])]
    cw3 = (W - 2 * 0.3) / 3
    for i, (h, b) in enumerate(cols):
        x = L + i * (cw3 + 0.3)
        colhead(s, x, 3.1, cw3, None, h, bl(b, sa=6), hsize=16, bsize=13, bh=1.6)
    sowhat(s, 'CFO und COO sind noch nicht eingebunden – ohne sie ist das Umsatzziel 2027 nicht erreichbar.')

    s = D.slide('content', 'Whitespace: Größtes Potenzial liegt in Digitalisierung an zwei Werken',
                'Account-Management | Whitespace-Analyse (intern)', 'Quelle: CRM, Account-Team; Stand [Datum]', key='whitespace', sticker_='Intern',
                notes=N('Whitespace-Matrix: Wo verkaufen wir schon, wo liegt Potenzial?', 'Felder je Standort × Leistung einfärben.',
                        'Jede blaue Outline-Zelle sollte eine Opportunity im CRM haben.'))
    sites = ['Werk A (DE)', 'Werk B (DE)', 'Werk C (IE)', 'Werk D (US)']
    svcs = ['Facility Design', 'CQV', 'Digitalisierung', 'OpEx', 'Supply Chain', 'PMO']
    M = [['a', 'a', 'o', 'a', 'n', 'a'], ['o', 'a', 'o', 'n', 'n', 'o'], ['n', 'o', 'n', 'o', 'n', 'n'], ['n', 'n', 'o', 'n', 'o', 'n']]
    x0 = L + 2.6; cw = (R - x0) / 6; rh = 0.85
    for j, sv in enumerate(svcs):
        text(s, x0 + j * cw, 1.45, cw, 0.5, sv, size=12, align='c', anchor='b', color=BLUE)
    hline(s, L, 2.0, W, BLACK)
    for i, st_ in enumerate(sites):
        y = 2.1 + i * rh
        text(s, L, y, 2.5, rh - 0.1, st_, size=14, anchor='m')
        for j in range(6):
            v = M[i][j]
            x = x0 + j * cw + 0.08
            if v == 'a':
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=BLUE, content='Kunde', size=11, color=WHITE, align='c', anchor='m')
            elif v == 'o':
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=WHITE, line=BLUE, lw=1.5, content='Potenzial', size=11, color=BLUE, align='c', anchor='m')
            else:
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=LSAND)
    for i, (f, l_, t) in enumerate([(BLUE, None, 'Bereits beauftragt'), (WHITE, BLUE, 'Potenzial (Opportunity)'), (LSAND, None, 'Nicht relevant')]):
        rect(s, L + i * 2.8, 5.65, 0.22, 0.22, fill=f, line=l_); text(s, L + i * 2.8 + 0.32, 5.61, 2.4, 0.3, t, size=11)

    s = D.slide('content', 'Pipeline: € 6,4 Mio. in Bearbeitung, € 1,9 Mio. gewichtet',
                'Account-Management | Pipeline-Trichter (intern)', 'Quelle: CRM; Stand [Datum]; Werte illustrativ', key='funnel', sticker_='Intern',
                notes=N('Pipeline nach Vertriebsphasen mit Konversionsraten.', 'Werte aus dem CRM-Report übernehmen.',
                        'Konversionsraten zwischen den Stufen zeigen, wo Marketing und Vertrieb ansetzen müssen.'))
    stages = [('Lead qualifiziert', 42, '€ 6,4 Mio.', None), ('Bedarf bestätigt', 24, '€ 4,1 Mio.', '57 %'), ('Angebot', 11, '€ 2,6 Mio.', '46 %'),
              ('Verhandlung', 6, '€ 1,5 Mio.', '55 %'), ('Gewonnen', 4, '€ 1,0 Mio.', '67 %')]
    cx = L + 3.6; maxw = 7.0
    for i, (n_, c, v, cr) in enumerate(stages):
        w_ = maxw * (1 - i * 0.17)
        y = 1.8 + i * 0.82
        rect(s, cx - w_ / 2, y, w_, 0.7, fill=BLUE if i == 4 else (MBLUE if i == 3 else SAND), content='%d  |  %s' % (c, v), size=14,
             color=WHITE if i == 4 else BLACK, align='c', anchor='m')
        text(s, cx + maxw / 2 + 0.2, y, 2.6, 0.72, n_, size=14, anchor='m')
        if cr:
            text(s, cx + maxw / 2 + 2.8, y - 0.2, 1.6, 0.4, '↓ ' + cr, size=12, color=BLUE, anchor='m')
    label(s, cx + maxw / 2 + 2.8, 1.45, 1.6, 'Konversion', color=DGRAY)
    label(s, cx - maxw / 2, 1.45, 4, 'Anzahl  |  Volumen', color=DGRAY)

    s = D.slide('content', 'Abschlussreife Opportunities haben sich in vier Quartalen verdoppelt',
                'Account-Management | Pipeline-Entwicklung (intern)', 'Quelle: CRM; € Mio.; Werte illustrativ', key='pipeline', sticker_='Intern',
                notes=N('Entwicklung der Pipeline nach Phasen über Zeit.', 'Daten quartalsweise aus dem CRM übernehmen.'))
    bar(s, L, 1.4, 8.4, 4.4, ['Q4 2025', 'Q1 2026', 'Q2 2026', 'Q3 2026'],
        [('Angebot / Verhandlung', [0.8, 1.0, 1.3, 1.6]), ('Bedarf bestätigt', [1.4, 1.5, 1.6, 1.5]), ('Lead qualifiziert', [2.0, 2.4, 2.2, 2.3])],
        stacked=True, colors=[BLUE, TAUPE, STONE], legend='b', gap=55, fmt='0.0', size=12)
    xr = 9.3; wr = R - xr
    kpi(s, xr, 1.6, wr, '×2,0', 'Abschlussreife Pipeline', 'Q4 2025 → Q3 2026', bigsize=30)
    kpi(s, xr, 3.4, wr, '42 %', 'Leads aus Marketing-Kampagnen', 'Webinare, Benchmark-Studie', bigsize=30)
    sowhat(s, 'Thought-Leadership-Kampagnen liefern 42 % der Leads – Marketing trägt messbar zur Pipeline bei.')

    s = D.slide('content', 'Quartalsreview Q3: Ziele übertroffen, zwei neue Opportunities',
                'Account-Management | Quartalsreview mit dem Kunden', 'Stand: [Datum]', key='qbr',
                notes=N('Quartalsreview (QBR) mit dem Kunden – zeigt Wertbeitrag und öffnet neue Themen.', 'KPIs, Highlights und Ausblick je Quartal aktualisieren.',
                        'Immer mit dem Wert für den Kunden beginnen, erst dann über neue Projekte sprechen.'))
    k = [('3', 'Projekte aktiv'), ('98 %', 'Meilensteine im Plan'), ('9,1 / 10', 'Zufriedenheit'), ('€ 0,8 Mio.', 'realisierter Nutzen')]
    cw = (W - 3 * 0.3) / 4
    for i, (a, b) in enumerate(k):
        kpi(s, L + i * (cw + 0.3), 1.5, cw, a, b, bigsize=30)
    cw2 = (W - 0.3) / 2
    for i, (h, b) in enumerate([('Highlights Q3', ['Design Freeze Werk A erreicht', 'Annex-1-Assessment Werk C abgeschlossen', 'Schulung von 25 Mitarbeitenden']),
                                ('Ausblick Q4', ['Go-live MES Pilot', 'Workshop Digitalisierung Werk B', 'Angebot OEE-Programm'])]):
        x = L + i * (cw2 + 0.3)
        rect(s, x, 3.0, cw2, 2.8, fill=LSAND if i == 0 else LBLUE)
        label(s, x + 0.25, 3.2, cw2 - 0.5, h)
        text(s, x + 0.25, 3.55, cw2 - 0.5, 2.1, bl(b, sa=8), size=14)

    s = D.slide('content', 'Kundengesundheit: Hohe Zufriedenheit, Zugang zur Geschäftsführung fehlt',
                'Account-Management | Health Score (intern)', 'Quelle: CRM, Befragung, Account-Team; Stand [Datum]', key='health', sticker_='Intern',
                notes=N('Frühwarnsystem für Key Accounts.', 'Kriterien und Schwellenwerte einheitlich für alle Accounts verwenden.',
                        'Der Health Score gehört als Feld ins CRM – dann ist er Portfolio-weit auswertbar.'))
    rows = [['Dimension', 'Indikator', 'Wert', 'Status', 'Maßnahme'],
            ['Zufriedenheit', 'Projektbewertung (1–10)', '9,1', '', '—'],
            ['Beziehung', 'Abgedeckte Buying-Center-Rollen', '4 / 6', '', 'Executive-Termin CFO, COO'],
            ['Wachstum', 'Umsatz vs. Vorjahr', '+18 %', '', '—'],
            ['Aktivität', 'Kontakte letzte 90 Tage', '23', '', '—'],
            ['Risiko', 'Wettbewerb im Account aktiv', 'Ja', '', 'Battlecard, Referenzbesuch']]
    tb = table(s, L, 1.5, W, rows, colw=[2.2, 3.6, 1.4, 1.4, 4.0], rowh=0.62, size=13, aligns=['l', 'l', 'c', 'c', 'l'])
    stt = ['g', 'y', 'g', 'g', 'r']
    cx = L + W * (7.2 + 0.7) / 12.6
    for r in range(5):
        rag(s, cx - 0.12, 1.5 + (r + 1) * 0.62 + 0.19, stt[r], 0.24)
    legend_rag(s, L, 5.5)

    s = D.slide('content', 'Die Kundenzufriedenheit steigt seit drei Quartalen',
                'Account-Management | Zufriedenheit', 'Quelle: Projektbefragung nach Meilensteinen, n = [xx]; Werte illustrativ', key='nps', sticker_='Illustrativ',
                notes=N('Entwicklung von Zufriedenheit bzw. NPS über die Zeit.', 'Daten aus Befragungstool übernehmen.'))
    line_chart(s, L, 1.4, 8.6, 4.4, ['Q4 25', 'Q1 26', 'Q2 26', 'Q3 26'], [('[Kunde]', [7.8, 8.2, 8.7, 9.1]), ('Portfolio-Durchschnitt', [8.0, 8.1, 8.1, 8.3])],
               fmt='0.0', labels='all', min_=6, max_=10, size=12)
    xr = 9.5; wr = R - xr
    label(s, xr, 1.5, wr, 'Treiber laut Befragung')
    text(s, xr, 1.85, wr, 3.0, bl(['Termintreue', 'Fachliche Tiefe des Teams', 'Proaktive Kommunikation von Risiken'], sa=8), size=14)

    s = D.slide('content', 'Wachstumspfad: Vom Assessment zur langfristigen Partnerschaft',
                'Account-Management | Cross- und Upselling', 'Werte illustrativ', key='growth', sticker_='Illustrativ',
                notes=N('Roadmap für die Entwicklung eines Accounts – intern oder mit dem Kunden.', 'Angebote und Jahre anpassen.',
                        'Land and Expand: Jede Stufe baut auf einem nachweisbaren Ergebnis der vorherigen auf.'))
    steps = [('2026', 'Einstieg', 'Annex-1-Assessment', '€ 0,2 Mio.'), ('2027', 'Projekt', 'Neue Isolator-Linie', '€ 1,2 Mio.'),
             ('2028', 'Ausweitung', 'MES-Rollout Werk B', '€ 0,9 Mio.'), ('2029+', 'Partnerschaft', 'Rahmenvertrag Engineering', '€ 1,5 Mio. p. a.')]
    cw = (W - 3 * 0.25) / 4
    for i, (y_, st_, o, v) in enumerate(steps):
        x = L + i * (cw + 0.25)
        h = 1.4 + i * 0.75
        yb = 5.8 - h
        rect(s, x, yb, cw, h, fill=BLUE if i == 3 else (MBLUE if i == 2 else (SAND if i == 1 else LSAND)))
        c = WHITE if i == 3 else BLACK
        text(s, x + 0.2, yb + 0.15, cw - 0.4, 0.3, y_ + ' | ' + st_, size=12, color=c)
        text(s, x + 0.2, yb + 0.5, cw - 0.4, 0.6, o, size=15, color=c)
        text(s, x + 0.2, yb + h - 0.5, cw - 0.4, 0.4, v, size=14, color=WHITE if i == 3 else BLUE)


# =====================================================================================
def s13(D):
    divider(D, 13, 'Frame-\nworks', N('Klassische Analyse-Frameworks im Körber-Design.', 'Inhalte ersetzen, Struktur beibehalten.',
                                      'Frameworks strukturieren – die Erkenntnis gehört trotzdem in den Titel.'))
    s = D.slide('content', 'SWOT: Starke Technologieposition, Abhängigkeit in der Lieferkette',
                'Frameworks | SWOT-Analyse', key='swot',
                notes=N('SWOT für Standort-, Projekt- oder Wettbewerbsanalysen.', 'Je Quadrant 3–4 Punkte; Implikation in den Titel.'))
    q = [('Stärken', ['Moderne Isolator-Technologie', 'Erfahrenes QA-Team', 'Hohe Lieferzuverlässigkeit'], BLUE),
         ('Schwächen', ['Papierbasierte Dokumentation', 'Lange Rüstzeiten', 'Insellösungen in der IT'], LSAND),
         ('Chancen', ['Wachstum Biologika', 'Förderprogramme Digitalisierung', 'Regionalisierung der Lieferketten'], LSAND),
         ('Risiken', ['Single Source bei Primärpackmitteln', 'Fachkräftemangel', 'Steigende regulatorische Anforderungen'], SAND)]
    cw, chh = (W - 0.3) / 2, 2.1
    for i, (h, b, f) in enumerate(q):
        x = L + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.2)
        c = WHITE if f == BLUE else BLACK
        rect(s, x, y, cw, chh, fill=f)
        text(s, x + 0.3, y + 0.2, 0.9, 0.9, h[0], size=44, color=WHITE if f == BLUE else BLUE)
        text(s, x + 1.25, y + 0.25, cw - 1.5, 0.4, h, size=17, color=c)
        text(s, x + 1.25, y + 0.75, cw - 1.5, 1.3, bl(b, sa=4), size=13, color=c)

    s = D.slide('content', 'Five Forces: Lieferantenmacht ist die größte Bedrohung der Marge',
                'Frameworks | Branchenanalyse nach Porter', key='fiveforces',
                notes=N('Branchenstruktur-Analyse (Porter).', 'Intensität je Kraft per Harvey Ball (0–4) und Kernaussage anpassen.'))
    cx, cy = 6.67, 3.6
    def force(x, y, h, b, q, hi=False):
        rect(s, x, y, 3.5, 1.25, fill=BLUE if hi else LSAND)
        text(s, x + 0.2, y + 0.12, 2.6, 0.35, h, size=14, color=WHITE if hi else BLACK)
        text(s, x + 0.2, y + 0.5, 3.1, 0.7, b, size=11, color=WHITE if hi else DGRAY)
        harvey(s, x + 3.0, y + 0.12, 0.32, q)
    rect(s, cx - 1.75, cy - 0.65, 3.5, 1.3, fill=BLACK, content=[{'t': 'Wettbewerb in der Branche', 'size': 14}, {'t': 'hoch – Preisdruck bei Generika', 'size': 11}], color=WHITE, align='c', anchor='m')
    force(cx - 1.75, 1.45, 'Neue Anbieter', 'Hohe Eintrittsbarrieren durch Regulatorik', 1)
    force(cx - 1.75, 4.55, 'Ersatzprodukte', 'Biosimilars und neue Therapieformen', 2)
    force(L, cy - 0.62, 'Lieferanten', 'Wenige Anbieter für Primärpackmittel', 4, True)
    force(R - 3.5, cy - 0.62, 'Abnehmer', 'Konzentration bei Großhandel und Kassen', 3)
    for (x1, y1, x2, y2) in [(cx, 2.7, cx, cy - 0.65), (cx, 4.55, cx, cy + 0.65), (L + 3.5, cy, cx - 1.75, cy), (R - 3.5, cy, cx + 1.75, cy)]:
        arrow(s, x1, y1, x2, y2, color=TAUPE)

    s = D.slide('content', 'Priorisierung: Drei Initiativen mit hohem Nutzen und geringem Aufwand zuerst',
                'Frameworks | Nutzen-Aufwand-Matrix', key='prio',
                notes=N('Priorisierung von Maßnahmen oder Initiativen.', 'Buchstaben-Kreise verschieben; Liste rechts anpassen.'))
    gx0, gy0, gw, gh = L + 0.55, 1.45, 6.6, 4.4
    quads = [('Quick Wins', 0, 0, LBLUE), ('Strategische Projekte', 1, 0, LSAND), ('Füllprojekte', 0, 1, LSAND), ('Vermeiden', 1, 1, LSAND)]
    for t, qx, qy, f in quads:
        rect(s, gx0 + qx * gw / 2, gy0 + qy * gh / 2, gw / 2 - 0.04, gh / 2 - 0.04, fill=f)
        text(s, gx0 + qx * gw / 2 + 0.15, gy0 + qy * gh / 2 + 0.1, 3, 0.3, t, size=12, color=BLUE)
    text(s, gx0, gy0 + gh + 0.05, gw, 0.3, 'Aufwand →', size=11, align='r')
    tb = text(s, 0, 0, gh, 0.35, 'Nutzen →', size=11, align='r')
    tb.rotation = 270; tb.left = I(gx0 - 0.4 - gh / 2); tb.top = I(gy0 + gh / 2 - 0.17)
    pts = [('A', 0.7, 0.7, True), ('B', 1.8, 1.1, True), ('C', 2.3, 0.6, True), ('D', 4.6, 0.8, False), ('E', 5.2, 1.6, False), ('F', 1.3, 3.1, False), ('G', 4.9, 3.4, False)]
    for t, px, py, hi in pts:
        oval(s, gx0 + px, gy0 + py, 0.45, fill=BLUE if hi else WHITE, line=None if hi else BLACK, content=t, size=13, color=WHITE if hi else BLACK, align='c', anchor='m', margin=0)
    xr = 8.0; wr = R - xr
    items = ['Rüst-Standard Linie 3', 'Freigabe-Checkliste', 'KPI-Board Shopfloor', 'MES-Einführung', 'Neue Isolator-Linie', 'Etikettendruck', 'Lagerumbau']
    for i, t in enumerate(items):
        y = 1.5 + i * 0.6
        oval(s, xr, y + 0.06, 0.36, fill=BLUE if i < 3 else WHITE, line=None if i < 3 else BLACK, content='ABCDEFG'[i], size=11,
             color=WHITE if i < 3 else BLACK, align='c', anchor='m', margin=0)
        text(s, xr + 0.55, y, wr - 0.55, 0.48, t, size=14, anchor='m')

    s = D.slide('content', 'Wertschöpfungskette: Herstellung und Qualität binden 60 % der Kosten',
                'Frameworks | Wertschöpfungskette', 'Werte illustrativ', key='valuechain', sticker_='Illustrativ',
                notes=N('Wertkette nach Porter, angepasst auf die Pharma-Produktion.', 'Kostenanteile und Aktivitäten anpassen.'))
    label(s, L, 1.45, 4, 'Unterstützende Aktivitäten', color=DGRAY)
    sup = ['Unternehmensinfrastruktur & Qualitätsmanagement', 'Personal & Qualifizierung', 'Technologie & Digitalisierung', 'Beschaffung']
    for i, t in enumerate(sup):
        rect(s, L, 1.75 + i * 0.45, W - 1.0, 0.38, fill=LSAND, content=t, size=12, anchor='m', margin=(0.2, 0, 0.1, 0))
    label(s, L, 3.7, 4, 'Primäre Aktivitäten', color=BLUE)
    prim = [('Eingangs-\nlogistik', '8 %'), ('Herstellung', '34 %'), ('Qualitätskontrolle', '26 %'), ('Ausgangs-\nlogistik', '12 %'), ('Service', '5 %')]
    cw = (W - 1.0 - 4 * 0.08) / 5
    for i, (t, p) in enumerate(prim):
        x = L + i * (cw + 0.08)
        hi = i in (1, 2)
        rect(s, x, 4.0, cw, 1.6, fill=BLUE if hi else SAND)
        text(s, x + 0.15, 4.1, cw - 0.3, 0.7, t, size=13, color=WHITE if hi else BLACK)
        text(s, x + 0.15, 4.95, cw - 0.3, 0.55, p, size=24, color=WHITE if hi else BLUE)
    rect(s, R - 0.85, 1.75, 0.85, 3.85, fill=BLACK)
    t_ = text(s, 0, 0, 3.85, 0.85, 'Marge', size=14, color=WHITE, align='c', anchor='m')
    t_.rotation = 270; t_.left = I(R - 0.425 - 1.925); t_.top = I(1.75 + 1.925 - 0.425)

    s = D.slide('content', 'Vom Zweck zu messbaren Zielen: Die Zielpyramide für [Projekt]',
                'Frameworks | Zielpyramide', key='pyramid',
                notes=N('Vision, Mission, Ziele und Maßnahmen in einer Logik.', 'Ebenen-Inhalte anpassen.'))
    lv = [('Vision', 'Zuverlässigster Lieferant steriler Arzneimittel in Europa', BLUE, 3.2),
          ('Mission', 'Kapazität, Qualität und Geschwindigkeit verbinden', MBLUE, 5.6),
          ('Ziele 2028', '+60 % Kapazität  |  0 kritische Beobachtungen  |  OEE 66 %', SAND, 8.0),
          ('Maßnahmen', 'Neue Linie  |  MES-Einführung  |  OEE-Programm  |  Schulung', LSAND, 10.4)]
    for i, (h, b, f, w_) in enumerate(lv):
        y = 1.5 + i * 1.08
        x = L + (W - w_) / 2
        rect(s, x, y, w_, 0.95, fill=f, content=[{'t': h, 'size': 15}, {'t': b, 'size': 12}], color=WHITE if f == BLUE else BLACK, align='c', anchor='m')

    s = D.slide('content', 'Der adressierbare Markt für Füll- und Fertigungsberatung beträgt € 1,2 Mrd.',
                'Frameworks | Marktgröße (TAM, SAM, SOM)', 'Quelle: [Studie, Jahr]; eigene Berechnung; Werte illustrativ', key='tam', sticker_='Illustrativ',
                notes=N('Marktgrößen-Herleitung für Strategie- und Go-to-Market-Diskussionen.', 'Werte und Quellen eintragen; Herleitung in den Notizen dokumentieren.'))
    cx = L + 2.9
    for d, f, yo in [(4.4, SAND, 0), (3.1, STONE, 1.3), (1.7, BLUE, 2.7)]:
        oval(s, cx - d / 2, 1.5 + yo, d, fill=f)
    xr = 6.4; wr = R - xr
    for i, (a, b, c) in enumerate([('€ 8,5 Mrd.', 'TAM – Total Addressable Market', 'Engineering- und Beratungsleistungen Pharma-Produktion, global'),
                                   ('€ 1,2 Mrd.', 'SAM – Serviceable Available Market', 'Sterile und biologische Produktion in Europa'),
                                   ('€ 60 Mio.', 'SOM – Serviceable Obtainable Market', 'Realistisch erreichbarer Anteil in 5 Jahren')]):
        y = 1.5 + i * 1.45
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, 2.4, 0.6, a, size=26, color=BLUE)
        text(s, xr + 2.5, y + 0.15, wr - 2.5, 0.35, b, size=14)
        text(s, xr + 2.5, y + 0.55, wr - 2.5, 0.7, c, size=12, color=DGRAY)

    s = D.slide('content', 'Ursache-Wirkung: Sechs Ursachengruppen für Abweichungen in der Abfüllung',
                'Frameworks | Ishikawa-Diagramm', key='ishikawa',
                notes=N('Ursachenanalyse (6M) für Abweichungen und Qualitätsprobleme.', 'Ursachen je Kategorie eintragen; Hauptursache blau.'))
    sx, ex, my = L, R - 2.4, 3.65
    hline(s, sx, my, ex - sx, BLACK, 2)
    rect(s, ex, my - 0.6, 2.4, 1.2, fill=BLUE, content='Abweichungen in der Abfüllung', size=14, color=WHITE, anchor='m', align='c')
    cats = [('Mensch', ['Einarbeitung', 'Schichtwechsel']), ('Maschine', ['Verschleiß Dosierpumpe', 'Sensorkalibrierung']), ('Methode', ['SOP unklar', 'Rüstreihenfolge']),
            ('Material', ['Stopfenqualität', 'Lieferantenwechsel']), ('Messung', ['Probenahme', 'Prüfmittel']), ('Mitwelt', ['Luftfeuchte', 'Druckkaskade'])]
    for i, (c, causes) in enumerate(cats):
        top = i < 3
        bx = sx + 0.6 + (i % 3) * 3.3
        y_end = 1.55 if top else 5.75
        elbow_ = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(bx), I(y_end), I(bx + 1.3), I(my))
        _strip_style(elbow_); elbow_.line.fill.solid(); setc(elbow_.line.color, TAUPE); elbow_.line.width = Pt(1.25)
        hi = c == 'Methode'
        rect(s, bx - 0.6, y_end - (0.42 if top else 0), 1.6, 0.42, fill=BLUE if hi else SAND, content=c, size=13, color=WHITE if hi else BLACK, align='c', anchor='m')
        for j, cz in enumerate(causes):
            fy = (y_end + 0.55 + j * 0.55) if top else (y_end - 0.95 - j * 0.55)
            fx = bx + 1.3 * ((fy - y_end) / (my - y_end))
            text(s, fx + 0.12, fy, 1.9, 0.35, cz, size=11, anchor='m')


# =====================================================================================
def s14(D):
    divider(D, 14, 'Diagramme', N('Native, editierbare PowerPoint-Diagramme im Körber-Stil.', 'Rechtsklick > „Daten bearbeiten“; Farben bleiben erhalten.',
                                    'Eine Botschaft pro Diagramm: Die relevante Datenreihe blau, alles andere grau.'))
    s = D.slide('content', 'Der Umsatz wächst seit 2022 um 12 % pro Jahr',
                'Diagramme | Säulendiagramm mit Wachstumsrate', 'Quelle: [Quelle]; € Mio.; Werte illustrativ', key='ch_col', sticker_='Illustrativ',
                notes=N('Zeitreihe mit Wachstumsrate (CAGR).', 'Daten bearbeiten; CAGR = (Ende/Anfang)^(1/Jahre) – 1.'))
    bar(s, L, 1.4, 8.4, 4.4, ['2022', '2023', '2024', '2025', '2026'], [('Umsatz', [2.0, 2.3, 2.6, 2.9, 3.2])], fmt='"€ "0.0" Mrd."', highlight=[3, 4], gap=55, size=12)
    disturber(s, 9.6, 1.9, [{'t': '+12 %', 'size': 32}, {'t': 'CAGR 2022–2026', 'size': 12}], d=2.4)
    text(s, 9.0, 4.6, 3.9, 1.0, 'Wachstum getragen von Biologika und Service-Geschäft.', size=13)

    s = D.slide('content', 'Service überholt bis 2026 das Produktgeschäft',
                'Diagramme | Gestapelte Säulen', 'Quelle: [Quelle]; Anteil am Umsatz; Werte illustrativ', key='ch_stack', sticker_='Illustrativ',
                notes=N('Zusammensetzung über Zeit (100 % gestapelt).', 'Fokus-Segment als unterste Reihe in Blau.'))
    bar(s, L, 1.4, 8.4, 4.4, ['2023', '2024', '2025', '2026'], [('Service', [0.32, 0.38, 0.44, 0.51]), ('Produkte', [0.52, 0.48, 0.44, 0.39]), ('Sonstiges', [0.16, 0.14, 0.12, 0.10])],
        stacked=True, pct=True, colors=[BLUE, STONE, SAND], legend='b', fmt='0%', gap=55, size=12)
    xr = 9.3; wr = R - xr
    kpi(s, xr, 1.6, wr, '51 %', 'Service-Anteil 2026', '+19 pp seit 2023', bigsize=32)

    s = D.slide('content', 'Deutschland und die USA stehen für die Hälfte des Umsatzes',
                'Diagramme | Ranking (Balken)', 'Quelle: [Quelle]; € Mio.; Werte illustrativ', key='ch_rank', sticker_='Illustrativ',
                notes=N('Ranking/Vergleich von Kategorien – absteigend sortiert.', 'Daten sortieren; Fokus-Balken blau (highlight).'))
    bar(s, L, 1.4, 8.4, 4.4, ['Deutschland', 'USA', 'Frankreich', 'Italien', 'Spanien', 'Polen', 'Sonstige'], [('Umsatz', [92, 81, 64, 55, 41, 33, 20])],
        kind='bar', fmt='0', highlight=[0, 1], gap=40, size=12)
    disturber(s, 9.8, 2.0, [{'t': '45 %', 'size': 32}, {'t': 'aus zwei Märkten', 'size': 12}], d=2.3)

    s = D.slide('content', 'Die Ausbringung erreicht nach neun Monaten das Zielniveau',
                'Diagramme | Liniendiagramm mit Zielwert', 'Quelle: MES; Einheiten pro Schicht in Tsd.; Werte illustrativ', key='ch_line', sticker_='Illustrativ',
                notes=N('Entwicklung über Zeit mit Zielwert.', 'Daten bearbeiten; Zielreihe gestrichelt grau.'))
    from pptx.enum.dml import MSO_LINE
    line_chart(s, L, 1.4, 9.0, 4.4, ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'],
               [('Ausbringung', [31, 32, 33, 35, 36, 38, 40, 41, 43, 43, 44, 44]), ('Ziel', [43] * 12)],
               colors=[BLUE, TAUPE], dashes=[None, MSO_LINE.DASH], fmt='0', labels='last', size=12, min_=25, max_=48)
    xr = 9.9; wr = R - xr
    kpi(s, xr, 1.6, wr, '+42 %', 'Ausbringung seit Start', bigsize=30)

    s = D.slide('content', 'Drei von vier Zielen sind erreicht',
                'Diagramme | Zielerreichung (Donuts)', 'Stand: [Datum]; Werte illustrativ', key='ch_donut', sticker_='Illustrativ',
                notes=N('Zielerreichung/Fortschritt als Ringdiagramme.', 'Wert und Restwert je Diagramm anpassen (Summe = 100 %).'))
    vals = [(1.0, 'OEE-Ziel', '66 % erreicht'), (1.0, 'Freigabezeit', '11 Tage erreicht'), (1.0, 'Schulungen', '40 von 40'), (0.72, 'Budget', '72 % verbraucht')]
    cw = W / 4
    for i, (v, h, b) in enumerate([(0.68, 'Kapazität', 'Ziel: +60 %'), (1.0, 'Compliance', 'Ziel: 0 kritische'), (1.0, 'Termin', 'Ziel: Go-live 09/27'), (1.0, 'Budget', 'Ziel: ±5 %')]):
        x = L + i * cw + (cw - 2.4) / 2
        doughnut(s, x, 1.6, 2.4, [v, 1 - v] if v < 1 else [1, 0], colors=[BLUE if v >= 1 else AMBER, SAND], hole=75)
        text(s, x, 2.45, 2.4, 0.7, '%d %%' % round(v * 100), size=18, align='c', anchor='m')
        text(s, L + i * cw, 4.15, cw, 0.35, h, size=16, align='c')
        text(s, L + i * cw, 4.55, cw, 0.35, b, size=12, align='c', color=DGRAY)
    sowhat(s, 'Nur die Kapazitätssteigerung liegt noch unter Ziel – der Ramp-up der Linie läuft bis Q2.')

    s = D.slide('content', 'Portfolio: Zwei Produkte rechtfertigen eine eigene Linie',
                'Diagramme | Blasendiagramm', 'Quelle: [Quelle]; Blasengröße = Umsatz; Werte illustrativ', key='ch_bubble', sticker_='Illustrativ',
                notes=N('Portfolio-Darstellung mit drei Dimensionen (x, y, Größe).', 'Daten bearbeiten; Fokus-Produkte als eigene Reihe in Blau.'))
    ch = scatter(s, L, 1.4, 8.6, 4.4, [('Produkte', [(70, 18, 40), (82, 12, 32), (30, 6, 12), (45, 9, 20), (25, 15, 8), (55, 4, 10)])],
                 bubble=True, xtitle='Volumen (Tsd. Einheiten)', ytitle='Wachstum p. a. (%)', xmin=0, xmax=100, ymin=0, ymax=25, size=12, bubble_scale=50)
    ser = ch.plots[0].series[0]
    for i in range(6):
        pt = ser.points[i]; pt.format.fill.solid(); setc(pt.format.fill.fore_color, BLUE if i < 2 else STONE)
        pt.data_label.has_text_frame = True; pt.data_label.text_frame.text = 'ABCDEF'[i]; pt.data_label.position = XL_LABEL_POSITION.CENTER
        r_ = pt.data_label.text_frame.paragraphs[0].runs[0]; r_.font.size = Pt(12); setc(r_.font.color, WHITE if i < 2 else BLACK)
    xr = 9.6; wr = R - xr
    label(s, xr, 1.5, wr, 'Lesart')
    text(s, xr, 1.85, wr, 3.0, bl(['Produkte A und B: hohes Volumen und Wachstum', 'Gemeinsam 58 % des Umsatzes', 'Kandidaten für eine dedizierte Linie'], sa=8), size=13)

    s = D.slide('content', 'Linie 3 hat den größten Nachholbedarf bei der Verfügbarkeit',
                'Diagramme | Tabelle mit Datenbalken', 'Quelle: MES; Werte illustrativ', key='ch_table', sticker_='Illustrativ',
                notes=N('Tabelle mit eingebetteten Balken – kompakter Vergleich mehrerer Kennzahlen.', 'Werte eintragen; Balkenlänge proportional anpassen (Breite = Wert × Spaltenbreite).'))
    rows = [['Linie', 'OEE', '', 'Verfügbarkeit', 'Leistung', 'Qualität'], ['Linie 1', '71 %', '', '84 %', '88 %', '96 %'], ['Linie 2', '66 %', '', '80 %', '86 %', '96 %'],
            ['Linie 3', '54 %', '', '68 %', '83 %', '95 %'], ['Linie 4', '62 %', '', '77 %', '84 %', '96 %']]
    tb = table(s, L, 1.5, W, rows, colw=[2.0, 1.2, 3.6, 1.9, 1.9, 1.9], rowh=0.7, size=14, aligns=['l', 'r', 'l', 'c', 'c', 'c'])
    x_bar = L + W * 3.2 / 12.5 + 0.1; bw_max = W * 3.6 / 12.5 - 0.3
    for r, v in enumerate([0.71, 0.66, 0.54, 0.62]):
        y = 1.5 + (r + 1) * 0.7 + 0.22
        rect(s, x_bar, y, bw_max * v, 0.26, fill=BLUE if r == 2 else STONE)
    c = tb.cell(3, 3); c.fill.solid(); setc(c.fill.fore_color, LBLUE)
    sowhat(s, 'Verfügbarkeit ist der schwächste OEE-Faktor von Linie 3 – Stillstandsanalyse priorisieren.')


# =====================================================================================
def s15(D):
    divider(D, 15, 'Abschluss', N('Zusammenfassung, Entscheidung, nächste Schritte, Kontakt.',
                                  'Mit konkreten nächsten Schritten und Verantwortlichen enden.',
                                  'Kein Termin endet ohne vereinbarten nächsten Schritt – im CRM dokumentieren.'))
    s = D.slide('content', 'Vier Kernaussagen zum Mitnehmen',
                'Abschluss | Zusammenfassung', key='takeaways',
                notes=N('Zusammenfassung vor Entscheidung oder Diskussion.', 'Die vier wichtigsten Botschaften der Präsentation – identisch mit den Action Titles.'))
    tk = [('Der Handlungsbedarf ist akut', 'Ab [Jahr] fehlen [xx] Mio. Einheiten Kapazität.'), ('Die Lösung ist klar', 'Neue Isolator-Linie plus Ertüchtigung der Bestandslinie.'),
          ('Der Business Case trägt', 'Payback in 2,8 Jahren, auch im konservativen Szenario positiv.'), ('Der Weg ist geplant', 'Fünf Phasen mit Gates – Go-live September 2027.')]
    for i, (h, b) in enumerate(tk):
        y = 1.5 + i * 1.08
        num(s, L, y + 0.15, i + 1, 0.55, size=16)
        text(s, L + 0.85, y + 0.05, 4.5, 0.75, h, size=19, anchor='m')
        text(s, L + 5.6, y + 0.05, 7.0, 0.75, b, size=15, anchor='m')
        if i < 3:
            hline(s, L + 0.85, y + 0.95, W - 0.85, STONE, 0.5)

    s = D.slide('content', 'Nächste Schritte: Vier Aktivitäten bis zur Entscheidung am [Datum]',
                'Abschluss | Nächste Schritte', key='nextsteps',
                notes=N('Verbindliche nächste Schritte mit Verantwortlichen und Terminen.', 'Gemeinsam im Termin ausfüllen; danach per Mail bestätigen.',
                        'Nächste Schritte direkt nach dem Termin als Aufgaben im CRM anlegen.'))
    rows = [['#', 'Aktivität', 'Verantwortlich', 'Termin'],
            ['1', 'Datenbereitstellung für Business-Case-Validierung', '[Kunde]: [Name]', '[TT.MM.]'],
            ['2', 'Referenzbesuch bei [Referenzkunde] organisieren', 'Körber: [Name]', '[TT.MM.]'],
            ['3', 'Finales Angebot inkl. Paketoptionen', 'Körber: [Name]', '[TT.MM.]'],
            ['4', 'Entscheidung im Investitionsausschuss', '[Kunde]: [Name]', '[TT.MM.]']]
    tb = table(s, L, 1.5, W, rows, colw=[0.6, 6.4, 3.4, 2.2], rowh=0.72, size=15)
    for r in range(1, 5):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=18, color=BLUE)
    sowhat(s, 'Mit diesen vier Schritten ist ein Projektstart am [Datum] realistisch.')

    s = D.slide('hl_dark', 'Ihre', key='discussion',
                notes=N('Übergang in die Diskussion.', 'Bild über „Bild ändern“ austauschen.'))
    {p.placeholder_format.idx: p for p in s.placeholders}[27].insert_picture(IMG + 'image24.jpg')
    D.ph(s, 29, 'Fragen')
    D.drop_empty(s, keep=(20, 21, 22, 23, 24, 27, 29))

    s = D.slide('end_contact', 'Vielen Dank!', key='end',
                notes=N('Schlussfolie mit Kontaktdaten.', 'Name, Funktion, Ort, Telefon und E-Mail eintragen.'))
    D.ph(s, 10, '[Vorname Name]\n[Funktion]'); D.ph(s, 14, '[Standort]'); D.ph(s, 15, '+49 [Telefonnummer]'); D.ph(s, 16, '[vorname.name]@koerber.com')

    s = D.slide('end', 'Thank you!', key='end_en',
                notes=N('Englische Schlussfolie ohne Kontaktdaten.', '–'))

    s = D.slide('legal', key='legal',
                notes=N('Rechtlicher Hinweis – Pflicht bei Angeboten und externen Unterlagen.', 'Text mit der Rechtsabteilung abstimmen.'))


# =====================================================================================
def s16(D):
    divider(D, 16, 'Toolkit', N('Raster, Regeln, Farben, Bausteine und Icons für eigene Folien.',
                                 'Nicht beim Kunden zeigen.', 'Neue Folien immer aus diesen Bausteinen bauen – so bleibt jede Folie konsistent.'))
    s = D.slide('content', 'Das Raster: Jedes Element hat einen festen Platz',
                'Toolkit | Raster und Maße', key='grid',
                notes=N('Referenz für alle, die neue Folien bauen.', 'Hilfslinien in PowerPoint: Ansicht > Führungslinien.',
                        'Maße (Zoll): Rand links 0,37 / rechts 12,97; Inhalt ab 1,45; So what bei 5,98; Spaltenabstand 0,3.'))
    rect(s, L, 1.45, W, 4.4, line=BLUE, dash=None)
    text(s, L + 0.15, 1.55, 6, 0.3, 'Inhaltsbereich  |  oben 1,45"  |  unten 5,80"', size=12, color=BLUE)
    cw = (W - 3 * 0.3) / 4
    for i in range(4):
        rect(s, L + i * (cw + 0.3), 2.0, cw, 3.65, fill=LBLUE)
        text(s, L + i * (cw + 0.3), 3.6, cw, 0.4, 'Spalte %d' % (i + 1), size=12, align='c', color=BLUE)
    text(s, L + cw, 2.6, 0.3, 0.4, '0,3"', size=9, align='c', color=BLUE)
    sowhat(s, 'Kernaussage immer an derselben Position (5,98") – sie ist das Erste, was Leser suchen.')
    # annotations to the right of title row
    for y, t in [(0.4, '← Titel: Action Title, 24 pt, max. 76 Zeichen'), (0.78, '← Tracker: „Kapitel | Thema“, 14 pt')]:
        text(s, 8.6, y, 4.2, 0.3, t, size=10, color=BLUE)

    s = D.slide('content', 'Farben und Typografie: Blau hebt hervor, Grau ordnet',
                'Toolkit | Farben und Schrift', 'Quelle: Körber Brand Hub', key='colors',
                notes=N('CI-Kurzreferenz.', 'Bei CI-Änderungen mit Brand & Communications abstimmen.'))
    cols = [('Körber Blau', '0060FF', BLUE, 'Hervorhebung, Fokus, Kernaussage'), ('Schwarz', '000000', BLACK, 'Text, Linien'),
            ('Warmgrau hell', 'E6E2DC', SAND, 'Flächen, Karten'), ('Warmgrau', 'BFB8AF', STONE, 'Vergleichswerte in Diagrammen'),
            ('Warmgrau dunkel', '9D968D', TAUPE, 'Pfeile, sekundäre Elemente'), ('Gelb', 'FFE32F', YELLOW, 'Nur Call to Action'),
            ('Amber', 'FEC037', AMBER, 'Status: gefährdet'), ('Orange', 'FE8623', ORANGE, 'Status: kritisch')]
    cw = (W - 3 * 0.25) / 4
    for i, (n_, hx, c, u) in enumerate(cols):
        x = L + (i % 4) * (cw + 0.25); y = 1.5 + (i // 4) * 1.6
        rect(s, x, y, 0.9, 0.9, fill=c, line=STONE if c == WHITE else None)
        text(s, x + 1.05, y, cw - 1.05, 0.3, n_, size=13)
        text(s, x + 1.05, y + 0.3, cw - 1.05, 0.3, '#' + hx, size=11, color=DGRAY)
        text(s, x + 1.05, y + 0.6, cw - 1.05, 0.7, u, size=11)
    hline(s, L, 4.85, W, BLACK)
    typo = [('Titel', '24 pt, Arial Regular'), ('Tracker / Untertitel', '14 pt'), ('Text', '12–14 pt'), ('Labels', '10 pt, Versalien, blau'), ('Quelle', '9 pt (Platzhalter)')]
    tw = W / 5
    for i, (a, b) in enumerate(typo):
        text(s, L + i * tw, 5.0, tw - 0.2, 0.3, a, size=13, color=BLUE)
        text(s, L + i * tw, 5.32, tw - 0.2, 0.3, b, size=12)

    s = D.slide('content', 'Bausteine zum Kopieren: Immer dieselben Elemente verwenden',
                'Toolkit | Bausteine', key='blocks',
                notes=N('Baukasten: Elemente kopieren und einfügen statt neu zeichnen.', '–',
                        'Elemente aus dieser Folie kopieren hält Abstände, Farben und Größen konsistent.'))
    label(s, L, 1.45, 3, 'Nummern und Status', color=DGRAY)
    num(s, L, 1.8, 1); num(s, L + 0.6, 1.8, 2, filled=False); rag(s, L + 1.3, 1.91, 'g'); rag(s, L + 1.65, 1.91, 'y'); rag(s, L + 2.0, 1.91, 'r'); rag(s, L + 2.35, 1.91, 'n')
    label(s, L, 2.5, 3, 'Harvey Balls (0–4)', color=DGRAY)
    for q in range(5):
        harvey(s, L + q * 0.55, 2.85, 0.38, q)
    label(s, L, 3.5, 3, 'Sticker und Tags', color=DGRAY)
    shape(s, SH.PENTAGON, L, 3.85, 1.35, 0.26, fill=BLUE, content='Illustrativ', size=9, color=WHITE, caps=True, spacing=0.8, anchor='m', margin=(0.1, 0, 0.05, 0))
    rrect(s, L + 1.55, 3.83, 1.1, 0.3, fill=WHITE, line=BLUE, radius=0.15, content='Big Pharma', size=10, color=BLUE, align='c', anchor='m', margin=0)
    label(s, L, 4.5, 3, 'Call to Action', color=DGRAY)
    rrect(s, L, 4.85, 2.7, 0.45, fill=YELLOW, radius=0.22, content='Entscheidung bis [Datum]', size=12, align='c', anchor='m', margin=0)
    x2 = 4.0
    label(s, x2, 1.45, 3, 'Prozess', color=DGRAY)
    chevrons(s, ['Schritt 1', 'Schritt 2', 'Schritt 3'], x2, 1.8, 4.2, 0.5, active=1, size=11)
    label(s, x2, 2.5, 3, 'Flussdiagramm-Symbole', color=DGRAY)
    rrect(s, x2, 2.85, 1.2, 0.5, fill=BLACK, radius=0.25, content='Start/Ende', size=10, color=WHITE, align='c', anchor='m', margin=0)
    rect(s, x2 + 1.4, 2.85, 1.2, 0.5, fill=SAND, content='Schritt', size=10, align='c', anchor='m')
    shape(s, SH.DIAMOND, x2 + 2.8, 2.75, 1.2, 0.7, fill=BLUE, content='Frage?', size=10, color=WHITE, align='c', anchor='m', margin=0)
    label(s, x2, 3.6, 3, 'Icon im Kreis', color=DGRAY)
    icon_circle(s, 'factory', x2, 3.9, 0.62); icon_circle(s, 'science', x2 + 0.8, 3.9, 0.62, fill=SAND, color=BLUE)
    label(s, x2, 4.75, 3, 'Kennzahl', color=DGRAY)
    text(s, x2, 5.0, 2, 0.6, '–14 pp', size=28, color=BLUE)
    x3 = 8.8; w3 = R - x3
    label(s, x3, 1.45, 3, 'Karte', color=DGRAY)
    card(s, x3, 1.8, w3, 1.6, 'Kartenüberschrift', 'Ein bis zwei Sätze mit den unterstützenden Fakten.', lab='Label', hsize=15, bsize=12)
    label(s, x3, 3.6, 3, 'Disturber (Körber CI)', color=DGRAY)
    disturber(s, x3, 3.95, [{'t': '25 %', 'size': 22}, {'t': 'Kernzahl', 'size': 11}], d=1.6)

    s = D.slide('content', 'Icon-Bibliothek: 117 Material Symbols, frei einfärbbar',
                'Toolkit | Icons', 'Material Symbols Outlined (Google, Apache 2.0); Icon kopieren, Farbe über Formfüllung', key='icons',
                notes=N('Icon-Bibliothek für eigene Folien.', 'Icon kopieren, einfügen, über „Formfüllung“ einfärben. Größe proportional ändern (Shift).',
                        'Pro Folie nur einen Icon-Stil – nicht mit anderen Icon-Sets mischen.'))
    names = sorted(json.load(open(os.path.join(HERE, 'icons.json'))).keys())
    cols_ = 13; cw = W / cols_; rh = 0.56
    for i, n_ in enumerate(names):
        x = L + (i % cols_) * cw; y = 1.4 + (i // cols_) * rh
        icon(s, n_, x + cw / 2 - 0.15, y, 0.3, BLUE)
        text(s, x, y + 0.31, cw, 0.2, n_.replace('_', ' '), size=7, align='c', color=DGRAY)
