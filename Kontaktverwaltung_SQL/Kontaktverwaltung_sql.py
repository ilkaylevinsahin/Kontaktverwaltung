# SQLite in Python
import sqlite3

# Datenbankverbindung
verbindung = sqlite3.connect("kontakte.db")

# Cursor erstellen
cursor = verbindung.cursor()

# Tabelle mit sqlite 3 erstellen
cursor.execute("""
        CREATE TABLE IF NOT EXISTS kontakte (   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        telefonnummer TEXT NOT NULL  
        
        )
    """)

# hergestellt 
verbindung.commit()


def kontakte_anzeigen():
    cursor.execute("""SELECT * FROM kontakte""")

    kontakte = cursor.fetchall()

    for kontakt in kontakte:
        id = kontakt[0]
        name = kontakt[1]
        email = kontakt[2]
        telefonnummer = kontakt[3]

        print("ID:",id)
        print("Name:",name)
        print("E-Mail:",email)
        print("Telefonnummer:",telefonnummer)
        print("--------------------------------")        


def kontakt_hinzufuegen():
    name = input("Name: ")
    email = input("email:")
    telefonnummer = input("Telefonnummer:")

    cursor.execute(""" 
            INSERT INTO kontakte(name, email, telefonnummer)
            VALUES (?, ?, ?)
            """,(name, email, telefonnummer))

    #gespeichert
    verbindung.commit()

    print("Kontakt erfolgreich hinzugefügt")


def kontakt_suchen():
    suchname = input("Name:")

    cursor.execute("""
            SELECT * FROM kontakte WHERE name = ?
            """, (suchname,))

    ergebnisse = cursor.fetchall()   # Datenbank durchsucht Tabelle

    if not ergebnisse:
        print("Der Kontakt ist nicht vorhanden!")
        return

    # gebe alle Kontaktdaten vom gefundenen Kontakt zurück
    for kontakt in ergebnisse:
        print("ID:", kontakt[0])
        print("Name:", kontakt[1])
        print("E-Mail:", kontakt[2])
        print("Telefonnummer:", kontakt[3])

def kontakt_loeschen():
    loeschname = input("Name:")

    cursor.execute("""
                    SELECT * FROM kontakte where name = ?
            """, (loeschname,))

    loeschname_ergebnis = cursor.fetchall()

    if not loeschname_ergebnis:
        print("Der Kontakt wurde nicht gefunden!")
        return
    
    cursor.execute("""
            DELETE FROM kontakte WHERE name = ?
            """, (loeschname,))

    verbindung.commit()

    print ("Der Kontakt wurde erfolgerich gelöscht!")


def kontakt_bearbeiten():
    bearbeiten_name = input("Welchen Kontakt möchten Sie bearbeiten?: ")

    cursor.execute("""
                    SELECT * FROM kontakte where name = ?
                """, (bearbeiten_name,))

    bearbeiten_ergebnis = cursor.fetchall()  #extrahieren wir alle Daten aus kontakte
                                              # und schauen ob der eingegebene Name existiert
    if not bearbeiten_ergebnis:
        print("Der Kontakt, den Sie bearbeiten möchte wurde nicht gefunden!")
        return
    else:
        print("")
        print("Welche Kontaktdaten möchten Sie bearbeiten?: ")
        print("")
        print("1. Name")
        print("2. E-Mail")
        print("3. Telefonnummer")

        try:
            eingabe_bearbeiten =  int(input("Bitte geben Sie eine Zahl zwischen 1-3 ein: "))
            if eingabe_bearbeiten < 1 or eingabe_bearbeiten > 3:
                print("Die Eingabe ist ungültig!")
                return
        except ValueError:   # Wenn Buchstaben eingegeben werden
            print("Bitte geben Sie nur Zahlen ein!")
            return
                
        

        if eingabe_bearbeiten == 1:
            edit_name = input("Name: ")
            cursor.execute("""
            UPDATE kontakte SET name = ? WHERE name = ?""",(edit_name,bearbeiten_name))
            print("Bearbeitung erfolgreich gespeichert!")

            verbindung.commit()

        elif eingabe_bearbeiten == 2:
            edit_email = input("E-Mail: ")
            cursor.execute("""
            UPDATE kontakte SET email = ? WHERE name = ?""",(edit_email,bearbeiten_name))
            print("Bearbeitung erfolgreich gespeichert!")

            verbindung.commit()

        elif eingabe_bearbeiten == 3:
            edit_tel = input("Telefonnummer")
            cursor.execute("""
            UPDATE kontakte SET telefonnummer = ? WHERE name = ?""",(edit_tel,bearbeiten_name))
            print("Bearbeitung erfolgreich gespeichert!")

            verbindung.commit()

        else:
            print("Bitte geben Sie nur Zahlen zwischen 1-3 ein! Vielen Dank!")  
    


while True:
    print("")
    print("--------------------")
    print("Kontaktverwaltung")
    print("")
    print("1. Kontakt hinzufügen")
    print("2. Kontakte_anzeigen")
    print("3. Kontakt löschen")
    print("4. Kontakt bearbeiten")
    print("5. Programm beenden")

    try:
        auswahl = int(input("Bitte geben Sie eine Zahl ein: "))
    except ValueError:
            print("Bitte gebe nur Zahlen ein!")
            continue

    if auswahl < 1 or auswahl > 5:
         print("Ungültige Auswahl!")
         continue


    if auswahl == 1:
        print("")
        print("")
        kontakt_hinzufuegen()

    elif auswahl == 2:
        print("")
        print("")
        kontakte_anzeigen()

    elif auswahl == 3:
        print("")
        print("")
        kontakt_loeschen()

    elif auswahl == 4:
        print("")
        print("")
        kontakt_bearbeiten()

    elif auswahl == 5:
        print("Programm wurde beendet")
        break




verbindung.close()




    