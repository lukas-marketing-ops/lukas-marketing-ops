# Körber Slide Library 2026 – English, content-neutral template slides
from kh import *
from kh import _strip_style

IMG = template_media()
LY.update(text=26, two_col=43, three_col=49, content_img=51, title_img_cols=61, half_circle_right=60, half_content=45)

TT = 'Action title that states the key message of the slide'
H = 'Headline'
D1 = 'Short description in one or two lines.'
KT = 'One sentence that states the so-what of this slide.'
B3 = ['First point', 'Second point', 'Third point']


def N(use, adapt, tip=None):
    t = 'USE: ' + use + '\n\nADAPT: ' + adapt
    if tip:
        t += '\n\nTIP: ' + tip
    return t


def divider(D, nr, name, notes):
    nr = len([n for n, _ in D.sections if not n.startswith('00')]) + 1  # numbered automatically in build order
    D.section('%02d %s' % (nr, name.replace('-\n', '').replace('\n', ' ')))
    s = D.slide('section_name_blue', notes=notes, key='sec%02d' % nr)
    D.ph(s, 25, '%02d' % nr)
    D.ph(s, 26, name)
    return s


def cs(D, chap, typ, key, notes, title=TT, source=None, sticker_=None, layout='content'):
    return D.slide(layout, title, '%s | %s' % (chap, typ), source, notes=notes, key=key, sticker_=sticker_)


def person(s, x, y, d=0.9):
    oval(s, x, y, d, fill=SAND)
    icon(s, 'person', x + d * 0.2, y + d * 0.2, d * 0.6, TAUPE)


def pic(s, idx, path):
    {p.placeholder_format.idx: p for p in s.placeholders}[idx].insert_picture(path)


def quad_axes(s, gx0, gy0, gw, gh, xl, yl):
    text(s, gx0, gy0 + gh + 0.05, gw, 0.3, xl + ' →', size=11, align='r')
    tb = text(s, 0, 0, gh, 0.35, yl + ' →', size=11, align='r')
    tb.rotation = 270; tb.left = I(gx0 - 0.4 - gh / 2); tb.top = I(gy0 + gh / 2 - 0.17)


