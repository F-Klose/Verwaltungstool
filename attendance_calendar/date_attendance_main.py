#----------------------------------------------
# --------------> importe  <-------------------
#----------------------------------------------
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QCalendarWidget
from PySide6.QtCore import QDate
from PySide6.QtGui import QTextCharFormat, QColor
from collections import Counter
from datetime import datetime
#----------------------------------------------
# ---------------> Pfade  <--------------------
#----------------------------------------------
CLASS_JSON_FILE = "meine_anwesenheit.json"
#----------------------------------------------
# --------------> Klassen  <-------------------
#----------------------------------------------
class AttendanceCalendar(QWidget):
    """
    Ein Kalender-Widget zur Erfassung persönlicher Anwesenheit.
    Status: Karlsruhe, Homeoffice, Urlaub, Krankheit, Feiertag.
    farben: anpassbar über STATUS_COLORS dict
    """

    STATUS_COLORS = {
        "Karlsruhe": "lightgreen",
        "Homeoffice": "#f7f78a",
        "Urlaub": "lightblue",
        "Krankheit": "lightcoral",
        "Feiertag": "lightgray"
    }

    STATUS_OPTIONS = list(STATUS_COLORS.keys())
#----------------------------------------------
# -------------> Functionen  <-----------------
#----------------------------------------------
    def __init__(self):
        """
        initialisiert das Kalender-Widget zur Anwesenheitserfassung
        1. Kalender-Widget zur Anzeige und Auswahl von Daten
        2. Label zur Anzeige des aktuellen Status für das ausgewählte Datum
        3. Dropdown-Menü zur Auswahl des Anwesenheitsstatus
        4. Button zum Speichern des ausgewählten Status für das ausgewählte Datum
        5. Anzeige der Anwesenheitsquote für den aktuellen Monat
        6. Hervorhebung der Tage im Kalender basierend auf dem gespeicherten Status
        7. Laden und Speichern der Anwesenheitsdaten in einer JSON-Datei
        8. Aktualisierung der Anzeige bei Datumsauswahl und Statusänderung
        9. Ungültige Datumsangaben in der JSON-Datei werden übersprungen und optional bereinigt
        10. Die Anwesenheitsquote wird als Prozentsatz für jeden Status im aktuellen Monat angezeigt
        11. Das Fenster hat den Titel "Meine Anwesenheit" und eine Größe von 420x350 Pixeln
        12. Die Statusoptionen sind anpassbar über die STATUS_OPTIONS Liste
        """
        super().__init__()
        self.setWindowTitle("Meine Anwesenheit")
        self.resize(420, 350)
#----------------------------------------------
# -----------------> Gui <---------------------
#----------------------------------------------
        # Widgets
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.status_label = QLabel()
        self.combo = QComboBox()
        self.combo.addItems(self.STATUS_OPTIONS)
        self.save_button = QPushButton("Status setzen")#status setzen button 

        # Neue Anzeige für Anwesenheitsquote
        self.stats_label = QLabel()
        self.stats_label.setStyleSheet("color: gray; font-size: 11px; margin-top: 4px;")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.status_label)
        layout.addWidget(self.combo)
        layout.addWidget(self.save_button)
        layout.addWidget(self.stats_label)
        self.setLayout(layout)

        # Signals
        self.save_button.clicked.connect(self.set_status_for_selected_date)
        self.calendar.clicked.connect(self.on_date_clicked)

        # Daten laden
        self.attendance = self.load_data()
        self.highlight_saved_days()
        self.update_stats_label()
