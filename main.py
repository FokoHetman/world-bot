from discord.ui import Button, View
from discord.utils import get
from discord.commands import Option
import discord
import random as r
import time as t
import asyncio
import json
import os
import datetime
from Classkraj import Kraj
timecount = 1
surowce = ['węgiel', 'żelazo', 'srebro', 'uran', 'złoto', "kobalt", "ropa naftowa"]

from map_gen import Map




class unit():
    def __init__(self, Classname, type, tier, cost, surowiec, surowiecilosc, cooldown):
        self.name=Classname
        self.type=type
        self.tier=int(tier)
        self.cost=int(cost)
        self.surowiec=surowiec
        self.surowiecilosc=int(surowiecilosc)
        self.cooldown=cooldown*60
units = {
    #sky
    "f15":unit("finf15","sky", 1, 50000, "zelazo", 50, 5),
    "mig29":unit("Mig29","sky", 2, 55000, "zelazo", 55, 8),
    "f16":unit("finf15","sky", 3, 60000, "srebro", 60, 10),
    "mh53":unit("finmh53","sky", 3, 62000, "zloto", 55, 10),
    "f35":unit("finf15","sky", 4, 70000, "zelazo", 70, 12),
    "lockheed":unit("finlockheed","sky", 4, 680000, "zelazo", 65, 12),
    "mig35":unit("Mig35","sky", 5, 75000, "srebro", 80, 15),
    "nighthawk":unit("finnighthawk","sky", 5, 80000, "srebro", 90, 15),
    "lancer":unit("Lancer","sky", 6, 100000, "zelazo", 150, 18),
    #ground
    "dywizja":unit("findywizje","ground", 1, 40000, "zelazo", 50, 5),
    "snajper":unit("snajperzy","ground", 2, 45000, "zelazo", 55, 8),
    "drużyna gazująca":unit("ekipagaz","ground", 3, 50000, "srebro", 60, 10),
    "działa przeciwlotnicze":unit("finprzeciwlot","ground", 4, 75000, "zloto", 65, 12),
    "artyleria":unit("finf15","ground", 5, 85000, "zelazo", 80, 15),
    "2s19":unit("betterarty","ground", 6, 95000, "srebro", 90, 18),
    "abrams":unit("abrams","ground", 6, 100000, "zelazo", 200, 18),
    #water
    "navy":unit("finNAVY","water", 1, 35000, "zloto", 60, 5),
    "okręt podwodny":unit("finpodwodne","water", 1, 50000, "zloto", 50, 5),
    "korweta":unit("korwety","water", 2, 55000, "zelazo", 55, 8),
    "fregata":unit("fregaty","water", 3, 60000, "srebro", 60, 10),
    "pancernik":unit("finf15","water", 4, 70000, "zelazo", 70, 12),
    "niszczyciel":unit("Mig35","water", 5, 75000, "srebro", 80, 15),
    "lotniskowiec":unit("finnighthawk","water", 6, 100000, "srebro", 90, 15),
    "okręt desantowy":unit("findesantowce","water", 6, 150000, "zelazo", 150, 18),
    #wywiad
    "zwiadowca":unit("finzwiadowca","wywiad", 1, 10000, "zelazo", 20, 15),
    "pluskwa":unit("pluskwy","wywiad", 1, 20000, "srebro", 25, 15),
    #bomby
    "granat":unit("nades","bomb", 1, 35000, "uran", 10, 5),
    "napalm":unit("bb","bomb", 2, 55000, "zloto", 20, 5),
    "bunker buster":unit("korwety","bomb", 2, 55000, "zelazo", 35, 8),
    "rakieta balistyczna":unit("balistyczne","bomb", 3, 60000, "srebro", 50, 10),
    "hwaseong":unit("Hwaseong","bomb", 4, 70000, "zelazo", 70, 12),
    "car":unit("tzaar","bomb", 5, 75000, "srebro", 80, 15)
         }


client = discord.Bot(intents=discord.Intents.all())
tree=client


map = client.create_group("map", "Mapmapmapmapmap map")
@map.command(name="gen")
async def mapgen(interaction):
    await interaction.response.defer()

    mapped={}
    with open(f"{interaction.guild.id}kraje.json","r+") as f:
        k=json.load(f)
    for i in k:
        x=r.randint(0,1000)
        y=r.randint(0,1000)
        mapped[f"{x} {y}"]=i
    map=Map(mapped)
    map.gen()
    await interaction.respond("Gotowe!", file=discord.File("map.png"))
    
@client.slash_command(description="Pong!") 
async def ping(ctx):
    await ctx.respond(f"Pong! {round(client.latency*1000, 0)}ms")
    
import os

def read(kraj, id):
    i=f"{kraj}"
    with open(f"{id}{kraj}.json", "r") as f:
        z=json.load(f)
        
        krajedict["{}".format(i)] = Kraj(i)
        krajedict["{}".format(i)].wywiadtree = z["wywiadtree"]
        krajedict["{}".format(i)].nades = z["granaty"]
        krajedict["{}".format(i)].napalm=z["napalm"]
        krajedict["{}".format(i)].bb=z["bunker buster"]
        krajedict["{}".format(i)].balistyczne=z["pociski balistyczne"]
        krajedict["{}".format(i)].Hwaseong=z["Hwaseong"]
        krajedict["{}".format(i)].tzaar=z["CAR"]


        krajedict["{}".format(i)].finbudzet=z["finbudzet"]
        krajedict["{}".format(i)].finludnosc=z["finludnosc"]
        krajedict["{}".format(i)].finteatralnaobrona=z["finteatralnaobrona"]
        krajedict["{}".format(i)].finNAVY=z["finNAVY"]
        krajedict["{}".format(i)].finbomby=z["finbomby"]
        krajedict["{}".format(i)].finf15=z["finf15"]
        krajedict["{}".format(i)].finf16=z["finf16"]
        krajedict["{}".format(i)].finf35=z["finf35"]
        krajedict["{}".format(i)].finlockheed=z["finlockheed"]
        krajedict["{}".format(i)].finmh53=z["finmh53"]
        krajedict["{}".format(i)].finhelikopterypiechoty=z["finhelikopterypiechoty"]
        krajedict["{}".format(i)].finnighthawk=z["finnighthawk"]
        krajedict["{}".format(i)].finpodwodne=z["finpodwodne"]

        krajedict["{}".format(i)].fregaty=z["fregaty"]

        krajedict["{}".format(i)].korwety=z["korwety"]
        krajedict["{}".format(i)].finnavy=z["Navy"]
        krajedict["{}".format(i)].findesantowce=z["okret desantowy"]

        krajedict[f"{i}"].abrams=z["abrams"]
        krajedict[f"{i}"].ekipagaz=z["drużyna gazująca"]
        krajedict[f"{i}"].snajperzy=z["snajperzy"]
        krajedict[f"{i}"].betterarty=z["2S19"]
        krajedict[f"{i}"].pluskwy=z["pluskwa"]
        krajedict["{}".format(i)].niszczyciel=z["niszczyciel"]

        krajedict["{}".format(i)].pancernik=z["pancernik"]
        krajedict["{}".format(i)].Mig29=z["Mig29"]
        krajedict["{}".format(i)].Mig35=z["Mig35"]
        krajedict[f"{i}"].Lancer=z["Lancer"]
        krajedict["{}".format(i)].finlodzie=z["finlodzie"]
        krajedict["{}".format(i)].finlotniskowce=z["finlotniskowce"]
        krajedict["{}".format(i)].finzwiadowca=z["finzwiadowca"]
        krajedict["{}".format(i)].findywizje=z["findywizje"]
        krajedict["{}".format(i)].finczolg=z["finczolg"]
        krajedict["{}".format(i)].finprzeciwlot=z["finprzeciwlot"]
        krajedict["{}".format(i)].finartyleria=z["finartyleria"]
        krajedict["{}".format(i)].finkawaleria=z["finkawaleria"]
        krajedict["{}".format(i)].finlandbonus=z["finlandbonus"]
        krajedict["{}".format(i)].finlanddebonus=z["finlanddebonus"]
        krajedict["{}".format(i)].finpodatek=z["finpodatek"]
        krajedict["{}".format(i)].finturystyka=z["finturystyka"]
        krajedict["{}".format(i)].finzloto=z["finzloto"]
        krajedict["{}".format(i)].finuran=z["finuran"]
        krajedict["{}".format(i)].finsrebro=z["finsrebro"]
        krajedict["{}".format(i)].finwegiel=z["finwegiel"]
        krajedict["{}".format(i)].finbudzet=z["finbudzet"]
        krajedict["{}".format(i)].finzelazo=z["finzelazo"]

        krajedict["{}".format(i)].watertree=z["watertree"]

        krajedict["{}".format(i)].skytree=z["skytree"]

        krajedict["{}".format(i)].groundtree=z["groundtree"]
        
        krajedict["{}".format(i)].bombtree=z["bombtree"]
        krajedict["{}".format(i)].finnafta=z["finnafta"]
        krajedict["{}".format(i)].finkobalt=z["finkobalt"]



startludnosc = 10000





krajedict = {}


"""grupy"""

unitgroup = client.create_group("jednostka", "Zarządzaj jednostkami")
wojna = client.create_group("wojna", "Zarządzaj wojną")
kraje = client.create_group("kraj", "Zarządzaj krajem")
sojusze = client.create_group("sojusz", "Zarządzaj sojuszami")
ulepsz = client.create_group("ulepsz", "Ulepszanie")
operator = client.create_group("operator", "Tylko dla world operatora!")
aukcja = client.create_group("aukcja", "Zarządzanie aukcjami")
rynek = client.create_group("rynek", "Zarządzanie rynkiem")


""" Quick Action"""
#samples
views = {}
opts = []
countrrr = {}
    
#Ulepsz


class sojuszeactions(discord.ui.View):
    @discord.ui.select(
        placeholder = "Wybierz akcję!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Lista sojuszy",
                description="Sprawdź listę sojuszy."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        with open(f"{interaction.guild.id}sojusze.json", "r+") as f:
            z = json.load(f)
        srt=""
        for i in z:
            srt=srt+f"\n {i}: {z[i]}"
        embed=discord.Embed(color=discord.Color.purple(), title="Sojusze", description=srt)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.message.delete()


class ulepszactions(discord.ui.View):
    @discord.ui.select(
        placeholder = "Wybierz aspekt do ulepszenia!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Turystyka",
                description="Ulepsz turystykę."
            ),
            discord.SelectOption(
                label="Drzewko Technologiczne",
                description="Ulepsz drzewko technologiczne."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        kraj = countrrr[str(interaction.user.id)]
        ctx=interaction
        if select.values[0]=="Turystyka":
            role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
            if role is not None and role.name == f"{kraj}":
                with open(f'{interaction.guild.id}kraje.json', "r") as f:
                    kraje = json.load(f)
                for i in kraje:
                    if i==kraj:
                        finbudzet = krajedict[f'{kraj}'].finbudzet
                        if finbudzet>5000000:
                            async def callback_tur(interaction):
                                finbudzet = krajedict[f'{kraj}'].finbudzet
                                finbudzet-=5000000
                                krajedict[f'{kraj}'].finbudzet=finbudzet
                                desc = f'ulepszono turystykę w kraju o 10%'
                                embed = discord.Embed(color=discord.Color.green(), title=f'TURYSTYKA', description=desc)
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                                krajedict[f'{kraj}'].finturystyka+=0.1
                            async def callback_tur_dec(interaction):
                                embed = discord.Embed(color=discord.Color.green(), description="anulowano")
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                            view_tur=View()
                            button_tur = Button(label="Tak", emoji="✔️", style=discord.ButtonStyle.green)
                            button_tur_dec = Button(label="Nie", style=discord.ButtonStyle.red)
                            button_tur.callback=callback_tur
                            button_tur_dec.callback=callback_tur_dec
                            view_tur.add_item(button_tur)
                            view_tur.add_item(button_tur_dec)
                            embed = discord.Embed(color=discord.Color.purple(), description="Czy jestes pewien ze chcesz ulepszyc turystyke za 5,000,000 waluty?")
                            await interaction.response.send_message(embed=embed, ephemeral=True, view=view_tur)
                        else:
                            desc = f'za mało funduszy!'
                            embed = discord.Embed(color=discord.Color.green(), title=f'TURYSTYKA', description=desc)
                            my_msg = await interaction.response.send_message(embed=embed, ephemeral=True)
                        krajedict[f'{kraj}'].finbudzet = finbudzet
            save(f"{kraj}", interaction.guild.id)
            await interaction.message.delete()
        else:
            class TreeUI(discord.ui.View):
                @discord.ui.select(
                    placeholder = "Wybierz drzewko!",
                    min_values = 1,
                    max_values = 1,
                    options = [
                        discord.SelectOption(
                            label="Wodne",
                            description="Ulepsz drzewko wodne."
                        ),
                        discord.SelectOption(
                            label="Naziemne",
                            description="Ulepsz drzewko naziemne."
                        ),
                        discord.SelectOption(
                            label="Powietrzne",
                            description="Ulepsz drzewko powietrzne."
                        ),
                        discord.SelectOption(
                            label="Wybuchowe",
                            description="Ulepsz drzewko wybuchowe."
                        )
                    ]
                )
                async def select_callback(self, select, interaction):
                    typ = select.values[0].lower()
                    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
                    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
                    if role is not None and role.name == f"{kraj}":
                        tier={}
                        tier1=5000000
                        tier2=7500000
                        tier3=10000000
                        tier4=15000000
                        tier5=20000000
                        tier["tier1"] = tier1
                        tier["tier2"] = tier2
                        tier["tier3"] = tier3
                        tier["tier4"] = tier4
                        tier["tier5"] = tier5
                        type = typ.lower()
                        if type=="info":
                            embed = discord.Embed(color=discord.Colour(0xFFFF00), title="Upgrade Tree", description = f"Koszty ulepszenia na 2tier: 5mln,\n Koszty ulepszenia na 3tier: 7.5mln,\n Koszty ulepszenia na 4tier: 10mln,\nKoszty ulepszenia na 5tier: 15mln,\nKoszty ulepszenia na 6tier: 20mln.")
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                        toooogle=False
                        for type in types:
                            if type==typ:
                                toooogle=True
                                new_type=type
                                typ=types[f"{typ}"]
                                up_kraj=krajedict[f"{kraj}"].__dict__
                                if up_kraj[f'{typ.var}']==6:
                                    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.yellow(), description="Juz masz maksymalny poziom drzewka!"), ephemeral=True)
                                else:
                                    if up_kraj["finbudzet"]>= tier[f"tier{up_kraj[f'{typ.var}']}"]:
                                        if up_kraj[f"fin{typ.surowiec}"]>=200:
                                            async def cbup1(interaction):
                                                up_kraj['finbudzet']-=tier[f"tier{up_kraj[f'{typ.var}']}"]
                                                up_kraj[f'fin{typ.surowiec}']-=200
                                                up_kraj[f'{typ.var}']+=1
                                                embed = discord.Embed(color=discord.Color.green(), title="Ulepszanie drzewka", description = f"Ulepszono drzewko technologiczne {new_type} na tier{up_kraj[f'{typ.var}']}!")
                                                await interaction.response.send_message(embed=embed, ephemeral=True)
                                                for i in up_kraj:
                                                    setattr(Kraj, i, up_kraj[i])
                                                save(f"{kraj}", interaction.guild.id)
                                            async def cbup2(interaction):
                                                await interaction.response.send_message(embed=discord.Embed(color=discord.Color.green(), description="Anulowano"), ephemeral=True)
                                            butup1=Button(label="Ulepsz",style=discord.ButtonStyle.green, emoji="✔️")
                                            butup2=Button(label="Anuluj", style=discord.ButtonStyle.red)
                                            
                                            
                                            butup1.callback=cbup1
                                            butup2.callback=cbup2
                                            view_up=View()
                                            view_up.add_item(butup1)
                                            view_up.add_item(butup2)
                                            ae=up_kraj[f'{typ.var}']
                                            brainfuck=f"tier{ae}"
                                            ae2=f'{tier[brainfuck]}'
                                            embed=discord.Embed(color=discord.Color.purple(), title="Ulepsz drzewko",description=f"Czy jestes pewien, ze chcesz ulepszyc drzewko technologiczne {type} na poziom {ae+1} za 200 {typ.surowiec} i {int(ae2): ,} budzetu?")
                                            await interaction.response.send_message(embed=embed, view=view_up, ephemeral=True)
                                        else:
                                            embed = discord.Embed(color=discord.Color.red(), title="Za malo surowca", description = f"Potrzebujesz  200 sztuk {typ.surowiec}!")
                                            await interaction.response.send_message(embed=embed, ephemeral=True)
                                    else:
                                        ae=up_kraj[f'{typ.var}']
                                        embed = discord.Embed(color=discord.Color.red(), title="Za malo pieniedzy", description = f"Potrzebujesz  {(tier[f'tier{ae}']): ,} budzetu!")
                                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        if toooogle==False:
                            embed = discord.Embed(color=discord.Color.red(), title="Zly typ", description = f"Wpisano zly typ!")
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                    
                    else:
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    save(f"{kraj}", interaction.guild.id)
                    await interaction.message.delete()
            await interaction.message.edit("Teraz wybierz drzewko!", view=TreeUI())
            
            
            
            
            
            
            
            
    
