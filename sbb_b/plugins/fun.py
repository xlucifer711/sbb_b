
import asyncio
import random
import re
import time
from random import choice, randint
from collections import deque
from telethon import events
import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


from sbb_b import CMD_HELP
from sbb_b.utils import admin_cmd


# ================= CONSTANT =================


GAMBAR_TITIT = """
šš
ššš
  ššš
    ššš
     ššš
       ššš
        ššš
         ššš
          ššš
          ššš
      šššš
 šššššš
 ššš  ššš
    šš       šš
"""

# ===========================================

@borg.on(admin_cmd(pattern=r"ŁŁ$"))
async def facepalm(e):
    """ Facepalm  š¤¦āā """
    await e.edit("š¤¦āā")

@borg.on(admin_cmd(pattern=r"ŁŁŁŁŲÆ$"))
async def iqless(e):
    await e.edit("Antivirus scan was completed \nā ļø Warning! This  donkey has Corona Virus")


@borg.on(admin_cmd(pattern=r"ggl (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@borg.on(admin_cmd(outgoing=True, pattern="ŁŲ§Ų“Ł$"))
async def fail(e):
        await e.edit("`\nāāāāāāāāāāāāāāāā `" 
                     "`\nāāāāāāāāāāāāāāāā `"    
                     "`\nāāāāāāāāāāāāāāāā `"       
                     "`\nāāāāāāāāāāāāāāāā `")    


@borg.on(admin_cmd(outgoing=True, pattern="ŁŁŁ$"))
async def lol(e):
        await e.edit("`\nā±āāā±ā±ā±ā­āāāā®āāā±ā±ā±ā± `" 
                     "`\nā±āāā±ā±ā±āā­āā®āāāā±ā±ā±ā± `"       
                     "`\nā±āāāāāāā°āāÆāāāāāāā± `" 
                     "`\nā±āāāāāā°āāāāÆāāāāāā± `") 
 
 
                                                                                   
@borg.on(admin_cmd(outgoing=True, pattern="ŁŁŁŁ$"))
async def lool(e):
        await e.edit("`\nā­ā­āāāā®ā®āāāāāāāāāā\nāāā­āāāÆāāāāāā²āāā±āā\nāāāā±āāāāāāāāā±āāā®ā`"
                     "`\nāāā°āāā±ā­ā®āā±ā±āā±ā±āāā\nāā°āāāāā°āÆāāā±ā±ā±ā°ā»ā«ā\nāāāāāā³āāāāāāā³āāāÆā`"
                     "`\nāāāāāāāāāāāāāāāāā `")
                     



@borg.on(admin_cmd(outgoing=True, pattern="ŁŲ±ŲÆŁ$"))
async def nih(e):
        await e.edit("`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\n >š¹ *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(ā¢_ā¢)`"
                     "`\nš¹<\ *`")


@borg.on(admin_cmd(outgoing=True, pattern="ŁŁŁ$"))  
async def gtfo(e):
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     "`\nā  ŁŁŁŲ± ŁŲ­ŲØ `"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@borg.on(admin_cmd(outgoing=True, pattern="ml(?: |$)(.*)"))
async def gtfo(e):
        message = e.pattern_match.group(1)
        await e.edit("`\nāāāāāāāāā`" 
                     "`\nāāāāāāāāā`"    
                     "`\nāā¼ā¼ā¼ā¼ā¼`"       
                     f"`\nā  {message}`"
                     "`\nāā²ā²ā²ā²ā²`"
                     "`\nāāāāāāāāā`"
                    "`\n āā   āā`")               


@borg.on(admin_cmd(outgoing=True, pattern="Ų§ŁŁ$")) 
async def taco(e):
        await e.edit("\n{\__/}"
                     "\n(ā_ā)"
                     "\n( >š® Ų§ŲŖŁŲ¶Ł ŁŲ¹Ų§ŁŲ§?")


@borg.on(admin_cmd(outgoing=True, pattern="ŲØŲ§Ł$"))  
async def paw(e):
        await e.edit("`(=āĻā=)")


@borg.on(admin_cmd(outgoing=True, pattern="tf$")) 
async def tf(e):
        await e.edit("(ĢæāĢæāĢæÄ¹ĢÆĢæĢæāĢæ Ģæ)Ģ  ")  
      

@borg.on(admin_cmd(outgoing=True, pattern="ŁŲ§Ų­ŲÆ$"))           
async def gey(e):
        await e.edit("`\nāāāā­āāāāāā®āāāāā\nāāāāāāāāāāāāāāā`"
                     "`\nāāāāāāā­āā®ā»ā®āāāā\nāāāā±ā²āāāāāāāāāā\nāāā­ā»āāā°āā»āā®āāāā`"
                     "`\nāāā°ā³āā­āāāā³āÆāāāā\nāāāāāāā°āāā«āU GAY`"
                    "\nāāāāāāāāāāāāāāā")    


@borg.on(admin_cmd(outgoing=True, pattern="ŲØŁŲŖ$"))
async def bot(e):
        await e.edit("` \n   ā²ā²ā­āāāāā® \nā­ā®āāāāāāā­ā® \nāā°ā«ā½ā½ā½ā£āÆā \nā°āā«ā³ā³ā³ā£āāÆ`"
                     "`\nā²ā²āāāāāā  \nā²ā²āāāāāā `")


@borg.on(admin_cmd(outgoing=True, pattern="Ų¬ŁŲŖ$"))
async def hey(e):
        await e.edit("\nāāāā±āāāāā²āā­āāāāā\nāāāāāāāāāāāŲ§ŁŲ§Ų¬ŁŲŖ!āš`"
                     "`\nāāāāāāāā³āāā°ā³ā\nāāāā­āā°āÆāā®āāāÆā°āāā\nā±āāāāāāāāāāā²āāāā`"
                     "`\nāāāā²āāāāā±āāāāāāā`")


@borg.on(admin_cmd(outgoing=True, pattern="ŲŖŁ$"))
async def nou(e):
        await e.edit("`\nāā­ā®ā­ā®\nāāāāā\nā­ā»āā»āā®`"
                     "`\nāāāāāā\nāāā­āāā®āā®\nāāāā­ā°āÆā°āÆā®`"
                     "`\nā«āā  ŲŖŁ Ų¹ŁŁ ŁŲ“Ł\nāāā°ā°āāāāāÆ`"
                     "`\nāāāā»āā`")



@borg.on(admin_cmd(outgoing=True, pattern="Ų®ŲÆ$"))
async def gtfo(e):
        await e.edit(
"\n......................................../Ā“ĀÆ/) "
"\n......................................,/ĀÆ../ "
"\n...................................../..../ "
"\n..................................../Ā“.ĀÆ/"
"\n..................................../Ā“ĀÆ/"
"\n..................................,/ĀÆ../ "
"\n................................../..../ "
"\n................................./Ā“ĀÆ./"
"\n................................/Ā“ĀÆ./"
"\n..............................,/ĀÆ../ "
"\n............................./..../ "
"\n............................/Ā“ĀÆ/"
"\n........................../Ā“ĀÆ./"
"\n........................,/ĀÆ../ "
"\n......................./..../ "
"\n....................../Ā“ĀÆ/"
"\n....................,/ĀÆ../ "
"\n.................../..../ "
"\n............./Ā“ĀÆ/'...'/Ā“ĀÆĀÆ`Ā·Āø "
"\n........../'/.../..../......./ĀØĀÆ\ "
"\n........('(...Ā“...Ā“.... ĀÆ~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.Ā·Ā“ "
"\n............\..............( "
"\n..............\.............\...")



@borg.on(admin_cmd(outgoing=True, pattern="ŁŁŁ ŁŁŲ§$"))
async def shalom(e):
    await e.edit(
        "\nššššššššš"
        "\nšš·š·š·š·š·š·š·š"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nššššš·šššš"
        "\nšš·š·š·š·ļøš·š·š·š"
        "\nššššššššš"
        "\nššššššššš"
        "\nšš·ššļøšššš·š"
        "\nšš·š·š·š·š·š·š·š"
        "\nšš·š·š·š·š·š·ļøš·š"
        "\nšš·ššššļøšš·š"
        "\nššššššššš")

@borg.on(admin_cmd(outgoing=True, pattern=r"(?:penis|dick)\s?(.)?"))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('š', emoji)
    await e.edit(titid)


