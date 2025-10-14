class EventManager:
    """Verwaltet Anwesenheits- und Statusdaten"""
    def __init__(self):
        self.events = {}  # {"2025-10-14": "K"}

    def add_event(self, date_str, code):
        self.events[date_str] = code

    def remove_event(self, date_str):
        if date_str in self.events:
            del self.events[date_str]

    def get_event(self, date_str):
        return self.events.get(date_str)
