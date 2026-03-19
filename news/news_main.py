#----------------------------------------------
# --------------> importe  <-------------------
#----------------------------------------------

import os
from supabase import create_client, Client
from datetime import datetime, timedelta
import subprocess
from postgrest.exceptions import APIError



#----------------------------------------------
# -------> funktionen der NEWS mit DB <--------
#----------------------------------------------
SUPABASE_BASE_URL = "https://fburyyzzewkdqxutuayl.supabase.co"
API_KEY = "sb_publishable_rRavetQ4CoLx_I29JkWOsQ_SvgyuP2u"


def get_news():
    """
    lädt alle News der letzten 30 Tage aus der SQLite-Datenbank und gibt sie als Liste von Strings zurück.
    Wenn keine News vorhanden sind, wird eine Liste mit dem Eintrag "Keine aktuellen Nachrichten." zurückgegeben.
    30 Tage werden als aktuell betrachtet.
    1. Verbindung zur SQLite-Datenbank herstellen
    2. Alle News abrufen, die in den letzten 30 Tagen erstellt wurden
    3. Verbindung zur Datenbank schließen
    4. Liste der News-Texte zurückgeben oder eine Standardnachricht, wenn keine News vorhanden sind
    5. Die News werden nach Erstellungsdatum absteigend sortiert
    6. Das Datum wird im Format "YYYY-MM-DD HH:MM:SS" gespeichert und verglichen
    """
    supabase = create_client(SUPABASE_BASE_URL, API_KEY)

    response = (
        supabase.table("news")
        .select("*")
        .execute()
    )

    news_list =[]
    for row in response.data:
        news_list.append(row["text"])
    return news_list if news_list else ["Keine aktuellen Nachrichten."]
def delete_old_news():
    pass
    

def add_news_item(text, db_path):
    """Fügt einen neuen News-Eintrag in die SQLite-Datenbank ein."""
    supabase = create_client(SUPABASE_BASE_URL, API_KEY)
    text = text.strip()
    if not text:
        return False
    try:
        response = (
            supabase.table("news")
            .insert({"text": text})
            .execute()
        )
    except APIError as e:
        print(f"Fehler beim News API: {e.message}")
        print(f"Fehlerdetails: {e.code}")
        return False
    except Exception as e:
        print(f"Allgemeiner Fehler beim Hinzufügen der News: {e}")
        return False
    return True


#TODO: 1.Loeschfunktion aufruf entfernen 2. funktion entfernen




