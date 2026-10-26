"""HD dry-brush strokes for FV Peinture.
Silhouette: CC0 brush041/brush011 (Dino0040, OpenGameArt). Interior detail: CC0 'Dry Stroke'
texture by David Revoy (davidrevoy.com/article263). Output: master WebP RGBA in src/assets/img.
"""
import numpy as np, sys
from PIL import Image
from scipy.ndimage import gaussian_filter, map_coordinates, zoom
Image.MAX_IMAGE_PIXELS=None
G=np.array([162,188,66],float)
rng=np.random.default_rng(7)
GB='/tmp/gb/grunge_brushes/increased_opacity/'
TEX=np.asarray(Image.open('/tmp/drystroke.jpg').convert('L'),float)/255
def mask(name,W):
    im=Image.open(GB+name).convert('RGBA');a=im.split()[3];im=im.crop(a.getbbox())
    a=np.asarray(im.split()[3],float)/255
    s=W/a.shape[1]; a=zoom(a,s,order=3)
    h,w=a.shape
    # fine ragged edge: displace by high-frequency noise
    n1=gaussian_filter(rng.standard_normal((h,w)),(0.6,30))*10
    n2=gaussian_filter(rng.standard_normal((h,w)),(0.6,30))*3
    yy,xx=np.mgrid[0:h,0:w]
    a=map_coordinates(a,[yy+n1,xx+n2],order=1,mode='constant')
    # bristle streaks (horizontal fibres) at native res
    fib=gaussian_filter(rng.standard_normal((h,w)),(0.7,60));fib/=fib.std()
    a=a*(1+0.18*fib)
    # sharpen edge: steep curve around 0.5 with grain dither
    grain=rng.random((h,w))*0.25-0.125
    a=np.clip((a-0.42+grain*(a<0.8))*3.2+0.5,0,1)
    return a
def bake(a,name,flip=False):
    h,w=a.shape
    t=TEX
    # tile/crop texture to size, stretched horizontally to follow the stroke
    t=zoom(t,(max(h/t.shape[0],0.6),max(w/t.shape[1]*0.8,0.6)),order=1)[:h,:w]
    if t.shape!=(h,w): t=np.pad(t,((0,h-t.shape[0]),(0,w-t.shape[1])),mode='reflect')
    t=(t-t.mean())/(t.std()+1e-6)
    height=gaussian_filter(a,1.6)+0.05*t*a
    gy,gx=np.gradient(height)
    inner=gaussian_filter(a,6)**4
    shade=(-gx*0.8-gy*1.0)*3.5*inner
    tone=gaussian_filter(rng.standard_normal(a.shape),(2,60));tone/=tone.std()+1e-6
    k=1+0.035*tone+0.07*t+shade
    k*=(0.9+0.1*a)
    rgb=np.clip(G*k[...,None]+np.clip(shade,0,None)[...,None]**1.4*40,0,255)
    out=np.dstack([rgb,a*255]).astype(np.uint8)
    im=Image.fromarray(out,'RGBA')
    if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
    im.save(f'src/assets/img/{name}.webp',quality=90,method=6)
    im.crop((0,0,min(900,w),min(400,h))).save(f'/tmp/{name}-crop.png')
    print(name,im.size)
bake(mask('brush041.png',3040),'stroke-hero')
bake(mask('brush011.png',1280),'stroke-small')
