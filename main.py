import time
import webbrowser

import filee as filee
import requests
import subprocess
import os

# import autoupdater

print("Helloo")
time.sleep(3)


def teambewerbung():
    os.system('cls')
    print("Willkommenm")
    time.sleep(1)
    print("Bitte gebe zunächst ein paar Informationen über dich an")
    time.sleep(1)

    name = input("Bitte gebe Den Namen von dir ein: ")
    server_name = input("Bitte gebe den Namen von dem RP Server ein: ")
    stärke_1 = input("Bitte gebe eine Stärke an: ")
    stärke_2 = input("Bitte gebe eine weitere Stärke ein: ")
    schwäche_1 = input("Bitte gebe eine Schwäche ein: ")
    schwäche_2 = input("Bitte gebe eine weitere Schwäche ein: ")
    gebi = input("Bitte gebe an wann du geboren wurdest: ")
    lange = input("Bitte gebe an wie lange du schon RP spielst: ")
    online_zeiten = input("Bitte gebe deine Online Zeiten an (Mo-Fr): ")
    onlinezeiten_we = input("Bitte gebe diene Online Zeiten an (Wochenende): ")
    discordd = input("Bitte gebe dein Discord Namen an: ")
    time.sleep(1)
    file = (f'{server_name} Bewerbung.txt')
    # ---------------------------------------------------------------------------------------------------
    with open(file, 'w') as f:
        f.write(f"Teambewerbung {server_name}\n")
        f.write("                                 Inhalt:                                  \n")
        f.write("-Infos über mich\n")
        f.write("-Stärken und Schwächen\n")
        f.write("-Meine Online Zeiten\n")
        f.write(f"-Warum genau {server_name}\n")
        f.write("-Warum möchte ich ins Team?\n")
        f.write("-Warum solltet ihr mich nehmen\n")
        f.write("-Kontaktinformationen\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Infos Über mich-------------\n")
        f.write(f"Guten Tag, ich heiße {name} und bin am {gebi} geboren\n")
        f.write(f"Ich spiele seit ca. {lange} schon aktiv GTA Roleplay\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Stärken und Schwächen-------------\n")
        f.write("Meine Stärken:\n")
        f.write(f"- {stärke_1}\n")
        f.write(f"- {stärke_2}\n")
        f.write("\n")
        f.write("Meine Schwächen: \n")
        f.write(f"- {schwäche_1}\n")
        f.write(f"- {schwäche_2}\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Meine Online Zeiten-------------\n")
        f.write(f"Von Montags bis Freitags kann ich von {online_zeiten}\n")
        f.write(f"Und am Wochenende von {onlinezeiten_we}\n")
        f.write("\n")
        f.write("\n")
        f.write(f"-------------Warum genau {server_name} -------------\n")
        f.write("Ich habe mir den Roleplay Server ""ausgesucht"" da mir der Server einfach gefällt. Der Server,\n")
        f.write("die Scirpts, die Spieler.\n")
        f.write(
            "Ich mag es einfach. Das ist endlich mal so ein Server der mir gefällt, ich suche schon soo lange ein\n")
        f.write("Server wo alles einfach so ist wie es auf diesem Server ist haha.\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Deshalb möchte ich ins Team-------------\n")
        f.write(
            "Ich möchte ins Team da mir das verhalten von dem Team gefällt. Auch wollte ich schon immer mal ein Teil des \n")
        f.write("Teams auf einem vernünftigen Server sein, der mir auch gefällt.\n")
        f.write(
            "Endlich finde ich, ich habe den richtigen Server gefunden bei dem ich mich gerne als eine Stelle im Team \n")
        f.write("bewerben möchte.\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Warum solltet ihr mich nehmen-------------\n")
        f.write(
            f"Ihr solltet mich nehmen, da ich schon eine Zeit lang RP spiele {lange} und deswegen mich schon ziehmlich gut\n")
        f.write(
            "auskenne. Außerdem kenne ich mich schon recht gut mit Support aus, denn ich habe schon beobachtet wie der Support\n")
        f.write("auf eurem Server abläuft.\n")
        f.write("\n")
        f.write("\n")
        f.write("-------------Schlusswort-------------\n")
        f.write("Ich würde mich sehr über eine postive Rückmeldung freuen.\n")
        f.write("Mit freundlichen Grüßen\n")
        f.write(name)
        f.write("\n")
        f.write("\n")
        f.write("-------------Kontaktinformationen-------------\n")
        f.write("Falls weitere Fragen bestehen ist hier auch nochmal mein Discord\n")
        f.write(f"Discord:  {discordd}\n")
    time.sleep(1)
    print(f"Deine Teambewerbung für {server_name} wurde erfolgreich erstell in {file}")
    os.system(f'{file}')
    input("Drücken zum Fortfahren..")


def Policebewerbung():
    os.system('cls')
    print("Willkommenm")
    time.sleep(1)
    print("Bitte wähle die Form deiner Bewerbung aus:")
    print("(1) OOC Bewerbung")
    print("(2) IC Bewerung")
    print("(3) OOC+IC Bewerbung")
    time.sleep(1)
    choice = input("Bitte gib eine Zahl zwischen 1 und 3 ein: ")

    def poocbw():
        os.system('cls')
        print("Willkommen")

        time.sleep(2)

        print("Bitte gebe ein folgende Informationen über dich ein: ")

        time.sleep(1)

        picname = input("Bitte gebe deinen Namen ein: ")
        picservername = input("Bitte gebe den Namen des Servers ein: ")
        piclaorls = input("LSPD oder LAPD?")
        picgeburtsort = input("Wann wurdest du geboren?: ")
        poocrplange = input("Wie lange spielst du schon RP?")
        time.sleep(2)
        filee = (f' {piclaorls} Bewerbung.txt')
        # ------------------------------------write--------------------------
        with open(filee, 'w') as a:
            a.write(f"Team bewerbung {piclaorls}\n")
        time.sleep(1)
        print(f"Deine Teambewerbung für {picservername} wurde erfolgreich erstell in {filee}")
        os.system(f'{filee}')
        input("Drücken zum Fortfahren..")

    if choice == '1':
        poocbw()


#    elif choice == '2':
#        picbw()
#    elif choice == '3':
#        poocicbw()


os.system('cls')
print("Bitte wähle aus welche art von Bewerbung du haben möchtest")
print("(1) Teambewerbung"),
print("(2) Police Bewerbung"),
print("(3) Medical Bewerbung")
choice = input("Bitte gebe eine Zahl zwischen 1 und ein: ")

if choice == '1':
    teambewerbung()
elif choice == '2':
    Policebewerbung()
##elif choice == '3':
#    Medicalbewerbung()
