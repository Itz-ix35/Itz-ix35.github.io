from PIL import Image
import sys

def make_thumb(infile, outfile, size=(200,200)):
    with Image.open(infile) as im:
        w, h = im.size
        if w > h:
            left = (w - h) // 2
            box = (left, 0, left + h, h)
        else:
            top = (h - w) // 2
            box = (0, top, w, top + w)
        im_cropped = im.crop(box)
        im_resized = im_cropped.resize(size, Image.LANCZOS)
        im_resized.save(outfile, format="PNG")

make_thumb(sys.argv[1], sys.argv[2])
