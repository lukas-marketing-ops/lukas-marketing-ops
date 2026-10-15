from en import *
from pptx.enum.dml import MSO_LINE
from kh import _strip_style


# =====================================================================================
def s11(D):
    C = 'Project steering'
    divider(D, 11, 'Project\nsteering', N('Slides for running lead projects: charter, status, steering committee, risks, decisions, closure.',
                                            'Update weekly or monthly; do not change the format.',
                                            'The same status format in every project makes projects comparable for customers and management.'))
    s = cs(D, C, 'Project charter', 'charter', N('Project charter for the kick-off.', 'Fill all fields; get sponsor sign-off.'), source='Approved by [sponsor], [date]')
    f = [('Objective', True), ('Sponsor', False), ('In scope', False), ('Out of scope', False), ('Deliverables', False), ('Budget', False),
         ('Timeline', False), ('Success criteria', True)]
    cw = (W - 0.3) / 2; chh = 0.95
    for i, (h, hi) in enumerate(f):
        x = L + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.15)
        rect(s, x, y, cw, chh, fill=BLUE if hi else LSAND)
        label(s, x + 0.2, y + 0.15, cw - 0.4, h, color=WHITE if hi else BLUE)
        text(s, x + 0.2, y + 0.42, cw - 0.4, 0.5, '[Entry]', size=15, color=WHITE if hi else BLACK)

    s = cs(D, C, 'Status report', 'status', N('Weekly status one-pager – always the same format.', 'Update overall status, progress and the four fields.',
                                              'The title states status plus the one thing management must know.'), source='Reporting period: [DD.MM.] – [DD.MM.]')
    rect(s, L, 1.5, 3.4, 4.3, fill=LSAND)
    label(s, L + 0.25, 1.7, 3, 'Overall status')
    oval(s, L + 0.25, 2.05, 0.6, fill=BLUE)
    text(s, L + 1.0, 2.05, 2.2, 0.6, 'On track', size=21, anchor='m')
    for i, (k, st) in enumerate([('Schedule', 'g'), ('Budget', 'g'), ('Quality', 'g'), ('Resources', 'y')]):
        y = 2.95 + i * 0.4
        rag(s, L + 0.25, y + 0.07, st); text(s, L + 0.6, y, 2.5, 0.35, k, size=14, anchor='m')
    label(s, L + 0.25, 4.7, 3, 'Progress')
    rect(s, L + 0.25, 5.05, 2.9, 0.2, fill=WHITE); rect(s, L + 0.25, 5.05, 2.9 * 0.5, 0.2, fill=BLUE)
    text(s, L + 0.25, 5.3, 2.9, 0.3, '00% (plan: 00%)', size=13)
    x0 = L + 3.7; cw = (R - x0 - 0.3) / 2; chh = 2.0
    for i, (h, f_) in enumerate([('Achieved', LSAND), ('Next steps', LSAND), ('Top risks', LSAND), ('Decisions needed', BLUE)]):
        x = x0 + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.3)
        rect(s, x, y, cw, chh, fill=f_)
        label(s, x + 0.2, y + 0.2, cw - 0.4, h, color=WHITE if f_ == BLUE else BLUE)
        text(s, x + 0.2, y + 0.5, cw - 0.4, chh - 0.6, bl(['Point', 'Point'], sa=4), size=14, color=WHITE if f_ == BLUE else BLACK)

    s = cs(D, C, 'Steering committee dashboard', 'steerco', N('Dashboard for the steering committee.', 'Recolour status dots: blue = on track, amber = at risk, orange = critical.',
                                                              'Amber and orange always need an action and an owner.'), source='As of: [date]')
    colw = [2.6, 1.7, 1.2, 1.2, 1.2, 4.7]
    rows = [['Workstream', 'Lead', 'Schedule', 'Budget', 'Quality', 'Comment / action']] + [['Workstream %d' % i, '[Name]', '', '', '', '[Comment]'] for i in range(1, 5)]
    table(s, L, 1.5, W, rows, colw=colw, rowh=0.7, size=15, aligns=['l', 'l', 'c', 'c', 'c', 'l'])
    xs = [L + W * sum(colw[:k]) / sum(colw) for k in range(7)]
    st = [['g', 'g', 'g'], ['g', 'y', 'g'], ['y', 'r', 'g'], ['g', 'g', 'n']]
    for r in range(4):
        for c in range(3):
            rag(s, (xs[2 + c] + xs[3 + c]) / 2 - 0.12, 1.5 + 0.7 * (r + 1) + 0.23, st[r][c], 0.24)
    legend_rag(s, L, 5.3, size=11, labels=('On track', 'At risk', 'Critical', 'Not started'))

    s = cs(D, C, 'Milestone tracker', 'mstracker', N('Milestones plan vs. forecast.', 'Update forecasts weekly; deviation in days.'), source='As of: [date]')
    rows = [['Milestone', 'Plan', 'Forecast / actual', 'Deviation', 'Status']] + [['Milestone %d' % i, '[DD.MM.YY]', '[DD.MM.YY]', '0 days', ''] for i in range(1, 6)]
    table(s, L, 1.5, W, rows, colw=[4.2, 1.9, 2.3, 1.9, 2.3], rowh=0.62, size=15, aligns=['l', 'c', 'c', 'c', 'l'])
    st = ['g', 'g', 'y', 'n', 'n']
    for r in range(1, 6):
        rag(s, L + W * (10.3 / 12.6) + 0.15, 1.5 + r * 0.62 + 0.21, st[r - 1])
        text(s, L + W * (10.3 / 12.6) + 0.45, 1.5 + r * 0.62, 1.8, 0.62, {'g': 'Reached', 'y': 'At risk', 'n': 'On track'}[st[r - 1]], size=14, anchor='m')

    s = cs(D, C, 'Budget', 'budget', N('Budget burn: plan vs. actual vs. forecast.', 'Edit chart data monthly.'), source='Source: project controlling; cumulative in €k')
    months = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']
    cd = CategoryChartData(); cd.categories = months
    cd.add_series('Plan', [10, 20, 32, 45, 55, 66, 76, 85, 92, 97, 100, 100])
    cd.add_series('Actual', [9, 19, 30, 42, 52, 62, None, None, None, None, None, None])
    cd.add_series('Forecast', [None, None, None, None, None, 62, 72, 81, 88, 94, 97, 98])
    ch = s.shapes.add_chart(XCT.LINE, I(L), I(1.4), I(8.6), I(4.4), cd).chart
    ch.font.size = Pt(13)
    for ser, c, d in zip(ch.plots[0].series, [STONE, BLUE, BLUE], [None, None, MSO_LINE.DASH]):
        ser.format.line.fill.solid(); setc(ser.format.line.color, c); ser.format.line.width = Pt(2.5); ser.smooth = False
        if d: ser.format.line.dash_style = d
    va = ch.value_axis; va.has_major_gridlines = True; va.major_gridlines.format.line.color.rgb = RGBColor.from_string(HEX['grid']); va.format.line.fill.background()
    ch.category_axis.major_tick_mark = XL_TICK_MARK.NONE
    ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
    xr = 9.5; wr = R - xr
    kpi(s, xr, 1.6, wr, '€0k', 'Actual cost (00% of budget)', bigsize=30)
    kpi(s, xr, 3.2, wr, '€0k', 'Forecast vs. plan at completion', bigsize=30)
    sowhat(s, KT)

    s = cs(D, C, 'Risk matrix', 'riskmatrix', N('Risk matrix (probability × impact).', 'Move the numbered circles; maintain the list on the right.'), source='As of: [date]')
    gx0, gy0, cs_ = L + 0.6, 1.45, 1.42
    heat = [[AMBER, ORANGE, ORANGE], [SAND, AMBER, ORANGE], [LSAND, SAND, AMBER]]
    for r in range(3):
        for c in range(3):
            rect(s, gx0 + c * (cs_ + 0.05), gy0 + r * (cs_ + 0.05), cs_, cs_, fill=heat[r][c])
    quad_axes(s, gx0, gy0, 3 * cs_ + 0.1, 3 * cs_ + 0.1, 'Probability', 'Impact')
    for n_, c, r in [(1, 2, 0), (2, 1, 0), (3, 1, 1), (4, 0, 2)]:
        num(s, gx0 + c * (cs_ + 0.05) + cs_ / 2 - 0.22, gy0 + r * (cs_ + 0.05) + cs_ / 2 - 0.22, n_, 0.44, filled=n_ <= 2, color=BLACK)
    xr = 6.0; wr = R - xr
    for i in range(4):
        y = 1.5 + i * 1.05
        num(s, xr, y + 0.08, i + 1, 0.4, filled=i < 2, color=BLACK)
        text(s, xr + 0.6, y, wr - 0.6, 0.35, 'Risk %d' % (i + 1), size=16)
        text(s, xr + 0.6, y + 0.4, wr - 0.6, 0.35, 'Mitigation: [action, owner, date]', size=13, color=DGRAY)
        if i < 3:
            hline(s, xr + 0.6, y + 0.9, wr - 0.6, STONE, 0.5)

    s = cs(D, C, 'Decision paper', 'decision', N('Standard format for steering committee decisions.', 'Fill question, options, recommendation and impact.',
                                                 'Pre-align with the decision makers – the meeting only confirms.'), source='For steering committee on [date]')
    rect(s, L, 1.5, W, 0.7, fill=LSAND)
    text(s, L + 0.25, 1.5, W - 0.5, 0.7, [{'t': [('Decision needed:  ', {'color': BLUE}), ('Question in one sentence?', {})]}], size=17, anchor='m')
    cw = 4.0
    for i in range(2):
        x = L + i * (cw + 0.3); hi = i == 1
        rect(s, x, 2.45, cw, 3.35, fill=BLUE if hi else LSAND)
        label(s, x + 0.25, 2.65, cw - 0.5, 'Option %s' % 'AB'[i] + (' – recommended' if hi else ''), color=WHITE if hi else BLUE)
        text(s, x + 0.25, 2.95, cw - 0.5, 0.4, 'Option name', size=19, color=WHITE if hi else BLACK)
        text(s, x + 0.25, 3.5, cw - 0.5, 2.0, bl(['Cost', 'Time', 'Risk'], sa=6), size=15, color=WHITE if hi else BLACK)
    xr = L + 2 * cw + 0.7; wr = R - xr
    label(s, xr, 2.5, wr, 'Impact of recommendation')
    for i, a in enumerate(['Schedule', 'Budget', 'Benefit']):
        y = 2.85 + i * 0.75
        hline(s, xr, y, wr, STONE, 0.5)
        text(s, xr, y + 0.1, 1.3, 0.5, a, size=14, color=BLUE)
        text(s, xr + 1.3, y + 0.1, wr - 1.3, 0.5, '[Impact]', size=14)
    rrect(s, xr, 5.3, wr, 0.5, fill=YELLOW, radius=0.25, content='Ask: approve option B', size=14, align='c', anchor='m', margin=0)

    s = cs(D, C, 'Change request', 'changerequest', N('Standard change request format.', 'Fill all fields; approval in the steering committee.'), source='CR no. [00]; submitted [date] by [name]')
    for i, h in enumerate(['Description', 'Rationale', 'Recommendation']):
        y = 1.5 + i * 1.12
        hline(s, L, y, 6.6, BLACK); label(s, L, y + 0.12, 6.6, h); text(s, L, y + 0.42, 6.6, 0.6, '[Entry in one or two lines]', size=15)
    xr = 7.4; wr = R - xr
    label(s, xr, 1.5, wr, 'Impact')
    for i, (k, st) in enumerate([('Schedule', 'y'), ('Cost', 'y'), ('Quality', 'g'), ('Risk', 'g')]):
        y = 1.85 + i * 0.75
        rect(s, xr, y, wr, 0.65, fill=LSAND)
        rag(s, xr + 0.2, y + 0.23, st)
        text(s, xr + 0.55, y, 1.3, 0.65, k, size=14, anchor='m')
        text(s, xr + 1.85, y, wr - 2.0, 0.65, '[Impact]', size=14, anchor='m')
    for i, t in enumerate(['Approval PL customer', 'Approval PL Körber', 'Approval steering committee']):
        hline(s, L + i * 4.3, 5.55, 3.9, BLACK); text(s, L + i * 4.3, 5.6, 3.9, 0.3, t + ' / date', size=12, color=DGRAY)

    s = cs(D, C, 'Project closure', 'closure', N('Closing slide for the last steering committee – basis for the reference.', 'Enter targets and actuals; check hand-over.',
                                                 'Trigger the reference approval and satisfaction survey right afterwards.'), source='Final report of [date]')
    rows = [['Target', 'Plan', 'Actual', '']] + [['Target %d' % i, '[Value]', '[Value]', ''] for i in range(1, 5)]
    table(s, L, 1.5, 7.2, rows, colw=[2.2, 2.0, 2.0, 1.0], rowh=0.65, size=15, aligns=['l', 'c', 'c', 'c'])
    for r in range(1, 5):
        icon(s, 'check_circle', L + 6.45, 1.5 + r * 0.65 + 0.16, 0.34, BLUE)
    xr = 8.1; wr = R - xr
    rect(s, xr, 1.5, wr, 3.6, fill=LSAND)
    label(s, xr + 0.25, 1.7, wr - 0.5, 'Hand-over to operations')
    for i in range(4):
        y = 2.1 + i * 0.65
        icon(s, 'task_alt', xr + 0.25, y + 0.05, 0.32, BLUE)
        text(s, xr + 0.7, y, wr - 0.9, 0.42, 'Hand-over item', size=15, anchor='m')
    sowhat(s, KT)


