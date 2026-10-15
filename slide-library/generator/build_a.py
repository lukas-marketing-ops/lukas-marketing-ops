from kh import *

IMG = template_media()
PH_PERSON = None


def N(einsatz, anpassen, tipp=None):
    t = 'EINSATZ: ' + einsatz + '\n\nANPASSEN: ' + anpassen
    if tipp:
        t += '\n\nTIPP: ' + tipp
    return t


def divider(D, nr, name, notes):
    D.section('%02d %s' % (nr, name.replace('\n', '').replace('-', '')))
    s = D.slide('section_name_blue', notes=notes, key='sec%02d' % nr)
    D.ph(s, 25, '%02d' % nr)
    D.ph(s, 26, name)
    return s


def person(s, x, y, d=0.9):
    oval(s, x, y, d, fill=SAND)
    icon(s, 'person', x + d * 0.2, y + d * 0.2, d * 0.6, TAUPE)


# =====================================================================================
def s00(D):
    D.section('00 Einstieg')
    s = D.slide('title_grad', 'Slide Library 2026\nPharma Consulting', key='cover',
                notes=N('Deckblatt der Bibliothek. Nicht im Kundentermin verwenden.',
                        'Version und Datum bei jeder Aktualisierung pflegen.'))
    D.ph(s, 14, 'Vorlagen für Kundentermine und Leadprojekte im Körber CI')
    D.ph(s, 15, 'Version 1.0 | Oktober 2026')
    D.ph(s, 12, 'For internal use')

    s = D.slide('content', 'In vier Schritten von der Bibliothek zur fertigen Kundenpräsentation',
                'Einstieg | Nutzung', 'Hinweis: Einsatzhinweise zu jeder Folie stehen in den Sprechernotizen', key='howto',
                notes=N('Kurzanleitung für alle, die mit der Bibliothek arbeiten.', 'Bei neuen Konventionen ergänzen.'))
    steps = [('Storyline wählen', 'Termin-Typ bestimmen und die passende Folienfolge aus dem Storyline-Baukasten übernehmen.'),
             ('Folien übernehmen', 'Folien kopieren oder über „Folien wiederverwenden“ einfügen – das Körber-Design bleibt erhalten.'),
             ('Inhalte schärfen', 'Zuerst den Action Title formulieren, dann [Platzhalter] ersetzen und Beispielwerte austauschen.'),
             ('Qualität prüfen', 'Eine Botschaft pro Folie, Quelle angegeben, Sticker entfernt, Klassifizierung gesetzt.')]
    cw = (W - 3 * 0.4) / 4
    for i, (h, b) in enumerate(steps):
        x = L + i * (cw + 0.4)
        colhead(s, x, 1.5, cw, None, h, b, n=i + 1, hsize=17, bsize=13, bh=1.4)
    y = 4.35
    rect(s, L, y, W, 2.0, fill=LSAND)
    label(s, L + 0.3, y + 0.25, 4, 'Konventionen in dieser Bibliothek')
    conv = [('[Eckige Klammern]', 'Platzhalter – vor dem Termin ersetzen'),
            ('Sticker „Illustrativ“', 'Beispielwerte – mit echten Daten ersetzen, dann Sticker löschen'),
            ('Blau', 'hebt die eine Sache hervor, auf die es ankommt – keine Dekoration'),
            ('So what', 'die Kernaussage der Folie in einem Satz')]
    for i, (a, b) in enumerate(conv):
        x = L + 0.3 + (i % 2) * 6.2; yy = y + 0.65 + (i // 2) * 0.6
        text(s, x, yy, 6.0, 0.5, [{'t': [(a + '  ', {'color': BLUE}), (b, {})]}], size=13)

    s = D.slide('content', 'Inhalt: 16 Kapitel entlang des Kundenprozesses',
                'Einstieg | Inhaltsverzeichnis (Kapitel anklicken)', key='toc',
                notes=N('Navigation im Bearbeitungsmodus und in der Bildschirmpräsentation: Kapitelzeile anklicken.',
                        'Wird beim Generieren automatisch mit Foliennummern befüllt.'))
    s = D.slide('content', 'Storyline-Baukasten: Für jeden Termin-Typ die passende Folienfolge',
                'Einstieg | Storylines', 'Foliennummern beziehen sich auf diese Bibliothek', key='story',
                notes=N('Startpunkt für jede neue Präsentation: Termin-Typ wählen, Folien in dieser Reihenfolge übernehmen.',
                        'Eigene Termin-Typen als Zeile ergänzen.',
                        'Faustregel: 1,5–2 Minuten pro Folie einplanen, 30 % der Zeit für Dialog reservieren.'))

    s = D.slide('content', 'Gute Folien folgen der Pyramide: erst Botschaft, dann Argumente, dann Belege',
                'Einstieg | Storytelling', key='rules',
                notes=N('Leitlinie für alle Autorinnen und Autoren.', '–',
                        'Test: Wer nur die Titel liest, muss die gesamte Story verstehen.'))
    # pyramid
    x0, w0 = L, 6.3
    shape(s, SH.RECTANGLE, x0, 1.5, w0, 0.75, fill=BLUE, content='Kernbotschaft = Action Title', size=15, color=WHITE, align='c', anchor='m')
    for i in range(3):
        bw = (w0 - 0.3) / 3
        shape(s, SH.RECTANGLE, x0 + i * (bw + 0.15), 2.5, bw, 0.65, fill=SAND, content='Argument %d' % (i + 1), size=13, align='c', anchor='m')
        for j in range(2):
            sw = (bw - 0.1) / 2
            shape(s, SH.RECTANGLE, x0 + i * (bw + 0.15) + j * (sw + 0.1), 3.4, sw, 0.55, line=STONE,
                  content='Beleg', size=12, align='c', anchor='m', color=DGRAY)
    text(s, x0, 4.15, w0, 0.9, 'Eine Folie = eine Botschaft. Der Titel ist ein vollständiger Satz mit dem Ergebnis – nicht das Thema.', size=13)
    xr = 7.2; wr = R - xr
    label(s, xr, 1.5, wr, 'Vom Thementitel zum Action Title')
    ex = [('Thema', 'OEE-Analyse Linie 3', STONE),
          ('Besser', 'Die OEE von Linie 3 liegt bei 54 %', TAUPE),
          ('Action Title', 'Die OEE liegt 14 pp unter Benchmark – Rüstzeiten sind der größte Hebel', BLUE)]
    for i, (a, b, c) in enumerate(ex):
        y = 1.9 + i * 1.0
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, 1.5, 0.3, a, size=11, color=c if c != STONE else DGRAY)
        text(s, xr, y + 0.38, wr, 0.6, b, size=15, color=BLUE if c == BLUE else BLACK)
    sowhat(s, 'Wer nur die Titel liest, muss die gesamte Story verstehen – das ist der Qualitätstest für jedes Deck.')


