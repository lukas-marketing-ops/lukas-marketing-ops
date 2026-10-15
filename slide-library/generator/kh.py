# Körber slide helpers (python-pptx) – builds on the Körber 2025 master
import copy, json, os, re, uuid
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR as TC
from pptx.enum.shapes import MSO_SHAPE as SH, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.chart.data import CategoryChartData, XyChartData, BubbleChartData
from pptx.enum.chart import XL_CHART_TYPE as XCT, XL_LEGEND_POSITION, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'src')
TEMPLATE = os.environ.get('KOERBER_TEMPLATE', os.path.join(SRC, 'k2025.pptx'))


def template_media():
    """extract the template's media folder once (photos for covers and cases)"""
    import zipfile, tempfile
    d = os.path.join(tempfile.gettempdir(), 'koerber_template_media')
    if not os.path.isdir(d):
        with zipfile.ZipFile(TEMPLATE) as z:
            for n in z.namelist():
                if n.startswith('ppt/media/'):
                    z.extract(n, d)
    return os.path.join(d, 'ppt', 'media') + '/'
I = Inches

# ---------------------------------------------------------------- colours
# (theme colour, brightness) -> follows the Körber theme; hex strings only where theme can't be used
BLUE = (TC.ACCENT_1, 0)
LBLUE = (TC.ACCENT_1, 0.85)
MBLUE = (TC.ACCENT_1, 0.55)
BLACK = (TC.TEXT_1, 0)
DGRAY = (TC.TEXT_1, 0.35)      # secondary text
WHITE = (TC.BACKGROUND_1, 0)
SAND = (TC.BACKGROUND_2, 0)    # E6E2DC warm grey
LSAND = (TC.BACKGROUND_2, 0.55)
STONE = (TC.TEXT_2, 0)         # BFB8AF
TAUPE = (TC.ACCENT_3, 0)       # 9D968D
YELLOW = (TC.ACCENT_4, 0)      # CTA / highlight only
AMBER = (TC.ACCENT_5, 0)
ORANGE = (TC.ACCENT_6, 0)
HEX = {'blue': '0060FF', 'sand': 'E6E2DC', 'stone': 'BFB8AF', 'taupe': '9D968D', 'black': '000000',
       'amber': 'FEC037', 'orange': 'FE8623', 'yellow': 'FFE32F', 'grid': 'D9D5CF', 'dgray': '595959'}

# layout indices in Körber 2025
LY = dict(title_blue=1, title_img=2, title_grad=3, title_light=4, agenda_blue=10, agenda=8,
          section_grad=12, section_blue=13, section_img=14, section_hl_blue=18, section_name_blue=20,
          section_name=21, hl_dark=24, content=31, content_xl=32, content_blue=33, no_content=35,
          quote=73, quote_blue=74, end=76, end_contact=77, legal=78)

# content frame (inches)
L, R, T, B = 0.37, 12.97, 1.35, 6.62
W = R - L


def setc(cf, c):
    """apply colour spec to a ColorFormat"""
    if isinstance(c, tuple):
        cf.theme_color = c[0]
        if c[1]:
            cf.brightness = c[1]
    else:
        cf.rgb = RGBColor.from_string(c)


def _strip_style(shape):
    st = shape._element.find(qn('p:style'))
    if st is not None:
        shape._element.remove(st)


# ---------------------------------------------------------------- text
def _bullet(p, char='•', level=0, color=None):
    pPr = p._p.get_or_add_pPr()
    marL = int(I(0.18 + 0.2 * level))
    pPr.set('marL', str(marL)); pPr.set('indent', str(-int(I(0.18))))
    for tag in ('a:buNone', 'a:buChar', 'a:buAutoNum', 'a:buFont', 'a:buClr'):
        for e in pPr.findall(qn(tag)):
            pPr.remove(e)
    if color is not None:
        buClr = etree.SubElement(pPr, qn('a:buClr'))
        clr = etree.SubElement(buClr, qn('a:schemeClr')); clr.set('val', 'accent1')
    f = etree.SubElement(pPr, qn('a:buFont')); f.set('typeface', 'Arial')
    b = etree.SubElement(pPr, qn('a:buChar')); b.set('char', char)


def _nobullet(p):
    pPr = p._p.get_or_add_pPr()
    if pPr.find(qn('a:buNone')) is None and pPr.find(qn('a:buChar')) is None:
        etree.SubElement(pPr, qn('a:buNone'))


