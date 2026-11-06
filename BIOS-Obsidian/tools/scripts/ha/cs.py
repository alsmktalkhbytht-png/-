import sys,glob
from PIL import Image
d,out=sys.argv[1],sys.argv[2]
fs=sorted(glob.glob(d+'/.build/booklet-pages/*.png'))[:int(sys.argv[3]) if len(sys.argv)>3 else None];ims=[Image.open(f) for f in fs];w,h=ims[0].size
ims=[i.resize((330,int(h*330/w))) for i in ims];W,H=ims[0].size;c=5;r=(len(ims)+c-1)//c
S=Image.new('RGB',(W*c,H*r),'white')
for i,im in enumerate(ims):S.paste(im,((i%c)*W,(i//c)*H))
S.save(out)
