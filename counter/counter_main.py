from git_funktions import git_pull_db, git_push_db
from under_funktions_main import init_db, get_counter, get_counter_total, update_counter, update_labels
DB_PATH = "stoerungen.db"
Art_der_störung = ["technisch", "algemein"]

def beenden(root):
    """
    Beendet die Anwendung und führt einen Git-Push der Datenbank durch.
    Diese Funktion wird aufgerufen, wenn der Benutzer die Anwendung schließt.
    Sie stellt sicher, dass alle Änderungen in der Datenbank vor dem Beenden gespeichert werden.
    """
    git_push_db()  # Vor dem Beenden noch einmal pushen
    root.destroy()

def main_admin():
    """
    Hauptfunktion für die Admin-Ansicht des Störungs-Counters.
    Diese Funktion initialisiert die Datenbank, zieht die neuesten Änderungen von Git,
    und zeigt eine GUI an, in der Störungen gezählt werden können.
    """
    init_db()
    git_pull_db()   # DB beim Start als Admin sofort pullen
    git_push_db()   # und sofort pushen (z.B. falls lokale Änderungen)
    pass

def main_view():
    """
    Hauptfunktion für die Anzeige des Störungs-Counters.
    Diese Funktion initialisiert die Datenbank, zieht die neuesten Änderungen von Git,
    und zeigt eine GUI an, die die aktuellen Störungen anzeigt.
    """
    init_db()
    pass

    def periodic_pull():
        git_pull_db()
        update_labels(counter_label, gesamt=True)
        root.after(15000, periodic_pull)
    update_labels(counter_label, gesamt=True)
    root.after(15000, periodic_pull)
    root.mainloop()
    pass


#TODO Gui erstellen
#TODO importe
#TODO funktionen ausbessern