def fill_tf(tf, content, size=13, color=BLACK, bold=False, align='l', anchor='t', italic=False,
            space_after=4, line_spacing=None, caps=False, spacing=None, margin=None, wrap=True):
    """content: str ('\n' = paragraph), or list of paragraphs; paragraph = str | dict(t=str|[(txt,opts)], ...)"""
    txBody = tf._txBody
    ps = txBody.findall(qn('a:p'))
    for e in ps[1:]:
        txBody.remove(e)
    for e in list(ps[0]):
        if e.tag != qn('a:pPr'):
            ps[0].remove(e)
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    if margin is not None:
        m = margin if isinstance(margin, (tuple, list)) else (margin,) * 4
        tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = [I(v) for v in m]
    tf.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(content, str):
        content = content.split('\n')
    first = True
    for para in content:
        if not isinstance(para, dict):
            para = {'t': para}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        al = para.get('align', align)
        p.alignment = {'l': PP_ALIGN.LEFT, 'c': PP_ALIGN.CENTER, 'r': PP_ALIGN.RIGHT}[al]
        sa = para.get('sa', space_after)
        p.space_after = Pt(sa)
        if para.get('sb'):
            p.space_before = Pt(para['sb'])
        ls = para.get('ls', line_spacing)
        if ls:
            p.line_spacing = ls
        if para.get('bullet'):
            _bullet(p, para.get('char', '•'), para.get('level', 0), color=para.get('bcolor'))
        elif para.get('num'):
            pass
        else:
            _nobullet(p)
        runs = para['t']
        if isinstance(runs, str):
            runs = [(runs, {})]
        for txt, o in runs:
            r = p.add_run()
            r.text = txt.upper() if para.get('caps', caps) else txt
            f = r.font
            f.size = Pt(o.get('size', para.get('size', size)))
            f.bold = o.get('bold', para.get('bold', bold))
            f.italic = o.get('italic', para.get('italic', italic))
            setc(f.color, o.get('color', para.get('color', color)))
            sp = o.get('spacing', para.get('spacing', spacing))
            if sp:
                r._r.get_or_add_rPr().set('spc', str(int(sp * 100)))
    return tf


def text(s, x, y, w, h, content, **kw):
    tb = s.shapes.add_textbox(I(x), I(y), I(w), I(h))
    kw.setdefault('margin', 0)
    fill_tf(tb.text_frame, content, **kw)
    if kw.get('name'):
        tb.name = kw['name']
    return tb


def label(s, x, y, w, txt, color=BLUE, size=10, h=0.25, align='l'):
    """small uppercase Körber label"""
    return text(s, x, y, w, h, txt, size=size, color=color, caps=True, spacing=1, align=align)


def shape(s, kind, x, y, w, h, fill=None, line=None, lw=1.0, content=None, dash=None, **kw):
    sp = s.shapes.add_shape(kind, I(x), I(y), I(w), I(h))
    _strip_style(sp)
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); setc(sp.fill.fore_color, fill)
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.fill.solid(); setc(sp.line.color, line); sp.line.width = Pt(lw)
        if dash:
            sp.line.dash_style = dash
    if content is not None:
        kw.setdefault('margin', 0.1)
        fill_tf(sp.text_frame, content, **kw)
    return sp


def rect(s, x, y, w, h, fill=None, line=None, **kw):
    return shape(s, SH.RECTANGLE, x, y, w, h, fill, line, **kw)


def rrect(s, x, y, w, h, fill=None, line=None, radius=0.08, **kw):
    sp = shape(s, SH.ROUNDED_RECTANGLE, x, y, w, h, fill, line, **kw)
    sp.adjustments[0] = min(0.5, radius / min(w, h))
    return sp


def oval(s, x, y, d, fill=None, line=None, **kw):
    return shape(s, SH.OVAL, x, y, d, d, fill, line, **kw)


def hline(s, x, y, w, color=BLACK, lw=0.75):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x), I(y), I(x + w), I(y))
    _strip_style(c); c.line.fill.solid(); setc(c.line.color, color); c.line.width = Pt(lw)
    return c


def vline(s, x, y, h, color=BLACK, lw=0.75):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x), I(y), I(x), I(y + h))
    _strip_style(c); c.line.fill.solid(); setc(c.line.color, color); c.line.width = Pt(lw)
    return c


def arrow(s, x1, y1, x2, y2, color=TAUPE, lw=1.25):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
    _strip_style(c); c.line.fill.solid(); setc(c.line.color, color); c.line.width = Pt(lw)
    ln = c.line._get_or_add_ln()
    te = etree.SubElement(ln, qn('a:tailEnd')); te.set('type', 'triangle'); te.set('w', 'med'); te.set('len', 'med')
    return c


def num(s, x, y, n, d=0.42, filled=True, size=None, color=BLUE):
    """numbered circle – Körber circle motif"""
    size = size or (14 if d >= 0.4 else 11)
    if filled:
        return oval(s, x, y, d, fill=color, content=str(n), size=size, color=WHITE, align='c', anchor='m', margin=0)
    return oval(s, x, y, d, fill=WHITE, line=color, lw=1.25, content=str(n), size=size, color=color, align='c', anchor='m', margin=0)


def dot(s, x, y, d, color):
    return oval(s, x, y, d, fill=color)


def harvey(s, x, y, d, q):
    """Harvey ball, q in 0..4"""
    oval(s, x, y, d, fill=WHITE, line=BLUE, lw=1.25)
    if q >= 4:
        oval(s, x, y, d, fill=BLUE, line=BLUE, lw=1.25)
    elif q > 0:
        sp = s.shapes.add_shape(SH.PIE, I(x), I(y), I(d), I(d))
        _strip_style(sp); sp.fill.solid(); setc(sp.fill.fore_color, BLUE); sp.line.fill.background()
        sp.adjustments[0] = 270 * 0.6
        sp.adjustments[1] = ((270 + 90 * q) % 360) * 0.6
    return