#Kraj
class countryactions(discord.ui.View):
    @discord.ui.select(
        placeholder = "Wybierz akcję!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Info",
                description="Sprawdź info o swoim kraju."
            ),
            discord.SelectOption(
                label="Lista",
                description="Sprawdź listę aktywnych krajów."
            ),
            discord.SelectOption(
                label="Mobilizacja",
                description="Mobilizuj jednostkę."
            ),
            discord.SelectOption(
                label="Wykopaliska",
                description="Rozpocznij wykopaliska."
            ),
            discord.SelectOption(
                label="Podatki",
                description="Zarządzaj podatkami w kraju."
            ),
            discord.SelectOption(
                label="Zapłać",
                description="Zapłać wybranemu krajowi."
            )
            
        ]
    )
    async def select_callback(self, select, interaction):
        kraj = countrrr[str(interaction.user.id)]
        if select.values[0]=="Info":
            read(f"{kraj}", interaction.guild.id)
            role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
            if role is not None and role.name == f"{kraj}":
                info = "**INFO O KRAJU:**\n"
                sss = krajedict[f"{kraj}"].__dict__
                for i in sss:
                    if i=="finlandbonus" or i=="finlanddebonus" or i=="toogledmobi" or i=="toogledwykop":
                        pass
                    else:
                        li = i
                        i = i.replace("name", "nazwa")
                        i = i.replace("tree", " drzewko")
                        i = i.replace("water", "wodne")
                        i = i.replace("_", " ")
                        i = i.replace("ground", "naziemne")
                        i = i.replace("sky", "powietrzne")
                        i = i.replace("bomb", "bombowe")
                        i = i.replace("tzaar", "Car")
                        i = i.replace("fin", "")
                        i = i.replace("nades", "granaty")
                        i = i.replace("przeciwlot", "działa przeciwlotnicze")
                        i = i.replace("nades", "granaty")
                        info = f"{info}\n{i}: {sss[li]},"
                title = "INFO"
                embed = discord.Embed(color=discord.Colour(0xFFFF00), title=title, description=info)

                i=kraj
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await interaction.message.delete()
        elif select.values[0]=="Lista":
            with open("bannedids.json",  'r+') as f:
                z = json.load(f)
            if f"{interaction.user.id}" in z:
                await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
                return
            with open(f"{interaction.guild.id}kraje.json", "r+") as f:
                z = json.load(f)
                krajestring="**kraje**"
                for i in z:
                    krajestring = krajestring + f"\n {i}"
                await interaction.response.send_message(embed=discord.Embed(color = discord.Color.purple(), description=krajestring), ephemeral=True)
            await interaction.message.delete()
        elif select.values[0]=="Podatki":
            class MyModal(discord.ui.Modal):
                def __init__(self, *args, **kwargs) -> None:
                    super().__init__(*args, **kwargs)

                    self.add_item(discord.ui.InputText(label="Kwota:", placeholder="Wpisz kwotę nowych podatków, max. 6000"))

                async def callback(self, interaction: discord.Interaction):
                    try:
                        kwota = int(self.children[0].value)
                    except:
                        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), title="Błąd", description="Kwota nie jest liczbą. Spróbuj ponownie"))
                    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
                    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
                    try:
                        a = krajedict[kraj]
                    except:
                        await interaction.response.send_message('nie znaleziono kraju', hidden=True)
                    if role is not None and role.name == f"{kraj}":
                        read(kraj, interaction.guild.id)
                        before=krajedict[f'{kraj}'].finpodatek
                        if kwota<=6000:
                            krajedict[f'{kraj}'].finpodatek = kwota
                            save(kraj, interaction.guild.id)
                            embed=discord.Embed(color=discord.Color.blue(), description=f"Zmieniono kwote podatkow z {before} na {kwota}")
                        else:
                            embed=discord.Embed(color=discord.Color.blue(), description=f"Za duza kwota! mozesz ustawic maksymalnie 6000")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    await interaction.message.edit("Zakończono")
                    await interaction.message.delete()
            await interaction.response.send_modal(MyModal(title="Podatki"))
        elif select.values[0]=="Mobilizacja":
            class Mobi(discord.ui.View):
                s_uni = []
                for i in units:
                    s_uni.append(discord.SelectOption(label=str(i), description=str(i)))
                s_uni2 = []
                for i in range(24):
                    s_uni2.append(s_uni[i])
                @discord.ui.select(
                    placeholder = "Wybierz jednostkę!",
                    min_values = 1,
                    max_values = 1,
                    options = s_uni2
                )
                async def select_callback(self, select, interaction):
                    jednostka=select.values[0]
                    class MobiModal(discord.ui.Modal):
                        def __init__(self, *args, **kwargs) -> None:
                            super().__init__(*args, **kwargs)

                            self.add_item(discord.ui.InputText(label="Ilość:", placeholder="Wpisz ilość jednostki do zmobilizowania, max. 20"))

                        async def callback(self, interaction: discord.Interaction):
                            try:
                                ilosc = int(self.children[0].value)
                            except:
                                await interaction.response.send_message("Zła ilość!", ephemeral=True)
                                return
                            if ilosc>20:
                                embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="za duża ilość!")
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                            else:
                                role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
                                if role==None:
                                    with open(f"{ctx.guild.id}countrytypes.json", 'r+') as f:
                                        types = json.load(f)
                                        if f"{kraj} owner" in types:
                                            owner = types[f'{kraj} owner']
                                            role2 = discord.utils.get(interaction.user.roles, name=f"{owner}")
                            embed = discord.Embed(title="Unsuccessfull operation", description = "Zadanie nie powiodło się, sprawdź czy posiadasz rolę kraju")
                            if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name==f"{owner}":
                                e=False
                                if jednostka in units:
                                    e= True
                                    if e:
                                        i = jednostka
                                        unit =  units[i]
                                        simple=krajedict[f"{kraj}"].__dict__
                                        if simple[f"{unit.type}tree"]>=unit.tier:
                                            if simple["finbudzet"]>=unit.cost*ilosc:
                                                if simple[f"fin{unit.surowiec}"]>=unit.surowiecilosc:
                                                    embed = discord.Embed(color=discord.Color.purple(), title="Mobilizacja", description=f"Rozpoczeto mobilizacje {unit.name} za {(unit.cost*ilosc): ,} oraz {unit.surowiecilosc}x{unit.surowiec}")                
                                                    await interaction.response.send_message(embed=embed, ephemeral=True)
                                                    krajedict[f"{kraj}"].toogledmobi+=1
                                                    await asyncio.sleep(units[jednostka].cooldown*ilosc)
                                                    krajedict[f"{kraj}"].toogledmobi-=1
                                                    simple["finbudzet"]-=unit.cost*ilosc
                                                    simple[f"fin{unit.surowiec}"]>=unit.surowiecilosc
                                                    embed = discord.Embed(color=discord.Color.purple(), title="Mobilizacja", description=f"Zakonczono mobilizacje {unit.name}")
                                                    simple[f"{unit.name}"]+=ilosc
                                                    simple["finbudzet"]-=unit.cost*ilosc
                                                    simple[f"fin{unit.surowiec}"]-=unit.surowiecilosc
                                                    for i in simple:
                                                        setattr(Kraj, i, simple[i])
                                                    try:
                                                        await interaction.user.send(embed=embed)
                                                    except:
                                                        await interaction.channel.send(f"{ctx.author.mention}, mobilizacja zakonczona")
                                                else:
                                                    embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"za malo {unit.surowiec}, potrzeba {unit.surowiecilosc}")
                                                    await interaction.response.send_message(embed=embed, ephemeral=True)
                                            else:
                                                embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Za malo budzetu, potrzeba {(unit.cost*ilosc): ,}")
                                                await interaction.response.send_message(embed=embed, ephemeral=True)
                                        else:
                                            embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Za niski poziom drzewka, wymagany jest {unit.tier} poziom drzewka")
                                            await interaction.response.send_message(embed=embed, ephemeral=True)
                                if e==False:
                                    embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Jednostka nie istnieje!")
                                    await interaction.response.send_message(embed=embed, ephemeral=True)
                        
                            save(f"{kraj}", interaction.guild.id)
                            await interaction.message.delete()
                    
                    await interaction.message.edit(f"Świetnie, teraz wybierz ilość.")
                    await interaction.response.send_modal(MobiModal(title="Mobilizacja"))
            await interaction.message.edit(f"Świetnie, teraz wybierz jednostkę.", view=Mobi())
                
                
        elif select.values[0]=="Wykopaliska":
            class WykUI(discord.ui.View):
                sur = []
                for i in surowce:
                    sur.append(discord.SelectOption(label=i, description=i))
                    
                
                @discord.ui.select(
                    placeholder = "Wybierz surowiec!",
                    min_values = 1,
                    max_values = 1,
                    options = sur
                )
                async def select_callback(self, select, interaction):
                    surowiec = select.values[0]
                    class WykModal(discord.ui.Modal):
                        def __init__(self, *args, **kwargs) -> None:
                            super().__init__(*args, **kwargs)

                            self.add_item(discord.ui.InputText(label="Kwota:", placeholder=f"Ile `{surowiec}` chcesz wykopać. max. 40"))

                        async def callback(self, interaction: discord.Interaction):
                            try:
                                ilosc = int(self.children[0].value)
                            except:
                                await interaction.response.send_message("zła ilość", ephemeral=True)
                                return
                            ctx=interaction
                            
                            role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
                            with open(f"{ctx.guild.id}countrytypes.json", "r") as f:
                                z = json.load(f)
                            for i in z:
                                if i==f"{kraj} owner":
                                    zwierzchik = z[f"{kraj} owner"]
                                    print(zwierzchik)
                                    role2 = discord.utils.get(ctx.user.roles, name=f"{zwierzchik}")
                            if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name == f"{zwierzchik}":
                                if krajedict[f"{kraj}"].toogledwykop>=2:
                                    embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="możesz mieć maksymalnie 2 włączone wykopy na raz")
                                    await interaction.response.send_message(embed=embed, ephemeral=True)
                                else:
                                    if ilosc>40:
                                        embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="możesz wykopać maksymalnie 40kg na raz")
                                        await interaction.response.send_message(embed=embed, ephemeral=True)
                                    else:
                                        krajedict[f"{kraj}"].toogledwykop+=1
                                        desc=f'kopanie {surowiec} rozpoczęte, wyniki będą przesłane na **DM**.'
                                        embed = discord.Embed(color=discord.Color.blue(), title='wykopy', description=desc)
                                        await interaction.response.send_message(embed=embed, ephemeral=True)
                                        mins = ilosc*timedelays[surowiec]
                                        await asyncio.sleep(mins*timecount)
                                        krajedict[f"{kraj}"].toogledwykop-=1
                                        ssimple = krajedict[f"{kraj}"].__dict__
                                        ssimple[corrects[str(surowiec)]]+=ilosc
                                                            
                                        try:
                                            embed = discord.Embed(color=discord.Color.green(), title='wykopy', description=f'kopanie {surowiec} w ilości {ilosc} zakończone.')
                                            await interaction.user.send(embed=embed)
                                        except:
                                            embed = discord.Embed(color=discord.Color.green(), title='wykopy', description=f'kopanie zakończone {interaction.user.mention}')
                                            await interaction.channel.send(embed=embed)
                                            for i in ssimple:
                                                setattr(Kraj, i, ssimple[i])
                                            
                            save(f"{kraj}", ctx.guild.id)
                            await interaction.message.delete()
                            
                    await interaction.response.send_modal(WykModal(title="Wykopaliska"))
                    await interaction.message.edit("Teraz podaj ilość.")
            await interaction.message.edit("Teraz wybierz surowiec.", view=WykUI())
            
            
            
        else:
            opts = []
            for i in krajedict:
                opts.append(discord.SelectOption(label=i, description=i))
            
            
            
            class CelUI(discord.ui.View):
                @discord.ui.select(
                    placeholder = "Wybierz kraj któremu chcesz zapłacić!",
                    min_values = 1,
                    max_values = 1,
                    options = opts
                )
                async def select_callback(self, select, interaction):
                    krajdocelowy=select.values[0]
                    class CelModal(discord.ui.Modal):
                        def __init__(self, *args, **kwargs) -> None:
                            super().__init__(*args, **kwargs)

                            self.add_item(discord.ui.InputText(label="Kwota:", placeholder="Ile chcesz zapłacić komuś, minimum 100.000"))

                        async def callback(self, interaction: discord.Interaction):
                            try:
                                kwota = int(self.children[0].value)
                            except:
                                await interaction.response.send_message("Zła kwota", ephemeral=True)
                                return
                            if kwota>=100000:
                
                                role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
                                embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
                                if role is not None and role.name == f"{kraj}":
                                    if krajedict[f"{kraj}"].finbudzet>=kwota:
                                        krajedict[f"{kraj}"].finbudzet-=kwota
                                        krajedict[f"{krajdocelowy}"].finbudzet+=kwota
                                        embed = discord.Embed(color=discord.Color.purple(), title="Transfer", description=f"{kraj} zapłacił {kwota: ,}$  {krajdocelowy}")
                                        await interaction.response.send_message(embed=embed)
                                    else:
                                        embed = discord.Embed(color=discord.Color.red(), title="Transfer", description=f"Za mało funduszy!")
                                        await interaction.response.send_message(embed=embed, ephemeral=True)
                                save(f"{kraj}", interaction.guild.id)
                                save(f"{krajdocelowy}", interaction.guild.id)
                            else:
                                embed = discord.Embed(color=discord.Color.red(), title="Transfer", description=f"Za mała kwota!")
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                            
                            await interaction.message.delete()
                    await interaction.message.edit(f"Teraz wpisz ile chcesz mu zapłacić!")
                    await interaction.response.send_modal(CelModal(title="Transfer"))
                    
            await interaction.message.edit(f"Jasne! Teraz wybierz kraj któremu chcesz zapłacić", view=CelUI())



