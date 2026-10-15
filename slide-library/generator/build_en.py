import sys; sys.path.insert(0, '.')
from kh import *
import en, en2, en3, en4
from en import N

DESC = {'Basic slides': 'Covers, agenda, executive summary, columns', 'Company introduction': 'Körber group, ecosystem, portfolio, team',
        'Customer situation': 'SCR, findings, issue tree, benchmark', 'Buying center': 'Roles, stakeholders, value messages',
        'Solution & value': 'Value proposition, options, recommendation', 'Business case': 'NPV, cash flow, value bridge, scenarios',
        'Approach & plan': 'Phases, Gantt, organisation, RACI', 'References': 'Case studies, logos', 'Proposal': 'Scope, packages, fees, action plan',
        'Kick-off & ways of working': 'Objectives, contacts, rules, data request', 'Analysis & diagnostics': 'Findings, heatmap, gaps, survey',
        'Processes': 'Swimlane, SIPOC, value stream, to-be', 'Target picture & roadmap': 'TOM, requirements, portfolio, waves',
        'Validation & compliance': 'V-model, FMEA, traceability, CQV status', 'Implementation & change': 'Open points, change, training, go-live',
        'Project steering': 'Status, steering committee, risks', 'Workshops': 'Objectives, exercise, voting, parking lot',
        'Account management': 'Account plan, whitespace, pipeline', 'Frameworks': 'SWOT, 2x2, five forces, market sizing',
        'Charts': 'Native, editable charts', 'Closing': 'Takeaways, next steps, contact', 'Appendix': 'Back-up, glossary, methodology',
        'Toolkit': 'Grid, colours, building blocks, icons'}
GROUPS = [('Basics & winning the project', 1, 9), ('Delivering the project', 10, 17), ('Growing the account & toolbox', 18, 23)]

STORY = [('First meeting', 'Understand needs, build trust', ['cover_blue', 'agenda', 'intro_group', 'intro_outcomes', 'intro_portfolio', 'scr', 'refs', 'nextsteps', 'end'], '45–60 min'),
         ('Company introduction', 'Position Körber Pharma Consulting', ['intro_cover', 'intro_group', 'intro_ecosystem', 'intro_outcomes', 'intro_portfolio', 'intro_map', 'team', 'end'], '15–20 min'),
         ('Discovery workshop', 'Analyse the situation, prioritise', ['cover_img', 'agenda_time', 'heard', 'issuetree', 'hypotheses', 'maturity', 'painpoints', 'swimlane', 'nextsteps'], '3–4 h'),
         ('Solution & proposal', 'Convince, prepare the decision', ['cover_img', 'agenda', 'scr', 'valueprop', 'options', 'evaluation', 'bc_summary', 'phases', 'gantt', 'team',
                                                                    'case1', 'offer', 'packages', 'recommendation', 'map_plan', 'end'], '60–90 min'),
         ('Project kick-off', 'Shared understanding, rules', ['cover_light', 'agenda', 'charter', 'phases', 'gantt', 'org', 'raci', 'governance', 'nextsteps'], '2–3 h'),
         ('Steering committee', 'Transparency, decisions', ['cover_light', 'agenda', 'status', 'steerco', 'mstracker', 'budget', 'riskmatrix', 'decision', 'nextsteps'], '60 min'),
         ('Analysis readout', 'Present findings, align priorities', ['cover_img', 'agenda', 'execsum', 'an_findings', 'an_heatmap', 'an_gaps', 'an_survey',
                                                                          'tp_principles', 'tp_quickwins', 'nextsteps'], '60–90 min'),
         ('Concept & roadmap', 'Agree target picture and roadmap', ['cover_img', 'agenda', 'execsum', 'tp_tom', 'tp_requirements', 'tp_vendor', 'tp_portfolio',
                                                                     'tp_roadmap', 'bc_summary', 'recommendation', 'nextsteps'], '60–90 min'),
         ('Validation kick-off', 'Align CQV approach and roles', ['cover_light', 'agenda', 'va_vmodel', 'va_deliverables', 'va_fmea', 'gantt', 'raci', 'nextsteps'], '2 h'),
         ('Go-live readiness review', 'Go / no-go decision', ['cover_light', 'status', 'va_status', 'im_training', 'im_opl', 'im_golive', 'im_cutover'], '60 min'),
         ('Customer workshop', 'Co-create results', ['cover_img', 'ws_objectives', 'ws_exercise', 'ws_board', 'ws_break', 'ws_voting', 'ws_parking', 'nextsteps'], '3–4 h'),
         ('Account planning (internal)', 'Steer the account', ['accountplan', 'buyingcenter', 'stakeholder', 'relmap', 'whitespace', 'funnel', 'health'], '90 min')]


def finalize(D):
    chaps = [(n[:2], n[3:], sl) for n, sl in D.sections if not n.startswith('00')]
    s = D.keys['toc']
    cw = (W - 2 * 0.3) / 3; rh = 0.49
    for g, (gname, a, z) in enumerate(GROUPS):
        x = L + g * (cw + 0.3)
        label(s, x, 1.42, cw, gname)
        for i, (nr, name, sl) in enumerate([c for c in chaps if a <= int(c[0]) <= z]):
            y = 1.72 + i * rh
            num(s, x, y + 0.07, nr, 0.36, size=9)
            text(s, x + 0.47, y + 0.01, cw - 1.3, 0.25, name, size=12)
            text(s, x + 0.47, y + 0.25, cw - 1.3, 0.22, DESC.get(name, ''), size=9, color=DGRAY)
            text(s, x + cw - 0.85, y, 0.85, rh, '%d–%d' % (D.number(sl[0]), D.number(sl[-1])), size=11, color=BLUE, anchor='m', align='r')
            hline(s, x, y + rh, cw, STONE, 0.5)
            hit = rect(s, x, y, cw, rh); hit.click_action.target_slide = sl[0]; hit.name = 'Link chapter ' + nr
    s = D.keys['story']
    rows = [['Meeting type', 'Goal', 'Recommended slides (in this order)', 'Duration']]
    for t, zl, keys, d in STORY:
        rows.append([t, zl, ', '.join(str(D.number(D.keys[k])) for k in keys), d])
    tb = table(s, L, 1.45, W, rows, colw=[2.6, 3.2, 5.6, 1.2], rowh=[0.36] + [0.385] * len(STORY), size=11)
    for r in range(1, len(rows)):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=11, color=BLUE)


D = Deck(TEMPLATE)
for f in [en.s00, en.s01, en.s02, en.s03, en.s04, en2.s05, en2.s06, en2.s07, en2.s10, en2.s09,
          en4.kickoff, en4.analysis, en2.s08, en4.target, en4.validation, en4.implementation, en3.s11, en4.workshops,
          en3.s12, en3.s13, en3.s14, en3.s15, en4.appendix, en3.s16]:
    f(D)
finalize(D)
out = sys.argv[1] if len(sys.argv) > 1 else 'Koerber_Slide_Library_2026_EN.pptx'
D.save(out); print('\n'.join(D.warn)); print(len(D.prs.slides), 'slides')