def sticker(s, txt='Illustrativ'):
    """Körber sticker (tag) in the subtitle row, right aligned"""
    w = 0.22 + 0.095 * len(txt)
    sp = shape(s, SH.PENTAGON, R - w, 0.78, w, 0.26, fill=BLUE, content=txt, size=9, color=WHITE, caps=True,
               spacing=0.8, align='l', anchor='m', margin=(0.1, 0, 0.05, 0))
    sp.name = 'Sticker'
    return sp


def disturber(s, x, y, content, d=1.97, fill=BLUE, **kw):
    """CI blue disturber: perfect circle, 5 cm"""
    kw.setdefault('size', 14); kw.setdefault('color', WHITE if fill == BLUE else BLUE)
    sp = oval(s, x, y, d, fill=fill, content=content, align='c', anchor='m', margin=0.15, **kw)
    sp.name = 'Disturber'
    return sp


SOWHAT_Y = 5.98


def sowhat(s, txt, y=None, h=None, lead='So what'):
    """takeaway box – fixed position on every slide (content must end at 5.8)"""
    y, h = SOWHAT_Y, 0.62
    box = rect(s, L, y, W, h, fill=SAND)
    box.name = 'Kernaussage'
    oval(s, L + 0.15, y + (h - 0.36) / 2, 0.36, fill=BLUE)
    icon(s, 'arrow_forward', L + 0.21, y + (h - 0.24) / 2, 0.24, WHITE)
    text(s, L + 0.68, y, W - 0.85, h, [{'t': [(lead + ':  ', {'bold': True, 'color': BLUE}), (txt, {})]}],
         size=13, anchor='m')
    return box


# ---------------------------------------------------------------- icons (Material Symbols from v7 library)
_ICONS = json.load(open(os.path.join(HERE, 'icons.json')))
_NS = ('xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
       'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
       'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')


def icon(s, name, x, y, size=0.4, color=BLUE):
    xml = _ICONS[name]
    root = etree.fromstring('<root %s>%s</root>' % (_NS, xml))
    sp = root[0]
    tree = s.shapes._spTree
    nid = max([int(e.get('id')) for e in tree.iter(qn('p:cNvPr'))] + [1]) + 1
    sp.find('.//' + qn('p:cNvPr')).set('id', str(nid))
    off = sp.find('.//' + qn('a:off')); ext = sp.find('.//' + qn('a:ext'))
    off.set('x', str(int(I(x)))); off.set('y', str(int(I(y))))
    ext.set('cx', str(int(I(size)))); ext.set('cy', str(int(I(size))))
    sf = sp.find(qn('p:spPr')).find(qn('a:solidFill'))
    for c in list(sf):
        sf.remove(c)
    if isinstance(color, tuple):
        m = {TC.ACCENT_1: 'accent1', TC.TEXT_1: 'tx1', TC.BACKGROUND_1: 'bg1', TC.BACKGROUND_2: 'bg2', TC.TEXT_2: 'tx2',
             TC.ACCENT_3: 'accent3', TC.ACCENT_4: 'accent4', TC.ACCENT_5: 'accent5', TC.ACCENT_6: 'accent6'}
        e = etree.SubElement(sf, qn('a:schemeClr')); e.set('val', m[color[0]])
    else:
        e = etree.SubElement(sf, qn('a:srgbClr')); e.set('val', color)
    tree.append(sp)
    return sp


def icon_circle(s, name, x, y, d=0.62, fill=BLUE, color=WHITE, ratio=0.58):
    oval(s, x, y, d, fill=fill)
    isz = d * ratio
    icon(s, name, x + (d - isz) / 2, y + (d - isz) / 2, isz, color)


# ---------------------------------------------------------------- pictures
def picture(s, path, x, y, w, h):
    from PIL import Image
    im = Image.open(path)
    iw, ih = im.size
    pic = s.shapes.add_picture(path, I(x), I(y), I(w), I(h))
    tr, ir = w / h, iw / ih
    if ir > tr:
        c = (1 - tr / ir) / 2; pic.crop_left = c; pic.crop_right = c
    else:
        c = (1 - ir / tr) / 2; pic.crop_top = c; pic.crop_bottom = c
    return pic


def circle_picture(s, path, x, y, d):
    pic = picture(s, path, x, y, d, d)
    geom = pic._element.spPr.find(qn('a:prstGeom'))
    geom.set('prst', 'ellipse')
    return pic


# ---------------------------------------------------------------- tables (consulting style: keylines, no banding)
def _cell_border(cell, side, color=None, w=0.75):
    tcPr = cell._tc.get_or_add_tcPr()
    tag = {'L': 'a:lnL', 'R': 'a:lnR', 'T': 'a:lnT', 'B': 'a:lnB'}[side]
    for e in tcPr.findall(qn(tag)):
        tcPr.remove(e)
    ln = etree.Element(qn(tag))
    if color is None:
        ln.set('w', '0'); etree.SubElement(ln, qn('a:noFill'))
    else:
        ln.set('w', str(int(Pt(w)))); sf = etree.SubElement(ln, qn('a:solidFill'))
        c = etree.SubElement(sf, qn('a:srgbClr')); c.set('val', color)
    # schema order: lnL lnR lnT lnB ... fill
    order = ['a:lnL', 'a:lnR', 'a:lnT', 'a:lnB']
    idx = 0
    for i, t in enumerate(order):
        if t == tag:
            break
        if tcPr.find(qn(t)) is not None:
            idx = list(tcPr).index(tcPr.find(qn(t))) + 1
    tcPr.insert(idx, ln)


