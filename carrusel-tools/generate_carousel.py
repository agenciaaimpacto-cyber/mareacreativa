#!/usr/bin/env python3
"""
Genera un carrusel de imagenes (1080x1350, estilo Marea Creativa: fondo azul
marino oscuro, texto blanco/turquesa bold) a partir de un archivo JSON de
slides. Adaptado del generador de Danny Mera Seguros / Radar Comercial.

Uso:
  python3 generate_carousel.py slides.json output_dir/

Formato de slides.json:
{
  "slides": [
    {"type": "hook", "tag": "OJO CON ESTO", "text": "No necesitas ser una **gran empresa** para hacer publicidad que funcione"},
    {"type": "text", "lines": ["No todos los negocios necesitan", "**cientos de clientes.**"], "sub": "Necesitan los suficientes para su meta."},
    {"type": "stat", "number": "4", "unit": "preguntas", "text": "son las que respondemos **antes de crear cualquier campana**"},
    {"type": "proof", "tag": "COMO TRABAJAMOS", "text": "Que vendes, cuantos clientes necesitas, cuanto puedes invertir **y que tendria que pasar** para que valga la pena", "source": "Marea Creativa"},
    {"type": "cta", "text": "Listo para conseguir **los clientes que necesitas?**", "button": "Escribenos por WhatsApp ->", "sub": "Conversemos primero sobre tu negocio."}
  ]
}

Marcado: **palabra** = resaltado en turquesa/cyan. El resto va en blanco (o
gris claro para subtitulos). Evita tildes fuera de UTF-8 raro; el script
soporta UTF-8 normal.
"""
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
PAD = 90
BG = (11, 31, 58)           # navy
ACCENT = (79, 195, 224)     # cyan (resaltado, mas legible que el turquesa oscuro sobre fondo navy)
WHITE = (255, 255, 255)
DIM = (196, 210, 226)
GRAY_LABEL = (140, 160, 184)
GRAY_SOURCE = (120, 140, 164)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(SCRIPT_DIR, "fonts")
BLACK_FONT_PATH = os.path.join(FONT_DIR, "ArchivoBlack-Regular.ttf")
VAR_FONT_PATH = os.path.join(FONT_DIR, "Archivo-Variable.ttf")

TOKEN_RE = re.compile(r"\*\*(.+?)\*\*|(\S+)")


def load_black(size):
    return ImageFont.truetype(BLACK_FONT_PATH, size)


def load_variable(size, weight=600, width=100):
    f = ImageFont.truetype(VAR_FONT_PATH, size)
    try:
        f.set_variation_by_axes([width, weight])
    except Exception:
        pass
    return f


def tokenize(text, base_color):
    """Como en el original, pero pega puntuacion pegada (sin espacio) al
    token anterior en vez de tratarla como una palabra suelta (evita
    '**vendes**,' -> 'vendes ,' con un espacio de mas antes de la coma)."""
    tokens = []
    last_end = None
    for m in TOKEN_RE.finditer(text):
        if m.group(1) is not None:
            words, color = m.group(1).split(), ACCENT
        else:
            words, color = [m.group(2)], base_color
        for w in words:
            if last_end == m.start() and tokens:
                prev_word, prev_color = tokens[-1]
                tokens[-1] = (prev_word + w, prev_color)
            else:
                tokens.append((w, color))
        last_end = m.end()
    return tokens


def wrap_and_draw(draw, xy, text, font, max_width, line_height, base_color,
                   align="left", center_x=None):
    tokens = tokenize(text, base_color)
    space_w = draw.textlength(" ", font=font)
    lines = []
    current, current_w = [], 0
    for word, color in tokens:
        w = draw.textlength(word, font=font)
        added = w if not current else space_w + w
        if current and current_w + added > max_width:
            lines.append(current)
            current, current_w = [], 0
            added = w
        current.append((word, color, w))
        current_w += added
    if current:
        lines.append(current)

    x0, y = xy
    for line in lines:
        line_w = sum(w for _, _, w in line) + space_w * (len(line) - 1)
        if align == "center":
            x = (center_x if center_x is not None else W / 2) - line_w / 2
        else:
            x = x0
        for word, color, w in line:
            draw.text((x, y), word, font=font, fill=color)
            x += w + space_w
        y += line_height
    return y


def brand_label(draw, side="right"):
    f = load_variable(24, weight=700)
    txt = "MAREA CREATIVA"
    if side == "right":
        w = draw.textlength(txt, font=f)
        draw.text((W - PAD - w, 60), txt, font=f, fill=GRAY_LABEL)
    else:
        draw.text((PAD, 60), txt, font=f, fill=GRAY_LABEL)


