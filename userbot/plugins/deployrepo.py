from userbot.Config import Config
from userbot import bot 

O = Config.OWNER_ID
Name = bot.me.first_name
M = f"[{Name}](tg://user?id={O})"

A = "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FModLso%2FSTRIP-AR&template=https%3A%2F%2Fgithub.com%2FModLso%2FSTRIP-AR"

B = "**⌔∮ اهلا عزيزي - {} \n⌔∮ رابط التنصيب - [اضغط هنا]({})**"

@Stripbot.on(icss_cmd(pattern="رابط التنصيب"))
async def _(e):
    await eor(e, B.format(M, A))
