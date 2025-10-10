class EventManager:
    """
    Verwalten von Anwesenheiten und anderen Ereignissen pro Tag.

    Die Events werden in einem Dictionary gespeichert, wobei das Datum als Schlüssel
    im Format "YYYY-MM-DD" und der Anwesenheitscode als Wert hinterlegt wird.

    Beispiel:
        manager = EventManager()
        manager.add_event("2025-10-10", "HO")
        code = manager.get_event("2025-10-10")  # "HO"
    """

    def __init__(self):
        """
        Initialisiert den EventManager mit einem leeren Dictionary.
        """
        self.events = {}  # { "YYYY-MM-DD": "Code" }

    def add_event(self, date_str, code):
        """
        Fügt ein Event für ein bestimmtes Datum hinzu oder überschreibt ein vorhandenes.

        Args:
            date_str (str): Datum im Format "YYYY-MM-DD"
            code (str): Anwesenheits- oder Eventcode, z.B. "K", "HO", "U", "F"
        """
        self.events[date_str] = code

    def get_event(self, date_str):
        """
        Gibt den Code eines Events für ein bestimmtes Datum zurück.

        Args:
            date_str (str): Datum im Format "YYYY-MM-DD"

        Returns:
            str | None: Der gespeicherte Code oder None, falls kein Event existiert.
        """
        return self.events.get(date_str, None)

    def remove_event(self, date_str):
        """
        Entfernt ein Event für ein bestimmtes Datum, falls vorhanden.

        Args:
            date_str (str): Datum im Format "YYYY-MM-DD"
        """
        if date_str in self.events:
            del self.events[date_str]

    def get_all_events(self):
        """
        Gibt alle gespeicherten Events zurück.

        Returns:
            dict: Dictionary aller Events im Format { "YYYY-MM-DD": "Code" }
        """
        return self.events