# =====================================================================================
def s00(D):
    D.section('00 Start here')
    s = D.slide('title_grad', 'Slide Library 2026\nPharma Consulting', key='cover',
                notes=N('Cover of the library. Do not use in customer meetings.', 'Update version and date with every release.'))
    D.ph(s, 14, 'Standard slides for customer meetings and lead projects in Körber CI')
    D.ph(s, 15, 'Version 2.0 | October 2026')
    D.ph(s, 12, 'For internal use')

    s = D.slide('content', 'Four steps from library to customer-ready presentation', 'Start here | How to use', key='howto',
                notes=N('Short guide for everyone working with the library.', 'Extend when new conventions are agreed.'))
    steps = [('Pick a storyline', 'Choose the meeting type and copy the recommended slide sequence.'),
             ('Copy the slides', 'Use “Reuse slides” or copy & paste – the Körber design is kept.'),
             ('Fill the content', 'Write the action title first, then replace all placeholders.'),
             ('Check quality', 'One message per slide, source given, stickers removed.')]
    cw = (W - 3 * 0.4) / 4
    for i, (h, b) in enumerate(steps):
        colhead(s, L + i * (cw + 0.4), 1.5, cw, None, h, b, n=i + 1, hsize=18, bsize=14, bh=1.4)
    rect(s, L, 4.4, W, 1.4, fill=LSAND)
    label(s, L + 0.3, 4.6, 6, 'Conventions')
    conv = [('[Square brackets]', 'placeholder – replace before use'), ('Blue', 'highlights the one thing that matters'),
            ('Key takeaway box', 'the so-what of the slide in one sentence'), ('Speaker notes', 'how to use and adapt each slide')]
    for i, (a, b) in enumerate(conv):
        x = L + 0.3 + (i % 2) * 6.2; y = 4.95 + (i // 2) * 0.4
        text(s, x, y, 6.0, 0.35, [{'t': [(a + '  ', {'color': BLUE}), (b, {})]}], size=13)

    s = D.slide('content', 'Contents: 23 chapters from first meeting to account growth', 'Start here | Contents (click a chapter)', key='toc',
                notes=N('Navigation: click a chapter to jump to it (also in slide show).', 'Filled automatically with slide numbers.'))
    s = D.slide('content', 'Storyline builder: the right slide sequence for every meeting type', 'Start here | Storylines',
                'Slide numbers refer to this library', key='story',
                notes=N('Starting point for every new presentation.', 'Add your own meeting types as rows.',
                        'Rule of thumb: 1.5–2 minutes per slide, keep 30% of the time for dialogue.'))


# =====================================================================================
def s01(D):
    divider(D, 1, 'Basic\nslides', N('Generic slides that fit every presentation: covers, agenda, text, columns, images, numbers, quote.',
                                      'Text placeholders are native Körber layout placeholders – just type.',
                                      'Start every deck with these slides and add specific modules from the later chapters.'))
    s = D.slide('title_blue', 'Presentation title\nin up to two lines', key='cover_blue',
                notes=N('Cover for customer meetings.', 'Use the customer’s topic as title, not “Körber presentation”.'))
    D.ph(s, 14, 'Subtitle: occasion, customer, purpose'); D.ph(s, 15, '[Day Month Year], [Location]'); D.ph(s, 12, 'Confidential')
    s = D.slide('title_img', 'Presentation title\nin up to two lines', key='cover_img',
                notes=N('Cover with image.', 'Right-click the picture > Change Picture (Körber Pictures Library).'))
    pic(s, 10, IMG + 'image12.jpeg')
    D.ph(s, 14, 'Subtitle: occasion, customer, purpose'); D.ph(s, 15, '[Day Month Year], [Location]'); D.ph(s, 12, 'Confidential')
    D.drop_empty(s, keep=(10, 12, 14, 15))
    s = D.slide('title_light', 'Presentation title\nin up to two lines', key='cover_light',
                notes=N('Cover for project meetings (kick-off, steering committee).', 'Add project name and date.'))
    D.ph(s, 14, 'Subtitle: occasion, customer, purpose'); D.ph(s, 15, '[Day Month Year], [Location]'); D.ph(s, 12, 'Confidential')

    s = D.slide('agenda_blue', 'Agenda', key='agenda', notes=N('Agenda with up to five items.', 'Phrase items as outcomes, not topics.'))
    for i in range(5):
        D.ph(s, 34 + 2 * i, '%02d' % (i + 1)); D.ph(s, 35 + 2 * i, 'Agenda item %d' % (i + 1))

    s = cs(D, 'Basics', 'Agenda with timing', 'agenda_time', N('Agenda for workshops and longer meetings.', 'Adapt times, topics, outcomes and owners.'),
           title='Agenda')
    rows = [['Time', 'Topic', 'Outcome', 'Owner']] + [['00:00 – 00:00', 'Topic %d' % i, 'Expected outcome', '[Name]'] for i in range(1, 6)]
    tb = table(s, L, 1.5, W, rows, colw=[1.8, 3.6, 5.0, 2.2], rowh=0.62, size=14)
    for r in range(1, 6):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=14, color=BLUE)

    s = cs(D, 'Basics', 'Text', 'text', N('Simple text slide with bullet levels of the Körber master.', 'Type into the placeholder; use the indent buttons for levels.'),
           layout='text')
    D.ph(s, 25, ['Main statement in one or two lines', {'t': 'Supporting point', 'bullet': True}, {'t': 'Supporting point', 'bullet': True},
                 {'t': 'Supporting point', 'bullet': True}], size=16, space_after=8)

    s = cs(D, 'Basics', 'Key message', 'statement', N('One strong statement – for transitions, summaries or a key insight.', 'Maximum three lines.'))
    text(s, L, 2.0, 9.5, 2.6, 'One key message that the audience should remember – in up to three lines.', size=32)
    text(s, L, 4.9, 9.5, 0.6, 'Supporting sentence with context or evidence.', size=16, color=DGRAY)
    disturber(s, 10.5, 2.3, [{'t': '00%', 'size': 30}, {'t': 'Key figure', 'size': 12}], d=2.2)

    s = cs(D, 'Basics', 'Two columns', 'two_col', N('Comparison or two perspectives.', 'Replace headlines and text.'))
    cw = (W - 0.5) / 2
    for i in range(2):
        colhead(s, L + i * (cw + 0.5), 1.5, cw, 'Label', H, bl(B3, sa=6), hsize=20, bsize=15, bh=2.5)

    s = cs(D, 'Basics', 'Three columns with icons', 'three_col', N('Three arguments, capabilities or steps.', 'Swap icons from the icon library (Toolkit).'))
    cw = (W - 2 * 0.5) / 3
    for i, ic in enumerate(['lightbulb', 'target', 'trending_up']):
        colhead(s, L + i * (cw + 0.5), 1.5, cw, None, H, D1, icon_=ic, hsize=20, bsize=15, bh=1.2)
    sowhat(s, KT)

    s = cs(D, 'Basics', 'Four cards', 'four_cards', N('Four topics with equal weight.', 'Highlight one card in blue only if it matters most.'))
    cw = (W - 3 * 0.3) / 4
    for i, ic in enumerate(['groups', 'settings', 'verified', 'speed']):
        card(s, L + i * (cw + 0.3), 1.5, cw, 3.0, H, D1, icon_=ic, hsize=17, bsize=14)
    sowhat(s, KT)

    s = cs(D, 'Basics', 'Six-box grid', 'six_grid', N('Overview of six topics (e.g., trends, focus areas).', 'Keep each box to one headline and one line.'))
    cw = (W - 2 * 0.5) / 3
    for i, ic in enumerate(['biotech', 'verified', 'memory', 'eco', 'local_shipping', 'groups']):
        x = L + (i % 3) * (cw + 0.5); y = 1.5 + (i // 3) * 2.15
        icon_circle(s, ic, x, y, 0.62)
        text(s, x + 0.85, y + 0.12, cw - 0.85, 0.4, H, size=18)
        hline(s, x, y + 0.85, cw, STONE, 0.5)
        text(s, x, y + 1.0, cw, 0.8, D1, size=14)

    s = cs(D, 'Basics', 'Text and image', 'text_img', N('Text with a large image.', 'Right-click the picture > Change Picture.'), layout='content_img')
    pic(s, 28, IMG + 'image21.jpeg')
    D.ph(s, 25, ['Main statement in one or two lines', {'t': 'Supporting point', 'bullet': True}, {'t': 'Supporting point', 'bullet': True},
                 {'t': 'Supporting point', 'bullet': True}], size=16, space_after=8)

    s = cs(D, 'Basics', 'Key figures', 'numbers', N('Three to four key figures.', 'Every number needs a label and a source.'), source='Source: [Source]')
    cw = (W - 3 * 0.4) / 4
    for i in range(4):
        kpi(s, L + i * (cw + 0.4), 1.8, cw, ['00%', '€0.0m', '000', '0x'][i], 'Label of the figure', 'Short explanation', bigsize=44)
    sowhat(s, KT)

    s = cs(D, 'Basics', 'Process in steps', 'steps', N('Simple sequence of 3–5 steps.', 'Delete or add chevrons and columns together.'))
    chevrons(s, ['Step 1', 'Step 2', 'Step 3', 'Step 4'], L, 1.5, W, 0.65, size=14)
    cw = (W - 3 * 0.06) / 4
    for i in range(4):
        x = L + i * (cw + 0.06)
        text(s, x + 0.1, 2.4, cw - 0.3, 0.4, H, size=17)
        text(s, x + 0.1, 2.85, cw - 0.3, 1.4, bl(['Activity', 'Activity', 'Deliverable'], sa=6), size=14)
    sowhat(s, KT)

    s = D.slide('quote', '“Customer or expert quote in up to three lines that supports the key message.”', key='quote',
                notes=N('Quote as emotional proof point.', 'Only with written approval; change the photo via Change Picture.'))
    pic(s, 34, IMG + 'image29.jpeg')
    D.ph(s, 14, '[First name Last name]\n[Job title, company]')

    s = D.slide('hl_dark', 'Short', key='hl', notes=N('Strong visual transition or chapter opener.', 'Two short words per line; change the picture via Change Picture.'))
    pic(s, 27, IMG + 'image19.png')
    D.ph(s, 29, 'headline')
    D.drop_empty(s, keep=(20, 21, 22, 23, 24, 27, 29))

    s = cs(D, 'Basics', 'Executive summary', 'execsum',
           N('One-page summary at the start of every analysis or recommendation deck (pyramid principle).',
             'Top box = the answer; three blocks = the supporting arguments; each with the evidence.',
             'Write this slide first and last: it is the storyline of the whole deck.'))
    rect(s, L, 1.5, W, 0.9, fill=BLUE, content='The answer: core message / recommendation in one or two lines', size=18, color=WHITE, anchor='m', margin=(0.3, 0.05, 0.3, 0.05))
    cw = (W - 2 * 0.3) / 3
    for i in range(3):
        x = L + i * (cw + 0.3)
        num(s, x, 2.65, i + 1, 0.45)
        text(s, x + 0.6, 2.65, cw - 0.6, 0.5, 'Supporting argument', size=17, anchor='m')
        hline(s, x, 3.25, cw, BLACK)
        text(s, x, 3.4, cw, 1.6, bl(['Evidence / fact', 'Evidence / fact', 'Evidence / fact'], sa=6), size=14)
    sowhat(s, KT, lead='Decision needed')

    s = cs(D, 'Basics', 'Agenda tracker', 'agenda_tracker',
           N('Repeat between chapters of long decks to show where you are.', 'Copy for every chapter and move the blue highlight.'),
           title='Agenda')
    for i in range(5):
        y = 1.55 + i * 0.85
        on = i == 1
        rect(s, L, y, W, 0.72, fill=BLUE if on else LSAND)
        text(s, L + 0.3, y, 0.8, 0.72, '%02d' % (i + 1), size=20, color=WHITE if on else BLUE, anchor='m')
        text(s, L + 1.2, y, 8, 0.72, 'Agenda item %d' % (i + 1), size=18, color=WHITE if on else BLACK, anchor='m')
        text(s, R - 2.3, y, 2.0, 0.72, '[00:00]', size=14, color=WHITE if on else DGRAY, anchor='m', align='r')

    s = cs(D, 'Basics', 'Empty slide with title', 'blank', N('Blank canvas in Körber layout for your own content.', 'Build from the building blocks in the Toolkit.'))


# =====================================================================================
def s02(D):
    divider(D, 2, 'Company\nintroduction', N('Körber Pharma Consulting introduction (based on Intro deck v5.1).',
                                               'Content is approved company messaging – adapt only the facts that change.',
                                               'Show two to three of these slides, chosen for the customer’s question – not all of them.'))
    s = D.slide('title_grad', 'Turning potential\ninto results', key='intro_cover',
                notes=N('Cover of the company introduction.', 'Add date and customer if needed.'))
    D.ph(s, 14, 'Helping life sciences organizations achieve meaningful business outcomes through consulting, technology and execution.')
    D.ph(s, 15, 'Körber Pharma Consulting GmbH')
    D.ph(s, 12, 'For internal use')

    s = cs(D, 'Company introduction', 'Körber group', 'intro_group',
           N('Shows the strength of the group behind the consulting team.', 'Update figures once a year (Brand Hub).',
             'Read bottom-up: global group → pharma business → consulting team.'),
           title='Backed by the strength of a global technology group', source='Source: Körber; figures as of [year]')
    levels = [('The Consulting Team', ['25+ years dedicated to life sciences consulting', 'Experts in GxP, MES, validation and digitalization',
                                      'Teams in Germany, Switzerland, France and the US'], BLUE, 4.0),
              ('Körber Pharma', ['125+ years of pharma technology expertise', 'Software, machinery, materials, packaging and consulting',
                                 'Trusted by global pharma and biotech leaders'], MBLUE, 5.2),
              ('Körber', ['~13,000 employees worldwide', '100+ locations globally', 'Digital, Pharma, Supply Chain and Technologies'], SAND, 6.4)]
    for i, (h, facts, f, w_) in enumerate(levels):
        y = 1.5 + i * 1.45
        x = L + (6.4 - w_) / 2
        rect(s, x, y, w_, 1.25, fill=f, content=h, size=18, color=WHITE if f == BLUE else BLACK, align='c', anchor='m')
        text(s, 7.2, y + 0.05, R - 7.2, 1.2, bl(facts, sa=3), size=13, anchor='m')
        hline(s, 7.2, y + 1.3, R - 7.2, STONE, 0.5) if i < 2 else None
    sowhat(s, 'One Körber. One ecosystem. 25+ years of dedicated life sciences consulting expertise.', lead='One Körber')

    s = cs(D, 'Company introduction', 'Körber Pharma ecosystem', 'intro_ecosystem',
           N('Differentiation through the Körber Pharma ecosystem.', 'Keep text short – the graphic carries the message.'),
           title='The Körber Pharma ecosystem unlocks the potential of your business')
    text(s, L, 1.6, 5.9, 1.2, 'Few partners combine consulting, software, machinery, materials and operational expertise across the pharmaceutical value chain. Körber does.',
         size=18)
    text(s, L, 3.1, 5.9, 2.5, bl(['Access to expertise from development to supply chain', 'Faster implementation with integrated solutions',
                                  'Value beyond stand-alone solutions'], sa=10), size=15)
    picture(s, os.path.join(HERE, 'ecosystem.png'), 7.4, 1.4, 5.0, 5.13)

    s = cs(D, 'Company introduction', 'Our promise', 'intro_outcomes',
           N('Why customers work with us – outcomes instead of deliverables.', 'Keep the 97% figure up to date.'),
           title='Focused on outcomes, not deliverables', source='Source: Körber Pharma Consulting customer data, [year]')
    pil = [('school', 'Industry expertise', ['Life sciences focused', 'Regulated environments', 'GxP excellence']),
           ('engineering', 'Execution excellence', ['Strategy through implementation', 'Hands-on delivery', 'Sustainable adoption']),
           ('trending_up', 'Business impact', ['Performance improvement', 'Faster time to value', 'Measurable results'])]
    cw = 2.85
    for i, (ic, h, b) in enumerate(pil):
        colhead(s, L + i * (cw + 0.4), 1.5, cw, None, h, bl(b, sa=6), icon_=ic, hsize=19, bsize=14, bh=1.6)
    disturber(s, 10.2, 1.6, [{'t': '97%', 'size': 40}, {'t': 'of customers choose to work with us again', 'size': 12}], d=2.5)
    sowhat(s, 'Strategy you can act on. Execution you can trust.', lead='Our promise')

    s = cs(D, 'Company introduction', 'Portfolio', 'intro_portfolio',
           N('Portfolio overview: signature offerings on top of core capabilities.', 'Highlight the offering relevant for the customer in blue.'),
           title='Where strategy, technology and execution come together')
    label(s, L, 1.4, 4, 'Signature offerings')
    so = [('query_stats', 'Production Digitalization Strategy', 'Focus digital investments for maximum impact'),
          ('hub', 'Digital Platform Integration', 'Turn fragmented systems into one platform'),
          ('rocket_launch', 'Fast Track to Production', 'Accelerate the way to a high-performance line'),
          ('psychology', 'AI Validation Framework', 'Validate and scale AI across your GxP organization')]
    cw = (W - 3 * 0.25) / 4
    for i, (ic, h, b) in enumerate(so):
        x = L + i * (cw + 0.25)
        rect(s, x, 1.7, cw, 1.55, line=BLUE, lw=1)
        icon(s, ic, x + 0.2, 1.85, 0.38, BLUE)
        text(s, x + 0.7, 1.85, cw - 0.85, 0.5, h, size=13, anchor='m')
        text(s, x + 0.2, 2.45, cw - 0.4, 0.75, b, size=12, color=DGRAY)
    rect(s, L, 3.4, W, 0.42, fill=BLUE, content='Life sciences expertise in action', size=13, color=WHITE, align='c', anchor='m')
    label(s, L, 3.95, 4, 'Core capabilities')
    cc = [('analytics', 'Digital Excellence', 'Turn process insights into measurable improvements'),
          ('lan', 'System Integration', 'Implement and operate critical manufacturing systems'),
          ('precision_manufacturing', 'Machinery Consulting', 'Turn equipment investments into reliable operations'),
          ('verified', 'Quality & Compliance', 'Build quality systems that are inspection-ready')]
    for i, (ic, h, b) in enumerate(cc):
        x = L + i * (cw + 0.25)
        rect(s, x, 4.25, cw, 1.3, fill=LSAND)
        icon(s, ic, x + 0.2, 4.4, 0.36, BLUE)
        text(s, x + 0.7, 4.4, cw - 0.85, 0.36, h, size=13, anchor='m')
        text(s, x + 0.2, 4.88, cw - 0.4, 0.62, b, size=12, color=DGRAY)
    fw = (W - 2 * 0.25) / 3
    for i, t in enumerate(['Project Management', 'Risk Management', 'Operations & Support']):
        rect(s, L + i * (fw + 0.25), 5.7, fw, 0.42, fill=SAND, content=t, size=12, align='c', anchor='m')

    s = cs(D, 'Company introduction', 'Presence', 'intro_map', N('Where our consulting teams are based.', 'Update locations if teams change.'),
           title='Dedicated teams in Germany, Switzerland, France and the US', source='Source: Körber Pharma Consulting')
    picture(s, os.path.join(HERE, 'worldmap.png'), L, 1.45, 8.2, 5.0)
    for px, py in [(900, 420), (878, 456), (842, 446), (470, 452)]:  # Germany, Switzerland, France, US (map pixel coords)
        oval(s, L + px * 8.2 / 1800 - 0.11, 1.45 + py * 5.0 / 1100 - 0.11, 0.22, fill=BLUE)
    xr = 9.0; wr = R - xr
    for i, (c, t) in enumerate([('Germany', '[City], [City]'), ('Switzerland', '[City]'), ('France', '[City]'), ('United States', '[City]')]):
        y = 1.6 + i * 1.0
        hline(s, xr, y, wr, BLACK)
        text(s, xr, y + 0.1, wr, 0.35, c, size=17)
        text(s, xr, y + 0.47, wr, 0.35, t, size=13, color=DGRAY)

    s = cs(D, 'Company introduction', 'Your team', 'team', N('Introduce the project team.', 'Insert photos via Change Picture or copy a circle photo.'),
           title='Your team for [project / topic]')
    cw = (W - 3 * 0.3) / 4
    for i in range(4):
        x = L + i * (cw + 0.3)
        person(s, x + (cw - 1.4) / 2, 1.6, 1.4)
        text(s, x, 3.2, cw, 0.35, '[First name Last name]', size=16, align='c')
        text(s, x, 3.6, cw, 0.3, '[Role in the project]', size=13, color=BLUE, align='c')
        hline(s, x + 0.3, 4.1, cw - 0.6, STONE)
        text(s, x + 0.3, 4.25, cw - 0.6, 1.3, bl(['Expertise', 'Relevant reference'], sa=4), size=13)


# =====================================================================================
def s03(D):
    C = 'Customer situation'
    divider(D, 3, 'Customer\nsituation', N('Show that we understood the customer: situation, findings, hypotheses, benchmark.',
                                            'Fill with customer-specific insights only.', 'This chapter builds credibility – listen first, then present.'))
    s = cs(D, C, 'Situation – complication – resolution', 'scr', N('Storyline opener following the SCR logic.', 'One headline and one supporting line per box.'))
    cw = (W - 2 * 0.45) / 3
    for i, (lab, f) in enumerate([('Situation', LSAND), ('Complication', SAND), ('Resolution', BLUE)]):
        x = L + i * (cw + 0.45)
        rect(s, x, 1.5, cw, 4.1, fill=f)
        c = WHITE if f == BLUE else BLACK
        label(s, x + 0.3, 1.75, cw - 0.6, lab, color=WHITE if f == BLUE else BLUE)
        text(s, x + 0.3, 2.1, cw - 0.6, 1.2, 'Headline in up to two lines', size=22, color=c)
        text(s, x + 0.3, 3.6, cw - 0.6, 1.0, D1, size=15, color=c)
        if i < 2:
            oval(s, x + cw + 0.04, 3.37, 0.37, fill=WHITE, line=STONE)
            icon(s, 'arrow_forward', x + cw + 0.1, 3.43, 0.25, BLUE)
    sowhat(s, KT)

    s = cs(D, C, 'What we heard', 'heard', N('Synthesis of stakeholder interviews.', 'Anonymised quotes in the customer’s words.'), source='Source: [x] interviews, [period]')
    for i in range(3):
        y = 1.5 + i * 1.45
        rect(s, L, y, 6.8, 1.25, fill=LSAND)
        text(s, L + 0.25, y + 0.05, 0.6, 0.8, '“', size=48, color=BLUE)
        text(s, L + 0.9, y + 0.25, 5.7, 0.5, 'Quote in the customer’s own words', size=16)
        text(s, L + 0.9, y + 0.78, 5.7, 0.3, '– [Role]', size=12, color=DGRAY)
    xr = 7.6; wr = R - xr
    label(s, xr, 1.5, wr, 'Our conclusion')
    for i in range(3):
        y = 1.9 + i * 1.3
        num(s, xr, y, i + 1, 0.45)
        text(s, xr + 0.65, y - 0.02, wr - 0.65, 0.35, H, size=18, color=BLUE)
        text(s, xr + 0.65, y + 0.38, wr - 0.65, 0.5, D1, size=14)

    s = cs(D, C, 'Issue tree', 'issuetree', N('MECE breakdown of the key question.', 'Key question as a SMART question; sub-questions must not overlap.'))
    shape(s, SH.RECTANGLE, L, 3.0, 2.9, 1.4, fill=BLUE, content='Key question in up to three lines', size=15, color=WHITE, anchor='m')
    for i in range(3):
        y = 1.5 + i * 1.6
        arrow(s, L + 2.9, 3.7, L + 3.5, y + 0.6, color=TAUPE)
        shape(s, SH.RECTANGLE, L + 3.5, y + 0.3, 3.0, 0.6, fill=SAND, content='Driver %d' % (i + 1), size=15, anchor='m')
        for j in range(2):
            yy = y + j * 0.7
            arrow(s, L + 6.5, y + 0.6, L + 7.0, yy + 0.27, color=STONE)
            shape(s, SH.RECTANGLE, L + 7.0, yy, 5.6, 0.55, line=STONE, content='Sub-question %d.%d' % (i + 1, j + 1), size=14, anchor='m')

    s = cs(D, C, 'Hypotheses', 'hypotheses', N('Hypothesis-driven work for discovery and steering committees.', 'Update status after each analysis wave.'),
           source='As of: [date]')
    rows = [['#', 'Hypothesis', 'Tested by', 'Status']] + [['H%d' % i, 'Hypothesis in one sentence', 'Analysis / method', 'Open'] for i in range(1, 4)]
    tb = table(s, L, 1.5, W, rows, colw=[0.8, 6.0, 4.0, 1.8], rowh=[0.45, 0.8, 0.8, 0.8], size=15, aligns=['l', 'l', 'l', 'c'])
    for r in range(1, 4):
        fill_tf(tb.cell(r, 0).text_frame, rows[r][0], size=16, color=BLUE)
        c = tb.cell(r, 3); c.fill.solid(); setc(c.fill.fore_color, SAND)
    sowhat(s, KT)

    s = cs(D, C, 'Maturity assessment', 'maturity', N('Result of a maturity assessment.', 'Move the dots horizontally (scale 1–5): filled = today, outline = target.'))
    x0, x1 = L + 3.6, L + 10.6
    step = (x1 - x0) / 4
    for k in range(5):
        text(s, x0 + k * step - 0.5, 1.45, 1.0, 0.3, str(k + 1), size=13, align='c', color=DGRAY)
    for i, (ist, ziel) in enumerate([(3, 4), (2.5, 4), (1.5, 4.5), (2, 3.5)]):
        y = 2.0 + i * 0.85
        text(s, L, y, 3.4, 0.4, 'Dimension %d' % (i + 1), size=16, anchor='m')
        hline(s, x0, y + 0.2, x1 - x0, STONE, 0.75)
        xi, xz = x0 + (ist - 1) * step, x0 + (ziel - 1) * step
        hline(s, xi, y + 0.2, xz - xi, BLUE, 3)
        oval(s, xi - 0.15, y + 0.05, 0.3, fill=BLUE)
        oval(s, xz - 0.15, y + 0.05, 0.3, fill=WHITE, line=BLUE, lw=2)
    dot(s, L, 5.55, 0.2, BLUE); text(s, L + 0.3, 5.5, 1.5, 0.3, 'Today', size=12)
    oval(s, L + 1.4, 5.55, 0.2, fill=WHITE, line=BLUE, lw=1.5); text(s, L + 1.7, 5.5, 1.5, 0.3, 'Target', size=12)
    sowhat(s, KT)

    s = cs(D, C, 'Benchmark', 'benchmark', N('Comparison with peers – creates urgency.', 'Right-click the chart > Edit Data; highlight the customer in blue.'),
           source='Source: [Benchmark, n = xx]')
    bar(s, L, 1.4, 8.0, 4.4, ['Best in class', 'Top quartile', 'Median', '[Customer]', 'Bottom quartile'], [('KPI', [0.8, 0.7, 0.6, 0.55, 0.45])],
        kind='bar', fmt='0%', highlight=3, gap=45, size=13)
    xr = 9.0; wr = R - xr
    kpi(s, xr, 1.6, wr, '–00 pp', 'Gap to top quartile', bigsize=32)
    kpi(s, xr, 3.3, wr, '€0.0m', 'Value of closing the gap', bigsize=32)
    sowhat(s, KT)

    s = cs(D, C, 'Pain points along the value chain', 'painpoints', N('Process view with the biggest pain points.', 'Highlight the steps with the highest impact in blue.'))
    chevrons(s, ['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5'], L, 1.5, W, 0.6, active=[2], size=13)
    cw = (W - 4 * 0.06) / 5
    for i in range(5):
        x = L + i * (cw + 0.06)
        rect(s, x, 2.25, cw, 3.5, fill=LBLUE if i == 2 else LSAND)
        text(s, x + 0.2, 2.45, cw - 0.4, 2.2, bl(['Pain point', 'Pain point'], sa=6), size=14)
        harvey(s, x + 0.2, 5.2, 0.34, [1, 2, 4, 2, 1][i])
        text(s, x + 0.65, 5.22, cw - 0.8, 0.3, 'Impact', size=12, color=DGRAY)
    sowhat(s, KT)


# =====================================================================================
def s04(D):
    C = 'Buying center'
    divider(D, 4, 'Buying\ncenter', N('Buying center, stakeholders and value messages – mostly internal slides.',
                                       'Do not show slides marked “Internal” to the customer.',
                                       'Complex B2B decisions involve 6–10 people – each needs their own argument.'))
    s = cs(D, C, 'Roles (internal)', 'buyingcenter', N('Opportunity and account planning.', 'Add the names of the customer’s people per role.',
                                                       'Maintain the buying-center role per contact in the CRM.'), sticker_='Internal')
    oval(s, 5.37, 2.3, 2.6, fill=BLUE, content='Decision\n[Project]', size=17, color=WHITE, align='c', anchor='m')
    roles = [('Decision maker', 'person'), ('Budget owner', 'euro'), ('User / operations', 'engineering'),
             ('Quality', 'verified'), ('IT / OT', 'lan'), ('Procurement', 'shopping_cart')]
    cw, chh = 4.5, 1.25
    for i, (r, ic) in enumerate(roles):
        x = L if i < 3 else R - cw
        y = 1.5 + (i % 3) * (chh + 0.2)
        rect(s, x, y, cw, chh, fill=LSAND)
        icon(s, ic, x + 0.25, y + 0.25, 0.42, BLUE)
        label(s, x + 0.9, y + 0.22, cw - 1.1, r)
        text(s, x + 0.9, y + 0.5, cw - 1.1, 0.35, '[Name, function]', size=15)
        text(s, x + 0.9, y + 0.85, cw - 1.1, 0.35, '“Key question of this role?”', size=12, italic=True, color=DGRAY)

    s = cs(D, C, 'Stakeholder matrix (internal)', 'stakeholder', N('Stakeholder strategy.', 'Move the circles; colour = attitude towards Körber.'), sticker_='Internal')
    gx0, gy0, gw, gh = L + 0.55, 1.5, 7.0, 4.3
    for t, qx, qy in [('Keep satisfied', 0, 0), ('Manage closely', 1, 0), ('Monitor', 0, 1), ('Keep informed', 1, 1)]:
        rect(s, gx0 + qx * gw / 2, gy0 + qy * gh / 2, gw / 2 - 0.03, gh / 2 - 0.03, fill=LBLUE if (qx, qy) == (1, 0) else LSAND)
        text(s, gx0 + qx * gw / 2 + 0.15, gy0 + qy * gh / 2 + 0.1, 3, 0.3, t, size=12, color=BLUE)
    quad_axes(s, gx0, gy0, gw, gh, 'Interest', 'Influence')
    for t, px, py, c in [('[Name]', 1.4, 0.7, ORANGE), ('[Name]', 4.8, 0.9, BLUE), ('[Name]', 2.2, 3.0, STONE), ('[Name]', 5.1, 3.0, BLUE)]:
        oval(s, gx0 + px, gy0 + py, 0.42, fill=c)
        text(s, gx0 + px + 0.5, gy0 + py + 0.06, 1.6, 0.3, t, size=12)
    xr = 8.6; wr = R - xr
    label(s, xr, 1.5, wr, 'Attitude towards Körber')
    for i, (c, t) in enumerate([(BLUE, 'Supporter'), (STONE, 'Neutral'), (ORANGE, 'Critical')]):
        dot(s, xr, 1.9 + i * 0.4, 0.2, c); text(s, xr + 0.3, 1.86 + i * 0.4, 2, 0.3, t, size=12)
    label(s, xr, 3.3, wr, 'Next steps')
    text(s, xr, 3.65, wr, 2, bl(['Action per stakeholder', 'Action per stakeholder'], sa=6), size=14)

    s = cs(D, C, 'Relationship map (internal)', 'relmap', N('Customer org chart with relationship status.', 'Adapt boxes to the customer organisation; initials = Körber owner.'),
           sticker_='Internal')
    def ob(x, y, st, own=None):
        f = {'p': BLUE, 'n': SAND, 'c': ORANGE, 'u': WHITE}[st]
        rect(s, x, y, 2.3, 0.85, fill=f, line=STONE if st == 'u' else None, content=[{'t': '[Function]', 'size': 13}, {'t': '[Name]', 'size': 11}],
             color=WHITE if st in ('p', 'c') else BLACK, anchor='m', align='c')
        if own:
            oval(s, x + 2.05, y - 0.15, 0.38, fill=WHITE, line=BLUE, content=own, size=9, color=BLUE, align='c', anchor='m', margin=0)
    ob(5.52, 1.5, 'u')
    xs = [1.2, 4.0, 6.8, 9.6]
    hline(s, xs[0] + 1.15, 2.7, xs[3] - xs[0], STONE); vline(s, 6.67, 2.35, 0.35, STONE)
    for x, st, o in zip(xs, ['p', 'p', 'n', 'c'], ['AB', 'CD', None, 'EF']):
        vline(s, x + 1.15, 2.7, 0.3, STONE); ob(x, 3.0, st, o)
        vline(s, x + 1.15, 3.85, 0.35, STONE); ob(x, 4.2, 'n' if st != 'p' else 'u')
    for i, (c, t) in enumerate([(BLUE, 'Supporter'), (SAND, 'Neutral'), (ORANGE, 'Critical'), (WHITE, 'No contact')]):
        rect(s, L + i * 1.8, 5.6, 0.22, 0.22, fill=c, line=STONE if c == WHITE else None)
        text(s, L + i * 1.8 + 0.3, 5.56, 1.4, 0.3, t, size=11)

    s = cs(D, C, 'Value messages per role', 'valuemsg', N('Messaging matrix for proposals and follow-ups.', 'Back every message with a measurable KPI.',
                                                            'Same solution, different stories: the CFO buys payback, QA buys inspection readiness.'))
    rows = [['Role', 'Priority', 'Our value message', 'Proof / KPI']] + [[r, '[Priority]', '[Value message in one line]', '[KPI]']
                                                                         for r in ['Decision maker', 'Budget owner', 'Operations', 'Quality', 'IT / OT']]
    tb = table(s, L, 1.5, W, rows, colw=[2.4, 2.6, 5.0, 2.6], rowh=0.7, size=14)
    for r in range(1, 6):
        fill_tf(tb.cell(r, 3).text_frame, '[KPI]', size=14, color=BLUE)
