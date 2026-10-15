import sys; sys.path.insert(0, '.')
from kh import *
import build_a, build_b, build_c
from build_a import N

CH = [(1, 'Titel & Agenda', 'Deckblätter, Agenda, Ziele, Teilnehmende'), (2, 'Über uns', 'Portfolio, Kompetenzen, Ökosystem, Team'),
      (3, 'Markt & Kundenverständnis', 'Trends, Ausgangslage, Hypothesen, Benchmark'), (4, 'Buying Center', 'Rollen, Stakeholder, Nutzenargumente'),
      (5, 'Lösung & Wert', 'Wertversprechen, Architektur, Optionen'), (6, 'Business Case', 'NPV, Cashflow, Sensitivität, Szenarien'),
      (7, 'Vorgehen & Plan', 'Phasen, Gantt, Organisation, RACI'), (8, 'Prozesse & Abläufe', 'Swimlane, SIPOC, Wertstrom, Soll-Prozess'),
      (9, 'Referenzen', 'Case Studies, Referenzmatrix, Zitate'), (10, 'Angebot', 'Scope, Pakete, Honorar, Mutual Action Plan'),
      (11, 'Projektsteuerung', 'Status, Steering Committee, Risiken'), (12, 'Account-Management', 'Account-Plan, Whitespace, Pipeline'),
      (13, 'Frameworks', 'SWOT, Five Forces, Priorisierung, TAM'), (14, 'Diagramme', 'Native, editierbare Diagramme'),
      (15, 'Abschluss', 'Kernaussagen, nächste Schritte, Kontakt'), (16, 'Toolkit', 'Raster, Farben, Bausteine, Icons')]

STORY = [('Erstgespräch', 'Bedarf verstehen, Vertrauen aufbauen', ['cover_blue', 'goals', 'participants', 'trends', 'scr', 'competencies', 'why', 'refs', 'case1', 'nextsteps', 'end'], '45–60 Min.'),
         ('Discovery-Workshop', 'Ausgangslage analysieren, priorisieren', ['cover_img', 'agenda_time', 'goals', 'trendmatrix', 'heard', 'issuetree', 'hypotheses', 'maturity', 'painpoints', 'swimlane', 'nextsteps'], '3–4 Std.'),
         ('Lösung & Angebot', 'Lösung überzeugend präsentieren, Entscheidung vorbereiten',
          ['cover_img', 'agenda', 'scr', 'valueprop', 'architecture', 'options', 'evaluation', 'bc_summary', 'costofdelay', 'phases', 'gantt', 'team', 'case1', 'offer', 'packages', 'recommendation', 'map_plan', 'end'], '60–90 Min.'),
         ('Projekt-Kick-off', 'Gemeinsames Verständnis, Spielregeln', ['cover_ko', 'agenda', 'charter', 'okr', 'phases', 'gantt', 'org', 'raci', 'governance', 'assumptions', 'plan90', 'nextsteps'], '2–3 Std.'),
         ('Steering Committee', 'Status transparent machen, entscheiden', ['cover_ko', 'agenda', 'status', 'steerco', 'mstracker', 'budget', 'riskmatrix', 'decision', 'nextsteps'], '60 Min.'),
         ('Quartalsreview (QBR)', 'Wert belegen, Wachstum öffnen', ['cover_blue', 'qbr', 'kpis', 'nps', 'growth', 'nextsteps'], '60 Min.'),
         ('Account-Planung (intern)', 'Account steuern, Pipeline entwickeln', ['accountplan', 'buyingcenter', 'stakeholder', 'relmap', 'whitespace', 'funnel', 'health'], '90 Min.')]


def ranges(nums):
    nums = sorted(set(nums)); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else ('%d–%d' % (nums[i], nums[j]) if j > i + 1 else '%d, %d' % (nums[i], nums[j])))
        i = j + 1
    return ', '.join(out)


def finalize(D):
    sl = list(D.prs.slides)
    secs = {name[:2]: slides for name, slides in D.sections}
    # TOC
    s = D.keys['toc']
    cw = (W - 0.5) / 2; rh = 0.56
    for i, (n_, name, desc) in enumerate(CH):
        x = L + (i // 8) * (cw + 0.5); y = 1.5 + (i % 8) * rh
        ss = secs['%02d' % n_]
        a, b = D.number(ss[0]), D.number(ss[-1])
        num(s, x, y + 0.08, '%02d' % n_, 0.4, size=10)
        text(s, x + 0.55, y + 0.02, cw - 1.8, 0.28, name, size=14)
        text(s, x + 0.55, y + 0.29, cw - 1.8, 0.25, desc, size=10, color=DGRAY)
        text(s, x + cw - 1.1, y + 0.02, 1.1, 0.5, '%d–%d' % (a, b), size=12, color=BLUE, anchor='m', align='r')
        hline(s, x, y + rh, cw, STONE, 0.5)
        hit = rect(s, x, y, cw, rh)
        hit.click_action.target_slide = ss[0]
        hit.name = 'Link Kapitel %02d' % n_
    # Storylines
    s = D.keys['story']
    rows = [['Termin-Typ', 'Ziel', 'Empfohlene Folien (in dieser Reihenfolge)', 'Dauer']]
    for t, z, keys, d in STORY:
        rows.append([t, z, ', '.join(str(D.number(D.keys[k])) for k in keys), d])
    tb = table(s, L, 1.45, W, rows, colw=[2.4, 3.2, 5.6, 1.4], rowh=[0.4] + [0.62] * len(STORY), size=12)
    for r in range(1, len(rows)):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=13, color=BLUE)
    # chapter dividers: add slide range to notes
    return


D = Deck(TEMPLATE)
for f in [build_a.s00, build_a.s01, build_a.s02, build_a.s03, build_a.s04, build_b.s05, build_b.s06, build_b.s07, build_b.s08, build_b.s09,
          build_c.s10, build_c.s11, build_c.s12, build_c.s13, build_c.s14, build_c.s15, build_c.s16]:
    f(D)
finalize(D)
out = sys.argv[1] if len(sys.argv) > 1 else 'Koerber_Slide_Library_2026.pptx'
D.save(out); print('\n'.join(D.warn)); print(len(D.prs.slides), 'slides')