class wojnyactions(discord.ui.View):
    
    @discord.ui.select(
        placeholder = "Wybierz akcję!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Wypowiedz",
                description="Wypowiedz wojne przeciwko krajowi."
            ),
            discord.SelectOption(
                label="Ultimatum",
                description="Wystaw komus ultimatum."
            ),
            discord.SelectOption(
                label="Jednostka",
                description="Ustaw jednostke na wojne."
            ),
            discord.SelectOption(
                label="Kapitulacja",
                description="Poddaj sie, warunki konca wojny okresla druga strona konfliktu."
            ),
            discord.SelectOption(
                label="Zwiad",
                description="Sprawdza stan wojsk danego kraju, niepotrzeba byc w wojnie aby go wykonac."
            ),
            discord.SelectOption(
                label="Podsluch",
                description="Zdobywa informacje o ukladzie jednostek przeciwnika."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0]=="Wypowiedz":
            opts = []
            with open(f"{interaction.guild.id}kraje.json","r+") as f:
                k=json.load(f)
            for i in k:
                opts.append(discord.SelectOption(label=i))
            
            
            
            class krajdocelowypick(discord.ui.View):
                @discord.ui.select(
                    placeholder = "Wybierz swój kraj!",
                    min_values = 1,
                    max_values = 1,
                    options = opts
                )
                async def select_callback(self, select, interaction):
                    krajdocelowy=select.values[0]
                    ctx=interaction
                    with open("bannedids.json",  'r+') as f:
                        z = json.load(f)
                    if f"{interaction.user.id}" in z:
                        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), hidden=True)
                        return
                    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
                    if role==None:
                        with open(f"{interaction.guild.id}countrytypes.json", 'r+') as f:
                            types = json.load(f)
                            if f"{kraj} owner" in types:
                                owner = types[f'{kraj} owner']
                                role2 = discord.utils.get(interaction.user.roles, name=f"{owner}")
                    embed = discord.Embed(title="Unsuccessfull operation", description = "Zadanie nie powiodło się, sprawdź czy posiadasz rolę kraju")
                    if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name==f"{owner}":
                        guild = interaction.guild
                        role = discord.utils.get(guild.roles,name="{}".format(krajdocelowy))
                        warid= r.randint(10000, 99999)
                        with open(f"{interaction.guild.id}wars.json", "r+") as f:
                            z = json.load(f)
                        with open(f"{interaction.guild.id}wars.json", "w") as f:
                            z[str(warid)]=f"{countr[str(interaction.user.id)]} / {krajdocelowy}"
                            json.dump(z, f)
                        desc=f"{kraj} zadeklarował wojnę na {krajdocelowy}, warID: {warid}"
                        embed = discord.Embed(color=discord.Color.red(), title="Wojna", description=desc)
                        with open(f"{ctx.guild.id}{warid}.json", 'w') as f:
                            text= {f"{kraj} attacking unit": None,
                            f"{kraj} support unit": None,
                            f"{krajdocelowy} attacking unit": None,
                            f"{krajdocelowy} support unit": None,
                            f"{kraj} attacking ammount": 0,
                            f"{kraj} support ammount": 0,
                            f"{krajdocelowy} attacking ammount": 0,
                            f"{krajdocelowy} support ammount": 0,}
                            json.dump(text, f)
                        with open(f"allwars.json", "r+") as f:
                            idds = json.load(f)
                        idds.append(warid)
                        with open(f"allwars.json", 'w') as f:
                            json.dump(idds, f)
                        await interaction.response.send_message(embed=embed)
                        for member in role.members:
                            if role in member.roles:
                                desc = f"{kraj} zadeklarował wojnę na tobie({krajdocelowy})! warID: {warid}"
                                embed = discord.Embed(color=discord.Color.red(), title="WAR", description=desc)
                                await member.send(embed=embed)
                                print(f'sent to {member}')
                                
                        await interaction.message.delete()
            await interaction.message.edit("Wybierz kraj na ktorym chcesz wypowiedziec wojne",view=krajdocelowypick())