# =====================================================================================
def s12(D):
    C = 'Account management'
    divider(D, 12, 'Account\nmanage-\nment', N('Account plan, whitespace, pipeline and account health – internal slides.', 'Take data from the CRM.',
                                             'These slides make the contribution of marketing and sales to revenue visible.'))
    s = cs(D, C, 'Account plan (internal)', 'accountplan', N('Account plan on a page for key accounts.', 'Create yearly, update quarterly.'),
           source='Source: CRM, as of [date]', sticker_='Internal')
    cw = (W - 3 * 0.3) / 4
    for i, (a, b) in enumerate([('€0.0m', 'Revenue last year'), ('€0.0m', 'Target this year'), ('€0.0m', 'Pipeline'), ('0 of 6', 'Buying-center roles covered')]):
        x = L + i * (cw + 0.3)
        rect(s, x, 1.5, cw, 1.3, fill=BLUE if i == 1 else LSAND)
        text(s, x + 0.2, 1.6, cw - 0.4, 0.6, a, size=28, color=WHITE if i == 1 else BLUE)
        text(s, x + 0.2, 2.25, cw - 0.4, 0.4, b, size=13, color=WHITE if i == 1 else BLACK)
    cw3 = (W - 2 * 0.3) / 3
    for i, h in enumerate(['Strategic objectives', 'Growth areas', 'Next activities']):
        colhead(s, L + i * (cw3 + 0.3), 3.1, cw3, None, h, bl(B3, sa=6), hsize=17, bsize=14, bh=1.6)

    s = cs(D, C, 'Whitespace (internal)', 'whitespace', N('Where we already sell and where potential lies.', 'Recolour cells per site × service.',
                                                          'Every outlined cell should have an opportunity in the CRM.'), sticker_='Internal')
    x0 = L + 2.6; cw = (R - x0) / 5; rh = 0.9
    M = [['a', 'a', 'o', 'n', 'a'], ['o', 'a', 'o', 'n', 'o'], ['n', 'o', 'n', 'o', 'n'], ['n', 'n', 'o', 'n', 'o']]
    for j in range(5):
        text(s, x0 + j * cw, 1.45, cw, 0.45, 'Service %d' % (j + 1), size=13, align='c', anchor='b', color=BLUE)
    hline(s, L, 2.0, W, BLACK)
    for i in range(4):
        y = 2.1 + i * rh
        text(s, L, y, 2.5, rh - 0.1, 'Site %d' % (i + 1), size=15, anchor='m')
        for j in range(5):
            v = M[i][j]; x = x0 + j * cw + 0.08
            if v == 'a':
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=BLUE, content='Customer', size=12, color=WHITE, align='c', anchor='m')
            elif v == 'o':
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=WHITE, line=BLUE, lw=1.5, content='Potential', size=12, color=BLUE, align='c', anchor='m')
            else:
                rect(s, x, y + 0.05, cw - 0.16, rh - 0.2, fill=LSAND)

    s = cs(D, C, 'Pipeline funnel (internal)', 'funnel', N('Pipeline by sales stage with conversion rates.', 'Copy values from the CRM report.',
                                                           'Conversion between stages shows where marketing and sales must act.'), source='Source: CRM, as of [date]', sticker_='Internal')
    cx = L + 3.6; maxw = 7.0
    label(s, cx - maxw / 2, 1.45, 4, 'Count  |  volume', color=DGRAY)
    for i in range(5):
        w_ = maxw * (1 - i * 0.17); y = 1.8 + i * 0.82
        rect(s, cx - w_ / 2, y, w_, 0.7, fill=BLUE if i == 4 else (MBLUE if i == 3 else SAND), content='0  |  €0.0m', size=15,
             color=WHITE if i == 4 else BLACK, align='c', anchor='m')
        text(s, cx + maxw / 2 + 0.2, y, 3.0, 0.7, ['Qualified lead', 'Need confirmed', 'Proposal', 'Negotiation', 'Won'][i], size=15, anchor='m')

    s = cs(D, C, 'Account health (internal)', 'health', N('Early warning for key accounts.', 'Use the same criteria and thresholds for all accounts.',
                                                         'Keep the health score as a CRM field – then it can be analysed portfolio-wide.'), sticker_='Internal')
    rows = [['Dimension', 'Indicator', 'Value', 'Status', 'Action']] + [[d, '[Indicator]', '[0]', '', '[Action]'] for d in ['Satisfaction', 'Relationship', 'Growth', 'Risk']]
    table(s, L, 1.5, W, rows, colw=[2.4, 3.6, 1.4, 1.4, 3.8], rowh=0.72, size=15, aligns=['l', 'l', 'c', 'c', 'l'])
    cx_ = L + W * (7.4 + 0.7) / 12.6
    for r, st in enumerate(['g', 'y', 'g', 'r']):
        rag(s, cx_ - 0.12, 1.5 + (r + 1) * 0.72 + 0.24, st, 0.24)
    legend_rag(s, L, 5.3, size=11, labels=('On track', 'At risk', 'Critical', 'Not started'))