def table(s, x, y, w, data, colw=None, rowh=0.36, size=12, header=True, hcolor=BLUE, fills=None,
          aligns=None, bold_first_col=False, hsize=None, line='BFB8AF', valign='m', zebra=False, styles=None):
    """data: list of rows (strings or (str, opts)). fills: {(r,c): colour}."""
    nr, nc = len(data), len(data[0])
    gf = s.shapes.add_table(nr, nc, I(x), I(y), I(w), I(sum(rowh) if isinstance(rowh, list) else rowh * nr))
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    for a in ('firstRow', 'bandRow', 'firstCol', 'lastRow', 'lastCol', 'bandCol'):
        tblPr.set(a, '0')
    sid = tblPr.find(qn('a:tableStyleId'))
    if sid is not None:
        sid.text = '{2D5ABB26-0587-4C30-8999-92F81FD0307C}'  # No Style, No Grid
    colw = colw or [w / nc] * nc
    tot = sum(colw)
    for i, cw in enumerate(colw):
        tbl.columns[i].width = I(w * cw / tot)
    for r in range(nr):
        tbl.rows[r].height = I(rowh if not isinstance(rowh, list) else rowh[r])
        for c in range(nc):
            cell = tbl.cell(r, c)
            v = data[r][c]
            o = {}
            if isinstance(v, tuple):
                v, o = v
            ishead = header and r == 0
            col = o.get('color', hcolor if ishead else BLACK)
            al = o.get('align', (aligns[c] if aligns else 'l'))
            cell.margin_left = I(0.08); cell.margin_right = I(0.08); cell.margin_top = I(0.03); cell.margin_bottom = I(0.03)
            cell.vertical_anchor = {'t': MSO_ANCHOR.TOP, 'm': MSO_ANCHOR.MIDDLE, 'b': MSO_ANCHOR.BOTTOM}[valign]
            fill_tf(cell.text_frame, v, size=o.get('size', (hsize or size) if ishead else size), color=col,
                    bold=o.get('bold', (bold_first_col and c == 0 and not ishead)), align=al, anchor=valign, space_after=0)
            f = (fills or {}).get((r, c)) or o.get('fill')
            if f is None and zebra and not ishead and r % 2 == 0:
                f = LSAND
            if f is not None:
                cell.fill.solid(); setc(cell.fill.fore_color, f)
            else:
                cell.fill.background()
            for sd in 'LR':
                _cell_border(cell, sd, None)
            _cell_border(cell, 'T', None)
            if ishead:
                _cell_border(cell, 'B', '000000', 1.0)
            else:
                _cell_border(cell, 'B', line, 0.5)
    return tbl


# ---------------------------------------------------------------- charts
def _fmt_axis_text(ax, size=11):
    ax.tick_labels.font.size = Pt(size)
    setc(ax.tick_labels.font.color, BLACK)


def _axis_line(ax, color='9D968D', visible=True):
    ax.format.line.fill.solid() if visible else ax.format.line.fill.background()
    if visible:
        ax.format.line.color.rgb = RGBColor.from_string(color); ax.format.line.width = Pt(0.75)