class aukcjeactions(discord.ui.View):
    
    @discord.ui.select(
        placeholder = "Wybierz akcję!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Aukcje",
                description="Sprawdź aktywne aukcje."
            ),
            discord.SelectOption(
                label="Stwórz Aukcje",
                description="Stwórz własną aukcje."
            ),
            discord.SelectOption(
                label="Postaw na Aukcje",
                description="Postaw na kogoś aukcje."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0]=="Aukcje":
            with open(f"{interaction.guild.id}aukcje.json", "r") as f:
                L = json.load(f)
                text=" "
                counter_au=0
                list_auction=[]
                for i in L:
                    if counter_au==0:
                        id, _ = i.split()
                        list_auction.append(id)
                        counter_au+=1
                    list_auction.append(L[f"{i}"])
                    counter_au+=1
                    if counter_au==7:
                        print(list_auction)
                        id= list_auction[0]
                        autor = list_auction[4]
                        przedmiot = list_auction[1]
                        cena = list_auction[3]
                        ilosc = list_auction[2]
                        min_roznica = list_auction[5]
                        aktualny_zwyciezca = list_auction[6]
                        text = text + f"\n**Aukcja kraju {autor}**\n**przedmiot aukcji:** {przedmiot}\n **ilosc:** {ilosc: ,}\n**minimalna roznica postawianych kwot:** {min_roznica: ,}\n**aktualna postawiona kwota:** {cena: ,}\n**aktualny zwyciezca:** {aktualny_zwyciezca}\n**id aukcji:** {id}\n\n"
                        list_auction=[]
                        counter_au=0
                    
                    
                print(text)
                embed = discord.Embed(color=discord.Color.purple(), title="Aukcje", description=text)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        elif select.values[0]=="Postaw na Aukcje":
            class idview(discord.ui.View):
                with open(f'{interaction.guild.id}aukcje.json', 'r+') as f:
                    un=json.load(f)
                un2=[]
                for i in un:
                    l=i.split()
                    i=str(l[0])
                    tooglere=True
                    for ni in un2:
                        if ni==i:
                            tooglere=False
                    if tooglere:
                        un2.append(discord.Option(label=i,description=i))
                print(un2)
                @discord.ui.select(
                    placeholder = "Wybierz id aukcji!",
                    min_values = 1,
                    max_values = 1,
                    options = un2
                )
                async def select_callback(self, select, interaction):
                    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
                    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
                    if role is not None and role.name == f"{kraj}":
                        with open(f"{interaction.guild.id}aukcje.json", "r") as f:
                            L = json.load(f)
                        if f"{id} przedmiot" in L:
                            if krajedict[f"{kraj}"].finbudzet>=twoja_kwota:
                                if yourbid>=L[f"{id} aktualna kwota"]+L[f"{id} minimalna roznica kwot"]:
                                    async def cb_bidding_accept(interaction):
                                        L[f"{id} aktualna kwota"]=twoja_kwota
                                        L[f"{id} aktualny zwyciezca"]=kraj
                                        embed = discord.Embed(color = discord.Color.green(), title="Aukcja", description=f"Kraj {kraj} postawil {(twoja_kwota): ,} na aukcje {id}")
                                        await interaction.response.send_message(embed=embed)
                                        with open(f"{interaction.guild.id}aukcje.json", "w+") as f:
                                            json.dump(L, f)
                                    async def cb_bidding_deny(interaction):
                                        embed = discord.Embed(color = discord.Color.green(), description=f"Anulowano")
                                        await interaction.response.send_message(embed=embed, ephemeral=True)
                                    button_bidding1 = Button(label="Tak", style=discord.ButtonStyle.green, emoji="✔️")
                                    
                                    button_bidding1.callback=cb_bidding_accept
                                    button_bidding2 = Button(label="Nie", style=discord.ButtonStyle.red)
                                    button_bidding2.callback=cb_bidding_deny
                                    view_bidding.add_item(button_bidding1)
                                    view_bidding.add_item(button_bidding2)
                                    embed=discord.Embed(description=f"Czy napewno chcesz postawic {(twoja_kwota): ,} na aukcje {id}", color=discord.Color.yellow())
                                else:
                                    embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Za mała kwota!")
                            else:
                                embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Za mało funduszy!")
                                
                            
                        else:
                            embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Złe ID!")
                    await interaction.response.send_message(embed=embed, ephemeral=True, view=view_bidding)
            await interaction.message.edit("Dobrze, teraz wybierz id aukcji", view=idview())
        else:
            
            
            
            
            price = cena_poczatkowa
            role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
            embed = discord.Embed(color=discord.Color.red(), title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
            mins=0
            minutes=czas
            if kraj=="help":
                await interaction.respond(embed=discord.Embed(color=discord.Color.blue(), description="stworz aukcje, po uplywie danego czasu, osoba ktora postawila na aukcje najwiecej dostanie licytowany przedmiot, a ty dostaniesz pieniadze. kraj-kraj ktorym dowodzisz, jednostka - licytowana jednostka (dostepne do wystawienia: F16, CAR, Mig29, Mig35, F35, lotniskowiec, złoto, węgiel, uran, srebro, żelazo, korweta, fregata), ilosc-ilosc licytowanej jednostki, poczatkowa_cena-poczatkowa cena aukcji, minimalna_roznica-minimalna roznica stawianych ofert (np. jesli ktos ostatnio stawil 100000 a minimalna_roznica to 50000, nastepna oferta musi byc minimalnie 150000), czas_do_konca_min-czas do konca aukcji w minutach"), ephemeral=True)
                return
            
            if role is not None and role.name == f"{kraj}":
                
                with open(f"{interaction.guild.id}aukcje.json", "r") as f:
                    L = json.load(f)
                id = r.randint(10000,99999)
                przedmiot=jednostka
                simpler=krajedict[f"{kraj}"].__dict__
                if simpler[przedmiot]>=ilosc:
                    L[f"{id} przedmiot"] = przedmiot
                    L[f"{id} ilosc"] = ilosc
                    L[f"{id} aktualna kwota"] = price
                    L[f"{id} autor aukcji"] = f"{kraj}"
                    L[f"{id} minimalna roznica kwot"] = minimalna_roznica
                    L[f"{id} aktualny zwyciezca"]="No One"
                    mins=minutes
                    with open(f"{interaction.guild.id}aukcje.json", "w+") as f:
                        json.dump(L, f)
                    embed=discord.Embed(color=discord.Color.blue(), title="aukcja", description=f"stworzono aukcje o {przedmiot}. ID: {id}! Więcej info `/aukcja info`")
                else:
                    embed=discord.Embed(color=discord.Color.red(), title="aukcja", description="za mała ilosc przedmiotu!")
                for i in simpler:
                    setattr(Kraj, i, simpler[i])
            await interaction.response.send_message(embed=embed)
            if mins==0:
                pass
            else:
            
                await asyncio.sleep(mins*60)
                with open(f"{interaction.guild.id}aukcje.json", "r") as f:
                    L = json.load(f)
                winner=L[f"{id} aktualny zwyciezca"]
                if winner=="No One":
                    embed = discord.Embed(color=discord.Color.blue(), title="Aukcja", description=f"Nikt nie wygrał aukcji {id}")
                else:
                    winner=L[f"{id} aktualny zwyciezca"]
                    simpler=krajedict[f"{kraj}"].__dict__
                    simpler[jednostka]-=ilosc
                    for i in simpler:
                        setattr(Kraj, i, simpler[i])
                    simpler2=krajedict[f"{winner}"].__dict__
                    simpler2[jednostka]+=ilosc
                    for i in simpler2:
                        setattr(Kraj, i, simpler2[i])
                    krajedict[f"{kraj}"].finbudzet+=L[f"{id} aktualna kwota"]
                    krajedict[f"{winner}"].finbudzet-=L[f"{id} aktualna kwota"]
                embed = discord.Embed(color=discord.Color.purple(), title="Aukcja", description=f"Aukcje {id} wygrał {winner}")
                await interaction.channel.send(embed=embed)
                del L[f"{id} przedmiot"]
                del L[f"{id} ilosc"]
                del L[f"{id} aktualna kwota"]
                del L[f"{id} autor aukcji"]
                del L[f"{id} minimalna roznica kwot"]
                del L[f"{id} aktualny zwyciezca"]
                with open("{interaction.guild.id}aukcje.json", "w+") as f:
                    json.dump(L, f)
                save(f"{kraj}", interaction.guild.id)
                save(f"{winner}", interaction.guild.id)



#main
class Action(discord.ui.View):
    
    @discord.ui.select(
        placeholder = "Wybierz grupę akcji!",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Wojna",
                description="Zarządzaj akcjami dotyczącymi wojny, np: wypowiedz wojnę."
            ),
            discord.SelectOption(
                label="Kraj",
                description="Zarządzaj akcjami dotyczącymi kraju, np: sprawdź ilość jednostek, ludności."
            ),
            discord.SelectOption(
                label="Ulepsz",
                description="Ulepsz turystykę lub drzewko technologiczne."
            ),
            discord.SelectOption(
                label="Sojusze",
                description="Sprawdź informacje dotycące sojuszy, np: listę."
            ),
            discord.SelectOption(
                label="Aukcje",
                description="Zarządzaj aukcjami, kupuj, sprawdzaj lub twórz aukcje."
            ),
            discord.SelectOption(
                label="Rynek",
                description="Zarządzaj rynkiem, kupuj, sprawdzaj lub twórz oferty."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        opts = []
        with open(f"{interaction.guild.id}kraje.json","r+") as f:
            k=json.load(f)
        for i in k:
            opts.append(discord.SelectOption(label=i))
        
        
        
        class KrajUI(discord.ui.View):
            @discord.ui.select(
                placeholder = "Wybierz swój kraj!",
                min_values = 1,
                max_values = 1,
                options = opts
            )
            async def select_callback(self, select, interaction):
                if get(interaction.guild.roles,name=select.values[0]) not in interaction.user.roles:
                    await interaction.response.send_message("Nie jestes przywodca tego kraju!",ephemeral=True)
                    await interaction.message.delete()
                    return
                countrrr[str(interaction.user.id)] = select.values[0]
                await interaction.message.edit(f"Jasne przywódco `{select.values[0]}`!, teraz wybierz akcję!", view=countryactions())
        class UlepszUI(discord.ui.View):
            @discord.ui.select(
                placeholder = "Wybierz swój kraj!",
                min_values = 1,
                max_values = 1,
                options = opts
            )
            async def select_callback(self, select, interaction):
                if get(interaction.guild.roles,name=select.values[0]) not in interaction.user.roles:
                    await interaction.response.send_message("Nie jestes przywodca tego kraju!",ephemeral=True)
                    await interaction.message.delete()
                    return
                countrrr[str(interaction.user.id)] = select.values[0]
                await interaction.message.edit(f"Jasne przywódco `{select.values[0]}`!, teraz wybierz aspekt do ulepszenia!", view=ulepszactions())     
        class AukcjeUI(discord.ui.View):
            @discord.ui.select(
                placeholder = "Wybierz swój kraj!",
                min_values = 1,
                max_values = 1,
                options = opts
            )
            async def select_callback(self, select, interaction):
                if get(interaction.guild.roles,name=select.values[0]) not in interaction.user.roles:
                    await interaction.response.send_message("Nie jestes przywodca tego kraju!",ephemeral=True)
                    await interaction.message.delete()
                    return
                countrrr[str(interaction.user.id)] = select.values[0]
                await interaction.message.edit(f"Jasne przywódco `{select.values[0]}`!, teraz wybierz akcję!", view=aukcjeactions())
        class WojnyUI(discord.ui.View):
            @discord.ui.select(
                placeholder = "Wybierz swój kraj!",
                min_values = 1,
                max_values = 1,
                options = opts
            )
            async def select_callback(self, select, interaction):
                if get(interaction.guild.roles,name=select.values[0]) not in interaction.user.roles:
                    await interaction.response.send_message("Nie jestes przywodca tego kraju!",ephemeral=True)
                    await interaction.message.delete()
                    return
                countrrr[str(interaction.user.id)] = select.values[0]
                await interaction.message.edit(f"Jasne przywódco `{select.values[0]}`!, teraz wybierz akcję!", view=wojnyactions())     
                
                
                
                
                
                
        views["Kraj"] = KrajUI
        views["Ulepsz"] = UlepszUI
        views["Sojusze"] = sojuszeactions
        views["Aukcje"] = AukcjeUI
        views["Wojna"] = WojnyUI
        chosen = views[select.values[0]]
        await interaction.message.edit(f"Wybierz swój kraj!", view=chosen())


quick = client.create_group("szybka", "Szybka Akcja")


@quick.command(
    name="akcja")
async def action(ctx):
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    await ctx.respond("Zaczynajmy!", view=Action())
    


async def countries(ctx: discord.AutocompleteContext):
    aer = []
    for i in krajedict:
        aer.append(i)
    return aer





@kraje.command(
    name="podatki",
    description="zmien podatki na  kwota/osoba, default = 1000"
)
async def _podatkichanger(ctx, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), kwota: Option(str, "Kwota którą chcesz ustawić")):
    try:
        a = krajedict[f'{kraj}']
    except:
        await ctx.respond('nie znaleziono kraju', ephemeral=True)
        return
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    try:
        a = krajedict[kraj]
    except:
        await interaction.response.send_message('nie znaleziono kraju', hidden=True)
    if role is not None and role.name == f"{kraj}":
        read(kraj, interaction.guild.id)
        before=krajedict[f'{kraj}'].finpodatek
        if kwota<=6000:
            krajedict[f'{kraj}'].finpodatek = kwota
            save(kraj, interaction.guild.id)
            embed=discord.Embed(color=discord.Color.blue(), description=f"Zmieniono kwote podatkow z {before} na {kwota}")
        else:
            embed=discord.Embed(color=discord.Color.blue(), description=f"Za duza kwota! mozesz ustawic maksymalnie 6000")
    await ctx.respond(embed=embed, ephemeral=True)
    
@operator.command(
    name="typ",
    description="Zmień typ kraju!"
)
async def _changetype(ctx, kraj: Option(str, "Kraj którego typ chcesz zmienić", autocomplete=countries), typ:Option(str, "Typ (kolonia, niepodlegle, prowincja)"), owning:Option(str, "Jakiego kraju ma być własnością, puste=żadnego")=None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    role = discord.utils.get(ctx.author.roles, name="World-Operator")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli World-Operator!")
    hide=True
    if role is not None and role.name == "World-Operator":
        with open(f"{ctx.guild.id}countrytypes.json", "r+") as f:
            z = json.load(f)
        with open(f"{ctx.guild.id}countrytypes.json", "w+") as f:
            types=["kolonia", "niepodlegle", "prowincja"]
            if typ in types:
                try:
                    z[f"{kraj}"] = typ
                    z[f"{kraj} owner"] = owning
                    json.dump(z, f)
                    embed = discord.Embed(color=discord.Color.blue(), title="Zmiana typu", description=f"Zmiana typu {kraj} powiodła się, od teraz panstwo to/jest {typ}.")
                    hide=False
                except:
                    embed = discord.Embed(color=discord.Color.red(), title="Zmiana typu", description="zły kraj!")
                    hide=True
            else:
                embed = discord.Embed(color=discord.Color.red(), title="Zmiana typu", description="zły typ!")
                hide=True   
    await ctx.respond(embed=embed, ephemeral=hide)
@aukcja.command(
    name="info",
    description="sprawdz dostepne aukcje, serio trzeba to tlumaczyc?"
)
async def _aukcje(ctx):
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if ctx.user.id in z:
        await ctx.respond(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    with open(f"{ctx.guild.id}aukcje.json", "r") as f:
        L = json.load(f)
        text=" "
        counter_au=0
        list_auction=[]
        for i in L:
            if counter_au==0:
                id, _ = i.split()
                list_auction.append(id)
                counter_au+=1
            list_auction.append(L[f"{i}"])
            counter_au+=1
            if counter_au==7:
                print(list_auction)
                id= list_auction[0]
                autor = list_auction[4]
                przedmiot = list_auction[1]
                cena = list_auction[3]
                ilosc = list_auction[2]
                min_roznica = list_auction[5]
                aktualny_zwyciezca = list_auction[6]
                text = text + f"\n**Aukcja kraju {autor}**\n**przedmiot aukcji:** {przedmiot}\n **ilosc:** {ilosc: ,}\n**minimalna roznica postawianych kwot:** {min_roznica: ,}\n**aktualna postawiona kwota:** {cena: ,}\n**aktualny zwyciezca:** {aktualny_zwyciezca}\n**id aukcji:** {id}\n\n"
                list_auction=[]
                counter_au=0
            
            
        print(text)
        embed = discord.Embed(color=discord.Color.purple(), title="Aukcje", description=text)
        await ctx.respond(embed=embed, ephemeral=True)
@aukcja.command(
    name="postaw",
    description="postaw kwote na aukcje, serio trzeba to tlumaczyc?"
)
async def _bidauction(ctx, kraj:Option(str, "Kraj którym władasz", autocomplete=countries), twoja_kwota: Option(int, "Kwota którą chcesz postawić")=None, id: Option(int, "ID aukcji")=None):
    interaction=ctx
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    yourbid=twoja_kwota
    view_bidding=View()
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.author.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="postaw na aukcje, jesli nikt nie postawi wiecej niz ty, wygrywasz licytowany przedmiot. kraj-kraj ktorym dowodzisz, id-id aukcji"), ephemeral=True)
        return
    if krajedict[kraj] == None:
        await interaction.response.send_message("Zla nazwa kraju!", ephemeral=True)
        return
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    if role is not None and role.name == f"{kraj}":
        with open(f"{interaction.guild.id}aukcje.json", "r") as f:
            L = json.load(f)
        if f"{id} przedmiot" in L:
            if krajedict[f"{kraj}"].finbudzet>=twoja_kwota:
                if yourbid>=L[f"{id} aktualna kwota"]+L[f"{id} minimalna roznica kwot"]:
                    async def cb_bidding_accept(interaction):
                        L[f"{id} aktualna kwota"]=twoja_kwota
                        L[f"{id} aktualny zwyciezca"]=kraj
                        embed = discord.Embed(color = discord.Color.green(), title="Aukcja", description=f"Kraj {kraj} postawil {(twoja_kwota): ,} na aukcje {id}")
                        await interaction.response.send_message(embed=embed)
                        with open(f"{interaction.guild.id}aukcje.json", "w+") as f:
                            json.dump(L, f)
                    async def cb_bidding_deny(interaction):
                        embed = discord.Embed(color = discord.Color.green(), description=f"Anulowano")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    button_bidding1 = Button(label="Tak", style=discord.ButtonStyle.green, emoji="✔️")
                    
                    button_bidding1.callback=cb_bidding_accept
                    button_bidding2 = Button(label="Nie", style=discord.ButtonStyle.red)
                    button_bidding2.callback=cb_bidding_deny
                    view_bidding.add_item(button_bidding1)
                    view_bidding.add_item(button_bidding2)
                    embed=discord.Embed(description=f"Czy napewno chcesz postawic {(twoja_kwota): ,} na aukcje {id}", color=discord.Color.yellow())
                else:
                    embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Za mała kwota!")
            else:
                embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Za mało funduszy!")
                
            
        else:
            embed = discord.Embed(color = discord.Color.red(), title="Aukcja", description=f"Złe ID!")
    await ctx.respond(embed=embed, ephemeral=True, view=view_bidding)

def save(kraj, id):
    with open(f"{id}{kraj}.json", "w") as f:
            i = kraj
            text = {
                "wywiadtree": krajedict["{}".format(i)].wywiadtree,
                "Mig29": krajedict["{}".format(i)].Mig29,
                "Mig35": krajedict["{}".format(i)].Mig35,
                "Lancer":  krajedict[f"{i}"].Lancer,
                "granaty": krajedict["{}".format(i)].nades,
                "napalm": krajedict["{}".format(i)].napalm,
                "bunker buster": krajedict["{}".format(i)].bb,
                "pociski balistyczne": krajedict["{}".format(i)].balistyczne,
                "Hwaseong": krajedict["{}".format(i)].Hwaseong,
                "CAR": krajedict["{}".format(i)].tzaar,
                "Navy": krajedict["{}".format(i)].finNAVY,
                "fregaty": krajedict["{}".format(i)].fregaty,
                
                "korwety":krajedict["{}".format(i)].korwety,

                "okret desantowy":krajedict["{}".format(i)].findesantowce,
                
                
                "abrams": krajedict[f"{i}"].abrams,
                "drużyna gazująca": krajedict[f"{i}"].ekipagaz,
                "snajperzy": krajedict[f"{i}"].snajperzy,
                "2S19": krajedict[f"{i}"].betterarty,
                "pluskwa": krajedict[f"{i}"].pluskwy,
                "niszczyciel":krajedict["{}".format(i)].niszczyciel,
                "pancernik":krajedict[f"{kraj}"].pancernik,
                "watertree": krajedict["{}".format(i)].watertree,
                "groundtree": krajedict["{}".format(i)].groundtree,
                "skytree": krajedict["{}".format(i)].skytree,
                "bombtree": krajedict["{}".format(i)].bombtree,
                "finbudzet": krajedict["{}".format(i)].finbudzet,
                "finludnosc": krajedict["{}".format(i)].finludnosc,
                "finteatralnaobrona": krajedict["{}".format(i)].finteatralnaobrona,
                "finNAVY": krajedict["{}".format(i)].finNAVY,
                "finbomby": krajedict["{}".format(i)].finbomby,
                "finf15": krajedict["{}".format(i)].finf15,
                "finf16": krajedict["{}".format(i)].finf16,
                "finf35": krajedict["{}".format(i)].finf35,
                "finlockheed": krajedict["{}".format(i)].finlockheed,
                "finmh53": krajedict["{}".format(i)].finmh53,
                "finhelikopterypiechoty": krajedict["{}".format(i)].finhelikopterypiechoty,
                "finnighthawk": krajedict["{}".format(i)].finnighthawk,
                "finpodwodne": krajedict["{}".format(i)].finpodwodne,

                

                "finlodzie": krajedict["{}".format(i)].finlodzie,
                "finlotniskowce": krajedict["{}".format(i)].finlotniskowce,
                "finzwiadowca": krajedict["{}".format(i)].finzwiadowca,
                "findywizje": krajedict["{}".format(i)].findywizje,
                "finczolg": krajedict["{}".format(i)].finczolg,
                "finprzeciwlot": krajedict["{}".format(i)].finprzeciwlot,
                "finartyleria": krajedict["{}".format(i)].finartyleria,
                "finkawaleria": krajedict["{}".format(i)].finkawaleria,
                "finlandbonus": krajedict["{}".format(i)].finlandbonus,
                "finlanddebonus": krajedict["{}".format(i)].finlanddebonus,
                "finpodatek": krajedict["{}".format(i)].finpodatek,
                "finturystyka": krajedict["{}".format(i)].finturystyka,
                "finzloto": krajedict["{}".format(i)].finzloto,
                "finuran": krajedict["{}".format(i)].finuran,
                "finsrebro": krajedict["{}".format(i)].finsrebro,
                "finwegiel": krajedict["{}".format(i)].finwegiel,
                "finzelazo": krajedict["{}".format(i)].finzelazo,
                "finkobalt": krajedict["{}".format(i)].finkobalt,
                "finnafta": krajedict["{}".format(i)].finnafta
            }
            json.dump(text, f)

async def avaible(ctx: discord.AutocompleteContext):
    return ["F16", "CAR", "Mig29", "Mig35", "F35", "lotniskowiec", "złoto", "węgiel", "uran", "srebro", "żelazo", "korweta", "fregata"]
carrot = {"F16": "finf16", "CAR": "tzaar", "Mig29": "Mig29", "Mig35": "Mig35", "F35": "finf35", "lotniskowiec": "finlotniskowce", "złoto": "finzloto", "węgiel": "finwegiel", "uran": "finuran", "srebro": "finsrebro", "żelazo": "finzelazo", "korweta": "korwety", "fregata": "fregaty"}
@aukcja.command(
    name="stwórz",
    description="stworz aukcje, serio trzeba to tlumaczyc?"
)
async def _createauction(ctx, kraj:Option(str, "Kraj którym władasz", autocomplete=countries), jednostka:Option(str, "Jednostka którą chcesz postawić na aukcje", autocomplete=avaible) = None, ilosc: Option(int, "Ilość jednostki")=None, cena_poczatkowa: Option(int, "Pierwsza cena") = None, minimalna_roznica: Option(int, "Różnica między stawianymi kwotami")=None, czas:Option(int, "Czas do zakończenia aukcji w minutach") = None):
    interaction = ctx
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.respond('nie znaleziono kraju', ephemeral=True)
        return
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.author.id}" in z:
        await interaction.respond(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    price = cena_poczatkowa
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(color=discord.Color.red(), title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    mins=0
    minutes=czas
    if kraj=="help":
        await interaction.respond(embed=discord.Embed(color=discord.Color.blue(), description="stworz aukcje, po uplywie danego czasu, osoba ktora postawila na aukcje najwiecej dostanie licytowany przedmiot, a ty dostaniesz pieniadze. kraj-kraj ktorym dowodzisz, jednostka - licytowana jednostka (dostepne do wystawienia: F16, CAR, Mig29, Mig35, F35, lotniskowiec, złoto, węgiel, uran, srebro, żelazo, korweta, fregata), ilosc-ilosc licytowanej jednostki, poczatkowa_cena-poczatkowa cena aukcji, minimalna_roznica-minimalna roznica stawianych ofert (np. jesli ktos ostatnio stawil 100000 a minimalna_roznica to 50000, nastepna oferta musi byc minimalnie 150000), czas_do_konca_min-czas do konca aukcji w minutach"), ephemeral=True)
        return
    
    if role is not None and role.name == f"{kraj}":
        
        with open(f"{interaction.guild.id}aukcje.json", "r") as f:
            L = json.load(f)
        id = r.randint(10000,99999)
        przedmiot=jednostka
        simpler=krajedict[f"{kraj}"].__dict__
        if simpler[carrot[przedmiot]]>=ilosc:
            L[f"{id} przedmiot"] = przedmiot
            L[f"{id} ilosc"] = ilosc
            L[f"{id} aktualna kwota"] = price
            L[f"{id} autor aukcji"] = f"{kraj}"
            L[f"{id} minimalna roznica kwot"] = minimalna_roznica
            L[f"{id} aktualny zwyciezca"]="No One"
            mins=minutes
            with open(f"{interaction.guild.id}aukcje.json", "w+") as f:
                json.dump(L, f)
            embed=discord.Embed(color=discord.Color.blue(), title="aukcja", description=f"stworzono aukcje o {przedmiot}. ID: {id}! Więcej info `/aukcja info`")
        else:
            embed=discord.Embed(color=discord.Color.red(), title="aukcja", description="za mała ilosc przedmiotu!")
        for i in simpler:
            setattr(Kraj, i, simpler[i])
    await interaction.respond(embed=embed)
    if mins==0:
        pass
    else:
        await asyncio.sleep(mins*60)
        with open(f"{interaction.guild.id}aukcje.json", "r") as f:
            L = json.load(f)
        winner=L[f"{id} aktualny zwyciezca"]
        if winner=="No One":
            embed = discord.Embed(color=discord.Color.blue(), title="Aukcja", description=f"Nikt nie wygrał aukcji {id}")
        else:
            winner=L[f"{id} aktualny zwyciezca"]
            simpler=krajedict[f"{kraj}"].__dict__
            simpler[carrot[przedmiot]] =ilosc
            for i in simpler:
                setattr(Kraj, i, simpler[i])
            simpler2=krajedict[f"{winner}"].__dict__
            simpler2[carrot[przedmiot]]+=iloscs
            for i in simpler2:
                setattr(Kraj, i, simpler2[i])
            krajedict[f"{kraj}"].finbudzet+=L[f"{id} aktualna kwota"]
            krajedict[f"{winner}"].finbudzet-=L[f"{id} aktualna kwota"]
        embed = discord.Embed(color=discord.Color.purple(), title="Aukcja", description=f"Aukcje {id} wygrał {winner}")
        await interaction.channel.send(embed=embed)
        del L[f"{id} przedmiot"]
        del L[f"{id} ilosc"]
        del L[f"{id} aktualna kwota"]
        del L[f"{id} autor aukcji"]
        del L[f"{id} minimalna roznica kwot"]
        del L[f"{id} aktualny zwyciezca"]
        with open("{interaction.guild.id}aukcje.json", "w+") as f:
            json.dump(L, f)
        save(f"{kraj}", interaction.guild.id)
        save(f"{winner}", interaction.guild.id)
@rynek.command(
    name="info",
    description="sprawdz rynek, serio trzeba to tlumaczyc?"
)
async def _rynek(interaction):
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.author.id}" in z:
        await ctx.respond(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    with open(f"{ctx.guild.id}rynek.json", "r") as f:
        L = json.load(f)
        text=" "
        rynek_list=[]
        for i in L:
            if len(rynek_list)==0:
                h, _ = i.split()
                rynek_list.append(h)
            rynek_list.append(L[f'{i}'])
            if len(rynek_list)==5:
                id = rynek_list[0]
                przedmiot = rynek_list[1]
                ilosc = rynek_list[2]
                cena = rynek_list[3]
                kraj = rynek_list[4]
                text+=f"**Aukcja kraju {kraj}**\n**przedmiot oferty**: {przedmiot}\n**ilosc przedmiotu**: {ilosc}\n**cena**: {cena}\n**id**: {id}\n\n\n"
                rynek_list=[]
        embed = discord.Embed(color=discord.Color.purple(), title="Rynek", description=text)
        await ctx.respond(embed=embed, ephemeral=True)


@rynek.command(
    name="kup",
    description="kup oferte z rynku"
)
async def _buyoffer(interaction, kraj:Option(str, "Kraj którym władasz", autocomplete=countries), id: int = None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="kup oferte,  dostaniesz kupiony przedmiot. kraj-kraj ktorym dowodzisz, id- id oferty, znajdziesz je przy ofercie"), ephemeral=True)
        return
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    if role is not None and role.name == f"{kraj}":
        with open(f"{interaction.guild.id}rynek.json", "r") as f:
            L = json.load(f)
        if f"{id} author" in L:
            if krajedict[f"{kraj}"].finbudzet>=L[f"{id} price"]:
                simpler = krajedict[f"{kraj}"].__dict__
                simpler[carrot[str(L["{id} item"])]]+=L[f"{id} amount"]
                for i in simpler:
                    setattr(Kraj, i, simpler[i])
                
                payto=L[f"{id} author"]
                print(payto)
                krajedict[f"{payto}"].finbudzet+=L[f"{id} price"]
                
                embed = discord.Embed(color = discord.Color.green(), title="oferta", description=f"Kupiono oferte {id}")

            
            else:
                embed = discord.Embed(color = discord.Color.red(), title="oferta", description=f"Za mało funduszy!")
                
            await interaction.response.send_message(embed=embed, ephemeral=True)
            

        save(f"{kraj}", interaction.guild.id)
        kraj=L[f"{id} author"]
        save(f"{kraj}", interaction.guild.id)
        with open(f"{interaction.guild.id}rynek.json", "r+") as f:
            x = json.load(f)
        del x[f"{id} price"]
        del x[f"{id} item"]
        del x[f"{id} author"]
        del x[f"{id} amount"]
        with open(f"{interaction.guild.id}rynek.json", "w+") as f:
            json.dump(x, f)

@rynek.command(
    name="stwórz",
    description="stwórz ofertę i wstaw ją na rynek"
)
async def _createoffer(interaction, kraj:Option(str, "Kraj którym władasz", autocomplete=countries), przedmiot:Option(str, "Przedmiot", autocomplete=avaible) = None, ilosc: int = None, cena: int = None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await ctx.respond('nie znaleziono kraju', ephemeral=True)
        return
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="stworz oferte i wstaw ja na rynek,  dostaniesz pienadze jesli ktos ja kupi. kraj-kraj ktorym dowodzisz. przedmiot-przedmiot ktory chcesz sprzedac (dostepne: zloto, srebro, wegiel, zelazo, balistyczne (pociski takie), Hwaesong (rakieta taka), ilosc-ilosc danego przedmiotu, cena - cena za przedmiot (nie za sztuke tylko za cala ilosc jaka wystawiles)"), ephemeral=True)
        return
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(color=discord.Color.red(), title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    if role is not None and role.name == f"{kraj}":
        with open(f"{interaction.guild.id}rynek.json", "r") as f:
            L = json.load(f)
            id = r.randint(10000,99999)
            simpler = krajedict[f"{kraj}"].__dict__
            if simpler[przedmiot]>=ilosc:
                simpler[przedmiot]-=ilosc
                L[f"{id} item"] = f"{przedmiot}"
                L[f"{id} amount"] = ilosc
                L[f"{id} price"] = cena
                L[f"{id} author"] = f"{kraj}"
                with open(f"{interaction.guild.id}rynek.json", "w+") as f:
                    json.dump(L, f)
                embed=discord.Embed(color=discord.Color.blue(), title="oferta", description=f"stworzono oferte {id}!")
            else:
                embed=discord.Embed(color=discord.Color.red(), title="oferta", description="za mała ilosc przedmiotu!")
        for i in simpler:
            setattr(Kraj, i, simpler[i])
                
                
        await ctx.respond(embed=embed, ephemeral=True)
        save(f"{kraj}", ctx.guild.id)
        
@kraje.command(
    name="zapłać",
    description="zaplac podana kwote danemu krajowi"
)
async def pay(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), krajdocelowy:Option(str, "Kraj któremu chcesz zapłacić", autocomplete=countries)=None, kwota:int=None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Za pomoca tej komendy mozesz zaplacic danemu krajowi pieniadze. kraj-kraj ktorym dowodzisz, krajdocelowy-kraj ktoremu chcesz zaplacic, kwota-kwota jaka chcesz zaplacic danemu kraju"), empheremal=True)
        return
    if kwota>=100000:
        
        role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
        embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
        if role is not None and role.name == f"{kraj}":
            if krajedict[f"{kraj}"].finbudzet>=kwota:
                krajedict[f"{kraj}"].finbudzet-=kwota
                krajedict[f"{krajdocelowy}"].finbudzet+=kwota
                embed = discord.Embed(color=discord.Color.purple(), title="Transfer", description=f"{kraj} zapłacił {kwota: ,}$  {krajdocelowy}")
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(color=discord.Color.red(), title="Transfer", description=f"Za mało funduszy!")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        save(f"{kraj}", interaction.guild.id)
        save(f"{krajdocelowy}", interaction.guild.id)
    else:
        embed = discord.Embed(color=discord.Color.red(), title="Transfer", description=f"Za mała kwota!")
        await interaction.response.send_message(embed=embed, ephemeral=True)
@kraje.command(
    name="lista",
    description="sprawdz liste krai"
)
async def countof(interaction):
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    with open(f"{interaction.guild.id}kraje.json", "r+") as f:
        z = json.load(f)
        krajestring="**kraje**"
        for i in z:
            krajestring = krajestring + f"\n {i}"
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.purple(), description=krajestring), ephemeral=True)
class type():
    def __init__(self, var, surowiec):
        self.var=var
        self.surowiec=surowiec
