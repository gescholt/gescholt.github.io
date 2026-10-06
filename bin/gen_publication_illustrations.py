"""Generate the per-publication SVG illustrations in _includes/publication_preview/.

Usage: python3 bin/gen_publication_illustrations.py _includes/publication_preview
"""
import math, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

STYLE = """<style>
.pi-bg{fill:color-mix(in srgb,var(--global-theme-color,#2458b3) 7%,transparent)}
.pi-ink{fill:none;stroke:var(--global-text-color,#333);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.pi-soft{fill:none;stroke:var(--global-text-color-light,#828282);stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round;opacity:.55}
.pi-acc{fill:none;stroke:var(--global-theme-color,#2458b3);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.pi-dot{fill:var(--global-theme-color,#2458b3);stroke:var(--global-bg-color,#fff);stroke-width:1.5}
.pi-pt{fill:var(--global-text-color,#333)}
.pi-wash{fill:color-mix(in srgb,var(--global-theme-color,#2458b3) 18%,transparent)}
.pi-txt{fill:var(--global-text-color-light,#828282);font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;opacity:.8}
</style>"""


def svg(name, title, body):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="{title}">\n'
           f'<title>{title}</title>\n{STYLE}\n<rect class="pi-bg" width="200" height="200" rx="14"/>\n{body}\n</svg>\n')
    with open(os.path.join(OUT, name), "w") as f:
        f.write(doc)
    print("wrote", name)


def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def poly(pts):
    return " ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)


def path(pts):
    return "M" + " L".join(f"{fmt(x)} {fmt(y)}" for x, y in pts)


# 1. Tropical resultants: two tropical lines meet in exactly one point; Sylvester band in the corner.
def tropical():
    b = []
    for (vx, vy) in [(70, 120), (145, 75)]:
        b.append(f'<polyline class="pi-ink" points="{poly([(12, vy), (vx, vy), (vx, 188)])}"/>')
        t = min(188 - vx, vy - 12)
        b.append(f'<line class="pi-ink" x1="{vx}" y1="{vy}" x2="{vx + t}" y2="{vy - t}"/>')
    # Sylvester matrix band pattern (4x4): filled = nonzero coefficient
    rows = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 1, 1, 1]]
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            cx, cy = 26 + 10 * j, 26 + 10 * i
            if v:
                b.append(f'<circle class="pi-pt" cx="{cx}" cy="{cy}" r="2.4" opacity=".55"/>')
            else:
                b.append(f'<circle class="pi-soft" cx="{cx}" cy="{cy}" r="2"/>')
    b.append('<circle class="pi-dot" cx="115" cy="75" r="5"/>')
    svg("HONG2017285.svg", "Two tropical lines meeting in a single point, with a Sylvester matrix band", "\n".join(b))


# 2. Semi-inverted linear space: a line becomes a hyperbola after inverting one coordinate.
def semi_inverted():
    cx, cy, s = 100, 100, 30
    X = lambda u: cx + s * u
    Y = lambda y: cy - s * y
    lim = 3.0
    b = []
    b.append(f'<line class="pi-soft" x1="{X(-lim)}" y1="{Y(0)}" x2="{X(lim)}" y2="{Y(0)}"/>')
    b.append(f'<line class="pi-soft" x1="{X(0)}" y1="{Y(lim)}" x2="{X(0)}" y2="{Y(-lim)}"/>')
    b.append(f'<line class="pi-soft" stroke-dasharray="3 3" x1="{X(-lim)}" y1="{Y(1)}" x2="{X(lim)}" y2="{Y(1)}"/>')
    # original line x + y = 1
    b.append(f'<line class="pi-soft" stroke-dasharray="5 4" x1="{X(-2)}" y1="{Y(3)}" x2="{X(3)}" y2="{Y(-2)}"/>')
    # generic line y = u - 1.5 meeting the hyperbola in two real points
    b.append(f'<line class="pi-soft" x1="{X(-1.5)}" y1="{Y(-3)}" x2="{X(3)}" y2="{Y(1.5)}"/>')

    def branch(us):
        pts = []
        for u in us:
            y = 1 - 1 / u
            if -lim <= y <= lim:
                pts.append((X(u), Y(y)))
        return pts

    n = 80
    pos = branch([0.2 + (lim - 0.2) * i / n for i in range(n + 1)])
    neg = branch([-lim + (lim - 0.2) * i / n for i in range(n + 1)])
    b.append(f'<path class="pi-acc" d="{path(pos)}"/>')
    b.append(f'<path class="pi-acc" d="{path(neg)}"/>')
    for u in (2.0, 0.5):
        b.append(f'<circle class="pi-dot" cx="{fmt(X(u))}" cy="{fmt(Y(1 - 1 / u))}" r="4.5"/>')
    svg("Vinzant_scholten.svg",
        "A line inverted in one coordinate becomes a hyperbola whose intersections with lines are all real",
        "\n".join(b))


