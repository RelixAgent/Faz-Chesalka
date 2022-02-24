import random
import sqlite3
import asyncio
import  aeval
import aiohttp
import os
import sys, time, datetime, requests
from discord_components import component
import discord_components
from discord import embeds, reaction
import discord
from discord.ext import commands 
from Cybernator import Paginator as pag
from discord_components import DiscordComponents, Button, ButtonStyle


TOKEN = "OTQzMTk3OTE0MjI5MDEwNTEy.Ygvjgg.49F2LXA2kCvJJYrbIoR5wu8wSU8"

db = sqlite3.connect('sueta.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS eblani (
    fazi INT,
    username TEXT,
    ziga INT
)""")
db.commit()


client = commands.Bot(command_prefix = ',', intents = discord.Intents.all())
bot = commands.Bot(command_prefix=',')
bot.remove_command( 'help' )


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Я запущен!")

@bot.command()
async def старт(ctx):
    await ctx.send('Начни искать фазчесалку фредди!!! Напиши "//Фаз" чтобы искать чесалку')
    caller = ctx.author.name
    caller = str(caller)
    sql.execute(f"SELECT * FROM eblani WHERE username = '{caller}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO eblani VALUES ({0}, '{caller}', {0})")
        db.commit()
        await ctx.send(f"{caller}, Ты записан в бд")

@bot.command()
async def фаз(ctx):
    caller = ctx.author.name
    caller = str(caller)
    for i in sql.execute(f"SELECT fazi FROM eblani WHERE username = '{caller}'"):
            balans = i[0]
    sql.execute(f"SELECT username FROM eblani WHERE username = '{caller}'")
    if sql.fetchone() is None:
            await ctx.send("Зарегайся //старт")
    else:
        faz = random.randint(1,3)
        if faz == 1:
            await ctx.send(f'{caller}, Ты не нашел фазчесалку:(')
        elif faz == 2:
            await ctx.send(f'{caller}, Ты нашёл фазчесалку, но проебал её по дороге домой. ЛОХ!!!')
        else:
            sql.execute(f"UPDATE eblani SET fazi = {balans + 1} WHERE username = '{caller}'")
            db.commit()
            await ctx.send("https://imgur.com/a/IkruTE3")
            await ctx.send(f'{caller}, Ты нашел фазчесалку!!')
@bot.command()
async def зорин(ctx):
    await ctx.send('Я его не уважаю')

@bot.command()
async def виталя(ctx):
    await ctx.send('Я его уважаю!')

@bot.command()
async def зига(ctx):
    caller = ctx.author.name
    caller = str(caller)
    for i in sql.execute(f"SELECT ziga FROM eblani WHERE username = '{caller}'"):
        balans = i[0]
    sql.execute(f"UPDATE eblani SET ziga = {balans + 1} WHERE username = '{caller}'")
    db.commit()
    await ctx.send("""░
░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░
+1 зига на твой баланс плотных зиг""")

@bot.command()
async def гитлер(ctx):
    await ctx.send("""░░░░░░░░░░░▄▄▄▄▄