types= {
    "wodne": type("watertree", "zloto"),
    "naziemne": type("groundtree", "zelazo"),
    "powietrzne": type("skytree", "srebro"),
    "bomby": type("bombtree", "uran")
    }
async def typer(ctx: discord.AutocompleteContext):
    return ["naziemne", "wodne", "powietrzne", "bomby"]
    
    
@ulepsz.command(
    name="drzewko",
    description="ulepsz dane drzewko technologiczne, serio pytasz?"
)
async def _upgradetree(ctx: discord.ApplicationContext, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), typ: Option(str, "Wybierz typ drzewka technologicznego!", autocomplete=typer)=None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    ctx=interaction
    if typ is not None:
        type=typ.lower()
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Za pomoca tej komendy mozesz ulepszyc dane drzewko technologiczne, w typ wpisz info aby dowiedziec sie o kosztach ulepszen, kraj-kraj ktorym dowodzisz, typ-typ drzewka np. wodne, naziemne, powietrzne, bomby. Koszty ulepszenia znajdziesz jesli w typ piszesz 'info'."), ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    if role is not None and role.name == f"{kraj}":
        tier={}
        tier1=5000000
        tier2=7500000
        tier3=10000000
        tier4=15000000
        tier5=20000000
        tier["tier1"] = tier1
        tier["tier2"] = tier2
        tier["tier3"] = tier3
        tier["tier4"] = tier4
        tier["tier5"] = tier5
        type = typ.lower()
        if type=="info":
            embed = discord.Embed(color=discord.Colour(0xFFFF00), title="Upgrade Tree", description = f"Koszty ulepszenia na 2tier: 5mln,\n Koszty ulepszenia na 3tier: 7.5mln,\n Koszty ulepszenia na 4tier: 10mln,\nKoszty ulepszenia na 5tier: 15mln,\nKoszty ulepszenia na 6tier: 20mln.")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        toooogle=False
        for type in types:
            if type==typ:
                toooogle=True
                new_type=type
                typ=types[f"{typ}"]
                up_kraj=krajedict[f"{kraj}"].__dict__
                if up_kraj[f'{typ.var}']==6:
                    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.yellow(), description="Juz masz maksymalny poziom drzewka!"), ephemeral=True)
                else:
                    if up_kraj["finbudzet"]>= tier[f"tier{up_kraj[f'{typ.var}']}"]:
                        if up_kraj[f"fin{typ.surowiec}"]>=200:
                            async def cbup1(interaction):
                                up_kraj['finbudzet']-=tier[f"tier{up_kraj[f'{typ.var}']}"]
                                up_kraj[f'fin{typ.surowiec}']-=200
                                up_kraj[f'{typ.var}']+=1
                                embed = discord.Embed(color=discord.Color.green(), title="Ulepszanie drzewka", description = f"Ulepszono drzewko technologiczne {new_type} na tier{up_kraj[f'{typ.var}']}!")
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                                for i in up_kraj:
                                    setattr(Kraj, i, up_kraj[i])
                                save(f"{kraj}", interaction.guild.id)
                            async def cbup2(interaction):
                                await interaction.response.send_message(embed=discord.Embed(color=discord.Color.green(), description="Anulowano"), ephemeral=True)
                            butup1=Button(label="Ulepsz",style=discord.ButtonStyle.green, emoji="✔️")
                            butup2=Button(label="Anuluj", style=discord.ButtonStyle.red)
                            
                            
                            butup1.callback=cbup1
                            butup2.callback=cbup2
                            view_up=View()
                            view_up.add_item(butup1)
                            view_up.add_item(butup2)
                            ae=up_kraj[f'{typ.var}']
                            brainfuck=f"tier{ae}"
                            ae2=f'{tier[brainfuck]}'
                            embed=discord.Embed(color=discord.Color.purple(), title="Ulepsz drzewko",description=f"Czy jestes pewien, ze chcesz ulepszyc drzewko technologiczne {type} na poziom {ae+1} za 200 {typ.surowiec} i {int(ae2): ,} budzetu?")
                            await interaction.response.send_message(embed=embed, view=view_up, ephemeral=True)
                        else:
                            embed = discord.Embed(color=discord.Color.red(), title="Za malo surowca", description = f"Potrzebujesz  200 sztuk {typ.surowiec}!")
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                    else:
                        ae=up_kraj[f'{typ.var}']
                        embed = discord.Embed(color=discord.Color.red(), title="Za malo pieniedzy", description = f"Potrzebujesz  {(tier[f'tier{ae}']): ,} budzetu!")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
        if toooogle==False:
            embed = discord.Embed(color=discord.Color.red(), title="Zly typ", description = f"Wpisano zly typ!")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    
    else:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    save(f"{kraj}", interaction.guild.id)

async def wars(ctx: discord.AutocompleteContext, guild):
    with open(f"allwars.json", 'r+') as f:
        liss = []
        for i in json.load(f):
            liss.append(i)
    return liss

