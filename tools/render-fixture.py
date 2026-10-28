#!/usr/bin/env python3
"""Render an explicitly synthetic, owned twelve-second shop scene and annotations."""
from pathlib import Path
import hashlib,json,subprocess
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'examples';OUT.mkdir(exist_ok=True)
WIDTH,HEIGHT,FPS,SECONDS=640,360,10,12
def box(t):
 x=80+min(t,3)*45 if t<3 else 215 if t<7 else 215+(t-7)*58
 return [round(x),180,round(x+32),230]
def frame(t):
 image=Image.new('RGB',(WIDTH,HEIGHT),'#eae6de');d=ImageDraw.Draw(image)
 font=ImageFont.load_default(size=16)
 d.rectangle((0,0,WIDTH,55),fill='#23262b');d.text((18,12),'Synthetic shop · authored annotations',font=font,fill='#ffffff')
 d.text((18,35),f'{t:04.1f}s / 12s',font=ImageFont.load_default(size=11),fill='#d7d9db')
 for x in [140,350]:
  d.rectangle((x,90,x+120,145),fill='#617b6b')
  for k in range(5):d.rectangle((x+9+k*21,100,x+21+k*21,130),fill='#c1d2c2')
 d.text((148,151),'Shelf',font=font,fill='#4e5a52');d.rectangle((470,260,600,310),fill='#a07859');d.text((490,277),'Checkout',font=font,fill='#ffffff')
 b=box(t);d.rounded_rectangle(b,8,fill='#3c6e8c');d.ellipse((b[0]+8,b[1]-13,b[0]+24,b[1]+3),fill='#3c6e8c');d.text((b[0]-1,b[3]+5),'P1',font=font,fill='#31444f')
 if 4<=t<8:d.rectangle((b[2]+2,b[1]+10,b[2]+13,b[1]+25),fill='#bb7453')
 d.text((18,HEIGHT-28),'Programmatic fixture · supplied labels · MIT',font=ImageFont.load_default(size=14),fill='#565c63')
 return image
target=OUT/'synthetic-shop.mp4'
p=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-f','rawvideo','-pixel_format','rgb24','-video_size',f'{WIDTH}x{HEIGHT}','-framerate',str(FPS),'-i','pipe:0','-an','-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart','-crf','24','-y',str(target)],stdin=subprocess.PIPE)
for i in range(FPS*SECONDS):p.stdin.write(frame(i/FPS).tobytes())
p.stdin.close();assert p.wait()==0
frame(4).save(OUT/'synthetic-shop.jpg',quality=92)
frames=[{'frame_index':i,'video_time_s':i/FPS,'tracks':[{'track_id':'P1','bbox_xyxy':box(i/FPS)}]} for i in range(FPS*SECONDS)]
tracks={'identity_scope':'recording_and_camera_local','fps':FPS,'width':WIDTH,'height':HEIGHT,'tracker':'authored-fixture/v1','frames':frames}
events=[]
for kind,start,end,description in [('touch',3.,4.,'Supplied label: P1 touches the example item.'),('pick_up',4.,5.,'Supplied label: P1 picks up the example item.'),('put_back',7.,8.,'Supplied label: P1 returns the example item.')]:
 events.append({'person_id':'P1','event':kind,'start_s':start,'end_s':end,'object_ref':'fixture-item-1','item_description':'Synthetic bottled beverage','location_description':'Example shelf','evidence':description})
viewer={'fps':FPS,'width':WIDTH,'height':HEIGHT,'source':'authored-fixture/v1','identity_scope':'recording_and_camera_local','frames':{str(i):[{'id':'P1','box':box(i/FPS)}] for i in range(FPS*SECONDS)}}
(OUT/'annotations.json').write_text(json.dumps({'basis':'authored synthetic fixture; supplied annotations','tracks':tracks,'viewer_tracks':viewer,'answer':{'people':{'P1':'Synthetic visitor'},'objects':{'fixture-item-1':'Synthetic bottled beverage'},'events':events}},indent=2)+'\n')
(OUT/'media-provenance.json').write_text(json.dumps({'author':'Peter Neyra','licence':'MIT','basis':'programmatically authored scene and supplied labels','generator':'tools/render-fixture.py','model_calls':0,'customer_footage':False,'width':WIDTH,'height':HEIGHT,'fps':FPS,'duration_seconds':SECONDS,'assets':{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['synthetic-shop.mp4','synthetic-shop.jpg','annotations.json']}},indent=2)+'\n')
print({'rendered':str(target),'bytes':target.stat().st_size,'provider_calls':0})