# =====================================================================================
def s01(D):
    divider(D, 1, 'Titel &\nAgenda', N('Deckblätter, Agenda und Einstieg in den Termin.', 'Kapitelnummer und -name im Platzhalter ändern.'))
    s = D.slide('title_blue', 'Kapazitätserweiterung\nsterile Abfüllung', key='cover_blue',
                notes=N('Deckblatt für Erstgespräch oder Angebotspräsentation.', 'Titel = Kundenthema, nicht „Körber Präsentation“.',
                        'Das Thema des Kunden in seiner Sprache benennen – das signalisiert Verständnis ab Folie 1.'))
    D.ph(s, 14, 'Erstgespräch mit [Kunde] | Vorschlag für das weitere Vorgehen')
    D.ph(s, 15, '[TT. Monat JJJJ], [Ort]')
    D.ph(s, 12, 'Confidential')
    s = D.slide('title_img', 'Gemeinsam zur\nvalidierten Anlage', key='cover_img',
                notes=N('Deckblatt mit Bild für Lösungspräsentation oder Kick-off.', 'Bild über „Bild ändern“ austauschen (Körber Pictures Library).'))
    {p.placeholder_format.idx: p for p in s.placeholders}[10].insert_picture(IMG + 'image12.jpeg')
    D.ph(s, 14, 'Lösungspräsentation für [Kunde] | [Projektname]')
    D.ph(s, 15, '[TT. Monat JJJJ], [Ort]')
    D.ph(s, 12, 'Confidential')
    D.drop_empty(s, keep=(10, 12, 14, 15))
    s = D.slide('title_light', 'Projekt-Kick-off\n[Projektname]', key='cover_ko',
                notes=N('Deckblatt für Kick-off, Steering Committee oder Abschlusspräsentation.', 'Projektname und Datum ergänzen.'))
    D.ph(s, 14, '[Kunde] und Körber Pharma Consulting')
    D.ph(s, 15, '[TT. Monat JJJJ], [Ort]')
    D.ph(s, 12, 'Confidential')

    s = D.slide('agenda_blue', 'Agenda', key='agenda',
                notes=N('Klassische Agenda mit bis zu fünf Punkten.', 'Punkte als Ergebnis formulieren, nicht als Thema.'))
    for i, t in enumerate(['Ziele für heute', 'Ihre Ausgangslage', 'Lösungsansatz und Vorgehen', 'Referenzen und Team', 'Nächste Schritte']):
        D.ph(s, 34 + 2 * i, '%02d' % (i + 1)); D.ph(s, 35 + 2 * i, t)

    s = D.slide('content', 'Agenda: In 90 Minuten von Ihrer Ausgangslage zu konkreten nächsten Schritten',
                'Titel & Agenda | Agenda mit Zeitplan', key='agenda_time',
                notes=N('Agenda für Workshops und längere Termine.', 'Zeiten, Themen und Verantwortliche anpassen.',
                        'Das Ergebnis je Block macht den Nutzen jedes Agendapunkts sichtbar.'))
    rows = [['Zeit', 'Thema', 'Ergebnis', 'Wer'],
            ['10:00 – 10:10', 'Begrüßung und Ziele', 'Gemeinsames Verständnis der Erwartungen', '[Name], [Name]'],
            ['10:10 – 10:35', 'Ihre Ausgangslage', 'Bestätigte Herausforderungen und Prioritäten', '[Kunde]'],
            ['10:35 – 11:00', 'Lösungsansatz', 'Bewertete Lösungsoptionen', 'Körber'],
            ['11:00 – 11:15', 'Referenzen', 'Übertragbare Erfahrungen', 'Körber'],
            ['11:15 – 11:30', 'Nächste Schritte', 'Vereinbarte Aktivitäten mit Terminen', 'Alle']]
    tb = table(s, L, 1.5, W, rows, colw=[1.6, 3.2, 4.6, 2.0], rowh=0.58, size=13)
    for r in range(1, 6):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=13, color=BLUE, anchor='m', space_after=0)
    sowhat(s, 'Jeder Agendapunkt hat ein Ergebnis – so wird aus der Präsentation ein Arbeitstermin.')

    s = D.slide('content', 'Heute wollen wir gemeinsam drei Ergebnisse erreichen',
                'Titel & Agenda | Ziele des Termins', key='goals',
                notes=N('Direkt nach der Agenda: Erwartungen synchronisieren.', 'Ziele mit dem Kunden vorab abstimmen.',
                        'Am Ende des Termins auf diese Folie zurückkommen und Ergebnisse abhaken.'))
    goals = [('forum', 'Verständnis', 'Ihre Ausgangslage, Ziele und Rahmenbedingungen sind gemeinsam bestätigt.'),
             ('target', 'Priorisierung', 'Die zwei bis drei wichtigsten Handlungsfelder sind identifiziert.'),
             ('flag', 'Vereinbarung', 'Nächste Schritte, Verantwortliche und Termine sind festgelegt.')]
    cw = (W - 2 * 0.5) / 3
    for i, (ic, h, b) in enumerate(goals):
        x = L + i * (cw + 0.5)
        icon_circle(s, ic, x, 1.55, 0.8)
        hline(s, x, 2.6, cw, BLACK)
        label(s, x, 2.75, cw, 'Ergebnis %d' % (i + 1))
        text(s, x, 3.05, cw, 0.45, h, size=20)
        text(s, x, 3.6, cw, 1.0, b, size=14)
    rect(s, L, 5.0, W, 0.8, fill=LSAND)
    text(s, L + 0.3, 5.0, W - 0.6, 0.8, [{'t': [('Nicht Ziel heute:  ', {'color': BLUE}),
                                               ('ein finales Angebot oder eine Detailplanung – beides folgt nach Klärung des Umfangs.', {})]}],
         size=13, anchor='m')

    s = D.slide('content', 'Am Tisch: Entscheider und Fachexperten beider Seiten',
                'Titel & Agenda | Teilnehmende', key='participants',
                notes=N('Vorstellungsrunde im Erstgespräch oder Kick-off.', 'Fotos per „Bild ändern“ in die Kreise einsetzen, Rollen ergänzen.',
                        'Buying-Center-Rolle intern notieren (siehe Kapitel 04) – nicht auf der Kundenfolie zeigen.'))
    for side, (lab, xs) in enumerate([('[Kunde]', L), ('Körber Pharma Consulting', L + 6.5)]):
        label(s, xs, 1.5, 6, lab, color=BLUE)
        hline(s, xs, 1.8, 6.1, BLACK)
        for i in range(4):
            x = xs + (i % 2) * 3.1; y = 2.05 + (i // 2) * 1.85
            person(s, x, y, 1.0)
            text(s, x + 1.2, y + 0.12, 1.85, 0.3, '[Vorname Name]', size=13)
            text(s, x + 1.2, y + 0.45, 1.85, 0.6, '[Funktion]\n[Bereich]', size=11, color=DGRAY)


# =====================================================================================
def s02(D):
    divider(D, 2, 'Über uns', N('Positionierung von Körber Pharma Consulting: Portfolio, Differenzierung, Team.',
                                'Nur die 2–3 Folien zeigen, die zur Fragestellung des Kunden passen.',
                                'Über uns kommt nach dem Kundenverständnis – nicht davor.'))
    s = D.slide('hl_dark', 'Komplexität', key='hl_about',
                notes=N('Emotionaler Einstieg in das Kapitel „Über uns“ oder in eine Keynote.', 'Bild aus der Körber Pictures Library wählen.'))
    {p.placeholder_format.idx: p for p in s.placeholders}[27].insert_picture(IMG + 'image19.png')
    D.ph(s, 29, 'wird Vorsprung')
    D.drop_empty(s, keep=(20, 21, 22, 23, 24, 27, 29))

    s = D.slide('content', 'Körber auf einen Blick: Pharma-Expertise mit der Stärke eines Konzerns',
                'Über uns | Kennzahlen', 'Quelle: [Körber Geschäftsbericht / Brand Hub, Jahr]', key='facts', sticker_='Zahlen einsetzen',
                notes=N('Einstieg in die Unternehmensvorstellung.', 'Aktuelle, freigegebene Kennzahlen aus dem Brand Hub einsetzen.',
                        'Maximal vier Zahlen – jede muss für den Kunden relevant sein.'))
    text(s, L, 1.5, 4.2, 3.6, [{'t': 'Wir planen, bauen, qualifizieren und optimieren pharmazeutische Produktionsanlagen – unabhängig vom Hersteller der Ausrüstung.', 'size': 18, 'sa': 12},
                               {'t': 'Als Teil der Körber-Gruppe verbinden wir Beratung mit Maschinen-, Software- und Service-Know-how.', 'size': 13, 'color': DGRAY}])
    stats = [('[xx]+', 'Jahre Erfahrung', 'in der Pharma-Produktion'), ('[xxx]+', 'Projekte', 'weltweit umgesetzt'),
             ('[xx]', 'Länder', 'mit Kundenprojekten'), ('[x.xxx]', 'Expertinnen & Experten', 'in der Körber-Gruppe Pharma')]
    for i, (a, b, c) in enumerate(stats):
        x = 5.0 + (i % 2) * 4.0; y = 1.5 + (i // 2) * 2.15
        rect(s, x, y, 3.75, 1.95, fill=LSAND if i else BLUE)
        col = WHITE if i == 0 else BLUE
        text(s, x + 0.3, y + 0.25, 3.2, 0.8, a, size=40, color=col)
        text(s, x + 0.3, y + 1.1, 3.2, 0.3, b, size=15, color=WHITE if i == 0 else BLACK)
        text(s, x + 0.3, y + 1.42, 3.2, 0.3, c, size=12, color=WHITE if i == 0 else DGRAY)

    s = D.slide('content', 'Wir begleiten Ihre Anlage über den gesamten Lebenszyklus',
                'Über uns | Leistungsportfolio', key='lifecycle',
                notes=N('Zeigt die Breite des Portfolios entlang des Asset-Lebenszyklus.', 'Leistungen je Phase an das eigene Angebot anpassen.',
                        'Im Termin die Phase markieren, in der der Kunde gerade steht (Phase blau, Rest sand).'))
    phases = ['Strategie & Machbarkeit', 'Konzept & Basic Design', 'Detail Design & Umsetzung', 'Qualifizierung & Validierung', 'Betrieb & Optimierung']
    chevrons(s, phases, L, 1.45, W, 0.62, size=12)
    svc = [['Standort- und Kapazitätsstrategie', 'Machbarkeitsstudien', 'Investitionsrechnung'],
           ['Prozess- und Layoutplanung', 'GMP-Zonenkonzepte', 'User Requirements (URS)'],
           ['Ausschreibung und Vergabe', 'Projekt- und Baumanagement', 'Lieferantensteuerung'],
           ['CQV-Strategie und -Pläne', 'IQ / OQ / PQ', 'Computer-System-Validierung'],
           ['OEE- und Lean-Programme', 'Digitalisierung & MES', 'Re-Qualifizierung']]
    qs = ['Wo und wie viel sollen wir investieren?', 'Wie sieht die optimale Anlage aus?', 'Wie bleiben wir in Zeit und Budget?',
          'Wie kommen wir sicher zur Freigabe?', 'Wie holen wir mehr aus der Anlage?']
    cw = (W - 4 * 0.06) / 5
    for i in range(5):
        x = L + i * (cw + 0.06)
        rect(s, x, 2.2, cw, 2.2, fill=LSAND)
        text(s, x + 0.18, 2.35, cw - 0.3, 2.0, bl(svc[i]), size=12)
        text(s, x + 0.05, 4.55, cw - 0.1, 0.8, [{'t': '„' + qs[i] + '“', 'italic': True}], size=12, color=DGRAY)
    label(s, L, 4.4, 3, '')
    sowhat(s, 'Ein Partner über alle Phasen vermeidet Wissensverluste an den Übergaben – dort entstehen die meisten Verzögerungen.')

    s = D.slide('content', 'Sechs Kompetenzfelder decken alle Fragestellungen der Pharma-Produktion ab',
                'Über uns | Kompetenzfelder', key='competencies',
                notes=N('Übersicht der Kompetenzfelder für Erstgespräche.', 'Kompetenzfelder und Beschreibungen anpassen.',
                        'Das für den Kunden relevanteste Feld blau hinterlegen.'))
    items = [('factory', 'Facility & Process Design', 'Konzept-, Basic- und Detailplanung für feste, sterile und biologische Darreichungsformen'),
             ('verified', 'GMP Compliance & CQV', 'Commissioning, Qualifizierung und Validierung nach EU-GMP und FDA'),
             ('memory', 'Digitalisierung & MES', 'MES-Einführung, Pharma 4.0, Data Integrity und OT-Sicherheit'),
             ('local_shipping', 'Supply Chain & Logistik', 'Material-, Lager- und Distributionskonzepte, Serialisierung'),
             ('account_tree', 'Projektmanagement & PMO', 'Steuerung von Investitionsprojekten bis zur Übergabe an den Betrieb'),
             ('speed', 'Operational Excellence', 'OEE-Steigerung, Lean Lab, Kapazitäts- und Personalplanung')]
    cw, ch_, gx, gy = (W - 2 * 0.3) / 3, 1.95, 0.3, 0.3
    for i, (ic, h, d) in enumerate(items):
        x = L + (i % 3) * (cw + gx); y = 1.45 + (i // 3) * (ch_ + gy)
        rect(s, x, y, cw, ch_, fill=LSAND)
        icon_circle(s, ic, x + 0.25, y + 0.25, 0.6)
        text(s, x + 0.25, y + 0.98, cw - 0.5, 0.35, h, size=16)
        text(s, x + 0.25, y + 1.35, cw - 0.5, 0.6, d, size=12, color=DGRAY)
    sowhat(s, 'Ein Ansprechpartner für Planung, Umsetzung und Qualifizierung reduziert Schnittstellen und Time-to-Market.')

    s = D.slide('content', 'Vier Kundensegmente – vier unterschiedliche Prioritäten',
                'Über uns | Kundensegmente', key='segments',
                notes=N('Zeigt, dass wir die Logik des jeweiligen Segments verstehen.', 'Herausforderungen je Segment mit aktuellen Markteinblicken schärfen.',
                        'Im Termin nur das Segment des Kunden vertiefen.'))
    segs = [('medication', 'Big Pharma', ['Globale Netzwerk-Harmonisierung', 'Portfolio-Shift zu Biologika', 'Kostendruck in reifen Produkten'], 'Standardisierte Werkskonzepte und Programm-PMO'),
            ('biotech', 'Biotech & ATMP', ['Schneller Scale-up aus der Klinik', 'Begrenzte interne Ressourcen', 'Neue regulatorische Pfade'], 'Flexible, modulare Anlagen und Ramp-up-Begleitung'),
            ('precision_manufacturing', 'CDMO', ['Auslastung und Multi-Produkt-Fähigkeit', 'Schnelle Technologietransfers', 'Kundenaudits'], 'Rüst- und Reinigungskonzepte, Transfer-Playbooks'),
            ('vaccines', 'Generika & OTC', ['Margendruck', 'Hohe Volumina', 'Lieferfähigkeit'], 'OEE-Programme und Automatisierung')]
    cw = (W - 3 * 0.3) / 4
    for i, (ic, h, ch2, us) in enumerate(segs):
        x = L + i * (cw + 0.3)
        icon(s, ic, x, 1.5, 0.5, BLUE)
        hline(s, x, 2.15, cw, BLACK)
        text(s, x, 2.28, cw, 0.4, h, size=18)
        label(s, x, 2.8, cw, 'Typische Herausforderungen', color=DGRAY)
        text(s, x, 3.1, cw, 1.4, bl(ch2), size=12)
        rect(s, x, 4.55, cw, 1.25, fill=LSAND)
        label(s, x + 0.18, 4.68, cw - 0.3, 'Unser Beitrag')
        text(s, x + 0.18, 4.98, cw - 0.3, 0.8, us, size=12)

    s = D.slide('content', 'Beratung, Technik und Software aus einer Hand verkürzen Schnittstellen',
                'Über uns | Körber-Ökosystem', key='ecosystem',
                notes=N('Differenzierung über das Körber-Ökosystem.', 'Bereiche an die aktuelle Struktur der Körber-Gruppe anpassen.',
                        'Betonen: Wir beraten herstellerunabhängig – das Ökosystem ist eine Option, keine Bedingung.'))
    cx, cy = 3.6, 3.75
    oval(s, cx - 1.05, cy - 1.05, 2.1, fill=BLUE, content='Ihr Projekt', size=16, color=WHITE, align='c', anchor='m')
    sats = [('Consulting', 'psychology', -1, -1), ('Maschinen & Anlagen', 'precision_manufacturing', 1, -1),
            ('Software & MES', 'memory', -1, 1), ('Service & Lifecycle', 'support_agent', 1, 1)]
    for t, ic, dx, dy in sats:
        x = cx + dx * 2.0 - 0.75; y = cy + dy * 1.45 - 0.75
        arrow(s, cx + dx * 0.78, cy + dy * 0.78, cx + dx * 1.5, cy + dy * 1.0, color=STONE)
        oval(s, x, y, 1.5, fill=WHITE, line=BLUE, lw=1.25)
        icon(s, ic, x + 0.55, y + 0.22, 0.4, BLUE)
        text(s, x + 0.1, y + 0.68, 1.3, 0.6, t, size=11, align='c')
    xr = 7.3; wr = R - xr
    pts = [('Consulting', 'Herstellerunabhängige Planung, Qualifizierung und Projektsteuerung'),
           ('Maschinen & Anlagen', 'Prozess-, Inspektions- und Verpackungstechnologie aus der Gruppe'),
           ('Software & MES', 'Integrierte Lösungen für papierlose, validierte Produktion'),
           ('Service & Lifecycle', 'Wartung, Ersatzteile und Modernisierung über die Lebensdauer')]
    for i, (h, b) in enumerate(pts):
        y = 1.5 + i * 1.05
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, wr, 0.3, h, size=15)
        text(s, xr, y + 0.45, wr, 0.5, b, size=12, color=DGRAY)
    sowhat(s, 'Weniger Schnittstellen bedeuten weniger Abstimmungsschleifen – und eine schnellere Freigabe.')

    s = D.slide('content', 'Drei Gründe, warum Kunden mit uns arbeiten',
                'Über uns | Differenzierung', key='why',
                notes=N('Kern der Positionierung – in jeder Lösungs- oder Angebotspräsentation.', 'Belege mit konkreten Projektergebnissen untermauern.',
                        'Differenzierung immer aus Kundensicht formulieren: Was hat der Kunde davon?'))
    why = [('engineering', 'Umsetzungsstärke', 'Wir planen nicht nur – wir begleiten bis zur validierten Anlage und übernehmen Verantwortung für das Ergebnis.', 'Beleg: [xx] % der Projekte in Zeit und Budget'),
           ('verified', 'Regulatorische Tiefe', 'Unsere Teams kennen EU-GMP, FDA und lokale Behörden aus der Praxis – Inspektionen inklusive.', 'Beleg: [xx] Inspektionen ohne kritische Beobachtung'),
           ('hub', 'Körber-Ökosystem', 'Zugriff auf Maschinen-, Software- und Service-Know-how der Gruppe – herstellerunabhängig eingesetzt.', 'Beleg: [xx] Projekte mit integriertem Lösungsansatz')]
    cw = (W - 2 * 0.5) / 3
    for i, (ic, h, b, p) in enumerate(why):
        x = L + i * (cw + 0.5)
        colhead(s, x, 1.5, cw, 'Grund %d' % (i + 1), h, b, icon_=ic, hsize=20, bsize=13, bh=1.4)
        rect(s, x, 4.55, cw, 0.75, fill=LSAND)
        text(s, x + 0.2, 4.55, cw - 0.4, 0.75, p, size=12, anchor='m', color=BLUE)

    s = D.slide('content', 'Wir verbinden strategische Beratung mit technischer Umsetzungstiefe',
                'Über uns | Wettbewerbsposition', 'Quelle: Eigene Einschätzung; Positionierung illustrativ', key='position', sticker_='Illustrativ',
                notes=N('Einordnung gegenüber Wettbewerbsgruppen – vor allem bei Ausschreibungen.', 'Wettbewerber nur als Gruppen zeigen, keine Namen auf Kundenfolien.',
                        'Intern kann die Matrix mit konkreten Wettbewerbern befüllt werden (Battlecard).'))
    gx0, gy0, gw, gh = L + 0.5, 1.5, 6.8, 4.3
    rect(s, gx0, gy0, gw / 2, gh / 2, fill=LSAND); rect(s, gx0 + gw / 2, gy0, gw / 2, gh / 2, fill=LBLUE)
    rect(s, gx0, gy0 + gh / 2, gw / 2, gh / 2, fill=LSAND); rect(s, gx0 + gw / 2, gy0 + gh / 2, gw / 2, gh / 2, fill=LSAND)
    arrow(s, gx0, gy0 + gh, gx0 + gw + 0.1, gy0 + gh, color=BLACK, lw=1)
    arrow(s, gx0, gy0 + gh, gx0, gy0 - 0.1, color=BLACK, lw=1)
    text(s, gx0, gy0 + gh + 0.08, gw, 0.3, 'Strategische Beratungstiefe →', size=11, align='r')
    tb = text(s, L - 0.05, gy0, 0.4, gh, 'Umsetzungs- und Technologiekompetenz →', size=11, align='r')
    tb.rotation = 270; tb.left = I(L - 1.95); tb.top = I(gy0 + gh / 2 - 0.2); tb.width = I(gh); tb.height = I(0.35)
    pos = [('Engineering-\nDienstleister', 1.2, 0.9, STONE), ('Strategie-\nberatungen', 5.4, 2.9, STONE),
           ('Wirtschafts-\nprüfer', 3.3, 2.6, STONE), ('Körber', 5.4, 0.8, BLUE)]
    for t, px, py, c in pos:
        d = 0.9 if c == BLUE else 0.7
        oval(s, gx0 + px, gy0 + py, d, fill=c)
        text(s, gx0 + px - 0.6, gy0 + py + d + 0.05, d + 1.2, 0.5, t, size=11, align='c', color=BLUE if c == BLUE else BLACK)
    xr = 8.3; wr = R - xr
    label(s, xr, 1.5, wr, 'Was das für Sie bedeutet')
    for i, (h, b) in enumerate([('Keine Lücke zwischen Konzept und Realität', 'Unsere Empfehlungen sind von Anfang an baubar und qualifizierbar.'),
                                ('Ein Team über alle Phasen', 'Wissen bleibt im Projekt – keine Übergabeverluste.'),
                                ('Messbare Ergebnisse', 'Wir werden am Betriebsergebnis gemessen, nicht an Konzeptpapieren.')]):
        y = 1.9 + i * 1.3
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, wr, 0.5, h, size=14)
        text(s, xr, y + 0.62, wr, 0.6, b, size=12, color=DGRAY)

    s = D.slide('content', 'Lokal präsent in Ihren Kernmärkten – global vernetzt',
                'Über uns | Präsenz', 'Quelle: [Körber, Stand JJJJ]', key='map', sticker_='Standorte einsetzen',
                notes=N('Präsenz und Nähe zum Kunden zeigen, v. a. bei internationalen Netzwerken.', 'Punkte auf die echten Standorte verschieben, Zahlen ergänzen.'))
    picture(s, os.path.join(HERE, 'worldmap.png'), L, 1.5, 8.2, 5.0)
    for px, py, big in [(4.05, 2.35, True), (3.85, 2.55, False), (4.3, 2.45, False), (1.8, 2.75, True), (6.9, 3.0, False), (5.6, 3.35, False)]:
        d = 0.32 if big else 0.2
        oval(s, L + px, 1.5 + py, d, fill=BLUE)
    xr = 9.0; wr = R - xr
    for i, (a, b) in enumerate([('[xx]', 'Standorte in Europa'), ('[xx]', 'Standorte in Nordamerika'), ('[xx]', 'Standorte in Asien-Pazifik')]):
        kpi(s, xr, 1.6 + i * 1.5, wr, a, b, bigsize=32)

    s = D.slide('content', 'Ihr Kernteam vereint Prozess-, Qualitäts- und Digitalisierungsexpertise',
                'Über uns | Team', key='team',
                notes=N('Vorstellung des Projektteams im Angebot oder Kick-off.', 'Fotos per „Bild ändern“ einsetzen, Profile auf die Kundenfrage zuschneiden.',
                        'Pro Person eine Referenz nennen, die für den Kunden relevant ist.'))
    roles = [('Projektleitung', ['[xx] Jahre Pharma-Projekte', 'PMP / IPMA', 'Referenz: [Projekt]']),
             ('Lead Process Engineering', ['Sterile Abfüllung, Isolatoren', 'Layout und Materialfluss', 'Referenz: [Projekt]']),
             ('Lead CQV', ['Qualifizierungsstrategie', 'EU-GMP, FDA, Annex 1', 'Referenz: [Projekt]']),
             ('Lead Digitalisierung', ['MES, Pharma 4.0', 'CSV / CSA', 'Referenz: [Projekt]'])]
    cw = (W - 3 * 0.3) / 4
    for i, (r, b) in enumerate(roles):
        x = L + i * (cw + 0.3)
        rect(s, x, 1.5, cw, 4.6, fill=LSAND)
        person(s, x + (cw - 1.3) / 2, 1.75, 1.3)
        text(s, x + 0.2, 3.25, cw - 0.4, 0.3, '[Vorname Name]', size=15, align='c')
        text(s, x + 0.2, 3.6, cw - 0.4, 0.3, r, size=12, color=BLUE, align='c')
        hline(s, x + 0.25, 4.05, cw - 0.5, STONE)
        text(s, x + 0.25, 4.2, cw - 0.5, 1.6, bl(b), size=12)

    s = D.slide('content', 'Fünf Prinzipien prägen unsere Zusammenarbeit mit Ihnen',
                'Über uns | Arbeitsweise', key='principles',
                notes=N('Kultur und Zusammenarbeit – gut für Kick-off und Angebot.', 'Prinzipien mit konkreten Beispielen aus Projekten ergänzen.'))
    pr = [('Ergebnis vor Konzept', 'Jede Empfehlung wird an ihrem Beitrag zu Zeit, Kosten und Qualität gemessen.'),
          ('Ein Team mit Ihnen', 'Gemischte Teams und gemeinsame Workshops statt Black-Box-Beratung.'),
          ('Transparenz', 'Wöchentlicher Status, offene Risiken und klare Entscheidungsvorlagen.'),
          ('Befähigung', 'Wissenstransfer an Ihr Team ist fester Bestandteil jedes Projekts.'),
          ('Compliance by Design', 'GMP-Anforderungen sind von Anfang an mitgedacht – nicht nachträglich ergänzt.')]
    for i, (h, b) in enumerate(pr):
        y = 1.5 + i * 0.9
        num(s, L, y + 0.1, i + 1, 0.5)
        text(s, L + 0.8, y + 0.15, 3.6, 0.4, h, size=17)
        text(s, L + 4.6, y + 0.15, 8.0, 0.6, b, size=13)
        if i < 4:
            hline(s, L + 0.8, y + 0.82, W - 0.8, STONE, 0.5)


# =====================================================================================
def s03(D):
    divider(D, 3, 'Markt &\nKunden-\nverständnis', N('Trends, Ausgangslage, Hypothesen und Analyse des Kunden.',
                                                   'Folien mit kundenspezifischen Erkenntnissen füllen.',
                                                   'Dieses Kapitel entscheidet über Glaubwürdigkeit – hier zeigen wir, dass wir zugehört haben.'))
    s = D.slide('content', 'Sechs Trends verändern die pharmazeutische Produktion bis 2030',
                'Markt & Kunde | Trends', 'Quelle: [Quelle, Jahr]', key='trends',
                notes=N('Einstieg ins Kundengespräch auf C-Level – Thought Leadership.', 'Trends mit aktuellen Studien und Zahlen belegen.',
                        'Mit der Frage abschließen: „Welche dieser Trends betreffen Sie am stärksten?“'))
    tr = [('biotech', 'Biologika & ATMP', 'Kleinere Chargen, höhere Komplexität: Anlagen müssen flexibel und multi-produktfähig werden.'),
          ('verified', 'Regulatorischer Druck', 'Annex 1, Data Integrity und KI-Regulierung erhöhen den Qualifizierungsaufwand.'),
          ('memory', 'Pharma 4.0 & KI', 'Papierlose Produktion und datenbasierte Freigabe werden zum Wettbewerbsfaktor.'),
          ('eco', 'Nachhaltigkeit', 'Energie- und Wasserverbrauch rücken in den Fokus von Investoren und Behörden.'),
          ('local_shipping', 'Resiliente Lieferketten', 'Regionalisierung und Second-Source-Strategien verändern Standortentscheidungen.'),
          ('groups', 'Fachkräftemangel', 'Automatisierung und Wissenssicherung werden zur Voraussetzung für Wachstum.')]
    cw = (W - 2 * 0.5) / 3
    for i, (ic, h, b) in enumerate(tr):
        x = L + (i % 3) * (cw + 0.5); y = 1.5 + (i // 3) * 2.3
        icon_circle(s, ic, x, y, 0.62)
        text(s, x + 0.85, y + 0.12, cw - 0.85, 0.4, h, size=17)
        hline(s, x, y + 0.85, cw, STONE, 0.5)
        text(s, x, y + 1.0, cw, 1.1, b, size=13)

    s = D.slide('content', 'Digitalisierung und Annex 1 haben für [Kunde] die höchste Priorität',
                'Markt & Kunde | Trend-Relevanz', 'Quelle: Workshop mit [Kunde], [Datum]; Bewertung illustrativ', key='trendmatrix', sticker_='Illustrativ',
                notes=N('Ergebnis eines Discovery-Workshops: Welche Trends sind für den Kunden relevant?', 'Kreise per Drag & Drop verschieben; Größe = Investitionsbedarf.'))
    gx0, gy0, gw, gh = L + 0.55, 1.45, 7.4, 4.5
    rect(s, gx0, gy0, gw, gh, fill=LSAND)
    rect(s, gx0 + gw / 2, gy0, gw / 2, gh / 2, fill=LBLUE)
    hline(s, gx0, gy0 + gh / 2, gw, WHITE, 1.5); vline(s, gx0 + gw / 2, gy0, gh, WHITE, 1.5)
    text(s, gx0, gy0 + gh + 0.08, gw, 0.3, 'Dringlichkeit (Zeithorizont) →', size=11, align='r')
    tb = text(s, 0, 0, gh, 0.35, 'Auswirkung auf das Geschäft →', size=11, align='r')
    tb.rotation = 270; tb.left = I(gx0 - 0.4 - gh / 2); tb.top = I(gy0 + gh / 2 - 0.17)
    text(s, gx0 + gw / 2 + 0.15, gy0 + 0.1, 3, 0.3, 'Jetzt handeln', size=11, color=BLUE)
    pts = [('Pharma 4.0 & KI', 5.3, 0.35, 1.0, True), ('Regulatorik', 4.0, 1.15, 0.85, True), ('Biologika', 2.6, 0.9, 0.75, False),
           ('Fachkräfte', 4.1, 2.6, 0.6, False), ('Lieferketten', 1.6, 2.9, 0.55, False), ('Nachhaltigkeit', 2.3, 3.4, 0.5, False)]
    for t, px, py, d, hi in pts:
        oval(s, gx0 + px, gy0 + py, d, fill=BLUE if hi else TAUPE)
        text(s, gx0 + px + d + 0.08, gy0 + py + d / 2 - 0.15, 1.6, 0.3, t, size=11)
    xr = 8.9; wr = R - xr
    label(s, xr, 1.5, wr, 'Implikationen')
    text(s, xr, 1.85, wr, 3.5, bl(['Digitalisierung der Chargenfreigabe als Hebel für Durchlaufzeit und Data Integrity',
                                   'Annex-1-Gap-Assessment vor der nächsten Inspektion',
                                   'Biologika-Strategie in der Standortplanung berücksichtigen'], sa=10), size=13)
    text(s, xr, 4.9, wr, 0.6, 'Kreisgröße = erwarteter Investitionsbedarf', size=10, color=DGRAY)

    s = D.slide('content', 'Ausgangslage: Wachstum trifft auf eine Anlage am Kapazitätslimit',
                'Markt & Kunde | Situation – Komplikation – Lösung', key='scr',
                notes=N('Storyline-Einstieg nach dem SCR-Prinzip (Situation, Complication, Resolution).',
                        'Drei Sätze mit kundenspezifischen Fakten füllen.', 'Die Komplikation muss für den Kunden schmerzhaft konkret sein.'))
    scr = [('Situation', 'Die Nachfrage nach [Produkt] wächst um [xx] % p. a.', 'Die Abfülllinie läuft im Drei-Schicht-Betrieb bei [xx] % Auslastung.', LSAND, BLACK),
           ('Komplikation', 'Ab [Jahr] fehlen [xx] Mio. Einheiten Kapazität', 'Annex 1 erfordert zudem Investitionen in die bestehende Linie.', SAND, BLACK),
           ('Lösung', 'Neue Isolator-Linie plus Ertüchtigung der Bestandslinie', 'Gestaffelte Umsetzung sichert die Lieferfähigkeit in jeder Phase.', BLUE, WHITE)]
    cw = (W - 2 * 0.45) / 3
    for i, (lab, h, b, f, c) in enumerate(scr):
        x = L + i * (cw + 0.45)
        rect(s, x, 1.5, cw, 3.9, fill=f)
        label(s, x + 0.3, 1.75, cw - 0.6, lab, color=WHITE if f == BLUE else BLUE)
        text(s, x + 0.3, 2.15, cw - 0.6, 1.4, h, size=20, color=c)
        text(s, x + 0.3, 3.75, cw - 0.6, 1.3, b, size=13, color=c)
        if i < 2:
            oval(s, x + cw + 0.04, 3.27, 0.37, fill=WHITE, line=STONE)
            icon(s, 'arrow_forward', x + cw + 0.1, 3.33, 0.25, BLUE)
    sowhat(s, 'Ohne Entscheidung bis [Quartal] entsteht ab [Jahr] eine Lieferlücke – der kritische Pfad beginnt heute.')

    s = D.slide('content', 'Was wir gehört haben: Drei Themen ziehen sich durch alle Gespräche',
                'Markt & Kunde | Interview-Synthese', 'Quelle: [x] Interviews mit [Kunde], [Zeitraum]', key='heard',
                notes=N('Synthese aus Stakeholder-Interviews – stärkt Vertrauen und Glaubwürdigkeit.',
                        'Originalzitate anonymisiert verwenden, Freigabe einholen.', 'Zitate in der Sprache des Kunden – nicht glätten.'))
    q = [('„Wir verlieren pro Rüstvorgang fast eine ganze Schicht.“', 'Leitung Produktion'),
         ('„Jede Abweichung kostet uns Wochen in der Freigabe.“', 'Leitung Qualitätssicherung'),
         ('„Wir haben die Daten – aber nicht dort, wo wir sie brauchen.“', 'Leitung IT/OT')]
    for i, (t, w_) in enumerate(q):
        y = 1.5 + i * 1.5
        rect(s, L, y, 6.6, 1.3, fill=LSAND)
        text(s, L + 0.25, y + 0.05, 0.6, 0.8, '“', size=48, color=BLUE)
        text(s, L + 0.9, y + 0.2, 5.5, 0.7, t, size=15)
        text(s, L + 0.9, y + 0.88, 5.5, 0.3, '– ' + w_, size=11, color=DGRAY)
    xr = 7.4; wr = R - xr
    label(s, xr, 1.5, wr, 'Unsere Schlussfolgerung')
    for i, (h, b) in enumerate([('Rüstzeiten', 'sind der größte Kapazitätshebel'), ('Freigabeprozess', 'ist der Engpass für die Durchlaufzeit'),
                                ('Datenintegration', 'ist die Voraussetzung für beides')]):
        y = 1.9 + i * 1.3
        num(s, xr, y, i + 1, 0.45)
        text(s, xr + 0.65, y - 0.02, wr - 0.65, 0.35, h, size=17, color=BLUE)
        text(s, xr + 0.65, y + 0.38, wr - 0.65, 0.5, b, size=13)

    s = D.slide('content', 'Die Kernfrage lässt sich in drei prüfbare Teilfragen zerlegen',
                'Markt & Kunde | Issue Tree', key='issuetree',
                notes=N('Strukturierung des Problems (MECE) zu Projektbeginn oder im Angebot.', 'Kernfrage als SMART-Frage formulieren; Teilfragen überschneidungsfrei.',
                        'Jede Teilfrage muss mit Daten beantwortbar sein – sonst weiter zerlegen.'))
    shape(s, SH.RECTANGLE, L, 3.0, 2.8, 1.5, fill=BLUE, content='Wie steigern wir die Kapazität um 30 % bis [Jahr] bei gleichbleibender Compliance?',
          size=13, color=WHITE, anchor='m')
    drv = [('Bestehende Linie', ['Wie stark lässt sich die OEE steigern?', 'Welche Rüstzeiten sind vermeidbar?']),
           ('Neue Kapazität', ['Welche Technologie ist zukunftsfähig?', 'Welcher Standort ist optimal?']),
           ('Organisation', ['Welche Schichtmodelle sind möglich?', 'Welche Qualifikationen fehlen?'])]
    for i, (d, subs) in enumerate(drv):
        y = 1.5 + i * 1.6
        arrow(s, L + 2.8, 3.75, L + 3.4, y + 0.6, color=TAUPE)
        shape(s, SH.RECTANGLE, L + 3.4, y + 0.3, 2.6, 0.6, fill=SAND, content=d, size=14, anchor='m')
        for j, q_ in enumerate(subs):
            yy = y + j * 0.7
            arrow(s, L + 6.0, y + 0.6, L + 6.5, yy + 0.27, color=STONE)
            shape(s, SH.RECTANGLE, L + 6.5, yy, 3.9, 0.55, line=STONE, content=q_, size=12, anchor='m')
            text(s, L + 10.6, yy, 2.0, 0.55, ['Analyse: [Methode]'], size=11, color=DGRAY, anchor='m')
    label(s, L + 10.6, 1.2, 2.0, 'Analyse')

    s = D.slide('content', 'Drei Hypothesen strukturieren die Analyse – zwei sind bereits bestätigt',
                'Markt & Kunde | Hypothesen', 'Stand: [Datum]', key='hypotheses',
                notes=N('Hypothesengetriebenes Arbeiten sichtbar machen (Discovery, Steering Committee).', 'Status nach jeder Analysewelle aktualisieren.'))
    rows = [['#', 'Hypothese', 'Prüfung durch', 'Ergebnis', 'Status'],
            ['H1', 'Rüst- und Reinigungszeiten verursachen > 50 % der OEE-Verluste', 'Auswertung Linienstillstände (12 Monate)', '62 % der Verluste – bestätigt', ''],
            ['H2', 'Die Chargenfreigabe ist der Engpass der Durchlaufzeit', 'Prozessaufnahme, Wertstromanalyse', 'Ø 18 Tage Freigabe – bestätigt', ''],
            ['H3', 'Ein Zwei-Schicht-Modell reicht nach Optimierung aus', 'Kapazitätsmodell, Szenarien', 'In Prüfung bis [Datum]', '']]
    tb = table(s, L, 1.5, W, rows, colw=[0.6, 4.2, 3.2, 3.2, 1.4], rowh=[0.45, 0.85, 0.85, 0.85], size=13, aligns=['l', 'l', 'l', 'l', 'c'])
    for r in range(1, 4):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=15, color=BLUE, anchor='m')
    for r, st in zip(range(1, 4), ['Bestätigt', 'Bestätigt', 'Offen']):
        c = tb.cell(r, 4)
        fill_tf(c.text_frame, st, size=11, color=WHITE if st != 'Offen' else BLACK, align='c', anchor='m')
        c.fill.solid(); setc(c.fill.fore_color, BLUE if st != 'Offen' else SAND)
    sowhat(s, 'Die bestätigten Hypothesen H1 und H2 bilden den Kern des Lösungsansatzes; H3 entscheidet über die Personalplanung.')

    s = D.slide('content', 'Der größte Reifegrad-Abstand liegt bei Daten & Systemen',
                'Markt & Kunde | Reifegrad-Assessment', 'Quelle: Assessment mit [Kunde], [Datum]; Werte illustrativ', key='maturity', sticker_='Illustrativ',
                notes=N('Ergebnis eines Reifegrad-Assessments (Digitalisierung, Compliance, OpEx).', 'Dimensionen und Werte (1–5) anpassen: Punkte horizontal verschieben.',
                        'Der Abstand Ist–Ziel priorisiert die Handlungsfelder.'))
    dims = [('Strategie & Governance', 3, 4), ('Prozesse', 2.5, 4), ('Daten & Systeme', 1.5, 4.5), ('Organisation & Skills', 2, 3.5), ('Compliance', 3.5, 4.5)]
    x0, x1 = L + 3.4, L + 10.4
    step = (x1 - x0) / 4
    for k in range(5):
        text(s, x0 + k * step - 0.5, 1.45, 1.0, 0.3, str(k + 1), size=12, align='c', color=DGRAY)
    text(s, x0 - 0.5, 1.72, 2, 0.3, 'Initial', size=10, color=DGRAY)
    text(s, x1 - 1.5, 1.72, 2, 0.3, 'Best Practice', size=10, color=DGRAY, align='r')
    for i, (d, ist, ziel) in enumerate(dims):
        y = 2.2 + i * 0.72
        text(s, L, y, 3.2, 0.4, d, size=14, anchor='m')
        hline(s, x0, y + 0.2, x1 - x0, STONE, 0.75)
        xi, xz = x0 + (ist - 1) * step, x0 + (ziel - 1) * step
        hline(s, xi, y + 0.2, xz - xi, BLUE, 3)
        oval(s, xi - 0.14, y + 0.06, 0.28, fill=BLUE)
        oval(s, xz - 0.14, y + 0.06, 0.28, fill=WHITE, line=BLUE, lw=2)
        gap = ziel - ist
        text(s, x1 + 0.6, y, 1.6, 0.4, '+%.1f' % gap, size=14, color=BLUE if gap >= 2.5 else BLACK, anchor='m')
    label(s, x1 + 0.6, 1.72, 1.6, 'Abstand', color=DGRAY)
    dot(s, L, 5.9, 0.18, BLUE); text(s, L + 0.28, 5.86, 1.5, 0.3, 'Ist', size=11)
    oval(s, L + 1.0, 5.9, 0.18, fill=WHITE, line=BLUE, lw=1.5); text(s, L + 1.28, 5.86, 1.5, 0.3, 'Ziel ([Jahr])', size=11)

    s = D.slide('content', 'Die Gesamtanlageneffektivität liegt 14 Prozentpunkte unter dem Benchmark',
                'Markt & Kunde | Benchmark', 'Quelle: [Benchmark-Datenbank, n = xx]; Werte illustrativ', key='benchmark', sticker_='Illustrativ',
                notes=N('Quantifizierter Vergleich mit Wettbewerb – erzeugt Handlungsdruck.', 'Diagramm per Rechtsklick > „Daten bearbeiten“ anpassen.',
                        'Immer die Lücke in Euro übersetzen – das ist die Sprache des CFO.'))
    bar(s, L, 1.4, 7.6, 4.4, ['Best in Class', 'Top-Quartil', 'Median', '[Kunde]', 'Unteres Quartil'], [('OEE', [0.78, 0.68, 0.59, 0.54, 0.45])],
        kind='bar', fmt='0%', highlight=3, gap=45, size=12)
    x0 = 8.5
    label(s, x0, 1.5, 4.4, 'Einordnung')
    for i, (big, t) in enumerate([('–14 pp', 'Abstand zum Top-Quartil'), ('€ 3,2 Mio.', 'Ergebnispotenzial p. a. bei Schließung der Lücke'),
                                  ('62 %', 'der Verluste durch Rüst- und Reinigungszeiten')]):
        y = 1.85 + i * 1.3
        hline(s, x0, y, R - x0, BLACK, 0.75)
        text(s, x0, y + 0.12, 4.4, 0.6, big, size=28, color=BLUE)
        text(s, x0, y + 0.72, 4.4, 0.4, t, size=12)
    sowhat(s, 'Rüst- und Reinigungsprozesse sind der größte Hebel – hier setzt Phase 1 an.')

    s = D.slide('content', 'Engpässe konzentrieren sich auf Abfüllung sowie Prüfung und Freigabe',
                'Markt & Kunde | Pain Points entlang der Wertschöpfung', 'Quelle: Prozessaufnahme bei [Kunde], [Datum]', key='painpoints',
                notes=N('Prozessaufnahme mit Engpassbewertung.', 'Prozessschritte und Pain Points des Kunden einsetzen; Harvey Balls = Schwere.'))
    steps = ['Wareneingang', 'Herstellung', 'Abfüllung', 'Prüfung & Freigabe', 'Distribution']
    chevrons(s, steps, L, 1.45, W, 0.6, active=[2, 3], size=12)
    pains = [['Manuelle Musterzüge', 'Doppelte Erfassung'], ['Papierbasierte Chargenprotokolle'], ['Rüstzeit Ø 7 h', 'Reinigungsvalidierung je Produkt'],
             ['Freigabe Ø 18 Tage', 'Abweichungen ohne Ursachenanalyse'], ['Kühlkette manuell überwacht']]
    sev = [1, 2, 4, 4, 1]
    cw = (W - 4 * 0.06) / 5
    for i in range(5):
        x = L + i * (cw + 0.06)
        rect(s, x, 2.2, cw, 3.55, fill=LSAND if i not in (2, 3) else LBLUE)
        text(s, x + 0.18, 2.35, cw - 0.3, 2.0, bl(pains[i]), size=12)
        harvey(s, x + 0.18, 5.25, 0.32, sev[i])
        text(s, x + 0.6, 5.27, cw - 0.7, 0.3, {1: 'gering', 2: 'mittel', 3: 'erhöht', 4: 'hoch'}[sev[i]], size=11, color=DGRAY)
    sowhat(s, 'Zwei von fünf Prozessschritten verursachen über 80 % der Durchlaufzeit – dort konzentrieren wir die Analyse.')

    s = D.slide('content', 'Regulatorische Anforderungen steigen – vier Meilensteine prägen Ihre Planung',
                'Markt & Kunde | Regulatorische Treiber', 'Quelle: EMA, EU-Kommission; Stand [Datum] – vor Verwendung prüfen', key='regulatory', sticker_='Vor Nutzung prüfen',
                notes=N('Regulatorischer Kontext für Qualitäts- und Compliance-Themen.', 'Termine vor jedem Einsatz prüfen und um kundenrelevante Regularien ergänzen (FDA, lokale Behörden).',
                        'Daten ändern sich – diese Folie hat das kürzeste Haltbarkeitsdatum der Bibliothek.'))
    ev = [('08/2023', 'EU-GMP Annex 1', 'Revidierte Anforderungen an die sterile Herstellung, inkl. Contamination Control Strategy'),
          ('08/2024', 'EU AI Act', 'Inkrafttreten; gestaffelte Pflichten für KI-Systeme in den Folgejahren'),
          ('10/2024', 'NIS2', 'Frist zur nationalen Umsetzung – höhere Anforderungen an die OT-Sicherheit'),
          ('2025+', 'EU-GMP Annex 11 / Annex 22', 'Überarbeitung computergestützter Systeme, neuer Anhang zu KI (Entwurf)'),
          ('[JJJJ]', '[Weitere Regularie]', '[Beschreibung und Relevanz für den Kunden]')]
    y0 = 3.2
    hline(s, L, y0, W, BLACK, 1.25)
    cw = W / 5
    for i, (d, h, b) in enumerate(ev):
        x = L + i * cw
        oval(s, x + 0.02, y0 - 0.13, 0.26, fill=BLUE if i < 4 else WHITE, line=BLUE, lw=1.5)
        text(s, x, y0 - 1.15, cw - 0.2, 0.5, d, size=24, color=BLUE)
        text(s, x, y0 - 0.6, cw - 0.2, 0.35, h, size=13)
        text(s, x, y0 + 0.35, cw - 0.25, 1.6, b, size=12, color=DGRAY)
    sowhat(s, 'Compliance-Anforderungen frühzeitig in die Anlagenplanung integrieren – Nachrüsten kostet ein Vielfaches.')


# =====================================================================================
def s04(D):
    divider(D, 4, 'Buying\nCenter', N('Buying Center, Stakeholder-Strategie und Entscheidungsprozess.',
                                       'Folien mit „intern“ nicht beim Kunden zeigen.',
                                       'Komplexe B2B-Entscheidungen werden von 6–10 Personen getroffen – jede braucht ihr eigenes Argument.'))
    s = D.slide('content', 'Im Buying Center entscheiden sechs Rollen – jede mit eigener Erfolgslogik',
                'Buying Center | Rollen (intern)', key='buyingcenter', sticker_='Intern',
                notes=N('Account- und Opportunity-Planung intern; Basis für Stakeholder-Strategie.', 'Namen der Personen beim Kunden je Rolle ergänzen.',
                        'Im CRM je Kontakt die Buying-Center-Rolle pflegen – das macht Abdeckung messbar.'))
    oval(s, 5.27, 2.25, 2.8, fill=BLUE, content='Investitions-\nentscheidung\n[Projekt]', size=16, color=WHITE, align='c', anchor='m')
    roles = [('Entscheider', 'Site Head / COO', '„Sichert das unsere Lieferfähigkeit?“', 'person'),
             ('Budget', 'CFO / Controlling', '„Wann rechnet sich das?“', 'euro'),
             ('Fachbereich', 'Produktion / Engineering', '„Funktioniert das im Betrieb?“', 'engineering'),
             ('Qualität', 'Head of QA / QP', '„Bestehen wir die Inspektion?“', 'verified'),
             ('IT / OT', 'CIO / OT-Leitung', '„Passt das in unsere Architektur?“', 'lan'),
             ('Einkauf', 'Procurement', '„Ist das Angebot vergleichbar und fair?“', 'shopping_cart')]
    cw, chh = 4.5, 1.32
    for i, (r, p, q, ic) in enumerate(roles):
        left = i < 3
        x = L if left else R - cw
        y = 1.45 + (i % 3) * (chh + 0.16)
        rect(s, x, y, cw, chh, fill=LSAND)
        icon(s, ic, x + 0.2, y + 0.2, 0.4, BLUE)
        label(s, x + 0.8, y + 0.2, cw - 1, r)
        text(s, x + 0.8, y + 0.45, cw - 1, 0.3, p, size=14)
        text(s, x + 0.8, y + 0.85, cw - 1, 0.5, q, size=12, italic=True, color=DGRAY)
        hline(s, x + cw if left else 8.07, y + chh / 2, 0.4 if True else 0, STONE) if False else None
    sowhat(s, 'Wir brauchen zu jeder Rolle einen Kontakt und ein passendes Nutzenargument – Lücken sind Deal-Risiken.', y=6.0, h=0.55)

    s = D.slide('content', 'Stakeholder-Matrix: Zwei Schlüsselpersonen müssen wir enger einbinden',
                'Buying Center | Einfluss und Haltung (intern)', 'Stand: [Datum]; Einschätzung Account-Team', key='stakeholder', sticker_='Intern',
                notes=N('Stakeholder-Strategie für Opportunity oder Account.', 'Personen als Kreise verschieben; Farbe = Haltung zu Körber.',
                        'Ziel: Alle Personen mit hohem Einfluss in den oberen rechten Quadranten bewegen.'))
    gx0, gy0, gw, gh = L + 0.55, 1.45, 7.2, 4.5
    quads = [('Zufriedenstellen', 0, 0), ('Eng einbinden', 1, 0), ('Beobachten', 0, 1), ('Informieren', 1, 1)]
    for t, qx, qy in quads:
        rect(s, gx0 + qx * gw / 2, gy0 + qy * gh / 2, gw / 2 - 0.03, gh / 2 - 0.03, fill=LBLUE if (qx, qy) == (1, 0) else LSAND)
        text(s, gx0 + qx * gw / 2 + 0.15, gy0 + qy * gh / 2 + 0.1, 3, 0.3, t, size=11, color=BLUE)
    text(s, gx0, gy0 + gh + 0.08, gw, 0.3, 'Interesse am Projekt →', size=11, align='r')
    tb = text(s, 0, 0, gh, 0.35, 'Einfluss auf die Entscheidung →', size=11, align='r')
    tb.rotation = 270; tb.left = I(gx0 - 0.4 - gh / 2); tb.top = I(gy0 + gh / 2 - 0.17)
    ppl = [('COO', 1.2, 0.6, ORANGE), ('CFO', 2.4, 1.1, STONE), ('Head of QA', 5.0, 0.8, BLUE), ('Leitung Produktion', 5.6, 1.6, BLUE),
           ('Einkauf', 2.0, 3.0, STONE), ('IT/OT', 4.6, 3.1, BLUE)]
    for t, px, py, c in ppl:
        oval(s, gx0 + px, gy0 + py, 0.42, fill=c)
        text(s, gx0 + px + 0.5, gy0 + py + 0.05, 1.8, 0.3, t, size=11)
    xr = 8.7; wr = R - xr
    label(s, xr, 1.5, wr, 'Haltung zu Körber')
    for i, (c, t) in enumerate([(BLUE, 'Befürworter'), (STONE, 'Neutral'), (ORANGE, 'Kritisch')]):
        dot(s, xr + i * 1.4, 1.88, 0.2, c); text(s, xr + i * 1.4 + 0.28, 1.84, 1.1, 0.3, t, size=11)
    label(s, xr, 2.5, wr, 'Nächste Schritte')
    text(s, xr, 2.85, wr, 3.0, bl(['COO: Executive-Termin mit [Körber-Geschäftsführung] bis [Datum]',
                                   'CFO: Business Case gemeinsam mit Controlling validieren',
                                   'Einkauf: frühzeitig Vergabekriterien abstimmen'], sa=8), size=13)

    s = D.slide('content', 'Beziehungen: Starker Zugang im Betrieb, Lücke in der Geschäftsführung',
                'Buying Center | Beziehungen (intern)', 'Stand: [Datum]', key='relmap', sticker_='Intern',
                notes=N('Organigramm des Kunden mit Beziehungsstatus – Grundlage für Account-Planung.', 'Boxen an die Organisation des Kunden anpassen; Kürzel = Körber-Owner.',
                        'Jede Box ohne Körber-Owner ist ein Handlungsfeld.'))
    def ob(x, y, t, n, st, own):
        f = {'p': BLUE, 'n': SAND, 'c': ORANGE, 'u': WHITE}[st]
        c = WHITE if st in ('p', 'c') else BLACK
        rect(s, x, y, 2.3, 0.85, fill=f, line=STONE if st == 'u' else None, content=[{'t': t, 'size': 12}, {'t': n, 'size': 10}], color=c, anchor='m', align='c')
        if own:
            oval(s, x + 2.05, y - 0.15, 0.38, fill=WHITE, line=BLUE, content=own, size=9, color=BLUE, align='c', anchor='m', margin=0)
    ob(5.52, 1.5, 'Geschäftsführung', '[Name]', 'u', None)
    xs = [1.2, 4.0, 6.8, 9.6]
    tops = [('Produktion', '[Name]', 'p', 'MM'), ('Qualität', '[Name]', 'p', 'AB'), ('Finanzen', '[Name]', 'n', None), ('IT / OT', '[Name]', 'c', 'KS')]
    hline(s, xs[0] + 1.15, 2.7, xs[3] - xs[0], STONE); vline(s, 6.67, 2.35, 0.35, STONE)
    for x, (t, n, st, o) in zip(xs, tops):
        vline(s, x + 1.15, 2.7, 0.3, STONE)
        ob(x, 3.0, t, n, st, o)
    subs = [(1.2, 'Engineering', 'p', 'MM'), (1.2, 'Instandhaltung', 'n', None), (4.0, 'QA Operations', 'p', None), (6.8, 'Einkauf', 'n', None), (9.6, 'Digitalisierung', 'u', None)]
    cnt = {}
    for x, t, st, o in subs:
        k = cnt.get(x, 0); cnt[x] = k + 1
        y = 4.2 + k * 1.05
        vline(s, x + 1.15, 3.85 + k * 1.05, 0.35, STONE)
        ob(x, y, t, '[Name]', st, o)
    leg = [(BLUE, 'Befürworter'), (SAND, 'Neutral'), (ORANGE, 'Kritisch'), (WHITE, 'Kein Kontakt')]
    for i, (c, t) in enumerate(leg):
        rect(s, L + i * 1.8, 6.3, 0.22, 0.22, fill=c, line=STONE if c == WHITE else None)
        text(s, L + i * 1.8 + 0.3, 6.27, 1.4, 0.3, t, size=10)
    oval(s, L + 7.4, 6.27, 0.28, fill=WHITE, line=BLUE, content='MM', size=7, color=BLUE, align='c', anchor='m', margin=0)
    text(s, L + 7.75, 6.27, 2.5, 0.3, 'Körber-Kontakt (Kürzel)', size=10)

    s = D.slide('content', 'Jede Rolle braucht ein eigenes Nutzenargument mit messbarem KPI',
                'Buying Center | Nutzenargumente je Rolle', key='valuemsg',
                notes=N('Messaging-Matrix für Angebot, Präsentation und Follow-up-Mails.', 'Argumente pro Opportunity schärfen; KPI mit Kundendaten belegen.',
                        'Dieselbe Lösung, sechs Geschichten: Der CFO kauft Payback, die QA kauft Inspektionssicherheit.'))
    rows = [['Rolle', 'Priorität', 'Unser Nutzenargument', 'Beleg / KPI'],
            ['Site Head / COO', 'Lieferfähigkeit, Wachstum', 'Kapazität 6 Monate früher am Markt', 'Time-to-Market –25 %'],
            ['CFO', 'Rendite, Planbarkeit', 'Investition amortisiert sich in unter 3 Jahren', 'Payback 2,8 Jahre, IRR 24 %'],
            ['Produktion', 'Stabile Prozesse', 'Weniger Rüst- und Reinigungszeit, höhere OEE', 'OEE +12 pp'],
            ['Qualität (QA)', 'Inspektionssicherheit', 'Annex-1-konforme Anlage von Beginn an', '0 kritische Beobachtungen'],
            ['IT / OT', 'Integration, Sicherheit', 'Validierte MES-Integration in die bestehende Architektur', 'CSV-Aufwand –30 %'],
            ['Einkauf', 'Vergleichbarkeit, Kosten', 'Transparente Festpreis-Pakete mit Meilensteinen', '100 % Leistungsbeschreibung']]
    tb = table(s, L, 1.5, W, rows, colw=[2.2, 2.4, 5.0, 3.0], rowh=0.6, size=13)
    for r in range(1, 7):
        fill_tf(tb.cell(r, 3).text_frame, rows[r][3], size=13, color=BLUE, anchor='m')

    s = D.slide('content', 'Discovery-Leitfaden: Mit offenen Fragen den wahren Bedarf je Rolle verstehen',
                'Buying Center | Discovery-Fragen (intern)', key='discovery', sticker_='Intern',
                notes=N('Gesprächsvorbereitung für Erstgespräch und Discovery.', 'Fragen je Opportunity ergänzen; Antworten im CRM dokumentieren.',
                        'Regel: 70 % zuhören, 30 % sprechen. Mit „Was wäre, wenn …?“ den Wert der Lösung quantifizieren lassen.'))
    qs = [('Entscheider', 'person', ['Woran wird Ihr Erfolg in drei Jahren gemessen?', 'Was passiert, wenn das Projekt ein Jahr später kommt?']),
          ('Budget', 'euro', ['Welche Renditeerwartung gilt für Investitionen?', 'Wie läuft der Freigabeprozess für CAPEX?']),
          ('Fachbereich', 'engineering', ['Wo verlieren Sie heute die meiste Zeit?', 'Was hat bei früheren Projekten nicht funktioniert?']),
          ('Qualität', 'verified', ['Welche Beobachtungen gab es bei der letzten Inspektion?', 'Wie bewerten Sie Ihre Annex-1-Readiness?']),
          ('IT / OT', 'lan', ['Welche Systeme sind gesetzt, welche offen?', 'Wie ist die OT-Sicherheit organisiert?']),
          ('Einkauf', 'shopping_cart', ['Nach welchen Kriterien wird vergeben?', 'Welche Vertragsmodelle bevorzugen Sie?'])]
    cw, chh = (W - 2 * 0.3) / 3, 2.15
    for i, (r, ic, q) in enumerate(qs):
        x = L + (i % 3) * (cw + 0.3); y = 1.5 + (i // 3) * (chh + 0.25)
        card(s, x, y, cw, chh, r, bl(q, sa=6), icon_=None, hsize=16, bsize=12)
        icon(s, ic, x + cw - 0.6, y + 0.2, 0.38, BLUE)

    s = D.slide('content', 'Die Entscheidung dauert 9 bis 15 Monate – wir begleiten jede Phase aktiv',
                'Buying Center | Entscheidungsprozess', 'Werte illustrativ; je Opportunity anpassen', key='journey', sticker_='Illustrativ',
                notes=N('Buying Journey des Kunden mit unseren Aktivitäten und Sales-Assets.', 'Phasen und Dauer an den Kunden anpassen.',
                        'Jede Phase hat ein Exit-Kriterium – im CRM als Opportunity-Stage abbilden.'))
    ph = ['Problem erkannt', 'Lösungssuche', 'Anforderungen', 'Anbieterauswahl', 'Entscheidung']
    chevrons(s, ph, L + 2.2, 1.45, W - 2.2, 0.6, size=12)
    rows = [('Beim Kunden', ['Engpass wird sichtbar', 'Recherche, Gespräche', 'URS, Budgetrahmen', 'RFP, Präsentationen', 'CAPEX-Freigabe']),
            ('Beteiligte', ['Produktion', '+ Engineering', '+ QA, IT, Finanzen', '+ Einkauf', 'Geschäftsführung']),
            ('Unser Beitrag', ['Thought Leadership, Benchmark', 'Discovery-Workshop', 'Machbarkeitsstudie', 'Angebot, Referenzbesuch', 'Business Case, MAP']),
            ('Dauer', ['1–3 Monate', '2–3 Monate', '2–4 Monate', '2–3 Monate', '1–2 Monate'])]
    cw = (W - 2.2 - 4 * 0.06) / 5
    for j, (lab, vals) in enumerate(rows):
        y = 2.25 + j * 0.85
        label(s, L, y + 0.2, 2.1, lab, color=BLUE if j == 2 else DGRAY)
        hline(s, L, y, W, STONE, 0.5)
        for i, v in enumerate(vals):
            x = L + 2.2 + i * (cw + 0.06)
            if j == 2:
                rect(s, x, y + 0.08, cw, 0.69, fill=LBLUE)
            text(s, x + 0.1, y + 0.08, cw - 0.2, 0.69, v, size=12, anchor='m')
    sowhat(s, 'Wer erst bei der Ausschreibung einsteigt, konkurriert über den Preis – wer in Phase 1 präsent ist, prägt die Anforderungen.')

    s = D.slide('content', 'Kompetenz und Referenzen entscheiden – der Preis folgt erst auf Platz vier',
                'Buying Center | Entscheidungskriterien', 'Quelle: [Kundenbefragung / Win-Loss-Analyse, n = xx]; Werte illustrativ', key='criteria', sticker_='Illustrativ',
                notes=N('Gewichtete Entscheidungskriterien (z. B. aus Win-Loss-Analysen oder Vergabeunterlagen).', 'Gewichte und Bewertung je Opportunity anpassen.',
                        'Die Kriterien früh mit dem Einkauf abstimmen – sie bestimmen das Bewertungsschema.'))
    crit = ['Fachliche Kompetenz', 'Referenzen', 'Team & Verfügbarkeit', 'Preis', 'Methodik', 'Regionale Präsenz']
    bar(s, L, 1.4, 6.6, 4.5, crit, [('Gewicht', [0.28, 0.22, 0.18, 0.15, 0.10, 0.07])], kind='bar', fmt='0%', highlight=[0, 1], gap=50, size=12)
    xr = 7.4
    label(s, xr, 1.5, 2.6, 'Körber'); label(s, xr + 2.6, 1.5, 2.6, 'Wettbewerber A')
    sc = [(4, 3), (3, 3), (3, 2), (2, 3), (4, 2), (3, 4)]
    for i, (a, b) in enumerate(sc):
        y = 1.95 + i * 0.66
        harvey(s, xr + 0.05, y, 0.36, a); harvey(s, xr + 2.65, y, 0.36, b)
    text(s, xr, 6.0, 5.5, 0.3, 'Harvey Balls: Bewertung aus Kundensicht (leer = schwach, voll = stark)', size=10, color=DGRAY)
