import sys, glob
from PIL import Image
d, out, sub = sys.argv[1], sys.argv[2], sys.argv[3]
fs = sorted(glob.glob(f"{d}/.build/{sub}/*.png"))
ims = [Image.open(f) for f in fs]
w, h = ims[0].width // 3, ims[0].height // 3
cols = 5; rows = (len(ims) + cols - 1) // cols
m = Image.new('RGB', (cols * w, rows * h), 'white')
for k, im in enumerate(ims): m.paste(im.resize((w, h)), ((k % cols) * w, (k // cols) * h))
m.save(out); print(len(fs))