# 3. Log-concave MLE: tent-shaped log-density over data points, exponentiated to a density.
def logconcave():
    base = 166
    xs = [30, 55, 85, 110, 140, 170]
    hs = [0, 38, 60, 62, 45, 0]

    def h(x):
        for i in range(len(xs) - 1):
            if xs[i] <= x <= xs[i + 1]:
                t = (x - xs[i]) / (xs[i + 1] - xs[i])
                return hs[i] + t * (hs[i + 1] - hs[i])
        return 0

    k, amp = 22.0, 92.0
    mx = math.exp(max(hs) / k)
    pts = []
    n = 140
    for i in range(n + 1):
        x = xs[0] + (xs[-1] - xs[0]) * i / n
        pts.append((x, base - amp * math.exp(h(x) / k) / mx))
    b = []
    b.append(f'<line class="pi-soft" x1="16" y1="{base}" x2="184" y2="{base}"/>')
    b.append(f'<path class="pi-wash" d="{path(pts)} L{xs[-1]} {base} L{xs[0]} {base} Z"/>')
    b.append(f'<polyline class="pi-ink" stroke-dasharray="4 3" points="{poly([(x, base - hh) for x, hh in zip(xs, hs)])}"/>')
    b.append(f'<path class="pi-acc" d="{path(pts)}"/>')
    for x in xs:
        b.append(f'<circle class="pi-pt" cx="{x}" cy="{base}" r="3"/>')
    svg("GROSDOS2023102448.svg",
        "A tent-shaped log-density over data points and its exponential, the log-concave maximum likelihood estimate",
        "\n".join(b))


# 4. Sparse moments: coalescent genealogy over a piecewise-constant population history.
def coalescent():
    b = []
    base = 172
    x0, x1 = 25, 175
    steps = [(25, 70, 22), (70, 115, 50), (115, 175, 34)]
    top = [(x0, base)]
    for a, c, hh in steps:
        top += [(a, base - hh), (c, base - hh)]
    top.append((x1, base))
    b.append(f'<path class="pi-wash" d="{path(top)} Z"/>')
    b.append(f'<polyline class="pi-acc" points="{poly(top[1:-1])}"/>')
    b.append(f'<line class="pi-soft" x1="16" y1="{base}" x2="184" y2="{base}"/>')
    # tree: tips at left (present), root at right (past)
    tips = [32, 48, 64, 80, 96]

    def elbow(xa, ya, xb, yb):
        return f'<polyline class="pi-ink" points="{poly([(xa, ya), (xb, ya), (xb, yb)])}"/>'

    nodes = []
    b.append(elbow(25, 32, 55, 40)); b.append(elbow(25, 48, 55, 40)); nodes.append((55, 40))
    b.append(elbow(25, 80, 80, 88)); b.append(elbow(25, 96, 80, 88)); nodes.append((80, 88))
    b.append(elbow(55, 40, 100, 52)); b.append(elbow(25, 64, 100, 52)); nodes.append((100, 52))
    b.append(elbow(100, 52, 150, 70)); b.append(elbow(80, 88, 150, 70)); nodes.append((150, 70))
    b.append(f'<line class="pi-ink" x1="150" y1="70" x2="{x1}" y2="70"/>')
    for x, y in nodes:
        b.append(f'<circle class="pi-dot" cx="{x}" cy="{y}" r="4"/>')
    for y in tips:
        b.append(f'<circle class="pi-pt" cx="25" cy="{y}" r="2.4"/>')
    svg("Rosen2022.svg", "A coalescent genealogy above a piecewise-constant population history", "\n".join(b))


