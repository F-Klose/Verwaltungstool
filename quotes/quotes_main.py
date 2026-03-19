#---------------------------------------------------------------------------------------------------------------------------------------------
#importe <----------------------------<------------------------------<------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

from supabase import create_client, Client, AuthApiError
from postgrest.exceptions import APIError
#---------------------------------------------------------------------------------------------------------------------------------------------
# funktionen <----------------------------<------------------------------<--------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

SUPABASE_BASE_URL = "https://fburyyzzewkdqxutuayl.supabase.co"
API_KEY = "sb_publishable_rRavetQ4CoLx_I29JkWOsQ_SvgyuP2u"
# TODO: Auslagern in Config

def get_quotes():
    supabase = create_client(SUPABASE_BASE_URL , API_KEY)

    response = (
        supabase.table("quotes")
        .select("text")
        .execute()
    )

    text_list = []
    for row in response.data:
        text_list.append(row['text'])
    return text_list if len(text_list) > 0 else ["Keine Zitate."]

def add_quotes(text, db_path):
    """Fügt ein neues Zitat in die Supabase-Datenbank ein."""
    supabase = create_client(SUPABASE_BASE_URL, API_KEY)

    text = text.strip()
    if not text:
        return False
    try: 
        response = (
            supabase.
            table("quotes").
            insert({"text": text}).
            execute()
        )
    except APIError as e:
        print(f"Ein API-Fehler ist aufgetreten: {e.message}")
        print(f"Status Code: {e.code}")
        return False
    except Exception as e:
        print(f"Unerwarter Fehler: {e}")
        return False

    return True