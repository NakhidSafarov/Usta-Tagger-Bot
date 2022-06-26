import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Salam 👋.Mən Usta Tagger Bot.\nSizin əvəzinizdən qruplarnızda istifadəçiləri tag edə bilərəm.Haqqımda daha ətraflı məlumat əldə etmək üçün /help əmrinə toxunun.",
                    buttons=(
                   
		      [Button.url('➕ Məni Qrupa Sal ➕', 'https://t.me/Ustataggerbot?startgroup=a')],
                      [Button.url('Developer 👨🏻‍💻', 'https://t.me/NakhidUsta')],
                      [Button.url(' Qurup 📣', 'https://t.me/USTABOTLAR')], 
		      [Button.url(' Kanal 🛠️', 'https://t.me/USTABOTLAR')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Usta Tagger Bot'un Kömək Menyusu.**\nƏmrlər📕.\n/all <səbəb> - 5-li Tag Edəcəkdir. \n/admins <səbəb> - Yalnız Adminləri Tag Edəcəkdir. \n/tektag <səbəb> - Tək-tək Tag Edəcəkdir.\n/etag <səbəb> - Emojilərlə Tag Edəcəkdir."
  await event.reply(helptext,
                    buttons=(
                      [Button.url('➕ Məni Qrupa Sal ➕', 'https://t.me/Ustataggerbot?startgroup=a')],
                      [Button.url('Developer 👨🏻‍💻', 'https://t.me/NakhidUsta')],
                      [Button.url(' Qurup 📣', 'https://t.me/USTABOTLAR')], 
		      [Button.url(' Kanal 🛠️', 'https://t.me/USTABOTLAR')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


#emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


#@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
#async def mentionall(event):
#  global anlik_calisan
 # if event.is_private:
 #   return await event.respond("**Bu əmr qruplar üçün etibarlıdır!. **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri yalnız adminlər istifadə edə bilər!. **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Köhnə mesajlar üçün userləri tag edə bilmərəm.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tag eləmək üçün səbəb yoxdur!. ")
  else:
    return await event.respond("**Taga başlamaq üçün səbəb yazın...**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag uğurlu şəkildə dayandırıldı**!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag uğurlu şəkildə dayandırıldı**! ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır!. **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri yalnız adminlər istifadə edə bilər!. **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Köhnə mesajlar üçün userləri tag edə bilmərəm.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Taga başlamaq üçün səbəb yoxdur!.")
  else:
    return await event.respond("**Taga başlamaq üçün səbəb yazın...**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag uğurlu şəkildə dayandırıldı**!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag uğurlu şəkildə dayandırıldı**! ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar*üçün etibarlıdır!. **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmri yalnız adminlər istifadə edə bilər!. **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Köhnə mesajlar üçün userləri tag edə bilmərəm. **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tagı başlamaq üçün səbəb yoxdur!. ")
  else:
    return await event.respond("**Taga başlamaq üçün səbəb yazın...**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**👤 [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tag uğurlu şəkildə dayandırıldı**! ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tag uğurlu şəkildə dayandırıldı**! ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

  

@client.on(events.NewMessage(pattern="^/tagadmin ?(.*)"))
async def mentionall(event):

        if tagadmin.pattern_match.group(1):
               seasons = tagadmin.pattern_match.group(1)
        else:
               seasons = ""

        chat = await tagadmin.get_input_chat()
        a_=0
        await tagadmin.delete()
        async for i in client.iter_participants(chat, filter=cp):
                if a_ == 500:
                        break
                a_+=5
                await tagadmin.client.send_message(tagadmin.chat_id, "{} {}".format(i.first_name, i.id, seasons))
                sleep(0.5)


print(">> Bot işləyir narahat olma 🚀 məlumat almaq üçün @ThrHassan yazın <<")
client.run_until_disconnected()
