import sys; sys.path.insert(0, '.')
from kh import *
import en, en2, en3
from en import N

CH = [(1, 'Basic slides', 'Covers, agenda, text, columns, images, numbers'), (2, 'Company introduction', 'Körber group, ecosystem, portfolio, team'),
      (3, 'Customer situation', 'SCR, findings, issue tree, benchmark'), (4, 'Buying center', 'Roles, stakeholders, value messages'),
      (5, 'Solution & value', 'Value proposition, options, recommendation'), (6, 'Business case', 'NPV, cash flow, value bridge, scenarios'),
      (7, 'Approach & plan', 'Phases, Gantt, organisation, RACI'), (8, 'Processes', 'Swimlane, SIPOC, value stream, to-be process'),
      (9, 'References', 'Case studies, logos'), (10, 'Proposal', 'Scope, packages, fees, mutual action plan'),
      (11, 'Project steering', 'Status, steering committee, risks'), (12, 'Account management', 'Account plan, whitespace, pipeline'),
      (13, 'Frameworks', 'SWOT, 2x2, five forces, market sizing'), (14, 'Charts', 'Native, editable charts'),
      (15, 'Closing', 'Takeaways, next steps, contact'), (16, 'Toolkit', 'Grid, colours, building blocks, icons')]

STORY = [('First meeting', 'Understand needs, build trust', ['cover_blue', 'agenda', 'intro_group', 'intro_outcomes', 'intro_portfolio', 'scr', 'refs', 'nextsteps', 'end'], '45–60 min'),
         ('Company introduction', 'Position Körber Pharma Consulting', ['intro_cover', 'intro_group', 'intro_ecosystem', 'intro_outcomes', 'intro_portfolio', 'intro_map', 'team', 'end'], '15–20 min'),
         ('Discovery workshop', 'Analyse the situation, prioritise', ['cover_img', 'agenda_time', 'heard', 'issuetree', 'hypotheses', 'maturity', 'painpoints', 'swimlane', 'nextsteps'], '3–4 h'),
         ('Solution & proposal', 'Convince, prepare the decision', ['cover_img', 'agenda', 'scr', 'valueprop', 'options', 'evaluation', 'bc_summary', 'phases', 'gantt', 'team',
                                                                    'case1', 'offer', 'packages', 'recommendation', 'map_plan', 'end'], '60–90 min'),
         ('Project kick-off', 'Shared understanding, rules', ['cover_light', 'agenda', 'charter', 'phases', 'gantt', 'org', 'raci', 'governance', 'nextsteps'], '2–3 h'),
         ('Steering committee', 'Transparency, decisions', ['cover_light', 'agenda', 'status', 'steerco', 'mstracker', 'budget', 'riskmatrix', 'decision', 'nextsteps'], '60 min'),
         ('Account planning (internal)', 'Steer the account', ['accountplan', 'buyingcenter', 'stakeholder', 'relmap', 'whitespace', 'funnel', 'health'], '90 min')]


def finalize(D):
    secs = {name[:2]: slides for name, slides in D.sections}
    s = D.keys['toc']
    cw = (W - 0.5) / 2; rh = 0.56
    for i, (n_, name, desc) in enumerate(CH):
        x = L + (i // 8) * (cw + 0.5); y = 1.5 + (i % 8) * rh
        ss = secs['%02d' % n_]
        num(s, x, y + 0.08, '%02d' % n_, 0.4, size=10)
        text(s, x + 0.55, y + 0.02, cw - 1.8, 0.28, name, size=14)
        text(s, x + 0.55, y + 0.29, cw - 1.8, 0.25, desc, size=10, color=DGRAY)
        text(s, x + cw - 1.1, y + 0.02, 1.1, 0.5, '%d–%d' % (D.number(ss[0]), D.number(ss[-1])), size=13, color=BLUE, anchor='m', align='r')
        hline(s, x, y + rh, cw, STONE, 0.5)
        hit = rect(s, x, y, cw, rh); hit.click_action.target_slide = ss[0]; hit.name = 'Link chapter %02d' % n_
    s = D.keys['story']
    rows = [['Meeting type', 'Goal', 'Recommended slides (in this order)', 'Duration']]
    for t, z, keys, d in STORY:
        rows.append([t, z, ', '.join(str(D.number(D.keys[k])) for k in keys), d])
    tb = table(s, L, 1.45, W, rows, colw=[2.6, 3.2, 5.4, 1.4], rowh=[0.4] + [0.6] * len(STORY), size=13)
    for r in range(1, len(rows)):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=13, color=BLUE)


D = Deck(TEMPLATE)
for f in [en.s00, en.s01, en.s02, en.s03, en.s04, en2.s05, en2.s06, en2.s07, en2.s08, en2.s09, en2.s10,
          en3.s11, en3.s12, en3.s13, en3.s14, en3.s15, en3.s16]:
    f(D)
finalize(D)
out = sys.argv[1] if len(sys.argv) > 1 else 'Koerber_Slide_Library_2026_EN.pptx'
D.save(out); print('\n'.join(D.warn)); print(len(D.prs.slides), 'slides')
