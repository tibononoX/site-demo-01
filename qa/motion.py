import asyncio, shutil, glob, os
from playwright.async_api import async_playwright
B='http://127.0.0.1:4321/site-demo-01/'; OUT='audit/v2/'
async def smooth(pg, y, ms=900):
    await pg.evaluate(f"window.scrollTo({{top:{y},behavior:'smooth'}})"); await pg.wait_for_timeout(ms)
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    # hover stills
    c=await b.new_context(viewport={'width':1440,'height':900},device_scale_factor=1);pg=await c.new_page()
    await pg.goto(B);await pg.wait_for_timeout(1600)
    btn=pg.locator('.hero .btn-g');bb=await btn.bounding_box()
    clip={'x':bb['x']-30,'y':bb['y']-30,'width':420,'height':bb['height']+60}
    await pg.screenshot(path=OUT+'hover-btn-avant.png',clip=clip);await btn.hover();await pg.wait_for_timeout(450);await pg.screenshot(path=OUT+'hover-btn-apres.png',clip=clip)
    await pg.keyboard.press('Tab');await pg.keyboard.press('Tab');await pg.wait_for_timeout(300);await pg.screenshot(path=OUT+'focus-visible.png',clip={'x':0,'y':0,'width':1440,'height':90})
    chip=pg.locator('.chip').nth(1);await chip.scroll_into_view_if_needed();await pg.wait_for_timeout(1200)
    bb=await pg.locator('.chips').bounding_box();clip={'x':bb['x']-20,'y':bb['y']-30,'width':bb['width']+40,'height':bb['height']+60}
    await pg.mouse.move(5,5);await pg.wait_for_timeout(400);await pg.screenshot(path=OUT+'hover-chip-avant.png',clip=clip)
    await chip.hover();await pg.wait_for_timeout(500);await pg.screenshot(path=OUT+'hover-chip-apres.png',clip=clip)
    nav=pg.locator('.nav a').nth(0);await nav.hover();await pg.wait_for_timeout(450);await pg.screenshot(path=OUT+'hover-nav-soulignement.png',clip={'x':0,'y':0,'width':1440,'height':90})
    await c.close()
    # video
    os.makedirs('/tmp/vid',exist_ok=True)
    c=await b.new_context(viewport={'width':1440,'height':900},record_video_dir='/tmp/vid',record_video_size={'width':1440,'height':900});pg=await c.new_page()
    await pg.goto(B);await pg.wait_for_timeout(2200)
    bb=await pg.locator('.hero .btn-g').bounding_box();await pg.mouse.move(bb['x']+40,bb['y']+20,steps=15);await pg.wait_for_timeout(700)
    await pg.mouse.move(700,450,steps=8)
    y=await pg.evaluate("document.querySelector('.prest').offsetTop-80");await smooth(pg,y,1500)
    for i in range(6):
        bb=await pg.locator('.chip').nth(i).bounding_box();await pg.mouse.move(bb['x']+bb['width']/2,bb['y']+bb['height']/2,steps=8);await pg.wait_for_timeout(380)
    y=await pg.evaluate("document.querySelector('.why').offsetTop-60");await smooth(pg,y,1400)
    y=await pg.evaluate("document.querySelector('.real').offsetTop-40");await smooth(pg,y,1300)
    bb=await pg.locator('.ba').bounding_box();cy=bb['y']+bb['height']/2
    await pg.mouse.move(bb['x']+bb['width']/2,cy,steps=6);await pg.mouse.down()
    await pg.mouse.move(bb['x']+bb['width']*0.2,cy,steps=20);await pg.mouse.move(bb['x']+bb['width']*0.8,cy,steps=30);await pg.mouse.move(bb['x']+bb['width']*0.5,cy,steps=15);await pg.mouse.up()
    y=await pg.evaluate("document.querySelector('.pp').offsetTop-120");await smooth(pg,y,1400)
    bb=await pg.locator('.card-p').bounding_box();await pg.mouse.move(bb['x']+200,bb['y']+100,steps=10);await pg.wait_for_timeout(600)
    bb=await pg.locator('.card-pro').bounding_box();await pg.mouse.move(bb['x']+100,bb['y']+60,steps=10);await pg.wait_for_timeout(600)
    y=await pg.evaluate("document.querySelector('.cta').offsetTop-100");await smooth(pg,y,1900)
    await smooth(pg,0,1500)
    v=pg.video;await c.close();path=await v.path();shutil.copy(path,'/tmp/motion.webm')
    await b.close()
asyncio.run(m())