@wojna.command(
    name="kapitulacja",
    description="oglos kapitulacje, warunki kapitulacji ustala przeciwnik"
)
async def _warcapitulation(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), warid:Option(int, "ID Wojny", autocomplete=wars)=None):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Za pomoca tej komendy mozesz oglosic kapitulacje, automatycznie zgadzasz sie na warunki postawione przez wroga"), ephemeral=True)
        return
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    embed = discord.Embed(color=discord.Colour(0xFF0000), title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli kraju!")
    if role is not None and role.name == f"{kraj}":
        with open(f"{interaction.guild.id}{warid}.json", 'w') as f:
            txt= {"end": True}
            json.dump(txt, f)
        desc = f'wojna {warid} skończona!'
        embed = discord.Embed(title="KAPITULACJA", description=f"{kraj} skapitulował w wojnie {warid}, {desc}")
    await interaction.response.send_message(embed=embed)

@wojna.command(
    name="zakończ",
    description="zakoncz wojne"
)
async def _endwar(interaction, warid:Option(int, "ID Wojny", autocomplete=wars), winner:str):
    ctx=interaction
    role = discord.utils.get(ctx.user.roles, name=f"World-Operator")
    embed = discord.Embed(color=discord.Colour(0xFF0000), title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli World-Operator!")
    if role is not None and role.name == "World-Operator":
        with open(f'{ctx.guild.id}{warid}.json', 'w') as f:
            txt= {"end": True}
            json.dump(txt, f)
            desc = f'wojna {warid} zakonczona. wygrany to is {winner}!'
            embed = discord.Embed(title=f"WOJNA ZAKOŃCZONA", description = desc)
            embed2 = discord.Embed(title=f"WOJNA ZAKOŃCZONA", description = f"wojna {warid} zakończona. Wygrał {winner}, proszę zaaktualizować mapę")
            for i in role.members:
                await i.send(embed=embed2)
    await ctx.response.send_message(embed=embed)
@wojna.command(
    name="info",
    description="info o wojnie, tylko dla World-Operator"
)
async def _warinfo(ctx, warid:Option(int, "ID Wojny", autocomplete=wars)=None):
    role = discord.utils.get(ctx.user.roles, name=f"World-Operator")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, potrzebujesz roli World-Operator!")
    if role is not None and role.name == "World-Operator":
        with open(f'{ctx.guild.id}{warid}.json', 'r+') as f:
            z = json.load(f)
        desc=""
        for i in z:
            desc = desc + f"{i}: {z[i]}\n"
        embed = discord.Embed(color=discord.Colour(0x0000FF), title=f"Info about war {warid}", description = desc)
    await ctx.respond(embed=embed, ephemeral=True)
@sojusze.command(
    name="lista",
    description="pokaz liste sojuszy"
)
async def _alliance(interaction):
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    with open(f"{ctx.guild.id}sojusze.json", "r+") as f:
        z = json.load(f)
        srt=""
        for i in z:
            srt=srt+f"\n {i}: {z[i]}"
        embed=discord.Embed(color=discord.Color.purple(), title="Sojusze", description=srt)
        await interaction.response.send_message(embed=embed)
async def typs(ctx:discord.AutocompleteContext):
    return ["support", "attack"]
@wojna.command(
    name="jednostka",
    description="ustaw jednostkę typ=support/attack"
)
async def _setaunit(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), typ:Option(str, "Typ", autocomplete=typs)=None, jednostka: str=None, ilosc: int=None, warid:Option(int, "ID Wojny", autocomplete=wars)=None):
    ctx=interaction
    amount = ilosc
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    if role==None:
        with open(f"{ctx.guild.id}countrytypes.json", 'r+') as f:
            owner = types[f'{kraj}']
            if f"{kraj} owner" in types:
                owner = types[f'{kraj} owner']
                role2 = discord.utils.get(ctx.user.roles, name=f"{owner}")
    read(kraj, ctx.guild.id)
    with open(f"{ctx.guild.id}wars.json") as f:
        warIDs= json.load(f)
    short = {
    "f16": "finf16",
    "f15": "finf15",
    "f35": "finf35",
    "mig29": "Mig29",
    "mig35": "Mig35",
    "lockheed": "finlockheed",
    "nighthawk": "finnighthawk",
    "mh53": "finmh53",
    "lancer": "Lancer",
    "napalm": "napalm",
    "pociski balistyczne": "balistyczne",
    "hwaseong": "Hwaseong",
    "granaty": "granaty",
    "bunker Buster": "bunker buster",
    "ekipa gazujaca": "dru\u017cyna gazuj\u0105ca",
    "snajperzy": "snajperzy",
    "abrams": "abrams",
    "2s19": "2S19",
    "lodzie podwodne": "finpodwodne",
    "lotniskowce": "finlotniskowce",
    "fregaty": "fregaty",
    "korwety": "korwety",
    "pancernik": "pancernik",
    "niszczyciel": "niszczyciel",
    "okret desantowy": "okret desantowy",
    "dywizje": "findywizje",
    "artyleria": "finartyleria",
    "kawaleria": "finkawaleria"}
    embed = discord.Embed(title="Unsuccessfull operation", description = "Niepowodzenie, sprawdź czy masz wystarczająco {} oraz czy posiadasz rolę kraju".format(jednostka))
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="za pomoca tej komendy ustawiasz jednostke na wojne, kraj- kraj ktorym zarzadzasz, jednostka-jednostka ktora chcesz wystawic, ilosc-ilosc jednostki, warid-id wojny na ktora chcesz wystawic jednostke"), ephemeral=True)
        return
    if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name==f"{owner}":
        for id in warIDs:
            if id==warid:
                x=None
                with open(f"{ctx.guild.id}{kraj}.json", "r+") as f:
                    x = json.load(f)
                if jednostka.lower() in short:
                    shorten=short[f"{jednostka}"]
                    if x[f"{shorten}"]>=amount:
                        x[f"{shorten}"]-=amount
                        
                        with open(f"{ctx.guild.id}{id}.json", 'r+') as f:
                            z = json.load(f)
                            if typ=="support":
                                z[f"{kraj} support unit"] = jednostka
                                z[f'{kraj} support ammount'] = amount
                                embed = discord.Embed(color=discord.Color.blue(), title="WAR UNITS", description = f"Udało się ustawić jednostkę typu support na {jednostka} oraz ilosc na {amount}")
                            elif typ=="attack":
                                z[f"{kraj} attacking unit"] = jednostka
                                z[f'{kraj} attacking ammount'] = amount
                                embed = discord.Embed(color=discord.Color.blue(), title="WAR UNITS", description = f"Udało się ustawić jednostkę typu attack na {jednostka} oraz ilosc na {amount}")
                            else:
                                embed = discord.Embed(color=discord.Color.red(), title="ERROR", description="wrong type!")
                        with open(f"{ctx.guild.id}{kraj}.json", "w+") as f:
                            json.dump(x, f)
                        with open(f"{ctx.guild.id}{id}.json", 'w') as f:
                            json.dump(z, f)
                    else:
                        embed = discord.Embed(description="za mala liczba jednostki!")
                else:
                    embed = discord.Embed(description="zla/nieobslugiwana jednostka!")
    await interaction.response.send_message(embed=embed, ephemeral=True)
    save(kraj, ctx.guild.id)
@wojna.command(
    name="ogłoś",
    description="wypowiedz wojnę krajowi"
)
async def _declareawar(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), cel: Option(str, "Kraj na którym chcesz wypowiedzieć wojnę", autocomplete=countries)):
    krajdocelowy=cel
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), hidden=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Za pomoca tej komendy mozesz wypowiedziec na innym kraju wojne. kraj- kraj ktorym zarzadzasz, krajdocelowy-kraj ktoremu chcesz wypowiedziec wojne"), ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    if role==None:
        with open(f"{ctx.guild.id}countrytypes.json", 'r+') as f:
            types = json.load(f)
            if f"{kraj} owner" in types:
                owner = types[f'{kraj} owner']
                role2 = discord.utils.get(ctx.user.roles, name=f"{owner}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Zadanie nie powiodło się, sprawdź czy posiadasz rolę kraju")
    if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name==f"{owner}":
        guild = ctx.guild
        role = discord.utils.get(guild.roles,name="{}".format(krajdocelowy))
        warid= r.randint(10000, 99999)
        with open(f"{ctx.guild.id}wars.json", "r+") as f:
            z = json.load(f)
        with open(f"{ctx.guild.id}wars.json", "w") as f:
            z.append(warid)
            json.dump(z, f)
        desc=f"{kraj} zadeklarował wojnę na {krajdocelowy}, warID: {warid}"
        embed = discord.Embed(color=discord.Color.red(), title="WAR", description=desc)
        with open(f"{ctx.guild.id}{warid}.json", 'w') as f:
            text= {f"{kraj} attacking unit": None,
            f"{kraj} support unit": None,
            f"{krajdocelowy} attacking unit": None,
            f"{krajdocelowy} support unit": None,
            f"{kraj} attacking ammount": 0,
            f"{kraj} support ammount": 0,
            f"{krajdocelowy} attacking ammount": 0,
            f"{krajdocelowy} support ammount": 0,}
            json.dump(text, f)
        with open(f"allwars.json", "r+") as f:
            idds = json.load(f)
        idds.append(warid)
        with open(f"allwars.json", 'w') as f:
            json.dump(idds, f)
        await interaction.response.send_message(embed=embed)
        for member in role.members:
            if role in member.roles:
                desc = f"{kraj} zadeklarował wojnę na tobie({krajdocelowy})! warID: {warid}"
                embed = discord.Embed(color=discord.Color.red(), title="WAR", description=desc)
                await member.send(embed=embed)
                print(f'sent to {member}')
@wojna.command(
    name="ultimatum",
    description="zadeklaruj ultimatum na kraju"
)
async def _ultimatum(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), cel: Option(str, "Kraj któremu chcesz wypowiedzieć ultimatum", autocomplete=countries)=None, warunki:str=None):
    krajdocelowy=cel
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, deklarujesz ultimatum na danym kraju, kraj ten moze przyjac te warunki albo je odrzucic. kraj-kraj ktorym dowodzisz, krajdocelowy-kraj ktoremu wystawiasz ultimatum, warunki-warunki ultimatum(np. placisz 5mln albo wojna"), ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = "Zadanie nie powiodło się, sprawdź czy posiadasz rolę kraju")
    if role is not None and role.name == f"{kraj}":
        role = discord.utils.get(ctx.guild.roles, name=f"{krajdocelowy}")
        for i in role.members:
            embed2 = discord.Embed(title="ULTIMATUM", description = f"{kraj} rzucił ultimatum na ciebie({krajdocelowy})! warunki: {warunki}")
            try:
                await i.send(embed=embed2)
            except:
                await interaction.response.send_message(f"<@{i.id}>")  
        embed = discord.Embed(title="ULTIMATUM", description = f"{kraj} rzucił ultimatum na {krajdocelowy}! warunki: {warunki}")
        await interaction.response.send_message(embed=embed)
@ulepsz.command(
    name="turystyka",
    description="ulepszenie turystyki"
)
async def _turystyka(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries)):
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, Ulepszasz turystyke. kraj-kraj ktorym dowodzisz. Za 5mln ulepszasz turystyke o 0.1"), ephemeral=True)
        return
    if krajedict[kraj] == None:
        await interaction.response.send_message("Zla nazwa kraju!", ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    if role is not None and role.name == f"{kraj}":
        with open(f'{interaction.guild.id}kraje.json', "r") as f:
            kraje = json.load(f)
        for i in kraje:
            if i==kraj:
                finbudzet = krajedict[f'{kraj}'].finbudzet
                if finbudzet>5000000:
                    async def callback_tur(interaction):
                        finbudzet = krajedict[f'{kraj}'].finbudzet
                        finbudzet-=5000000
                        krajedict[f'{kraj}'].finbudzet=finbudzet
                        desc = f'ulepszono turystykę w kraju o 10%'
                        embed = discord.Embed(color=discord.Color.green(), title=f'TURYSTYKA', description=desc)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        krajedict[f'{kraj}'].finturystyka+=0.1
                    async def callback_tur_dec(interaction):
                        embed = discord.Embed(color=discord.Color.green(), description="anulowano")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    view_tur=View()
                    button_tur = Button(label="Tak", emoji="✔️", style=discord.ButtonStyle.green)
                    button_tur_dec = Button(label="Nie", style=discord.ButtonStyle.red)
                    button_tur.callback=callback_tur
                    button_tur_dec.callback=callback_tur_dec
                    view_tur.add_item(button_tur)
                    view_tur.add_item(button_tur_dec)
                    embed = discord.Embed(color=discord.Color.purple(), description="Czy jestes pewien ze chcesz ulepszyc turystyke za 5,000,000 waluty?")
                    await interaction.response.send_message(embed=embed, ephemeral=True, view=view_tur)
                else:
                    desc = f'za mało funduszy!'
                    embed = discord.Embed(color=discord.Color.green(), title=f'TURYSTYKA', description=desc)
                    my_msg = await interaction.response.send_message(embed=embed, ephemeral=True)
                krajedict[f'{kraj}'].finbudzet = finbudzet
    save(f"{kraj}", interaction.guild.id)


@wojna.command(
    name="podsłuch",
    description="info o wojnie :D"
)
async def _podsluch(interaction, *, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), warid: Option(str, "ID Wojny", autocomplete=wars)=None):
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, podkladasz pluskwe pod dywan wroga, bot pokaze ci wszystkie jednostki jakie wystawil wrog na wojne. kraj-kraj ktorym dowodzisz, warid-id wojny"), ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    embed = discord.Embed(title="Unsuccessfull operation", description = f"Niepowodzenie, potrzebujesz roli {kraj}!")
    if role is not None and role.name == f"{kraj}":
        with open(f"{ctx.guild.id}wars.json", 'r+') as f:
            f = json.load(f)
            if warid in f:
                if krajedict[f"{kraj}"].pluskwy>=1:
                    with open(f'{ctx.guild.id}{warid}.json', 'r+') as f:
                        z = json.load(f)
                        desc=""
                        for i in z:
                            desc = desc + f"{i}: {z[i]}"
                        embed = discord.Embed(color=discord.Colour(0x0000FF), title=f"Info about war {warid}", description = desc)
                else:
                    embed= discord.Embed(color=discord.Colour(0xFFFF00), title=f"Info about war {warid}", description = "Nie masz pluskw!")
            else:
                embed= discord.Embed(color=discord.Colour(0xFFFF00), title=f"Info about war {warid}", description = "Wrong warid!")
                
    await interaction.response.send_message(embed=embed, ephemeral=True)
    save(f"{kraj}", ctx.guild.id)