def bar(s, x, y, w, h, cats, series, kind='col', stacked=False, pct=False, colors=None, labels=True,
        fmt='0', legend=None, gap=60, overlap=None, highlight=None, val_axis=False, size=11, label_pos=None,
        point_colors=None, max_=None, min_=None, title=None):
    t = {('col', False, False): XCT.COLUMN_CLUSTERED, ('col', True, False): XCT.COLUMN_STACKED,
         ('col', True, True): XCT.COLUMN_STACKED_100, ('bar', False, False): XCT.BAR_CLUSTERED,
         ('bar', True, False): XCT.BAR_STACKED, ('bar', True, True): XCT.BAR_STACKED_100}[(kind, stacked, pct)]
    cd = CategoryChartData(); cd.categories = cats
    for n, v in series:
        cd.add_series(n, v)
    gf = s.shapes.add_chart(t, I(x), I(y), I(w), I(h), cd)
    ch = gf.chart
    ch.font.size = Pt(size)
    setc(ch.font.color, BLACK)
    ch.has_title = bool(title)
    if title:
        ch.chart_title.text_frame.text = title
        ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(12)
    colors = colors or [BLUE, STONE, SAND, TAUPE, BLACK, LBLUE]
    plot = ch.plots[0]
    plot.gap_width = gap
    if overlap is not None:
        plot.overlap = overlap
    elif stacked:
        plot.overlap = 100
    for i, ser in enumerate(plot.series):
        ser.format.fill.solid(); setc(ser.format.fill.fore_color, colors[i % len(colors)])
        ser.format.line.fill.background()
        ser.invert_if_negative = False
    if point_colors:
        for i, c in enumerate(point_colors):
            if c is not None:
                pt = plot.series[0].points[i]
                pt.format.fill.solid(); setc(pt.format.fill.fore_color, c)
    if highlight is not None:
        ser = plot.series[0]
        for i in range(len(cats)):
            pt = ser.points[i]; pt.format.fill.solid()
            setc(pt.format.fill.fore_color, BLUE if i in (highlight if isinstance(highlight, (list, tuple)) else [highlight]) else STONE)
    if labels:
        plot.has_data_labels = True
        dl = plot.data_labels
        dl.number_format = fmt; dl.number_format_is_linked = False
        dl.font.size = Pt(size)
        if label_pos:
            dl.position = label_pos
        elif not stacked:
            dl.position = XL_LABEL_POSITION.OUTSIDE_END
        else:
            dl.position = XL_LABEL_POSITION.CENTER
        if stacked:
            for i, ser in enumerate(plot.series):
                c = colors[i % len(colors)]
                ser.data_labels.font.size = Pt(size)
                ser.data_labels.number_format = fmt; ser.data_labels.number_format_is_linked = False
                ser.data_labels.position = XL_LABEL_POSITION.CENTER
                ser.data_labels.show_value = True
                setc(ser.data_labels.font.color, WHITE if c in (BLUE, BLACK, TAUPE) else BLACK)
    va = ch.value_axis; ca = ch.category_axis
    va.has_major_gridlines = False; va.has_minor_gridlines = False
    if max_ is not None:
        va.maximum_scale = max_
    if min_ is not None:
        va.minimum_scale = min_
    va.visible = val_axis
    if val_axis:
        _fmt_axis_text(va, size); va.format.line.fill.background()
        va.has_major_gridlines = True
        va.major_gridlines.format.line.color.rgb = RGBColor.from_string(HEX['grid']); va.major_gridlines.format.line.width = Pt(0.5)
        va.tick_labels.number_format = fmt; va.tick_labels.number_format_is_linked = False
    ca.major_tick_mark = XL_TICK_MARK.NONE
    _fmt_axis_text(ca, size); _axis_line(ca)
    if kind == 'bar':
        ca.reverse_order = True
        if not val_axis:
            pass
    ch.has_legend = bool(legend)
    if legend:
        ch.legend.position = {'b': XL_LEGEND_POSITION.BOTTOM, 't': XL_LEGEND_POSITION.TOP, 'r': XL_LEGEND_POSITION.RIGHT}[legend]
        ch.legend.include_in_layout = False
        ch.legend.font.size = Pt(size)
    return ch


def line_chart(s, x, y, w, h, cats, series, colors=None, fmt='0', labels='last', legend='b', size=11,
               widths=None, dashes=None, markers=True, val_axis=True, min_=None, max_=None, smooth=False):
    cd = CategoryChartData(); cd.categories = cats
    for n, v in series:
        cd.add_series(n, v)
    gf = s.shapes.add_chart(XCT.LINE_MARKERS if markers else XCT.LINE, I(x), I(y), I(w), I(h), cd)
    ch = gf.chart; ch.font.size = Pt(size); setc(ch.font.color, BLACK)
    colors = colors or [BLUE, TAUPE, STONE, BLACK]
    for i, ser in enumerate(ch.plots[0].series):
        c = colors[i % len(colors)]
        ser.format.line.fill.solid(); setc(ser.format.line.color, c)
        ser.format.line.width = Pt((widths or [2.5, 1.75, 1.75, 1.75])[i % 4])
        ser.smooth = smooth
        if dashes and dashes[i]:
            ser.format.line.dash_style = dashes[i]
        if markers:
            ser.marker.style = 8  # circle
            ser.marker.size = 6
            ser.marker.format.fill.solid(); setc(ser.marker.format.fill.fore_color, c)
            ser.marker.format.line.fill.background()
        if labels == 'all':
            ser.data_labels.show_value = True
            ser.data_labels.number_format = fmt; ser.data_labels.number_format_is_linked = False
            ser.data_labels.position = XL_LABEL_POSITION.ABOVE; ser.data_labels.font.size = Pt(size)
        elif labels == 'last':
            pt = ser.points[len(cats) - 1]
            pt.data_label.has_text_frame = False
            pt.data_label.position = XL_LABEL_POSITION.RIGHT
            dl = pt.data_label._get_or_add_dLbl()
            for tag, val in (('c:numFmt', None),):
                pass
            sv = dl.find(qn('c:showVal'))
            if sv is None:
                sv = etree.SubElement(dl, qn('c:showVal'))
            sv.set('val', '1')
            pt.data_label.font.size = Pt(size); pt.data_label.font.bold = True
            setc(pt.data_label.font.color, c)
    va = ch.value_axis; ca = ch.category_axis
    va.visible = val_axis
    va.has_major_gridlines = val_axis
    if val_axis:
        va.major_gridlines.format.line.color.rgb = RGBColor.from_string(HEX['grid']); va.major_gridlines.format.line.width = Pt(0.5)
        va.format.line.fill.background(); _fmt_axis_text(va, size)
        va.tick_labels.number_format = fmt; va.tick_labels.number_format_is_linked = False
    if min_ is not None:
        va.minimum_scale = min_
    if max_ is not None:
        va.maximum_scale = max_
    ca.major_tick_mark = XL_TICK_MARK.NONE; _fmt_axis_text(ca, size); _axis_line(ca)
    ch.has_legend = bool(legend)
    if legend:
        ch.legend.position = {'b': XL_LEGEND_POSITION.BOTTOM, 't': XL_LEGEND_POSITION.TOP, 'r': XL_LEGEND_POSITION.RIGHT}[legend]
        ch.legend.include_in_layout = False; ch.legend.font.size = Pt(size)
    return ch


