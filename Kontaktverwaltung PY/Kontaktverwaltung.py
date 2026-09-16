# Kontaktverwaltung

import json

def kontakte_speichern():
    with open("kontakte.json", "w") as datei:
        json.dump(kontakte, datei)



def kontakte_laden():
    try:
        with open("kontakte.json", "r") as datei:
            return json.load(datei)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
kontakte = kontakte_laden()

def kontakt_hinzufuegen():
    name = input("name: ")
    email = input("email: ")
    telefonnummer = input("telefonnummer: ")

    if name == "":
        print("Der Name darf nicht leer sein!")
        return   # hier beendet return die Funktion

    if email == "":
            print("Die E-Mail darf nicht leer sein!")
            return

    if telefonnummer == "":
            print("Die Telefonnummer darf nicht leer sein!")
            return

    kontakt = {
        "name": name,
        "email": email,
        "telefonnummer": telefonnummer}

    kontakte.append(kontakt)
    kontakte_speichern()

    print("Kontakt wurde erfolgreich hinzugefügt!")

def kontakte_anzeigen():
    if not kontakte:
        print("Keine Kontakte vorhanden!")
        return
    
    for kontakt in kontakte:
        print("name:", kontakt["name"])
        print("e-Mail:", kontakt["email"])
        print("telefonnummer:", kontakt["telefonnummer"])
        print("------------------------------")

def kontakt_suchen():
    suchname = input("Name suchen: ")

    if suchname == "":
        print("Ungültige Auswahl, bitte gebe einen Namen ein!")
        return
    
    for kontakt in kontakte:
        if suchname == kontakt["name"]:
            print("Kontakt gefunden!")
            print("Name: ", kontakt["name"])
            print("E-Mail: ", kontakt["email"])
            print("Telefonnummer: ", kontakt["telefonnummer"])
            return
       
    print("Kein Kontakt gefunden!")

def kontakt_loeschen():
    name = input("Welchen Kontakt möchten Sie löschen?:")

    if name == "":
        print("Der Name darf nicht leer sein!")
        return

    for kontakt in kontakte:
        if name == kontakt["name"]:
            kontakte.remove(kontakt)
            kontakte_speichern()
            print("Der Kontakt wurde erfolgreich gelöscht")
            return
  
    print("Kontakt wurde nicht gefunden!")


def kontakt_bearbeiten():
    bearbeite_name = input("Von wem möchtest du die Kontaktdaten bearbeiten?: ")

    for kontakt in kontakte:
        if bearbeite_name == kontakt["name"]:
            print("Name: ", kontakt["name"])
            print("E-Mail: ", kontakt["email"])
            print("Telefonnummer:", kontakt["telefonnummer"])


            eigenschaften = input("""
            Was genau möchtest du bearbeiten?: 
            1. Name
            2. E-Mail
            3. Telefonnummer
            4. Abbrechen
            

            Auswahl: """)

            if eigenschaften == "1":
                kontakt["name"] = input("Neuer Name: ")

            elif eigenschaften == "2":
                kontakt["email"] = input("Neue E-Mail: ")

            elif eigenschaften == "3":
                kontakt["telefonnummer"] = input("Neue Telefonnummer: ")

            elif eigenschaften == "4":
                return

            else:
                print("Ungültige Auswahl!")
                return

            kontakte_speichern()
            return

    print("Kontakt wurde nicht gefunden!")


while True:

    print("==== Kontaktverwaltung ====")
    print("")
    print("1. Kontakt hinzufügen")
    print("2. Kontakte anzeigen")
    print("3. Kontakt suchen")
    print("4. Kontakt löschen")
    print("5. Kontakt bearbeiten")
    print("6. Programm beenden")
    print("")

    try:
        auswahl = int(input("Auswahl: "))
    except ValueError:
        print("Bitte gib eine Zahl ein!: ")
        continue

    if auswahl < 1 or auswahl > 6:
        print("Ungültige Auswahl!")
        continue

    if auswahl == 1:
        kontakt_hinzufuegen()

    elif auswahl == 2:
        kontakte_anzeigen()

    elif auswahl == 3:
        kontakt_suchen()

    elif auswahl == 4:
        kontakt_loeschen()

    elif auswahl == 5:
        kontakt_bearbeiten()
        
    elif auswahl == 6:
        print("Programm beendet")
        break


    