@wojna.command(
    name="zwiad",
    description="wysyla zwiadowce do krajdocelowy"
)
async def _zwiad(interaction, *, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), cel: Option(str, "Kraj który chcesz śledzić", autocomplete=countries)=None):
    krajdocelowy=cel
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    ctx=interaction
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, wysylasz zwiadowce, bot, jesli zwiadowca przezyl pokaze ci sily kraju docelowego, jesli  zwiadowca nie przezyl, bot powie ci jak on zmarl. kraj-kraj ktorym dowodzisz, krajdocelowy-kraj, ktorego sily wojskowe chcesz zobaczyc"), ephemeral=True)
        return
    if krajedict[kraj] == None:
        await ctx.send("Zla nazwa kraju!", hidden=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    if role is not None and role.name == f"{kraj}":
        with open(f'{ctx.guild.id}kraje.json', "r") as f:
            kraje = json.load(f)
        for i in kraje:
            if i==kraj:
                finzwiadowca = krajedict['{}'.format(kraj)].finzwiadowca
                if finzwiadowca>0:
                    finzwiadowca-=1
                    x = r.randint(0,100)
                    if x>=50:
                        read(krajdocelowy, interaction.guild.id)
                        i=krajdocelowy
                        info = f'drzewko wodne = {krajedict[f"{i}"].watertree},\ndrzewko ziemne = {krajedict[f"{i}"].groundtree},\ndrzewko powietrzne = {krajedict[f"{i}"].skytree},\ndrzewko bomb/rakiet = {krajedict[f"{i}"].bombtree},\nbudżet = {krajedict[f"{i}"].finbudzet: ,},\nludnosc = {krajedict[f"{i}"].finludnosc: ,},\nzelazo = {krajedict[f"{i}"].finzelazo},\nwegiel = {krajedict[f"{i}"].finwegiel},\nsrebro = {krajedict[f"{i}"].finsrebro},\nuran = {krajedict[f"{i}"].finuran},\nzłoto = {krajedict[f"{i}"].finzloto},\nNAVY = {krajedict[f"{i}"].finNAVY},\nłodzie podwodne = {krajedict[f"{i}"].finpodwodne},\nfregaty = {krajedict[f"{i}"].fregaty},\nlotniskowce = {krajedict[f"{i}"].finlotniskowce},\nkorwety = {krajedict[f"{i}"].korwety},\npancerniki={krajedict[f"{i}"].pancernik},\nniszczyciele={krajedict[f"{i}"].niszczyciel},\nokręty desantowe={krajedict[f"{i}"].findesantowce},\nartyleria = {krajedict[f"{i}"].finartyleria},\ndywizje = {krajedict[f"{i}"].findywizje},\nzwiadowcy = {krajedict[f"{i}"].finzwiadowca},\ndziała przeciwlotnicze = {krajedict[f"{i}"].finprzeciwlot},\nf16 = {krajedict[f"{i}"].finf16},\nf35 = {krajedict[f"{i}"].finf35},\nnighthawk = {krajedict[f"{i}"].finnighthawk},\nlockheed = {krajedict[f"{i}"].finlockheed},\nhelikoptery piechoty = {krajedict[f"{i}"].finhelikopterypiechoty}.'
                        title = "ZWIAD"
                        embed = discord.Embed(color=discord.Color.green(), title="Zwiad", description=info)
                        try:
                            msg = await ctx.author.send(embed=embed)
                            await interaction.response.send_message("info wyslane na dm!", ephemeral=True)
                        except:
                            await interaction.response.send_message("Masz zablokowane DM! Odblokuj wiadomości od członków serwera! Ze względu na to wyślemy info na ten kanał", embed=embed, ephemeral=True)


                    else:
                        z = r.choice(['został znaleziony', 'został złapany', 'został zabity', 'zgubił się'])
                        title = 'Zwiad się nie powiódł!'
                        desc = f'zwiadowca {z}'
                        embed = discord.Embed(color=discord.Colour(0xFF0000), title=title, description=desc)
                        try:
                            await interaction.user.send(embed=embed)
                            await interaction.response.send_message('sprawdź dm!', ephemeral=True)
                        except:
                            await interaction.response.send_message("Masz zablokowane DM! Odblokuj wiadomości od członków serwera! Ze względu na to wyślemy info na ten kanał", embed=embed, ephemeral=True)
                else:
                    title = 'Nie masz zwiadowców!'
                    desc = 'zrekrutuj zwiadowcę!'
                    embed = discord.Embed(title=title, description=desc)
                    await interaction.response.send_message(embed=embed)
                krajedict['{}'.format(kraj)].finzwiadowca = finzwiadowca
    save(f"{kraj}", ctx.guild.id)



timedelays = {
    "węgiel": 40,
    "żelazo": 45,
    "srebro": 35,
    "uran": 70,
    "złoto": 50,
    "kobalt": 60,
    "ropa naftowa": 100    
}
corrects = {
        "węgiel": "finwegiel",
        "żelazo": "finzelazo",
        "srebro": "finsrebro",
        "uran": "finuran",
        "złoto": "finzloto",
        "kobalt": "finkobalt",
        "ropa naftowa": "finnafta",
}
async def mater(ctx: discord.AutocompleteContext):
    return surowce
@kraje.command(
    name="wykopaliska",
    description="rozpoczyna wykopaliska w danym kraju"
)
async def _wykopaliska(interaction, *, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), surowiec: Option(str, "Surowiec", autocomplete=mater)=None, ilosc: int=None):
    ctx=interaction
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    with open(f"{ctx.guild.id}countrytypes.json", "r") as f:
        z = json.load(f)
    
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{ctx.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, rozpoczynasz wykopaliska w danym kraju, po ich zakonczeniu dostajesz dana ilosc surowca. kraj-kraj ktorym dowodzisz, surowiec-surowiec ktory chcesz wykowac(dostepne: srebro złoto uran węgiel żelazo), ilosc-ilosc surowca, ktora chcesz wykopac."), ephemeral=True)
        return
    if krajedict[kraj] == None:
        await interaction.response.send_message("Zla nazwa kraju!", ephemeral=True)
        return
    role = discord.utils.get(ctx.user.roles, name=f"{kraj}")
    with open(f"{ctx.guild.id}countrytypes.json", "r") as f:
        z = json.load(f)
    for i in z:
        if i==f"{kraj} owner":
            zwierzchik = z[f"{kraj} owner"]
            print(zwierzchik)
            role2 = discord.utils.get(ctx.user.roles, name=f"{zwierzchik}")
    if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name == f"{zwierzchik}":
        if krajedict[f"{kraj}"].toogledwykop>=2:
            embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="możesz mieć maksymalnie 2 włączone wykopy na raz")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            if ilosc>40:
                embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="możesz wykopać maksymalnie 40kg na raz")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                krajedict[f"{kraj}"].toogledwykop+=1
                desc=f'kopanie {surowiec} rozpoczęte, wyniki będą przesłane na **DM**.'
                embed = discord.Embed(color=discord.Color.blue(), title='wykopy', description=desc)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                mins = ilosc*timedelays[surowiec]
                await asyncio.sleep(mins*timecount)
                krajedict[f"{kraj}"].toogledwykop-=1
                ssimple = krajedict[f"{kraj}"].__dict__
                ssimple[corrects[str(surowiec)]]+=ilosc
                                    
                try:
                    embed = discord.Embed(color=discord.Color.green(), title='wykopy', description=f'kopanie {surowiec} w ilości {ilosc} zakończone.')
                    await interaction.user.send(embed=embed)
                except:
                    embed = discord.Embed(color=discord.Color.green(), title='wykopy', description=f'kopanie zakończone {interaction.user.mention}')
                    await interaction.channel.send(embed=embed)
                    for i in ssimple:
                        setattr(Kraj, i, ssimple[i])
                    
    save(f"{kraj}", ctx.guild.id)
    



@kraje.command(name = "info", description = "wyswietl informacje o swoim kraju")
async def info(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries)):
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    ctx=interaction.response.send_message
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await ctx(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), ephemeral=True)
        return
    if krajedict[kraj] == None:
        await ctx("Zla nazwa kraju!", ephemeral=True)
        return
    read(f"{kraj}", interaction.guild.id)
    role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
    if role is not None and role.name == f"{kraj}":
        info = "**INFO O KRAJU:**\n"
        sss = krajedict[f"{kraj}"].__dict__
        print(sss)
        for i in sss:
            if i=="finlandbonus" or i=="finlanddebonus" or i=="toogledmobi" or i=="toogledwykop":
                pass
            else:
                li = i
                i = i.replace("name", "nazwa")
                i = i.replace("tree", " drzewko")
                i = i.replace("water", "wodne")
                i = i.replace("_", " ")
                i = i.replace("ground", "naziemne")
                i = i.replace("sky", "powietrzne")
                i = i.replace("bomb", "bombowe")
                i = i.replace("tzaar", "Car")
                i = i.replace("fin", "")
                i = i.replace("nades", "granaty")
                i = i.replace("przeciwlot", "działa przeciwlotnicze")
                i = i.replace("nades", "granaty")
                info = f"{info}\n{i}: {sss[li]},"
        title = "INFO"
        embed = discord.Embed(color=discord.Colour(0xFFFF00), title=title, description=info)

        i=kraj
        await ctx(embed=embed, ephemeral=True)
    with open(f"{interaction.guild.id}countrytypes.json", "r") as f:
        z = json.load(f)
    for i in z:
        if i==f"{kraj} owner":
            zwierzchik = z[f"{kraj} owner"]
            print(zwierzchik)
            role = discord.utils.get(interaction.user.roles, name=f"{zwierzchik}")
            if role is not None and role.name == f"{zwierzchik}":
                for i in sss:
                    if i=="finlandbonus" or i=="finlanddebonus" or i=="toogledmobi" or i=="toogledwykop":
                        pass
                    else:
                        li = i
                        i = i.replace("name", "nazwa")
                        i = i.replace("tree", " drzewko")
                        i = i.replace("water", "wodne")
                        i = i.replace("_", " ")
                        i = i.replace("ground", "naziemne")
                        i = i.replace("sky", "powietrzne")
                        i = i.replace("bomb", "bombowe")
                        i = i.replace("tzaar", "Car")
                        i = i.replace("fin", "")
                        i = i.replace("nades", "granaty")
                        i = i.replace("przeciwlot", "działa przeciwlotnicze")
                        i = i.replace("nades", "granaty")
                        info = f"{info}\n{i}: {sss[li]},"
                #info = f'drzewko wodne = {krajedict[f"{kraj}"].watertree},\ndrzewko ziemne = {krajedict[f"{kraj}"].groundtree},\ndrzewko powietrzne = {krajedict[f"{kraj}"].skytree},\ndrzewko bomb/rakiet = {krajedict[f"{kraj}"].bombtree},\nbudżet = {krajedict[f"{kraj}"].finbudzet: ,},\nludnosc = {krajedict[f"{kraj}"].finludnosc: ,},\nzelazo = {krajedict[f"{kraj}"].finzelazo},\nwegiel = {krajedict[f"{kraj}"].finwegiel},\nropa naftowa = {krajedict[f"{kraj}"].finnafta},\nkobalt = {krajedict[f"{kraj}"].finkobalt},\nsrebro = {krajedict[f"{kraj}"].finsrebro},\nuran = {krajedict[f"{kraj}"].finuran},\nzłoto = {krajedict[f"{kraj}"].finzloto},\nłodzie podwodne = {krajedict[f"{kraj}"].finpodwodne},\nfregaty = {krajedict[f"{kraj}"].fregaty},\nlotniskowce = {krajedict[f"{kraj}"].finlotniskowce},\nkorwety = {krajedict[f"{kraj}"].korwety},\npancerniki={krajedict[f"{kraj}"].pancernik},\nniszczyciele={krajedict[f"{kraj}"].niszczyciel},\nokręty desantowe={krajedict[f"{kraj}"].findesantowce},\nartyleria = {krajedict[f"{kraj}"].finartyleria},\ndywizje = {krajedict[f"{kraj}"].findywizje},\nzwiadowcy = {krajedict[f"{kraj}"].finzwiadowca},\ndziała przeciwlotnicze = {krajedict[f"{kraj}"].finprzeciwlot},\nf16 = {krajedict[f"{kraj}"].finf16},\nnapalm = {krajedict[f"{kraj}"].napalm},\ngranaty = {krajedict[f"{kraj}"].nades},\nbunker buster = {krajedict[f"{kraj}"].bb},\nf35 = {krajedict[f"{kraj}"].finf35},\nnighthawk = {krajedict[f"{kraj}"].finnighthawk},\nlockheed = {krajedict[f"{kraj}"].finlockheed},\nsnajper={krajedict[f"{kraj}"].snajperzy},\ndrużyna gazująca={krajedict[f"{kraj}"].ekipagaz},\nS19={krajedict[f"{kraj}"].betterarty},\nbalistyczne={krajedict[f"{kraj}"].balistyczne},\nHwaseong={krajedict[f"{kraj}"].Hwaseong},\n,\nCAR={krajedict[f"{kraj}"].tzaar},\nhelikoptery piechoty = {krajedict[f"{kraj}"].finhelikopterypiechoty},\npluskwy={krajedict[f"{kraj}"].pluskwy},\nabrams={krajedict[f"{kraj}"].abrams}'
                title = "INFO"
                embed = discord.Embed(color=discord.Colour(0xFFFF00), title=title, description=info)
                msg = await ctx(embed=embed, ephemeral=True)
            else:
                embed = f'wymagana rola kraju'
                title = "INFO"
                embed = discord.Embed(title=title, description=embed)


                msg = await ctx(embed=embed, ephemeral=True)
    





global counting




counting=-1

@operator.command(
    name="session_create",
    description="creates session"
) 
async def _session(interaction):
    guild = interaction.guild
    await guild.create_role(name="World-Operator")
    with open(f"{interaction.guild.id}kraje.json", "w") as f:
        json.dump({}, f)
    with open(f"{interaction.guild.id}wars.json", "w") as f:
        json.dump({}, f)
    with open(f"{interaction.guild.id}rynek.json", "w") as f:
        json.dump({}, f)
    with open(f"{interaction.guild.id}sojusze.json", "w") as f:
        json.dump({}, f)
    with open(f"{interaction.guild.id}aukcje.json", "w") as f:
        json.dump({}, f)
    with open(f"{interaction.guild.id}countrytypes.json", "w") as f:
        json.dump({}, f)
    await interaction.response.send_message(embed=discord.Embed(color=discord.Color.green(), title="Session", description="Session has been set up successfully"))
@operator.command(
    name="create",
    description="tworzy kraj, tylko dla World-Operator"
)
async def _create(interaction, kraj: str):
    role = discord.utils.get(interaction.user.roles, name=f"World-Operator")
    if role is not None and role.name == f"World-Operator":
        if len(kraj)>=35:
            desc = "Too much characters"
            embed=discord.Embed(title='dude', description=desc)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            
            global counting
            counting+=1
            guild = interaction.guild
            await guild.create_role(name=kraj)
            try:
                with open(f"{interaction.guild.id}kraje.json", "r") as f:
                    z = json.load(f)
            except:
                await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description="Nie stworzyles sesji! Uzyj /session_create aby stworzyc sesje!"), ephemeral=True)
            ID = f'{counting}.{datetime.datetime.now()}'
            z[f'{kraj}'] = ID
            with open(f"{interaction.guild.id}kraje.json", "w") as f:
                json.dump(z, f)
            krajedict["{}".format(kraj)]=Kraj(kraj)

            save(f"{kraj}", interaction.guild.id)
                        
            desc = f'Stworzono kraj {kraj}'
            embed = discord.Embed(title='{}'.format(kraj), description=desc)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
    else:
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.red(), description="Nie jestes World-Operator!"), ephemeral=True)
@operator.command(
    name="ban",
    description="usuwa dostep do bota, tylko dla World Bot Devs"
)
async def ban(interaction, user: discord.Member, *, reason:str = None):
    if interaction.user.id==678191118063632388:
        with open("bannedids.json",  'r+') as f:
            z = json.load(f)
        z[f"{user.id}"] = reason
        with open("bannedids.json",  'w+') as f:
            json.dump(z, f)
        embed = discord.Embed(color = discord.Color.red(), description=f"{user.mention} zostal zbanowany z world bot :tm: powod: {reason}")
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(embed = discord.Embed(color = discord.Color.red(), description=f"you're not world bot dev!"), ephemeral=True)
@sojusze.command(
    name="usuń",
    description="usun sojusz, tylko dla World-Operator"
)
async def test(interaction, nazwa:str, powod:str):
    role = discord.utils.get(interaction.user.roles, name=f"World-Operator")
    if role is not None and role.name == f"World-Operator":
        try:
            with open(f"{ctx.guild.id}sojusze.json", 'r+') as f:
                z = json.load(f)
            button_da = Button(label="Tak", style=discord.ButtonStyle.green, emoji="✔️")
            button_daN = Button(label="Nie", style=discord.ButtonStyle.red)
            async def callback_da(interaction):
                try:
                    del z[f"{nazwa}"]
                except:
                    await interaction.response.send_message(embed= discord.Embed(color= discord.Color.red(), description="error 14, alliance does not exist"), ephemeral=True)
                    return
                with open(f"{ctx.guild.id}sojusze.json", 'w+') as f:
                    json.dump(z, f)
                
                await interaction.response.send_message(embed=discord.Embed(color= discord.Color.purple(), description=f"usunieto  {nazwa}"))
            async def callback_daN(interaction):
                interaction.response.send_message(embed= discord.Embed(color= discord.Color.green(), description="anulowano"), ephemeral=True)
            button_da.callback=callback_da
            button_daN.callback=callback_daN
            view_da=View()
            view_da.add_item(button_da)
            view_da.add_item(button_daN)
            await interaction.response.send_message(embed= discord.Embed(view=view_da, color= discord.Color.red(), description="Czy napewno chcesz usunac sojusz?"), ephemeral=True)
            
        except:
            await interaction.response.send_message(embed=discord.Embed(color= discord.Color.red(), description="error 13, broken file "), ephemeral=True)
    else:
        await interaction.response.send_message("nie jestes operatorem!", ephemeral=True)