def doughnut(s, x, y, d, vals, colors=None, hole=72, labels=False, size=11, cats=None):
    cd = CategoryChartData(); cd.categories = cats or [str(i) for i in range(len(vals))]
    cd.add_series('S', vals)
    gf = s.shapes.add_chart(XCT.DOUGHNUT, I(x), I(y), I(d), I(d), cd)
    ch = gf.chart; ch.has_legend = False; ch.has_title = False; ch.font.size = Pt(size)
    colors = colors or [BLUE, SAND, STONE, TAUPE, BLACK]
    ser = ch.plots[0].series[0]
    for i in range(len(vals)):
        pt = ser.points[i]; pt.format.fill.solid(); setc(pt.format.fill.fore_color, colors[i % len(colors)])
        pt.format.line.fill.solid(); pt.format.line.color.rgb = RGBColor(255, 255, 255); pt.format.line.width = Pt(1.5)
    # hole size
    dn = ch._chartSpace.find('.//' + qn('c:doughnutChart'))
    hs = dn.find(qn('c:holeSize'))
    if hs is None:
        hs = etree.SubElement(dn, qn('c:holeSize'))
    hs.set('val', str(hole))
    if labels:
        ch.plots[0].has_data_labels = True
        ch.plots[0].data_labels.number_format = '0%'; ch.plots[0].data_labels.number_format_is_linked = False
    return ch


def scatter(s, x, y, w, h, series, colors=None, size=11, xfmt='0', yfmt='0', bubble=False, xtitle=None, ytitle=None,
            xmin=None, xmax=None, ymin=None, ymax=None, labels=None, bubble_scale=60):
    if bubble:
        cd = BubbleChartData()
        for n, pts in series:
            sr = cd.add_series(n)
            for px, py, pz in pts:
                sr.add_data_point(px, py, pz)
        gf = s.shapes.add_chart(XCT.BUBBLE, I(x), I(y), I(w), I(h), cd)
    else:
        cd = XyChartData()
        for n, pts in series:
            sr = cd.add_series(n)
            for px, py in pts:
                sr.add_data_point(px, py)
        gf = s.shapes.add_chart(XCT.XY_SCATTER, I(x), I(y), I(w), I(h), cd)
    ch = gf.chart; ch.font.size = Pt(size); setc(ch.font.color, BLACK)
    ch.has_title = False
    colors = colors or [BLUE, TAUPE, STONE, BLACK]
    for i, ser in enumerate(ch.plots[0].series):
        c = colors[i % len(colors)]
        if bubble:
            ser.format.fill.solid(); setc(ser.format.fill.fore_color, c)
            ser.format.line.fill.background()
        else:
            ser.format.line.fill.background()
            ser.marker.style = 8; ser.marker.size = 11
            ser.marker.format.fill.solid(); setc(ser.marker.format.fill.fore_color, c)
            ser.marker.format.line.fill.background()
    if bubble:
        bc = ch._chartSpace.find('.//' + qn('c:bubbleChart'))
        bs = bc.find(qn('c:bubbleScale'))
        if bs is None:
            bs = etree.SubElement(bc, qn('c:bubbleScale'))
        bs.set('val', str(bubble_scale))
    va, ca = ch.value_axis, ch.category_axis
    for ax, fmt, mn, mx, ttl in ((va, yfmt, ymin, ymax, ytitle), (ca, xfmt, xmin, xmax, xtitle)):
        ax.has_major_gridlines = False
        _fmt_axis_text(ax, size); _axis_line(ax)
        ax.tick_labels.number_format = fmt; ax.tick_labels.number_format_is_linked = False
        ax.major_tick_mark = XL_TICK_MARK.NONE
        if mn is not None: ax.minimum_scale = mn
        if mx is not None: ax.maximum_scale = mx
        if ttl:
            ax.has_title = True; ax.axis_title.text_frame.text = ttl
            r = ax.axis_title.text_frame.paragraphs[0].runs[0]; r.font.size = Pt(size); r.font.bold = False
    ch.has_legend = len(series) > 1
    if ch.has_legend:
        ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(size)
    return ch


