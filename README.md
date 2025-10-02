---
marp = True
---
# Verwaltungstool

Dieses Verwaltungstool wurde entwickelt, um sämtliche organisatorische Aufgaben während unserer Umschulung effizient und übersichtlich zu gestalten. Ziel ist es, alle bisher genutzten Einzeltools in einer zentralen Anwendung zusammenzuführen und sowohl Verwaltungs- als auch Hilfsfunktionen bereitzustellen.

**Teamgröße:** 2 Personen

---

## Funktionsübersicht

### Verwaltungstools
- **Tagesberichte:** Automatisierte Erstellung von Tagesberichten als Textdateien mit spezifischer Benennung.
- **Berichtszählung & Kategorisierung:** Übersichtliche Einteilung der Berichte in Kategorien wie Präsenz, Homeoffice, Krank, Urlaub und Sonderfälle.
- **Duplikatkontrolle:** Sicherstellung, dass keine Tagesberichte doppelt angelegt werden.

---

### Hilfstools
- **Quiz:** Zufällige Lerneinheiten mit 2–4 Antwortmöglichkeiten, Auswertung und Lernfortschritts-Tracking.
- **Störungscounter:** Sammlung und Auswertung technischer und allgemeiner Störungen (wird von allen Anwendern geteilt, keine personenbezogenen Daten).
- **News:** Kurzmitteilungen, die für 2 Wochen sichtbar bleiben und automatisiert über GitHub verteilt werden.
- **Merksätze:** Rotierende Anzeige von Merksätzen, die alle 120 Sekunden wechseln.
- **Passwort generrator**
erstellt passwörter mit random zeichen auf angebene länge 
---

## Technische Umsetzung

- **Programmiersprache:** Python
- **GUI:** PySide6
- **Hauptfenster:** Die zentrale Steuerung erfolgt über die Datei `Main.py`.
- **Datenschutz:** Es werden keine personenbezogenen Daten verarbeitet. Alle geteilten Inhalte (News, Merksätze, Quizfragen) sind anonymisiert.

---

## GitHub & Versionsverwaltung

- **Datenverteilung:** News, Merksätze und Quizfragen werden über GitHub bereitgestellt, ohne Speicherung von Benutzerdaten.
- **Branch-Strategie:** Nach jeder Änderung wird ein neuer Branch erstellt. Die Versionsnummern werden wie folgt erhöht:
  - Start: 0.00 (nur README)
  - Neue Funktion: +0.01
  - Fertiges Modul: +0.10
  - Projektabschluss: 1.0

---

## Lizenz

- **MIT-Lizenz:** Kompatibel mit Python und PySide6. Bei Weiterverwendung ist eine Erwähnung erforderlich.
- **PySide6 & Python:** Beide Komponenten unterliegen eigenen Lizenzen.

---

## Kalenderfunktion

Der integrierte Kalender erstellt ein Raster basierend auf dem aktuellen Datum. Jeder Tag ist als anklickbare Box dargestellt und bietet folgende Optionen:
- **Tagesbericht erstellen:** Vier Varianten, z.B. `2025_09_22_tagesbericht_K`

---

- **Steuerungsmenü (oben):**
  - Vorheriger Monat
  - Nächster Monat
  - Prüfungsfunktion (Duplikate erkennen, Listenabgleich)
  - Zählfunktion (prozentuale Übersicht vorhandener Berichte)

---

- **Menü (unten):**
  - Zurück-Button
  - Button zum Festlegen des Speicherverzeichnisses für Tagesberichte
  - Umschalten des Kalenderlayouts (KW-/Monatsansicht)

---

## Passwortgenerator

Der integrierte Passwortgenerator ermöglicht die Erstellung sicherer Passwörter mit frei wählbarer Länge. Passwörter werden verschlüsselt lokal gespeichert. Für die Entschlüsselung ist ein Master-Passwort erforderlich.

---

## Prüfer und Zähler

Für die effiziente Verwaltung und Kontrolle der Tagesberichte stehen zwei eigenständige Python-Skripte zur Verfügung:

- **Zähler:** Dieses Skript ermöglicht die automatische Ermittlung der Anzahl vorhandener Tagesberichte. So kann jederzeit nachvollzogen werden, wie viele Berichte bereits erstellt wurden und wie hoch der aktuelle Erfüllungsgrad (Prozentsatz) ist.
- **Prüfer:** Mit diesem Skript lassen sich Tagesberichte auf Duplikate und fehlende Einträge überprüfen. Dadurch wird sichergestellt, dass keine doppelten Berichte existieren und keine Berichte fehlen. Die Ergebnisse können direkt mit den Anwesenheitslisten der Dozenten abgeglichen werden.

Diese Werkzeuge unterstützen eine schnelle und zuverlässige Kontrolle der Anwesenheit und Berichterstattung und helfen dabei, die eigenen Planungen optimal anzupassen.


---

## Zielsetzung

Mit diesem Tool schaffen wir eine zentrale, datenschutzkonforme und benutzerfreundliche Lösung für alle relevanten Verwaltungs- und Lernprozesse während unserer Umschulung. Die modulare Struktur ermöglicht eine einfache Erweiterung und Anpassung an zukünftige Anforderungen.

---