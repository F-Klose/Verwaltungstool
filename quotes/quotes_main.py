#---------------------------------------------------------------------------------------------------------------------------------------------
#importe <----------------------------<------------------------------<------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
import sqlite3
import subprocess
from quotes.git_funktions import git_pull_db, git_push_db

#---------------------------------------------------------------------------------------------------------------------------------------------
# funktionen <----------------------------<------------------------------<--------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def get_quotes(db_path="quotes/quotes.db"):
    """Lädt alle Zitate aus der SQLite-Datenbank und gibt sie als Liste von Strings zurück."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute ("SELECT text FROM Zitat")
    quotes = cursor.fetchall()
    conn.close()
    return [row[0] for row in quotes] if quotes else ["Keine Zitate."]

def add_quotes(text, db_path="quotes/quotes.db"):
    """Fügt ein neues Zitat in die SQLite-Datenbank ein."""
    if not text.strip():
        return False
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO Zitat (text) VALUES (?)", (text.strip(),))
    conn.commit()
    conn.close()
    git_pull_db()
    return True

def git_pull_quotesdb():
    """Holt die aktuelle quotes.db von Git."""
    git_pull_db()

def git_push_quotesdb(commit_message="Update quotes.db"):
    """Pusht die aktuelle quotes.db zu Git."""
    git_push_db()

def git_merge_quotesdb():
    """Führt ein git merge aus (z.B. nach Pull)."""
    try:
        subprocess.run(["git", "merge"], check=True)
        print("Git Merge für quotes.db ausgeführt.")
    except Exception as e:
        print(f"Fehler bei git merge: {e}")