@operator.command(
    name="set_msg_channel",
    description="ustaw kanal z self eventami bota"
)
async def setchannel(interaction):
    role = discord.utils.get(interaction.user.roles, name=f"World-Operator")
    if role is not None and role.name == f"World-Operator":
        with open("main_channels.json", 'r+') as f:
            z = json.load(f)
        z[f"{interaction.guild.id}"]=interaction.channel.id
        with open("main_channels.json", 'r+') as f:
            json.dump(z, f)
        await interaction.response.send_message("gotowe", ephemeral=True)
    
async def zdarzenieloop():
    await client.wait_until_ready()
    for guild in client.guilds:
        with open("main_channels.json", 'r+') as f:
            z = json.load(f)
        try:
            channel = client.get_channel(z[f"{guild.id}"])
        except:
            print("errno200")
        try:
            with open(f"{guild.id}kraje.json", "r+") as f:
                kraje = json.load(f)
        except:
            print(f"guild {guild.name} doesn't have any session")
            return
        rd = r.randint(1,len(kraje))
        countr=0
        for i in kraje:
            finludnosc = krajedict[f"{i}"].finludnosc
            countr+=1
            print(rd, countr)
            if rd==countr:
                list = ["Trzęsienie ziemii", "Wulkan", 'Tsunami']
                choose = r.choice(list)
                ludnoscstratna=r.randint(45,100)
                if ludnoscstratna>krajedict[f"{i}"].finludnosc:
                    ludnoscstratna=krajedict[f"{i}"].finludnosc
                    finludnosc-= ludnoscstratna
                    list = ["Trzęsienie ziemii", "Wulkan", 'Tsunami']
                    choose = r.choice(list)
                    desc = f'{choose} wystartowało w {i}. Zmarło {ludnoscstratna} osób. Kraj upadl, nie ma wiecej osob w kraju'
                    embed = discord.Embed(color=discord.Color.red(), title=f'{choose}', description=desc)
                    await channel.send(embed=embed)
                    krajedict[f"{i}"].finludnosc = finludnosc
                    save(i, guild.id)
                    return
                finludnosc-= ludnoscstratna
                desc = f'{choose} wystartowało w {i}. Zmarło {ludnoscstratna} osób.'
                embed = discord.Embed(color=discord.Color.red(), title=f'{choose}', description=desc)
                await channel.send(embed=embed)
                krajedict[f"{i}"].finludnosc = finludnosc
                save(i, guild.id)

            if krajedict[f"{i}"].finturystyka*5000<krajedict[f"{i}"].finpodatek:
                if krajedict[f"{i}"].finturystyka*10000<krajedict[f"{i}"].finpodatek:
                    ludnoscstratna = r.randint(450, 1000)
                else:
                    ludnoscstratna = r.randint(50, 100)
                if ludnoscstratna>krajedict[f"{i}"].finludnosc:
                    ludnoscstratna=krajedict[f"{i}"].finludnosc
                    krajedict[f"{i}"].finludnosc-= ludnoscstratna
                    desc = f'Emigracja wystartowała w {i}. Emigrowało {ludnoscstratna} osób.'
                    embed = discord.Embed(color = discord.Color.red(), title=f'Emigracja', description=desc)
                    await channel.send(embed=embed)
                    save(i, guild.id)
                    return
                finludnosc-= ludnoscstratna
                
                desc = f'Emigracja wystartowała w {i}. Emigrowało {ludnoscstratna} osób.'
                embed = discord.Embed(color = discord.Color.red(), title=f'Emigracja', description=desc)
                my_msg = await channel.send(embed=embed)
                krajedict[f"{i}"].finludnosc = finludnosc
                save(i, guild.id)
            elif krajedict[f"{i}"].finturystyka*5000>krajedict[f"{i}"].finpodatek:
                ludnoscstratna=r.randint(10,40)
                if krajedict[f"{i}"].finturystyka*5000>=krajedict[f"{i}"].finpodatek*1.5:
                    ludnoscstratna= ludnoscstratna*2
                finludnosc+= ludnoscstratna
                desc = f'Imigracja wystartowała w {i}. Imigrowało {ludnoscstratna} osób.'
                embed = discord.Embed(color=discord.Color.blue(), title=f'Imigracja', description=desc)
                my_msg = await channel.send(embed=embed)
                krajedict[f"{i}"].finludnosc=finludnosc
                save(i, guild.id)
    await asyncio.sleep(20*60*60)
                
async def podatkiloop():
    for guild in client.guilds:
        try:
            with open(f"{guild.id}kraje.json", "r+") as f:
                kraje = json.load(f)
        except:
            print(f"guild {guild.name} doesn't have any session")
            return
        for i in kraje:
            read(i, guild.id)
            finludnosc = krajedict[f"{i}"].finludnosc
            finbudzet = krajedict[f"{i}"].finbudzet
            finpodatek = krajedict[f"{i}"].finpodatek
            finzaplata = finpodatek*finludnosc
            finbudzet += finzaplata
                
            krajedict['{}'.format(i)].finbudzet = finbudzet
            save(f"{i}", guild.id)
        title = "Podatki"
        desc = f"Podatki zostaly wplacone do budzetu wszystkich panstw z tej sesji"
        embed = discord.Embed(color = discord.Color.purple(), title=title, description=desc)
        with open("main_channels.json", 'r+') as f:
            z = json.load(f)
        try:
            channel = client.get_channel(z[f"{guild.id}"])
            await channel.send(embed=embed)
        except:
            print(f"no main channel found in guild {guild.name}")
    print('zebrano podatki!')
    await asyncio.sleep(86400)
        


@operator.command(
    name="podatkieveryone",
    description="podatki"
)
async def podatkieveryone(interaction, bez:str=None):
    role = discord.utils.get(interaction.user.roles, name=f"World-Operator")
    if role is not None and role.name == f"World-Operator":
        with open(f"{interaction.guild.id}kraje.json", "r+") as f:
            kraje = json.load(f)
            
            for i in kraje:
                e=True
                if e:
                    read(i, interaction.guild.id)
                    finludnosc = krajedict[f"{i}"].finludnosc
                    finbudzet = krajedict[f"{i}"].finbudzet
                    finpodatek = krajedict[f"{i}"].finpodatek
                    print(finpodatek)
                    finzaplata = finpodatek*finludnosc
                    finbudzet += finzaplata
                    
                    krajedict['{}'.format(i)].finbudzet = finbudzet
                    save(f"{i}", ctx.guild.id)
            title = "Podatki"
            desc = f"Podatki zostaly wplacone do budzetu wszystkich panstw z tej sesji"
            embed = discord.Embed(title=title, description=desc)
            await interaction.channel.send(embed=embed)
    else:
        await interaction.response.send_message("no perms?", ephemeral=True)
    
@sojusze.command(
    name="dodaj",
    description="stworz nowy sojusz, tylko dla World-Operator"
)
async def calliance(interaction, nazwa:str, czlonkowie:str):
    role = discord.utils.get(interaction.user.roles, name=f"World-Operator")
    if role is not None and role.name == f"World-Operator":
        try:
            with open(f"{ctx.guild.id}sojusze.json", 'r+') as f:
                z = json.load(f)
            z[f"{nazwa}"] = czlonkowie
            with open(f"{ctx.guild.id}sojusze.json", 'w+') as f:
                json.dump(z, f)
            await interaction.response.send_message(embed=discord.Embed(color= discord.Color.purple(), description=f"stworzono {nazwa}"))
        except:
            await interaction.response.send_message(embed=discord.Embed(color= discord.Color.red(), description="error 13, broken file"), ephemeral=True)
    else:
        await interaction.response.send_message("no perms?", ephemeral=True)
#pojazdy 60-120, jednostki 10 20


def finsave():
    pass
wodne=30
ziemne=30
powietrzne=30
bomby=500



listofunits ="**Lista Jednostek**"
for i in units:
    nunit=units[i]
    listofunits=listofunits+f"\\n**{i}**: {nunit.type} {nunit.tier} **cena/sztuka**:{nunit.cost: ,}. czas wytwarzania 1 sztuki: {nunit.cooldown/60}min"
    
    
Uchoices = []
for i in units:
    Uchoices.append(str(i))
print(Uchoices)
async def unitschoice(ctx: discord.AutocompleteContext):
    return Uchoices
@kraje.command(
    name="mobilizacja",
    description="mobilizuj jednostke"
)

async def _createArmy(interaction, kraj: Option(str, "Kraj którym władasz", autocomplete=countries), jednostka: Option(str, "Wybierz jednostkę", autocomplete=unitschoice), ilosc: int = None):
    jednostka = jednostka.name
    try:
        a = krajedict[f'{kraj}']
    except:
        await interaction.response.send_message('nie znaleziono kraju', ephemeral=True)
        return
    print(jednostka)
    with open("bannedids.json",  'r+') as f:
        z = json.load(f)
    if f"{interaction.user.id}" in z:
        await interaction.response.send_message(embed=discord.Embed(color = discord.Color.red(), description="Jestes permanentnie zbanowany z World Bot :tm:, nie mozesz uzywac komend"), hidden=True)
        return
    
    if kraj=="help":
        await interaction.response.send_message(embed=discord.Embed(color=discord.Color.blue(), description="Uzywajac tej komendy, rozpoczynasz mobilizacje w danym kraju, po jej zakonczeniu dostajesz dana ilosc jednostki, jakie jednostki mozna stworzyc? >w 'kraj' wpisz 'info', wypisze to wszystkie jednostki jakie mozna stworzyc na danym poziomie drzewka technologicznego . kraj-kraj ktorym dowodzisz, jednostka-jednostka ktora chcesz zmobilizowac, ilosc-ilosc jednostki, jaka chcesz zmobilizowac."), ephemeral=True)
        return
    if kraj=="info":       
        embed = discord.Embed(color=discord.Colour(0xFFFF00), description=listofunits.replace("\\n", "\n"))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    try:
        if krajedict[f"{kraj}"].toogledmobi>0:
            embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="mozesz mobilizowac max 1 jednostke na raz")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
    except:
        await interaction.response.send_message("zla nazwa kraju!", ephemeral=True)
    
    role2=None
    if jednostka is not None:
        jednostka = jednostka.lower()
    if ilosc==None:
        ilosc=10
    if ilosc>20:
        embed=discord.Embed(color=discord.Colour(0xFFFF00), title="LIMIT", description="za duża ilość!")
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        role = discord.utils.get(interaction.user.roles, name=f"{kraj}")
        if role==None:
            with open(f"{ctx.guild.id}countrytypes.json", 'r+') as f:
                types = json.load(f)
                if f"{kraj} owner" in types:
                    owner = types[f'{kraj} owner']
                    role2 = discord.utils.get(interaction.user.roles, name=f"{owner}")
        embed = discord.Embed(title="Unsuccessfull operation", description = "Zadanie nie powiodło się, sprawdź czy posiadasz rolę kraju")
        if role is not None and role.name == f"{kraj}" or role2 is not None and role2.name==f"{owner}":
            e=False
            if jednostka in units:
                e= True
                if e:
                    i = jednostka
                    unit =  units[i]
                    simple=krajedict[f"{kraj}"].__dict__
                    if simple[f"{unit.type}tree"]>=unit.tier:
                        if simple["finbudzet"]>=unit.cost*ilosc:
                            if simple[f"fin{unit.surowiec}"]>=unit.surowiecilosc:
                                embed = discord.Embed(color=discord.Color.purple(), title="Mobilizacja", description=f"Rozpoczeto mobilizacje {unit.name} za {(unit.cost*ilosc): ,} oraz {unit.surowiecilosc}x{unit.surowiec}")                
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                                krajedict[f"{kraj}"].toogledmobi+=1
                                await asyncio.sleep(units[jednostka].cooldown*ilosc)
                                krajedict[f"{kraj}"].toogledmobi-=1
                                simple["finbudzet"]-=unit.cost*ilosc
                                simple[f"fin{unit.surowiec}"]>=unit.surowiecilosc
                                embed = discord.Embed(color=discord.Color.purple(), title="Mobilizacja", description=f"Zakonczono mobilizacje {unit.name}")
                                simple[f"{unit.name}"]+=ilosc
                                simple["finbudzet"]-=unit.cost*ilosc
                                simple[f"fin{unit.surowiec}"]-=unit.surowiecilosc
                                for i in simple:
                                    setattr(Kraj, i, simple[i])
                                try:
                                    await interaction.user.send(embed=embed)
                                except:
                                    await interaction.channel.send(f"{ctx.author.mention}, mobilizacja zakonczona")
                            else:
                                embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"za malo {unit.surowiec}, potrzeba {unit.surowiecilosc}")
                                await interaction.response.send_message(embed=embed, ephemeral=True)
                        else:
                            embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Za malo budzetu, potrzeba {(unit.cost*ilosc): ,}")
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                    else:
                        embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Za niski poziom drzewka, wymagany jest {unit.tier} poziom drzewka")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
            if e==False:
                embed = discord.Embed(color=discord.Color.red(), title="Mobilizacja", description=f"Jednostka nie istnieje!")
                await interaction.response.send_message(embed=embed, ephemeral=True)
        
        save(f"{kraj}", interaction.guild.id)
@client.event
async def on_ready():
    
    loop=asyncio.get_event_loop()
    a1=loop.create_task(podatkiloop())
    #loop.run_until_complete(a1)
    loop=asyncio.get_event_loop()
    a2=loop.create_task(zdarzenieloop())
    for guild in client.guilds:
        print(guild.name)
        try:
            with open(f'{guild.id}kraje.json', "r") as f:
                krajee = json.load(f)
                print(krajee)
                for i in krajee:
                    krajedict["{}".format(i)]=Kraj(i)
                    read(i, guild.id)
                    print(i, "works")
            warIDs = []
            with open(f'{guild.id}wars.json', 'r+') as f:
                z = json.load(f)
                for i in z:
                    warIDs.append(i)
            print(f"guild {guild.name} successfully loaded")
        except:
            print(f"guild {guild.name} doesn't have any session")
    print('Gotowy do gry - {0.user}'.format(client))
TOKEN = "TOKEN"

client.run(TOKEN)
 
