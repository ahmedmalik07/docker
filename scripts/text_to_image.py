#!/usr/bin/env python3
"""Convert text files into PNG images (simple wrapper using Pillow)."""
import sys
from pathlib import Path
import textwrap

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    print("Pillow is required. Install with: python -m pip install --user pillow")
    raise


def render_text_file_to_png(txt_path: Path, out_path: Path, width=1200, font_path=None, font_size=14, padding=16, bg=(255, 255, 255), fg=(0, 0, 0)):
    text = txt_path.read_text(encoding='utf-8', errors='replace')

    # choose font
    if font_path and Path(font_path).exists():
        font = ImageFont.truetype(str(font_path), font_size)
    else:
        font = ImageFont.load_default()

    # wrap text to fit width
    # estimate max chars per line from average character width
    test_img = Image.new('RGB', (10, 10))
    draw = ImageDraw.Draw(test_img)

    # estimate average character width using textbbox
    bbox_M = draw.textbbox((0, 0), 'M', font=font)
    avg_char_w = max(1, bbox_M[2] - bbox_M[0])
    max_chars = max(40, int((width - 2 * padding) / avg_char_w))

    wrapped_lines = []
    for paragraph in text.splitlines():
        if paragraph.strip() == '':
            wrapped_lines.append('')
        else:
            wrapped_lines.extend(textwrap.wrap(paragraph, width=max_chars, replace_whitespace=False))

    # compute image height using textbbox for line height
    bbox_A = draw.textbbox((0, 0), 'A', font=font)
    line_h = (bbox_A[3] - bbox_A[1]) + 4
    height = padding * 2 + line_h * max(1, len(wrapped_lines))

    img = Image.new('RGB', (width, height), color=bg)
    draw = ImageDraw.Draw(img)

    y = padding
    for line in wrapped_lines:
        draw.text((padding, y), line, font=font, fill=fg)
        y += line_h

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(out_path))
    print(f"Wrote {out_path}")


def main():
    base = Path(__file__).resolve().parents[1]
    shots = Path(base) / 'screenshots'

    mapping = {
        shots / 'compose_logs.txt': shots / 'compose_logs.png',
        shots / 'docker_ps.txt': shots / 'docker_ps.png',
    }

    for txt, png in mapping.items():
        if txt.exists():
            render_text_file_to_png(txt, png)
        else:
            print(f"Source {txt} not found, skipping")


if __name__ == '__main__':
    main()
