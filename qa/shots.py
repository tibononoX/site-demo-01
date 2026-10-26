import asyncio, sys
from playwright.async_api import async_playwright
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:4321'
PAGES=sys.argv[2].split(',') if len(sys.argv)>2 else ['']
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        for path in PAGES:
            for w in (1440,390):
                pg=await b.new_page(viewport={'width':w,'height':900})
                r=await pg.goto(f'{BASE}/{path}'); await pg.add_style_tag(content='body{position:relative}.bar{position:absolute!important}')
                await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
                sw=await pg.evaluate('document.documentElement.scrollWidth')
                name=(path.strip('/').replace('/','_') or 'accueil')+f'-{w}.png'
                await pg.screenshot(path='qa/'+name,full_page=True); print(r.status,name,'scrollWidth',sw,'OK' if sw<=w else 'OVERFLOW')
        await b.close()
asyncio.run(main())