# 5. Morse minimizers: level sets inside a box with minima and saddles marked.
def morse():
    b = []
    b.append('<rect class="pi-ink" x="15" y="15" width="170" height="170" rx="4"/>')
    b.append('<rect class="pi-soft" x="24" y="24" width="152" height="152" rx="44"/>')
    minima = [((60, 70), [(12, 9), (24, 18), (36, 27)], -20),
              ((135, 60), [(10, 13), (20, 26), (30, 38)], 30),
              ((100, 140), [(14, 10), (28, 20), (42, 30)], 10)]
    for (cx, cy), radii, rot in minima:
        for rx, ry in radii:
            b.append(f'<ellipse class="pi-soft" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})"/>')
    for sx, sy in [(97, 62), (78, 108), (122, 102)]:
        b.append(f'<path class="pi-ink" d="M{sx - 3.5} {sy - 3.5} L{sx + 3.5} {sy + 3.5} M{sx - 3.5} {sy + 3.5} L{sx + 3.5} {sy - 3.5}"/>')
    for (cx, cy), _, _ in minima:
        b.append(f'<circle class="pi-dot" cx="{cx}" cy="{cy}" r="5"/>')
    svg("safey2026probabilistic.svg", "Level sets of a Morse function on a box, with its local minima and saddles marked", "\n".join(b))


# 6. Lotka–Volterra: trajectory spiralling into a feasible, stable equilibrium; sign pattern in the corner.
def lotka_volterra():
    b = []
    ox, oy = 30, 170
    b.append(f'<polyline class="pi-ink" points="{poly([(ox, 22), (ox, oy), (184, oy)])}"/>')
    b.append(f'<path class="pi-ink" d="M{ox - 4} 28 L{ox} 21 L{ox + 4} 28"/>')
    b.append(f'<path class="pi-ink" d="M178 {oy - 4} L185 {oy} L178 {oy + 4}"/>')
    ex, ey = 110, 95
    # nullclines
    b.append('<line class="pi-soft" stroke-dasharray="5 4" x1="40" y1="126.5" x2="180" y2="63.5"/>')
    b.append('<line class="pi-soft" stroke-dasharray="5 4" x1="70" y1="159" x2="150" y2="31"/>')
    r0, turns = 68.0, 2.6
    k = math.log(r0 / 4.0) / (turns * 2 * math.pi)
    rot = math.radians(-25)
    pts = []
    n = 600
    for i in range(n + 1):
        th = turns * 2 * math.pi * i / n
        r = r0 * math.exp(-k * th)
        x, y = r * math.cos(th), 0.72 * r * math.sin(th)
        xr = x * math.cos(rot) - y * math.sin(rot)
        yr = x * math.sin(rot) + y * math.cos(rot)
        pts.append((ex + xr, ey - yr))
    b.append(f'<path class="pi-acc" d="{path(pts)}"/>')
    # arrowhead at the start of the trajectory, pointing along the flow
    (x1, y1), (x2, y2) = pts[0], pts[6]
    ang = math.atan2(y2 - y1, x2 - x1)

    def rotp(px, py):
        return (x1 + px * math.cos(ang) - py * math.sin(ang), y1 + px * math.sin(ang) + py * math.cos(ang))

    tri = [rotp(0, -4.5), rotp(8, 0), rotp(0, 4.5)]
    b.append(f'<polygon points="{poly(tri)}" fill="var(--global-theme-color,#2458b3)"/>')
    b.append(f'<circle class="pi-dot" cx="{ex}" cy="{ey}" r="5"/>')
    # sign pattern of the interaction matrix
    b.append('<path class="pi-soft" d="M52 28 L48 28 L48 56 L52 56 M80 28 L84 28 L84 56 L80 56"/>')
    for i, row in enumerate(["+ −", "− +"]):
        b.append(f'<text class="pi-txt" x="66" y="{41 + 13 * i}" text-anchor="middle">{row}</text>')
    svg("celik2026strata.svg",
        "A Lotka–Volterra trajectory spiralling into a feasible stable equilibrium, with the interaction sign pattern",
        "\n".join(b))


tropical(); semi_inverted(); logconcave(); coalescent(); morse(); lotka_volterra()
