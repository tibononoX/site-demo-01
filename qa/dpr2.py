import asyncio, sys
from playwright.async_api import async_playwright
B='http://127.0.0.1:4321/site-demo-01/'; tag=sys.argv[1]
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    c=await b.new_context(viewport={'width':1440,'height':900},device_scale_factor=2,reduced_motion='reduce');pg=await c.new_page()
    await pg.goto(B);await pg.wait_for_load_state('networkidle');await pg.wait_for_timeout(500)
    await pg.screenshot(path=f'audit/v2/strokes-dpr2-{tag}.png',clip={'x':720,'y':560,'width':720,'height':340})
    await b.close()
asyncio.run(m())