# =====================================================================================
def s13(D):
    C = 'Frameworks'
    divider(D, 13, 'Frame-\nworks', N('Classic analysis frameworks in Körber design.', 'Replace content, keep the structure.',
                                    'Frameworks structure the thinking – the insight still belongs in the title.'))
    s = cs(D, C, 'SWOT', 'swot', N('SWOT for site, project or competitive analyses.', 'Three points per quadrant; implication into the title.'))
    cw, chh = (W - 0.3) / 2, 2.1
    for i, (h, f) in enumerate([('Strengths', BLUE), ('Weaknesses', LSAND), ('Opportunities', LSAND), ('Threats', SAND)]):
        x = L + (i % 2) * (cw + 0.3); y = 1.5 + (i // 2) * (chh + 0.2)
        c = WHITE if f == BLUE else BLACK
        rect(s, x, y, cw, chh, fill=f)
        text(s, x + 0.3, y + 0.2, 0.9, 0.9, h[0], size=44, color=WHITE if f == BLUE else BLUE)
        text(s, x + 1.25, y + 0.25, cw - 1.5, 0.4, h, size=18, color=c)
        text(s, x + 1.25, y + 0.75, cw - 1.5, 1.3, bl(B3, sa=4), size=14, color=c)

    s = cs(D, C, '2x2 prioritisation matrix', 'prio', N('Prioritisation of initiatives.', 'Move the letter circles; adapt the list on the right.'))
    gx0, gy0, gw, gh = L + 0.55, 1.5, 6.6, 4.3
    for t, qx, qy, f in [('Quick wins', 0, 0, LBLUE), ('Strategic projects', 1, 0, LSAND), ('Fill-ins', 0, 1, LSAND), ('Avoid', 1, 1, LSAND)]:
        rect(s, gx0 + qx * gw / 2, gy0 + qy * gh / 2, gw / 2 - 0.04, gh / 2 - 0.04, fill=f)
        text(s, gx0 + qx * gw / 2 + 0.15, gy0 + qy * gh / 2 + 0.1, 3, 0.3, t, size=13, color=BLUE)
    quad_axes(s, gx0, gy0, gw, gh, 'Effort', 'Impact')
    for t, px, py, hi in [('A', 0.8, 0.8, True), ('B', 2.0, 1.2, True), ('C', 4.6, 0.8, False), ('D', 1.4, 3.0, False), ('E', 4.9, 3.2, False)]:
        oval(s, gx0 + px, gy0 + py, 0.48, fill=BLUE if hi else WHITE, line=None if hi else BLACK, content=t, size=14,
             color=WHITE if hi else BLACK, align='c', anchor='m', margin=0)
    xr = 8.0; wr = R - xr
    for i in range(5):
        y = 1.5 + i * 0.7
        oval(s, xr, y + 0.06, 0.4, fill=BLUE if i < 2 else WHITE, line=None if i < 2 else BLACK, content='ABCDE'[i], size=12,
             color=WHITE if i < 2 else BLACK, align='c', anchor='m', margin=0)
        text(s, xr + 0.6, y, wr - 0.6, 0.52, 'Initiative', size=15, anchor='m')

    s = cs(D, C, 'Five forces', 'fiveforces', N('Industry structure analysis (Porter).', 'Rate intensity with Harvey balls (0–4).'))
    cx, cy = 6.67, 3.6
    def force(x, y, h, q, hi=False):
        rect(s, x, y, 3.5, 1.2, fill=BLUE if hi else LSAND)
        text(s, x + 0.2, y + 0.15, 2.6, 0.4, h, size=16, color=WHITE if hi else BLACK)
        text(s, x + 0.2, y + 0.6, 3.1, 0.5, D1, size=12, color=WHITE if hi else DGRAY)
        harvey(s, x + 3.0, y + 0.15, 0.34, q)
    rect(s, cx - 1.75, cy - 0.6, 3.5, 1.2, fill=BLACK, content='Industry rivalry', size=16, color=WHITE, align='c', anchor='m')
    force(cx - 1.75, 1.45, 'New entrants', 1); force(cx - 1.75, 4.6, 'Substitutes', 2)
    force(L, cy - 0.6, 'Suppliers', 4, True); force(R - 3.5, cy - 0.6, 'Buyers', 3)
    for (x1, y1, x2, y2) in [(cx, 2.65, cx, cy - 0.6), (cx, 4.6, cx, cy + 0.6), (L + 3.5, cy, cx - 1.75, cy), (R - 3.5, cy, cx + 1.75, cy)]:
        arrow(s, x1, y1, x2, y2, color=TAUPE)

    s = cs(D, C, 'Value chain', 'valuechain', N('Value chain (Porter) adapted to pharma production.', 'Adapt activities and shares.'))
    label(s, L, 1.45, 4, 'Support activities', color=DGRAY)
    for i in range(3):
        rect(s, L, 1.75 + i * 0.5, W - 1.0, 0.42, fill=LSAND, content='Support activity', size=13, anchor='m', margin=(0.2, 0, 0.1, 0))
    label(s, L, 3.45, 4, 'Primary activities', color=BLUE)
    cw = (W - 1.0 - 4 * 0.08) / 5
    for i in range(5):
        x = L + i * (cw + 0.08); hi = i == 1
        rect(s, x, 3.75, cw, 1.85, fill=BLUE if hi else SAND)
        text(s, x + 0.15, 3.9, cw - 0.3, 0.6, 'Activity', size=15, color=WHITE if hi else BLACK)
        text(s, x + 0.15, 4.85, cw - 0.3, 0.55, '00%', size=26, color=WHITE if hi else BLUE)
    rect(s, R - 0.85, 1.75, 0.85, 3.85, fill=BLACK)
    t_ = text(s, 0, 0, 3.85, 0.85, 'Margin', size=15, color=WHITE, align='c', anchor='m')
    t_.rotation = 270; t_.left = I(R - 0.425 - 1.925); t_.top = I(1.75 + 1.925 - 0.425)

    s = cs(D, C, 'Goal pyramid', 'pyramid', N('Vision, mission, goals and measures in one logic.', 'Adapt the level contents.'))
    for i, (h, f, w_) in enumerate([('Vision', BLUE, 3.4), ('Mission', MBLUE, 5.8), ('Goals', SAND, 8.2), ('Measures', LSAND, 10.6)]):
        y = 1.5 + i * 1.08
        rect(s, L + (W - w_) / 2, y, w_, 0.95, fill=f, content=[{'t': h, 'size': 17}, {'t': D1, 'size': 13}], color=WHITE if f == BLUE else BLACK, align='c', anchor='m')

    s = cs(D, C, 'Market sizing', 'tam', N('TAM / SAM / SOM derivation.', 'Enter values and sources; document the derivation in the notes.'), source='Source: [Study, year]')
    cx = L + 2.9
    for d, f, yo in [(4.4, SAND, 0), (3.1, STONE, 1.3), (1.7, BLUE, 2.7)]:
        oval(s, cx - d / 2, 1.5 + yo, d, fill=f)
    xr = 6.4; wr = R - xr
    for i, (a, b) in enumerate([('€0.0bn', 'TAM – total addressable market'), ('€0.0bn', 'SAM – serviceable available market'), ('€0m', 'SOM – serviceable obtainable market')]):
        y = 1.5 + i * 1.45
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, 2.4, 0.6, a, size=28, color=BLUE)
        text(s, xr + 2.5, y + 0.15, wr - 2.5, 0.35, b, size=15)
        text(s, xr + 2.5, y + 0.55, wr - 2.5, 0.6, '[Definition]', size=13, color=DGRAY)

    s = cs(D, C, 'Root cause (Ishikawa)', 'ishikawa', N('Root-cause analysis (6M).', 'Enter causes per category; main cause in blue.'))
    sx, ex, my = L, R - 2.4, 3.65
    hline(s, sx, my, ex - sx, BLACK, 2)
    rect(s, ex, my - 0.6, 2.4, 1.2, fill=BLUE, content='Effect / problem', size=15, color=WHITE, anchor='m', align='c')
    for i, c in enumerate(['People', 'Machine', 'Method', 'Material', 'Measurement', 'Environment']):
        top = i < 3; bx = sx + 0.6 + (i % 3) * 3.3; y_end = 1.55 if top else 5.75
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(bx), I(y_end), I(bx + 1.3), I(my))
        _strip_style(ln); ln.line.fill.solid(); setc(ln.line.color, TAUPE); ln.line.width = Pt(1.25)
        rect(s, bx - 0.7, y_end - (0.42 if top else 0), 1.8, 0.42, fill=SAND, content=c, size=14, align='c', anchor='m')
        for j in range(2):
            fy = (y_end + 0.55 + j * 0.55) if top else (y_end - 0.95 - j * 0.55)
            fx = bx + 1.3 * ((fy - y_end) / (my - y_end))
            text(s, fx + 0.2, fy, 1.8, 0.35, 'Cause', size=13, anchor='m')