# ---------------------------------------------------------------- deck
class Deck:
    def __init__(self, template):
        self.prs = Presentation(template)
        lst = self.prs.slides._sldIdLst
        for sid in list(lst):
            self.prs.part.drop_rel(sid.rId); lst.remove(sid)
        self.sections = []  # (name, [slides])
        self.keys = {}
        self.warn = []

    def section(self, name):
        self.sections.append((name, []))

    def slide(self, layout='content', title=None, sub=None, source=None, notes=None, key=None, sticker_=None):
        lay = self.prs.slide_layouts[LY[layout] if isinstance(layout, str) else layout]
        s = self.prs.slides.add_slide(lay)
        self.sections[-1][1].append(s)
        ph = {p.placeholder_format.idx: p for p in s.placeholders}
        if title is not None and 0 in ph:
            ph[0].text_frame.text = title
            if layout in ('content', 'content_blue') and len(title) > 76:
                self.warn.append('LONG TITLE (%d): %s' % (len(title), title))
        if sub is not None and 14 in ph:
            ph[14].text_frame.text = sub
        if source is not None and 20 in ph:
            ph[20].text_frame.text = source
        # remove unused empty text placeholders that would show prompts (keep footer/date/number)
        if notes:
            s.notes_slide.notes_text_frame.text = notes
        if key:
            self.keys[key] = s
        if sticker_:
            sticker(s, sticker_)
        return s

    def ph(self, s, idx, content, **kw):
        p = {p.placeholder_format.idx: p for p in s.placeholders}[idx]
        if isinstance(content, str) and not kw:
            p.text_frame.text = content
        else:
            fill_tf(p.text_frame, content, **kw)
        return p

    def drop_empty(self, s, keep=(20, 21, 22, 23, 24)):
        for p in list(s.placeholders):
            idx = p.placeholder_format.idx
            if idx in keep:
                continue
            if p.has_text_frame and not p.text_frame.text.strip():
                p._element.getparent().remove(p._element)

    def number(self, s):
        return list(self.prs.slides).index(s) + 1

    def save(self, path):
        # sections (p14:sectionLst)
        pres = self.prs.part._element
        ids = {s.slide_id: s for s in self.prs.slides}
        extLst = pres.find(qn('p:extLst'))
        if extLst is None:
            extLst = etree.SubElement(pres, qn('p:extLst'))
        for e in list(extLst):
            if e.get('uri') == '{521415D9-36F7-43E2-AB2F-B90AF26B5E84}':
                extLst.remove(e)
        P14 = 'http://schemas.microsoft.com/office/powerpoint/2010/main'
        ext = etree.Element(qn('p:ext')); ext.set('uri', '{521415D9-36F7-43E2-AB2F-B90AF26B5E84}')
        sl = etree.SubElement(ext, '{%s}sectionLst' % P14, nsmap={'p14': P14})
        for name, slides in self.sections:
            sec = etree.SubElement(sl, '{%s}section' % P14)
            sec.set('name', name); sec.set('id', '{%s}' % str(uuid.uuid4()).upper())
            l = etree.SubElement(sec, '{%s}sldIdLst' % P14)
            for s in slides:
                e = etree.SubElement(l, '{%s}sldId' % P14); e.set('id', str(s.slide_id))
        extLst.insert(0, ext)
        self.prs.save(path)


# ---------------------------------------------------------------- patterns
def bl(items, size=None, **kw):
    """bullet paragraphs"""
    out = []
    for it in items:
        d = {'t': it, 'bullet': True, 'sa': kw.get('sa', 4)}
        if size: d['size'] = size
        out.append(d)
    return out


def colhead(s, x, y, w, lab=None, head=None, body=None, icon_=None, n=None, hsize=17, bsize=12, bh=1.6, line=BLACK):
    """Körber keyline column: icon/number, keyline, label, heading, body"""
    yy = y
    if icon_:
        icon(s, icon_, x, yy, 0.42, BLUE); yy += 0.6
    if n is not None:
        num(s, x, yy, n); yy += 0.6
    hline(s, x, yy, w, line, 0.75); yy += 0.12
    if lab:
        label(s, x, yy, w, lab); yy += 0.3
    if head:
        nl = head.count('\n') + 1
        text(s, x, yy, w, 0.32 * nl + 0.05, head, size=hsize); yy += 0.32 * nl + 0.12
    if body:
        text(s, x, yy, w, bh, body, size=bsize)
    return yy


def chevrons(s, items, x, y, w, h=0.55, active=None, size=12, gap=0.06, done=None):
    n = len(items); cw = (w - gap * (n - 1)) / n
    for i, t in enumerate(items):
        kind = SH.PENTAGON if i == 0 else SH.CHEVRON
        on = (active is None) or (i == active) or (isinstance(active, (list, tuple)) and i in active)
        fill = BLUE if on else SAND
        sp = shape(s, kind, x + i * (cw + gap), y, cw + (0.18 if i < n - 1 else 0), h, fill=fill,
                   content=t, size=size, color=WHITE if on else BLACK, align='c', anchor='m', margin=(0.08, 0.02, 0.04, 0.02))
        try:
            sp.adjustments[0] = min(0.5, 0.22 / h * h / (cw) * 2) if False else sp.adjustments[0]
        except Exception:
            pass
    return cw


def card(s, x, y, w, h, head=None, body=None, fill=LSAND, icon_=None, lab=None, hsize=15, bsize=12, hcolor=BLACK, bcolor=BLACK, pad=0.22):
    rect(s, x, y, w, h, fill=fill)
    yy = y + pad
    if icon_:
        icon(s, icon_, x + pad, yy, 0.4, BLUE if fill not in (BLUE,) else WHITE); yy += 0.55
    if lab:
        label(s, x + pad, yy, w - 2 * pad, lab, color=BLUE if fill != BLUE else WHITE); yy += 0.28
    if head:
        nl = head.count('\n') + 1
        text(s, x + pad, yy, w - 2 * pad, 0.28 * nl + 0.06, head, size=hsize, color=hcolor); yy += 0.28 * nl + 0.14
    if body:
        text(s, x + pad, yy, w - 2 * pad, max(0.3, y + h - yy - pad / 2), body, size=bsize, color=bcolor)
    return yy