░░░░░░░▄▄█████████▄▄
░░░░▄▀▀▀▀█▀▀▀▀▀▀█████▄
░░▄██████░░░░░░░░░░░▀██
░▐██████▌░░░░░░░░░░░░░▐▌
░███████▌░░░░░░░░░░░░░░█
▐████████░░░░░░░░░░░░░░░█
▐██████▌░░░░░▄▀▀▀▀▀▄░▀░▄▄▌
░█▀▀███▀░░░░░░▄▀█▀░░░▐▄▄▄▌
▐░▌▀▄░░░░░░░░░░▄▄▄▀░░░▌▀░▌
░▌▐░░▌░░░░░░░░░░░▀░░░░▐░▐
░▐░▀▄▐░░░░░░░░░░░▌▌░▄▄░▐░▌
░░▀█░▄▀░░░░░░░░░▐░▐▄▄▄▄▀▐
░░░▌▀░▐░░░░░░░░▄▀░░▀▀▀▀░▌
░░░▐░░░░░░░░░▌░░░▄▀▀▀▀▄▐
░░░▌░░░░░░░░░▐░░░░░▄▄░░▌
░░█▀▄░░░▐░▐░░░░░░░░░░░█
░█░█░▀▀▄░▌░█░░░▀▀▄▄▄▄▀
█░░░▀▄░░▀▀▄▄█░░░░░▄▀
░░░░░░▀▄░░░░▀▀▄▄▄▀▐
█░░░░░░░▀▄░░░░░▐░▌▐
░█░░░░░░░░▀▄░░░▌░▐▌▐
░░█░░░░░░░░░█░▐░▄▄▌░█▀▄
░░░█░░░░░░░░░█▌▐░▄▐░░▀▄▀▀▄▄
░░░░█░░░░░░░░░▀▄░░▐░░░▀▄░░░▀▀▄▄
░░░░░▀▄░▄▀█░░░░░█░░▌░░░░▀▄░░░░░█""")


@bot.command()
async def Помощь(ctx):
    await ctx.send("""Мои команды:
    гитлер
    зига
    зорин
    виталя
    фаз
    старт
    !ПЕРЕД ВСЕМИ КОМАНДАМИ ПРЕФИКС '//' """)

@bot.command()
async def Профиль(ctx):
    caller = ctx.author.name
    caller = str(caller)
    for i in sql.execute(f"SELECT username FROM eblani WHERE username = '{caller}'"):
        idishka = i[0]
    for i in sql.execute(f"SELECT fazi FROM eblani WHERE username = '{caller}'"):
        balans = i[0]
    await ctx.send(f"Твой профиль:\nИмя: {idishka}\n Найдено фазчесалок: {balans} ")

@bot.command()
async def чичерин(ctx):
    member = await bot.fetch_user(802610385081073714)
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")
    await ctx.send(f"{member.mention} ты че хуита нулевая в рот тебя ебал, по головно ты своим ртом наши члены пересчитал")

@bot.command()
async def нацист(ctx):
    caller = ctx.author.name
    caller = str(caller)
    for i in sql.execute(f"SELECT ziga FROM eblani WHERE username = '{caller}'"):
        balans = i[0]
    await ctx.send(f"Ты нацист на {balans * 2}%")

@bot.command(aliases = ['калькулятор'])
async def __calc(ctx, chislo1: int = 0,  chislo2: int = 0):
    if chislo1 == None:
        await ctx.send("где первое число?")
    elif chislo2 == None:
        await ctx.send("А где второе число?")
    elif chislo1 > 1001:
        await ctx.send("ИДИ НАХУЙ С ТАКИМИ ЧИСЛАМИ")
    elif chislo2 > 1001:
        await ctx.send("ИДИ НАХУЙ С ТАКИМИ ЧИСЛАМИ")
    else:
        await ctx.send(f"Решил!!! сложение:{chislo1 + chislo2}\nУмножение:{chislo1 * chislo2}\n Степень:{chislo1 ** chislo2}\nВычитание:{chislo1 - chislo2}\nДеление:{chislo1 / chislo2}")

@bot.command(aliases = ['жабаскрипт', 'жаба', 'жаваскрипт', 'жава'])
async def __java(ctx, chislo1: str = None,  chislo2: str = None):
    if chislo1 == None:
        await ctx.send("где первое число?")
    elif chislo2 == None:
        await ctx.send("А где второе число?")
    else:
        await ctx.send(f"Решил!!! сложение: '{chislo1 + chislo2}'")

def minify_text(txt):
    return str(txt)
 # Захотелось использовать лямбду и всё в одну строку... но решил хоть как-то сделать читабельней


@bot.command(aliases = ['eval', 'aeval', 'evaulate', 'выполнить', 'exec', 'execute', 'calc', 'калк'])
async def __eval(ctx, *, content):

    # Проверка на то, записан ли код в Markdown'овском блоке кода и его "очистка":
    code = "\n".join(content.split("\n")[1:])[:-3] if content.startswith("```") and content.endswith("```") else content
    standart_args = { # Стандартные библиотеки и переменные, которые будут определены в коде. Для удобства. Кстати, я уже добавил несколько встроенных либ и переменных из d.py
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "tasks": tasks,
        "ctx": ctx,
        "asyncio": asyncio,
        "aiohttp": aiohttp,
        "os": os,
        'sys': sys,
        "time": time,
        "datetime": datetime,
        "random": random,
        "requests": requests
    }
    start = time.time() # запись стартового таймстампа для расчёта времени выполнения
    try:
        r = await aeval.aeval(f"""{code}""", standart_args, {}) # выполняем код
        ended = time.time() - start # рассчитываем конец выполнения
        print(r)
        if not code.startswith('#nooutput'): # Если код начинается с #nooutput, то вывода не будет
            embed = discord.Embed(title = "Успешно!", description = f"Выполнено за: {ended}", color = 0xfef201)
            """
             Есть нюанс: если входные/выходные данные будут длиннее 1024 символов, то эмбед не отправится, а функция выдаст ошибку.
             Именно поэтому сверху стоит print(r), а так же есть функция minify_text, которая
             минифицирует текст для эмбеда во избежание БэдРеквеста (который тут возникает когда слишком много символов). Поставил специально лимит на 900, чтобы точно хватило
            """
            embed.add_field(name = f'Входные данные:', value = f'`{minify_text(code) }`')
            embed.add_field(name = f'Выходные данные:', value = f'`{minify_text(r) }`', inline=False) 
            await ctx.send(embed = embed) # Отправка, уиии
    except Exception as e: # Ловим ошибки из строки с выполнением нашего кода (и не только!)
        ended = time.time() - start # Сново считаем время, но на этот раз до ошибки
        if not code.startswith('#nooutput'): # Аналогично коду выше
            code = minify_text(code)
            embed = discord.Embed(title = f"При выполнении возникла ошибка.\nВремя: {ended}", description = f'Ошибка:\n```py\n{e}```', color = 0x2e00ff)
            embed.add_field(name = f'Входные данные:', value = f'`{minify_text(code)}`', inline=False)
            await ctx.send(embed = embed)
            raise e # Ну и поднимем исключение



#@bot.command(aliases = ['adm', 'admin', 'pan', 'panel', 'Adm'])
#async def __adm(ctx):
#    caller = ctx.author.name
#    caller = str(caller)
#    if caller != 'Weeталий':
#        ctx.send("Зорин еблан, соси хуй")
#    else:
#        embed1 = discord.Embed(title="Админ панель 1", description='test 1')
#        embed2 = discord.Embed(title="Админ панель 2", description='test 2')
#        embed3 = discord.Embed(title="Админ панель 3", description='test 3')
#        embed4 = discord.Embed(title="Админ панель 5", description='test 4')
#        embeds = [embed1, embed2, embed3, embed4]
#        message = await ctx.send(embed=embed1)
#        page = pag(bot, message, only=ctx.author, use_more=False, embeds=embeds)
#        await page.start()


@bot.command(aliases = ['админ', 'адм', 'панель', 'adm', 'admin', 'pan'])
async def __admpanel(ctx):
    caller = ctx.author.name
    caller = str(caller)
    if caller != "Weeталий":
        ctx.send("Зорин еблан соси")
    else:
        await ctx.send(
            embed = discord.Embed(title = "welcome to the club buddy"),
            components = [
                Button(style=ButtonStyle.blue, label="Очистить базу данных"),
                Button(style=ButtonStyle.red, label="Отмена")
            ]
        )
        response = await bot.wait_for('button_click')
        if response.channel == ctx.channel:
            if response.component.label == "Очистить базу данных":
                sql.execute("DELETE FROM eblani")
                await response.respond(content = "База данных очищенна!")
            elif response.component.label == "Отмена":
                await response.respond(content = "Ну и нахуй ты ушел? :(")



bot.run(TOKEN)