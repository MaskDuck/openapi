import aiohttp
from urllib.parse import quote_plus

token = None

def set_token(token):
    # We need to make it global otherwise we will not be able to access it
    global token
    token = token

async def lyrics(song_name):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(f'https://api.openrobot.xyz/api/lyrics/{quote_plus(query)}', headers={'Authorization': token}) as resp:
            js = await resp.json() 
            return [js['title'], js['artist'], js['lyrics']]
            
       

    
