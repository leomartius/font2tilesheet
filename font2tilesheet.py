#!/usr/bin/env python3
import argparse
from pathlib import Path

from PIL import BdfFontFile, Image, ImageDraw, ImageFont

# ASCII characters from 0x20 (space) to 0x7E (tilde)
ASCII = [chr(i) for i in range(0x20, 0x7F)]


def convert_and_load_font(bdf_path):
    bdf_path = Path(bdf_path)
    base_name = bdf_path.stem
    pil_font_path = f"{base_name}.pil"

    with bdf_path.open("rb") as bdf_file:
        try:
            bdf = BdfFontFile.BdfFontFile(bdf_file)
        except SyntaxError as err:
            error_message = f"Failed to parse the BDF file '{bdf_path}'"
            raise ValueError(error_message) from err
        bdf.save(pil_font_path)

    return ImageFont.load(pil_font_path)


def generate_tilesheet(font, output_file, *, cols=16, show_image=False):
    char_table = ASCII
    rows = -(-len(char_table) // cols)
    char_bbox = font.getbbox("M")
    cell_width = char_bbox[2] - char_bbox[0]
    cell_height = char_bbox[3] - char_bbox[1]
    img_width = cols * cell_width
    img_height = rows * cell_height

    image = Image.new("RGB", (img_width, img_height), color="black")
    draw = ImageDraw.Draw(image)

    for row in range(rows):
        for col in range(cols):
            char_index = row * cols + col
            if char_index < len(char_table):
                x = col * cell_width
                y = row * cell_height
                draw.text((x, y), char_table[char_index], font=font, fill="white")

    image.save(output_file)

    if show_image:
        image.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate an ASCII tilesheet from a BDF font.",
    )
    parser.add_argument(
        "bdf_path",
        metavar="FONT",
        type=str,
        help="path to the BDF font file",
    )
    parser.add_argument(
        "--cols",
        type=int,
        default=16,
        help="number of columns in the tilesheet (default: 16)",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="display the generated image",
    )
    args = parser.parse_args()

    font = convert_and_load_font(args.bdf_path)
    base_name = Path(args.bdf_path).stem
    output_file = f"{base_name}.png"

    generate_tilesheet(font, output_file, cols=args.cols, show_image=args.show)