# =====================================================================================
def s14(D):
    C = 'Charts'
    divider(D, 14, 'Charts', N('Native, editable PowerPoint charts in Körber style.', 'Right-click > Edit Data; colours stay.',
                                'One message per chart: the relevant series in blue, everything else grey.'))
    cats = ['Cat. 1', 'Cat. 2', 'Cat. 3', 'Cat. 4', 'Cat. 5']
    s = cs(D, C, 'Column chart', 'ch_col', N('Time series or comparison.', 'Edit data; highlight the relevant columns in blue.'), source='Source: [Source]')
    bar(s, L, 1.4, 8.6, 4.4, cats, [('Series', [20, 23, 26, 29, 32])], fmt='0', highlight=[4], gap=55, size=13)
    disturber(s, 9.9, 2.0, [{'t': '+00%', 'size': 30}, {'t': 'Key figure', 'size': 12}], d=2.3)

    s = cs(D, C, 'Stacked columns (100%)', 'ch_stack', N('Composition over time.', 'Focus segment as the bottom series in blue.'), source='Source: [Source]')
    bar(s, L, 1.4, 8.6, 4.4, ['Year 1', 'Year 2', 'Year 3', 'Year 4'], [('Segment A', [0.3, 0.38, 0.44, 0.5]), ('Segment B', [0.5, 0.46, 0.42, 0.4]),
                                                                    ('Segment C', [0.2, 0.16, 0.14, 0.1])],
        stacked=True, pct=True, colors=[BLUE, STONE, SAND], legend='b', fmt='0%', gap=55, size=13)
    kpi(s, 9.5, 1.6, R - 9.5, '00%', 'Share of segment A', bigsize=32)

    s = cs(D, C, 'Ranking bars', 'ch_rank', N('Ranking of categories – sorted descending.', 'Sort data; focus bars in blue.'), source='Source: [Source]')
    bar(s, L, 1.4, 8.6, 4.4, cats, [('Value', [90, 75, 60, 45, 30])], kind='bar', fmt='0', highlight=[0], gap=45, size=13)
    disturber(s, 9.9, 2.0, [{'t': '00%', 'size': 30}, {'t': 'Key figure', 'size': 12}], d=2.3)

    s = cs(D, C, 'Line chart with target', 'ch_line', N('Development over time with target value.', 'Edit data; target series dashed grey.'), source='Source: [Source]')
    line_chart(s, L, 1.4, 9.0, 4.4, ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12'],
               [('Actual', [30, 32, 33, 35, 36, 38, 40, 41, 43, 43, 44, 44]), ('Target', [43] * 12)],
               colors=[BLUE, TAUPE], dashes=[None, MSO_LINE.DASH], fmt='0', labels='last', size=13, min_=25, max_=48)
    kpi(s, 9.9, 1.6, R - 9.9, '+00%', 'Key figure', bigsize=30)

    s = cs(D, C, 'Target achievement (donuts)', 'ch_donut', N('Progress or target achievement.', 'Edit value and remainder (sum = 100%).'))
    cw = W / 4
    for i, v in enumerate([0.68, 1.0, 1.0, 0.85]):
        x = L + i * cw + (cw - 2.4) / 2
        doughnut(s, x, 1.6, 2.4, [v, 1 - v] if v < 1 else [1, 0], colors=[BLUE if v >= 1 else AMBER, SAND], hole=75)
        text(s, x, 2.45, 2.4, 0.7, '%d%%' % round(v * 100), size=20, align='c', anchor='m')
        text(s, L + i * cw, 4.15, cw, 0.35, 'Target %d' % (i + 1), size=17, align='c')
        text(s, L + i * cw, 4.55, cw, 0.35, '[Definition]', size=13, align='c', color=DGRAY)
    sowhat(s, KT)

    s = cs(D, C, 'Bubble chart', 'ch_bubble', N('Portfolio view with three dimensions (x, y, size).', 'Edit data; colour focus points blue.'), source='Source: [Source]')
    ch = scatter(s, L, 1.4, 8.6, 4.4, [('Items', [(70, 18, 40), (82, 12, 32), (30, 6, 12), (45, 9, 20), (25, 15, 8)])],
                 bubble=True, xtitle='Dimension X', ytitle='Dimension Y', xmin=0, xmax=100, ymin=0, ymax=25, size=13, bubble_scale=50)
    ser = ch.plots[0].series[0]
    for i in range(5):
        pt = ser.points[i]; pt.format.fill.solid(); setc(pt.format.fill.fore_color, BLUE if i < 2 else STONE)
        pt.data_label.has_text_frame = True; pt.data_label.text_frame.text = 'ABCDE'[i]; pt.data_label.position = XL_LABEL_POSITION.CENTER
        r_ = pt.data_label.text_frame.paragraphs[0].runs[0]; r_.font.size = Pt(13); setc(r_.font.color, WHITE if i < 2 else BLACK)
    label(s, 9.6, 1.5, R - 9.6, 'Reading')
    text(s, 9.6, 1.85, R - 9.6, 2.5, bl(['Insight', 'Insight'], sa=8), size=15)

    s = cs(D, C, 'Table with data bars', 'ch_table', N('Compact comparison of several KPIs.', 'Bar length = value × column width.'), source='Source: [Source]')
    rows = [['Item', 'KPI', '', 'KPI 2', 'KPI 3']] + [['Item %d' % i, '00%', '', '00%', '00%'] for i in range(1, 5)]
    table(s, L, 1.5, W, rows, colw=[2.4, 1.4, 4.2, 2.2, 2.2], rowh=0.75, size=15, aligns=['l', 'r', 'l', 'c', 'c'])
    xb = L + W * 3.8 / 12.4 + 0.1; bmax = W * 4.2 / 12.4 - 0.3
    for r, v in enumerate([0.71, 0.66, 0.54, 0.62]):
        rect(s, xb, 1.5 + (r + 1) * 0.75 + 0.24, bmax * v, 0.27, fill=BLUE if r == 2 else STONE)
    sowhat(s, KT)


