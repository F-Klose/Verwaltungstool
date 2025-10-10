from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QGroupBox, QLabel, QGridLayout
)
import sys
#from counter import counter_main, git_funktions, under_funktions,
from counter.counter_main import start_application 
from counter import git_funktions, under_funktions

#nivht fertig
#TODO: Buttons mit Funktionen belegen, Git Befehle einbauen,verbindungen fertigen zu den nächsten fenstern,news funktion schreiben einbinden,mekrsätze funktion schreiben mit auto rotation und steuerung
#TODO: Design verbessern, prüfen ob alles funktioniert, layout anpassen


class InfoFenster(QWidget):
    def __init__(self, titel):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(titel)
        layout.addWidget(label)
        button_layout = QHBoxLayout()
        # Navigation Buttons für News
        button_layout.addWidget(QPushButton("Vor"))
        button_layout.addWidget(QPushButton("Zurück"))
        button_layout.addWidget(QPushButton("Neu"))
        layout.addLayout(button_layout)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verwaltungstool")

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # oobere Buttons
        top_layout = QHBoxLayout()
        btn_counter = QPushButton("Störungs Counter")
        btn_counter.clicked.connect(self.oeffne_counter)

        top_layout.addWidget(btn_counter)
        top_layout.addWidget(QPushButton("Platzhalter quiz"))
        top_layout.addWidget(QPushButton("Platzhalter passwotgenerator"))
        top_layout.addWidget(QPushButton("Platzhalter Kalender"))
        main_layout.addLayout(top_layout)

        # mittlere Info-Fenster
        middle_layout = QHBoxLayout()
        middle_layout.addWidget(InfoFenster("news-Fenster Links"))
        middle_layout.addWidget(InfoFenster("merksaetze-Fenster Rechts"))
        main_layout.addLayout(middle_layout)

        # Untere Buttons steuerung main fenster
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(QPushButton("Beenden")) #git push und pull ausführen dann beenden
        bottom_layout.addWidget(QPushButton("Aktualisieren")) #git pull und push nutzen
        main_layout.addLayout(bottom_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
    def oeffne_counter(self):
        self.counter_window = start_application()
        self.counter_window.exec()
        self.counter_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())