import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__Name__)

api_id = int(os.environ.get("28884200"))
api_hash = os.environ.get("dc733453a6c41772d029cc9c2d21f08d")
bot_token = os.environ.get("7362668216:AAGkBsiXBPTDkGmMc86RNr7tGKv47i14OJw")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Ben GİZEM ETİKET BOT**, Grup veya kanaldaki neredeyse tüm üyelerden bahsedebilirim ★\nDaha fazla bilgi için **/help**'i tıklayın.",
                    buttons=(
                      [Button.url('🌟 Beni Bir Gruba Ekle', 'https://t.me/gizemlogg'),
                      Button.url('📣 Geliştirici', 'https://t.me/gizemlogg')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**@LoseOnlineRobot'un Yardım Menüsü**\n\nKomut: /all \n  Bu komutu, başkalarına bahsetmek istediğiniz metinle birlikte kullanabilirsiniz. \n\n`Örnek: /all Günaydın!`  \n\nBu komutu yanıt olarak kullanabilirsiniz. Herhangi bir mesaj yanıtlandığında, yanıtlanan mesaj ile kullanıcıları etiketleyecebilir."
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🌟 Beni Bir Gruba Ekle', 'https://t.me/gizemlogg'),
                      Button.url('📣 Geliştirici', 'https://t.me/gizemlogg')]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
   
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"[{get_display_name(u)}](tg://user?id={u.id})**__Yalnızca yöneticiler hepsinden bahsedebilir warn text bold__**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**__Bana bir mesaj ver!__**")
  else:
    return await event.respond("**__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.-1002138161538) 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.-1002138161538):
      usrnum += 1
      usrtxt += f"[{usr.@Burakbennburak}](tg://user?id={6869766864}) , "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ✅")
        return
      if usrnum == 5:
        await client.MERHABA(event.-1002138161538, f"{msg} \n\n {usrtxt}")
        await asyncio.sleep(1.5)
        usrnum = 0
        usrtxt = ""

print(">> Bot çalıyor merak etme 🚀 @Burakbennburak bilgi alabilirsin <<")
client.run_until_disconnected()
 