# =====================================================================================
def s15(D):
    C = 'Closing'
    divider(D, 15, 'Closing', N('Summary, next steps, Q&A, contact.', 'End with concrete next steps and owners.',
                                'No meeting ends without an agreed next step – log it in the CRM.'))
    s = cs(D, C, 'Key takeaways', 'takeaways', N('Summary before decision or discussion.', 'Use the action titles of the presentation.'))
    for i in range(4):
        y = 1.5 + i * 1.08
        num(s, L, y + 0.15, i + 1, 0.55, size=16)
        text(s, L + 0.85, y + 0.05, 4.5, 0.75, 'Takeaway %d' % (i + 1), size=20, anchor='m')
        text(s, L + 5.6, y + 0.05, 7.0, 0.75, D1, size=16, anchor='m')
        if i < 3:
            hline(s, L + 0.85, y + 0.95, W - 0.85, STONE, 0.5)

    s = cs(D, C, 'Next steps', 'nextsteps', N('Binding next steps with owners and dates.', 'Fill in during the meeting; confirm by e-mail.',
                                              'Create the steps as tasks in the CRM right after the meeting.'))
    rows = [['#', 'Activity', 'Owner', 'Date']] + [[str(i), 'Activity', '[Name]', '[DD.MM.]'] for i in range(1, 5)]
    tb = table(s, L, 1.5, W, rows, colw=[0.6, 6.6, 3.2, 2.2], rowh=0.75, size=16)
    for r in range(1, 5):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=18, color=BLUE)
    sowhat(s, KT)

    s = D.slide('hl_dark', 'Questions &', key='discussion', notes=N('Transition into Q&A.', 'Change the picture via Change Picture.'))
    pic(s, 27, IMG + 'image24.jpg')
    D.ph(s, 29, 'discussion')
    D.drop_empty(s, keep=(20, 21, 22, 23, 24, 27, 29))

    s = D.slide('end_contact', 'Thank you!', key='end', notes=N('Closing slide with contact details.', 'Enter name, role, location, phone and e-mail.'))
    D.ph(s, 10, '[First name Last name]\n[Role]'); D.ph(s, 14, '[Location]'); D.ph(s, 15, '+49 [phone]'); D.ph(s, 16, '[first.last]@koerber.com')

    s = D.slide('legal', key='legal', notes=N('Legal disclaimer – mandatory for proposals and external documents.', 'Align text with Legal.'))