def swipe_hint(draw):
    f = load_variable(24, weight=700)
    txt = "DESLIZA ->"
    w = draw.textlength(txt, font=f)
    draw.text((W - PAD - w, H - 90), txt, font=f, fill=GRAY_LABEL)


def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


def render_hook(slide):
    img, d = new_canvas()
    brand_label(d)
    y = 300
    if slide.get("tag"):
        f = load_variable(28, weight=700)
        d.text((PAD, y), slide["tag"].upper(), font=f, fill=ACCENT)
        y += 70
    f = load_black(76)
    wrap_and_draw(d, (PAD, y), slide["text"], f, W - 2 * PAD, 92, WHITE)
    swipe_hint(d)
    return img


def render_text(slide):
    img, d = new_canvas()
    brand_label(d)
    y = 480
    f = load_black(62)
    for line in slide.get("lines", []):
        y = wrap_and_draw(d, (PAD, y), line, f, W - 2 * PAD, 76, WHITE)
        y += 6
    if slide.get("sub"):
        fs = load_variable(34, weight=500)
        wrap_and_draw(d, (PAD, y + 24), slide["sub"], fs, W - 2 * PAD, 46, DIM)
    swipe_hint(d)
    return img


def render_stat(slide):
    img, d = new_canvas()
    brand_label(d)
    fnum = load_black(220)
    y = 480
    d.text((PAD, y), slide["number"], font=fnum, fill=ACCENT)
    if slide.get("unit"):
        numw = d.textlength(slide["number"], font=fnum)
        funit = load_black(100)
        d.text((PAD + numw + 10, y + 100), slide["unit"], font=funit, fill=ACCENT)
    y += 280
    fs = load_variable(40, weight=700)
    wrap_and_draw(d, (PAD, y), slide["text"], fs, W - 2 * PAD, 52, WHITE)
    swipe_hint(d)
    return img


def render_proof(slide):
    img, d = new_canvas()
    brand_label(d)
    y = 300
    if slide.get("tag"):
        f = load_variable(28, weight=700)
        d.text((PAD, y), slide["tag"].upper(), font=f, fill=ACCENT)
        y += 70
    f = load_black(64)
    y = wrap_and_draw(d, (PAD, y), slide["text"], f, W - 2 * PAD, 80, WHITE)
    if slide.get("source"):
        fs = load_variable(20, weight=500)
        d.text((PAD, H - 90), slide["source"], font=fs, fill=GRAY_SOURCE)
    return img


def render_cta(slide):
    img, d = new_canvas()
    brand_label(d, side="left")
    f = load_black(58)
    y = wrap_and_draw(d, (PAD, 300), slide["text"], f, W - 2 * PAD, 74, WHITE,
                       align="center", center_x=W / 2)
    if slide.get("button"):
        fb = load_black(36)
        btn_text = slide["button"]
        tw = d.textlength(btn_text, font=fb)
        box_w, box_h = tw + 88, 100
        box_x = (W - box_w) / 2
        box_y = y + 60
        d.rounded_rectangle([box_x, box_y, box_x + box_w, box_y + box_h],
                             radius=10, fill=ACCENT)
        d.text((box_x + 44, box_y + 28), btn_text, font=fb, fill=BG)
        y = box_y + box_h + 40
    if slide.get("sub"):
        fs = load_variable(30, weight=500)
        wrap_and_draw(d, (PAD, y + 20), slide["sub"], fs, W - 2 * PAD, 40, DIM,
                       align="center", center_x=W / 2)
    return img


RENDERERS = {
    "hook": render_hook,
    "text": render_text,
    "stat": render_stat,
    "proof": render_proof,
    "cta": render_cta,
}


def main():
    if len(sys.argv) != 3:
        print("Uso: generate_carousel.py slides.json output_dir/")
        sys.exit(1)
    slides_path, out_dir = sys.argv[1], sys.argv[2]
    with open(slides_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    os.makedirs(out_dir, exist_ok=True)
    for i, slide in enumerate(data["slides"], start=1):
        renderer = RENDERERS.get(slide["type"])
        if not renderer:
            print(f"Tipo de slide desconocido: {slide['type']}")
            sys.exit(1)
        img = renderer(slide)
        out_path = os.path.join(out_dir, f"slide-{i}.png")
        img.save(out_path, "PNG")
        print(f"Guardado {out_path}")


if __name__ == "__main__":
    main()
