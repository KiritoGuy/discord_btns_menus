# Package Name: [discord-btns-menus](https://pypi.org/project/discord-btns-menus/)

#### A responsive package for Buttons, DropMenus, Combinations and Paginator

##### • This module makes the process a lot easier !
[![python badge](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/ "Python")

[![CodeQL](https://github.com/Modern-Realm/discord_btns_menus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Modern-Realm/discord_btns_menus/actions/workflows/codeql-analysis.yml)
[![Generic badge](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/)
![Github License](https://img.shields.io/badge/license-MIT-blue)
![Windows](https://img.shields.io/badge/os-windows-yellow)
![Linux](https://img.shields.io/badge/os-linux-yellow)

[![GitHub stars](https://img.shields.io/github/stars/Modern-Realm/discord_btns_menus?color=gold)](https://github.com/Modern-Realm/discord_btns_menus/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Modern-Realm/discord_btns_menus?color=%2332cd32)](https://github.com/Modern-Realm/discord_btns_menus/network)
[![GitHub issues](https://img.shields.io/github/issues/Modern-Realm/discord_btns_menus?color=orange)](https://github.com/Modern-Realm/discord_btns_menus/issues)

#### Join [Official Discord Server](https://discord.gg/GVMWx5EaAN  "click to Join") for more guidance !

<hr/>

# Key Features

### <li> Buttons </li>

### <li> DropMenus </li>

### <li> Combinations (Usage of both Buttons & DropMenus) </li>

### <li> Paginator ![Generic badge](https://img.shields.io/badge/NEW-gold.svg) </li>

<hr/>

# Installation

Python 3.8 or higher is required !

```shell
# Linux/macOS
  python3 -m pip install discord-btns-menus

# Windows
  # Method-1:
    py -3 -m pip install discord-btns-menus
    # or
    python -m pip install discord-btns-menus
  # Method-2:
    pip install discord-btns-menus

# Using GIT for ALPHA or BETA Versions
  # Method-1:
    pip install git+https://github.com/Modern-Realm/discord_btns_menus.git
  # Method-2:
    pip install -U git+https://github.com/Modern-Realm/discord_btns_menus
```

<hr/>

# REQUIRED DEPENDENCIES

> #### You can use ANY ONE of the below Package

- ## [py-cord](https://github.com/Pycord-Development/pycord)
- ## [nextcord](https://github.com/nextcord/nextcord)
- ## [discord.pyV2.0](https://github.com/Rapptz/discord.py)
- ## [disnake](https://github.com/DisnakeDev/disnake) <br/>
  `For disnake you should Refactor all discord terms to disnake terms to make Package work`

> <b>Note:</b> Don't install more than one **DEPENDENCY !**

<hr/>

# Sample Usage

Create a file with '.py ' extension, Like: **main.py**

```python
from btns_menus.Buttons import SButton, SingleButton
from btns_menus.DropMenus import SDropMenu, DuoDropMenu
from btns_menus.Combinations import BtnAndDropMenu, MultiBtnAndMenu

import discord
from discord.ext import commands

intents = discord.Intents.all()
activity = discord.Game("&help - phoenix")

client = commands.Bot(command_prefix="&", intents=intents, activity=activity)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Bot is Ready !")


@client.command()
async def test(ctx):
    user = ctx.author

    btn1 = SButton(label="Hello", response="Hello have a nice day !")

    view_ = SingleButton(user, btn1).view()
    await ctx.send("click here !", view=view_)


if __name__ == "__main__":
    client.run('token')

```

<hr/>

# Example for <u>Buttons</u>:

Button type
**[DuoButton](https://github.com/Modern-Realm/discord_btns_menus/blob/main/package/btns_menus/Buttons.py)**, for more
samples go to <a href="https://github.com/Modern-Realm/discord_btns_menus/blob/main/Examples/buttons.py">
Examples/Buttons</a>

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author
    btn1 = SButton(label="Wave 👋", response=f"Hello {user.mention} have a nice day !")
    btn2 = SButton(label="Bye", response=f"Bye {user.mention} see you later !", style=ButtonStyle.secondary)
    view_ = DuoButton(user, btn1, btn2).view()

    await ctx.send(f"Sample buttons ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/Modern-Realm/discord_btns_menus/blob/main/media/bin/sample_buttons.gif" 
    alt="Button-Samples.gif" height="400" width="300">
</p>

<hr/>

# Examples for <u>DropMenus</u>:

DropMenu type
**[DuoDropMenu](https://github.com/Modern-Realm/discord_btns_menus/blob/main/package/btns_menus/DropMenus.py)**, for
more samples go to <a href="https://github.com/Modern-Realm/discord_btns_menus/blob/main/Examples/drop_menus.py">
Examples/DropMenuss</a>

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author

    menu1 = SDropMenu(placeholder="select one", options=[
        SelectOption(label="username"),
        SelectOption(label="None of the above")
    ])
    menu1.add_query(("username", f"username: {user.name}"))

    menu2 = SDropMenu(placeholder="choose one", options=[
        SelectOption(label="discriminator"),
        SelectOption(label="None of the above")
    ])
    menu2.add_query(("discriminator", f"discriminator: {user.discriminator}"))

    view_ = DuoDropMenu(user, menu1, menu2).view()

    await ctx.send(f"Sample buttons ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/Modern-Realm/discord_btns_menus/blob/main/media/bin/sample_dropmenus.gif"
    alt="DropMenu-Samples.gif" height="400" width="300">
</p>

<hr/>

# Buttons & DropMenus combination

##### • In this feature you can make & send Buttons and DropMenus together

##### • For more examples for mixture of btns & menus go to <u><a href="https://github.com/Modern-Realm/discord_btns_menus/blob/main/Examples/combinations.py">Examples/combinations</a></u>

<br/>

## Examples for <u>combinations</u>

Usage of both Buttons and DropMenus at once ...

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author

    btn1 = SButton(label="Delete Menu", style=ButtonStyle.danger, delete_msg=True)
    menu1 = SDropMenu(placeholder="Select one", options=[
        SelectOption(label="About Python", value="python")
    ])
    menu1.add_query(("python", "Python is a widely-used, interpreted, object-oriented and"
                               " high-level programming language with dynamic semantics, used for general-purpose programming.\n"
                               "It was created by Guido van Rossum, and first released on February 20, 1991."))

    view_ = BtnAndDropMenu(user, btn1, menu1).view()

    await ctx.send(f"Sample buttons & Menus combinations ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/Modern-Realm/discord_btns_menus/blob/main/media/bin/sample_combinations.gif"
    alt="Sample-Combinations.gif" height="400" width="300">
</p>

<hr/>

# Example for <u>MultiButtons</u>

Button type
**[MultiButton](https://github.com/Modern-Realm/discord_btns_menus/blob/main/package/btns_menus/Buttons.py#L190)**, for
more samples go to <a href="https://github.com/Modern-Realm/discord_btns_menus/blob/main/btns_menus/Buttons.py">
Examples/Buttons</a>

The Process
for **[MultiDropMenu](https://github.com/Modern-Realm/discord_btns_menus/blob/main/package/btns_menus/DropMenus.py#L194)**
will be the same ...

```python
@client.command()
async def test(ctx):
    user: discord.Member = ctx.author
    user_avatar = user.display_avatar or user.default_avatar

    btn1 = SButton(label="username", style=ButtonStyle.primary, response=user.name)
    btn2 = SButton(label="discriminator", style=ButtonStyle.secondary, response=user.discriminator)
    btn4 = SButton(label="Avatar", style=ButtonStyle.secondary, response=str(user_avatar), ephemeral=True)
    btn3 = SButton(label="Server Name", style=ButtonStyle.secondary, response=user.guild.name)
    btn5 = SButton(label="Display Name", style=ButtonStyle.secondary, response=user.display_name)
    btn6 = SButton(label="Delete Menu", style=ButtonStyle.danger, delete_msg=True)

    buttons = [btn1, btn2, btn3, btn4, btn5, btn6]

    view_ = MultiButton(user, buttons).view()

    await ctx.send(f"Sample Usage of Multi Buttons ...", view=view_)
```

### Preview:

<p align="center">
    <img src="https://github.com/Modern-Realm/discord_btns_menus/blob/main/media/bin/sample_multibuttons.gif"
    alt="Sample-Combinations.gif" height="400" width="300">
</p>

<hr/>

# Example for Paginator

[![Generic badge](https://img.shields.io/badge/NEW-Feature-gold.svg)](https://shields.io/)

It is used for help commands which sends the embeds like page-wise using buttons & Drop Menus

```python
from btns_menus.Paginator import *
from datetime import datetime
import discord


# This function is for sample purposes, use discord.Embed instead [RECOMMENDED]
def embed(context: str, color=0xffff00, timestamp: bool = False) -> discord.Embed:
    present_time = datetime.utcnow() if timestamp else None
    em = discord.Embed(description=context, color=discord.Color(color), timestamp=present_time)
    return em


@client.command()
async def help(ctx):
    user = ctx.author

    embeds = [embed("embed-1"), embed("embed-2"), embed("embed-3"),
              embed("embed-4"), embed("embed-5"), embed("embed-6")]
    cmd_list = [
        SOption(name="moderation", embed_=embeds[1]),
        SOption(name="giveaways", embed_=embeds[2]),
        SOption(name="links", embed_=embeds[3])
    ]

    view_ = Paginator(user, embeds, commands_list=cmd_list).view()
    await ctx.send(embed=embeds[0], view=view_)
```

<p align="center">
    <img src="https://github.com/Modern-Realm/discord_btns_menus/blob/main/media/bin/sample_paginator.gif"
    alt="Sample-Combinations.gif" height="400" width="300">
</p>

<hr/>

# Project Links

You can get support/help/guidance from below social-media links

- [Home Page](https://github.com/Modern-Realm)
- [Official Discord Server](https://discord.gg/GVMWx5EaAN)
- [PyPi Package](https://pypi.org/project/discord-btns-menus/)
- [Documentation](https://github.com/Modern-Realm)

<hr/>