# =====================================================================================
def s16(D):
    divider(D, 16, 'Toolkit', N('Grid, rules, colours, building blocks and icons for your own slides.', 'Do not show to customers.',
                                 'Always build new slides from these building blocks – this keeps every slide consistent.'))
    s = D.slide('content', 'Every element has a fixed position', 'Toolkit | Grid', key='grid',
                notes=N('Reference for everyone building new slides.', 'View > Guides.', 'Inches: margin left 0.37 / right 12.97; content from 1.45; key takeaway at 5.98; column gap 0.3.'))
    rect(s, L, 1.45, W, 4.4, line=BLUE)
    text(s, L + 0.15, 1.55, 6, 0.3, 'Content area  |  top 1.45"  |  bottom 5.80"', size=13, color=BLUE)
    cw = (W - 3 * 0.3) / 4
    for i in range(4):
        rect(s, L + i * (cw + 0.3), 2.0, cw, 3.65, fill=LBLUE)
        text(s, L + i * (cw + 0.3), 3.6, cw, 0.4, 'Column %d' % (i + 1), size=13, align='c', color=BLUE)
    sowhat(s, 'Key takeaway always at the same position (5.98") – it is the first thing readers look for.')
    for y, t in [(0.4, '← Title: action title, 24 pt, max. 76 characters'), (0.78, '← Tracker: “chapter | slide type”, 14 pt')]:
        text(s, 8.4, y, 4.4, 0.3, t, size=10, color=BLUE)

    s = D.slide('content', 'Blue highlights, grey structures', 'Toolkit | Colours and typography', 'Source: Körber Brand Hub', key='colors',
                notes=N('CI quick reference.', 'Align CI changes with Brand & Communications.'))
    cols = [('Körber blue', '0060FF', BLUE, 'Highlight, focus'), ('Black', '000000', BLACK, 'Text, lines'), ('Warm grey light', 'E6E2DC', SAND, 'Areas, cards'),
            ('Warm grey', 'BFB8AF', STONE, 'Comparison values'), ('Warm grey dark', '9D968D', TAUPE, 'Arrows, secondary'), ('Yellow', 'FFE32F', YELLOW, 'Call to action only'),
            ('Amber', 'FEC037', AMBER, 'Status: at risk'), ('Orange', 'FE8623', ORANGE, 'Status: critical')]
    cw = (W - 3 * 0.25) / 4
    for i, (n_, hx, c, u) in enumerate(cols):
        x = L + (i % 4) * (cw + 0.25); y = 1.5 + (i // 4) * 1.6
        rect(s, x, y, 0.9, 0.9, fill=c)
        text(s, x + 1.05, y, cw - 1.05, 0.3, n_, size=14)
        text(s, x + 1.05, y + 0.3, cw - 1.05, 0.3, '#' + hx, size=12, color=DGRAY)
        text(s, x + 1.05, y + 0.6, cw - 1.05, 0.5, u, size=12)
    hline(s, L, 4.85, W, BLACK)
    tw = W / 5
    for i, (a, b) in enumerate([('Title', '24 pt Arial regular'), ('Tracker', '14 pt'), ('Text', '14–16 pt'), ('Labels', '10 pt caps, blue'), ('Source', '9 pt (placeholder)')]):
        text(s, L + i * tw, 5.0, tw - 0.2, 0.3, a, size=14, color=BLUE)
        text(s, L + i * tw, 5.32, tw - 0.2, 0.3, b, size=13)

    s = D.slide('content', 'Copy these building blocks instead of drawing new ones', 'Toolkit | Building blocks', key='blocks',
                notes=N('Copy and paste elements instead of redrawing them.', '–', 'Copying from this slide keeps spacing, colours and sizes consistent.'))
    label(s, L, 1.45, 3, 'Numbers and status', color=DGRAY)
    num(s, L, 1.8, 1); num(s, L + 0.6, 1.8, 2, filled=False)
    for k, st in enumerate('gyrn'):
        rag(s, L + 1.3 + k * 0.35, 1.91, st)
    label(s, L, 2.5, 3, 'Harvey balls (0–4)', color=DGRAY)
    for q in range(5):
        harvey(s, L + q * 0.55, 2.85, 0.38, q)
    label(s, L, 3.5, 3, 'Stickers and tags', color=DGRAY)
    shape(s, SH.PENTAGON, L, 3.85, 1.2, 0.26, fill=BLUE, content='Internal', size=9, color=WHITE, caps=True, spacing=0.8, anchor='m', margin=(0.1, 0, 0.05, 0))
    rrect(s, L + 1.4, 3.83, 1.1, 0.3, fill=WHITE, line=BLUE, radius=0.15, content='Segment', size=10, color=BLUE, align='c', anchor='m', margin=0)
    label(s, L, 4.5, 3, 'Call to action', color=DGRAY)
    rrect(s, L, 4.85, 2.7, 0.45, fill=YELLOW, radius=0.22, content='Decision by [date]', size=12, align='c', anchor='m', margin=0)
    x2 = 4.0
    label(s, x2, 1.45, 3, 'Process', color=DGRAY)
    chevrons(s, ['Step 1', 'Step 2', 'Step 3'], x2, 1.8, 4.2, 0.5, active=1, size=11)
    label(s, x2, 2.5, 3, 'Flow chart symbols', color=DGRAY)
    rrect(s, x2, 2.85, 1.2, 0.5, fill=BLACK, radius=0.25, content='Start / end', size=10, color=WHITE, align='c', anchor='m', margin=0)
    rect(s, x2 + 1.4, 2.85, 1.2, 0.5, fill=SAND, content='Step', size=10, align='c', anchor='m')
    shape(s, SH.DIAMOND, x2 + 2.8, 2.75, 1.2, 0.7, fill=BLUE, content='Question?', size=10, color=WHITE, align='c', anchor='m', margin=0)
    label(s, x2, 3.6, 3, 'Icon in circle', color=DGRAY)
    icon_circle(s, 'factory', x2, 3.9, 0.62); icon_circle(s, 'science', x2 + 0.8, 3.9, 0.62, fill=SAND, color=BLUE)
    label(s, x2, 4.75, 3, 'Key figure', color=DGRAY)
    text(s, x2, 5.0, 2, 0.6, '00%', size=28, color=BLUE)
    x3 = 8.8; w3 = R - x3
    label(s, x3, 1.45, 3, 'Card', color=DGRAY)
    card(s, x3, 1.8, w3, 1.6, H, D1, lab='Label', hsize=16, bsize=13)
    label(s, x3, 3.6, 3, 'Disturber (Körber CI)', color=DGRAY)
    disturber(s, x3, 3.95, [{'t': '00%', 'size': 22}, {'t': 'Key figure', 'size': 11}], d=1.6)

    s = D.slide('content', 'Google Material Symbols – 117 icons, recolourable', 'Toolkit | Icons',
                'Google Material Symbols Outlined (Apache 2.0) – copy an icon, recolour via Shape Fill', key='icons',
                notes=N('Icon library: Google Material Symbols, as recommended in the Körber 2025 template (“Google Icons”).',
                        'Copy, paste, recolour via Shape Fill; resize proportionally with Shift.',
                        'More icons: fonts.google.com/icons (style Outlined, weight 200) – insert as SVG and convert to shape.'))
    names = sorted(json.load(open(os.path.join(HERE, 'icons.json'))).keys())
    cols_ = 13; cw = W / cols_; rh = 0.56
    for i, n_ in enumerate(names):
        x = L + (i % cols_) * cw; y = 1.4 + (i // cols_) * rh
        icon(s, n_, x + cw / 2 - 0.15, y, 0.3, BLUE)
        text(s, x, y + 0.31, cw, 0.2, n_.replace('_', ' '), size=7, align='c', color=DGRAY)