#----------------------------------------------
# -------------> Functionen  <-----------------
#----------------------------------------------
    def load_data(self):
        """
        lädt die Anwesenheitsdaten aus der JSON-Datei.
        """
        try:
            with open(CLASS_JSON_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        """
        speichert die Anwesenheitsdaten in der JSON-Datei.
        """
        with open(CLASS_JSON_FILE, "w", encoding="utf-8") as f:# speichert die daten in der json datei, pfad in der variable CLASS_JSON_FILE
            json.dump(self.attendance, f, indent=2, ensure_ascii=False)

    def on_date_clicked(self, qdate: QDate):
        """
        anklicken eines datums im kalender
        zeigt den aktuellen status für das ausgewählte datum an
        ändert das label entsprechend
        """
        date_str = qdate.toString("yyyy-MM-dd")# datum im format jahr-monat-tag
        status = self.attendance.get(date_str)
        self.status_label.setText(f"Status am {date_str}: {status or 'Kein Status gesetzt'}")

    def set_status_for_selected_date(self):
        """
        status für das ausgewählte datum setzen
        """
        qdate = self.calendar.selectedDate()
        if not qdate.isValid():
            print(f"Ungültiges Datum: {qdate}")
            return  # nichts speichern

        date_str = qdate.toString("yyyy-MM-dd")
        status = self.combo.currentText()
        self.attendance[date_str] = status
        self.save_data()
        self.status_label.setText(f"Status am {date_str}: {status}")
        self.highlight_day(qdate, status)
        self.update_stats_label()

    def highlight_day(self, qdate: QDate, status: str):
        """Hebt einen Tag im Kalender basierend auf dem Status hervor."""
        fmt = QTextCharFormat()
        fmt.setBackground(QColor(self.STATUS_COLORS.get(status, "white")))
        self.calendar.setDateTextFormat(qdate, fmt)

    def highlight_saved_days(self):
        """Hebt alle gespeicherten Tage im Kalender hervor."""
        for date_str, status in self.attendance.items():
            qdate = QDate.fromString(date_str, "yyyy-MM-dd")
            if qdate.isValid():
                self.highlight_day(qdate, status)

    def update_stats_label(self): # ansatzpunkt für die berechnung der statistik für jahre oder gesamter schulungszeitraum z.b. 10.03.2025 bis 10.03.2027 in for schleifen ??villeicht über abfrage des schulungszeitraums ??
        """Berechnet die Monatsstatistik und aktualisiert die Anzeige.
        1. Berechnet die Anwesenheitsstatistik für den aktuellen Monat
        2. Überspringt ungültige Datumsangaben in der JSON-Datei
        3. Optional: Bereinigt die JSON-Datei von ungültigen Einträgen
        4. Aktualisiert das stats_label mit der Anwesenheitsquote für den aktuellen Monat
        5. Zeigt die Quote als Prozentsatz für jeden Status an
        6. Wenn keine Einträge für den Monat vorhanden sind, wird eine entsprechende Nachricht angezeigt
        7. Die Statistik wird im Format "Status: Prozentsatz%" angezeigt, getrennt durch " / "
        8. Die Berechnung basiert auf der Anzahl der Tage pro Status im aktuellen Monat
        9. Die Anzeige wird automatisch aktualisiert, wenn ein neuer Status gesetzt wird
        10. Die Funktion wird beim Initialisieren des Widgets und nach dem Setzen eines Status aufgerufen
        11. Die Statistik berücksichtigt nur Einträge aus dem aktuellen Monat und Jahr
        12. Die JSON-Datei wird nur bei Bedarf bereinigt, um Datenverlust zu vermeiden
        """
        now = datetime.now()
        year, month = now.year, now.month

        # ---------------------------
        # Ungültige Einträge überspringen
        # ---------------------------
        monthly_entries = {} # nur gültige einträge für den monat
        for date_str, status in self.attendance.items():
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print(f"⚠️ Ungültiges Datum übersprungen: {date_str} → {status}")
                continue
            if dt.year == year and dt.month == month:
                monthly_entries[date_str] = status

        # ---------------------------
        # JSON automatisch bereinigen (optional)
        # ---------------------------
        if len(monthly_entries) != len(self.attendance): # ungültige einträge gefunden
            self.attendance = monthly_entries
            self.save_data()
            print("🔧 Ungültige Einträge aus der JSON entfernt.")

        # ---------------------------
        # Anzeige aktualisieren
        # ---------------------------
        if not monthly_entries: # keine einträge
            self.stats_label.setText("Keine Einträge für diesen Monat.")
            return

        counts = Counter(monthly_entries.values())  # zähle vorkommen der status
        total_days = sum(counts.values()) # gesamtanzahl der tage im monat

        stats_text = " / ".join(
            f"{status}: {round((counts.get(status, 0) / total_days) * 100)}%" # prozentualer anteil
            for status in self.STATUS_OPTIONS
            if counts.get(status) 
        )

        self.stats_label.setText(f"Anwesenheitsquote ({month:02d}/{year}): {stats_text}") # aktualisiere das label