def kpi(s, x, y, w, big, lab, sub=None, color=BLUE, bigsize=36, line=True):
    if line:
        hline(s, x, y, w, BLACK, 0.75)
    text(s, x, y + 0.12, w, 0.7, big, size=bigsize, color=color)
    text(s, x, y + 0.12 + bigsize / 72 * 1.25, w, 0.5, lab, size=12)
    if sub:
        text(s, x, y + 0.12 + bigsize / 72 * 1.25 + 0.42, w, 0.4, sub, size=10, color=DGRAY)


def rag(s, x, y, status, d=0.2):
    c = {'g': BLUE, 'y': AMBER, 'r': ORANGE, 'n': STONE}[status]
    return dot(s, x, y, d, c)


def legend_rag(s, x, y, size=10):
    for i, (st, t) in enumerate([('g', 'Im Plan'), ('y', 'Gefährdet'), ('r', 'Kritisch'), ('n', 'Nicht gestartet')]):
        rag(s, x + i * 1.45, y + 0.03, st, 0.16)
        text(s, x + i * 1.45 + 0.24, y, 1.2, 0.25, t, size=size)


def waterfall(s, x, y, w, h, cats, vals, totals, fmt='{:+.1f}', tfmt='{:.1f}', size=11, colors=None):
    """totals: indices that are absolute bars; vals for totals = absolute value, else delta"""
    base, up, down, tot = [], [], [], []
    run = 0
    for i, v in enumerate(vals):
        if i in totals:
            base.append(0); tot.append(v); up.append(0); down.append(0); run = v
        else:
            if v >= 0:
                base.append(run); up.append(v); down.append(0); run += v
            else:
                run += v; base.append(run); down.append(-v); up.append(0)
            tot.append(0)
    cd = CategoryChartData(); cd.categories = cats
    for n, v in (('Basis', base), ('Summe', tot), ('Zunahme', up), ('Abnahme', down)):
        cd.add_series(n, v)
    gf = s.shapes.add_chart(XCT.COLUMN_STACKED, I(x), I(y), I(w), I(h), cd)
    ch = gf.chart; ch.font.size = Pt(size); setc(ch.font.color, BLACK); ch.has_legend = False
    plot = ch.plots[0]; plot.gap_width = 45; plot.overlap = 100
    cols = colors or [None, BLUE, STONE, BLACK]
    for i, ser in enumerate(plot.series):
        if cols[i] is None:
            ser.format.fill.background(); ser.format.line.fill.background()
        else:
            ser.format.fill.solid(); setc(ser.format.fill.fore_color, cols[i]); ser.format.line.fill.background()
    for i, v in enumerate(vals):
        si = 1 if i in totals else (2 if v >= 0 else 3)
        dl = plot.series[si].points[i].data_label
        dl.has_text_frame = True
        dl.text_frame.text = (tfmt if i in totals else fmt).format(v).replace('.', ',')
        dl.position = XL_LABEL_POSITION.INSIDE_END if i in totals else XL_LABEL_POSITION.CENTER
        r = dl.text_frame.paragraphs[0].runs[0]; r.font.size = Pt(size)
        setc(r.font.color, WHITE if si in (1, 3) else BLACK)
    va = ch.value_axis; va.visible = False; va.has_major_gridlines = False
    ca = ch.category_axis; ca.major_tick_mark = XL_TICK_MARK.NONE; _fmt_axis_text(ca, size); _axis_line(ca)
    return ch


def gantt(s, x, y, w, rows, months, lab_w=3.0, rowh=0.42, size=12):
    """rows: (label, start, end, kind) with start/end in month units (0-based, float); kind 'bar'|'ms'|'hl'"""
    gx = x + lab_w; gw = w - lab_w; mw = gw / len(months)
    for i, m in enumerate(months):
        text(s, gx + i * mw, y, mw, 0.3, m, size=11, align='c', color=DGRAY)
    hline(s, x, y + 0.35, w, BLACK, 0.75)
    for i in range(len(months) + 1):
        vline(s, gx + i * mw, y + 0.35, rowh * len(rows) + 0.1, 'E6E2DC', 0.5)
    for j, (lab, a, b, kind) in enumerate(rows):
        yy = y + 0.45 + j * rowh
        text(s, x, yy, lab_w - 0.1, rowh, lab, size=size, anchor='m')
        if kind == 'ms':
            d = 0.24
            sp = shape(s, SH.DIAMOND, gx + a * mw - d / 2, yy + (rowh - d) / 2, d, d, fill=BLACK)
        else:
            rect(s, gx + a * mw + 0.02, yy + 0.09, (b - a) * mw - 0.04, rowh - 0.18, fill=BLUE if kind == 'hl' else STONE)
    return y + 0.45 + len(rows) * rowh


def elbow(s, x1, y1, x2, y2, color=TAUPE, lw=1.0, head=True):
    c = s.shapes.add_connector(MSO_CONNECTOR.ELBOW, I(x1), I(y1), I(x2), I(y2))
    _strip_style(c); c.line.fill.solid(); setc(c.line.color, color); c.line.width = Pt(lw)
    if head:
        ln = c.line._get_or_add_ln()
        te = etree.SubElement(ln, qn('a:tailEnd')); te.set('type', 'triangle'); te.set('w', 'med'); te.set('len', 'med')
    return c
