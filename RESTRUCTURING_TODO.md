# SF
-Dokus für Funktionen im attendance_calendar
-Namen der Ornder - einheitlich umbennenen
-Code in ENG-Sprache
-verschiedene Main.py ümbenennen zur übersicht
-/Elekrotechnick/read_me:E.technick.md umbennenen
-Setup-Datei anlegen die über alle ordner hinweg das setup übernimmt 
-flask mit gerhard datei - entscheidung ? /styles/flask_mit_gerhardt.md
-/zahlensysteme/main/main.py übersichtlicher gestalten
-Licensetxt überarbeiten - wegen supabase
-start.py zur allgemeinen setupdatei integrieren 
-db.dateien mit supabase integrieren

-ordnerstruktur überlegen für übersichtlichkeit
-my_project/
├── main.py
├── utils.py
├── models.py
├── services.py
├── test_main.py
├── requirements.txt
└── README.md














# FK
x-styles/md datei könnte weg
-styles/ hier neuen ordener für assets darein dann icon.png
x-counter/löschmich.py löschen
-counter/ git_funktions.py und db nach umstellung entfernen 
-password/ hat noch keine readme
-quiz/ doppel DB
x-quiz/ DB_script.py wird nach umstellung auf supabase unnoetig
-quotes/ DB loeschen da schon übertragen 
x-quotes/ DB erstellungs script kann weg
x-Script/ altlast
-Projekt/ readme akttualiseren in PDF 
-verwaltungstool/ DB´s aufraeumen 
-Verwaltungstool/unterordner/ readme tittel anpassung 
-bennenungen im gesammten projekt standatisieren 
-im gesammten projekt sind __pycache__ datein 
-utils/ wird nach umstellung auf supabase unnoetig
-news/DB nach umstellung DB koennte 
x-start.py veraltet 








# GA


[x] obsolete Dateien löschen 

[x] src-Verzeichnis anlegen
[x] alles bis auf .gitignore, .venv, .vscode, requirements.txt und Readmes erstmal in den src-Ordner verschieben

[ ] data-Verzeichnis anlegen (2 Unterverzeichnisse, sqlite und json)

[ ] in allen packages __init__.py anlegen
[ ] alle imports anpassen


[ ] Datenbanken in data/sqlite-Ordner verschieben
[ ] json-Dateien in data/json-Ordner verschieben
[ ] **alle** Dateipfade anpassen/normalisieren

[ ] zentrale config-Datei anlegen
[ ] zentrale pyproject.toml anlegen
[ ] .env anlegen (gitignore!)

[ ] Entscheidung zu supabase/lokal treffen (bleibt beides?)


[ ] supabase-Anbindung aus experimental-Branch picken
[ ] supabase vs. sqlite konfigurierbar machen 
[ ] supabase-Anbindung dokumentieren
[ ] json-Speicher-Mechanik auf datenbanken umstellen

[ ] security-Features in supabase reaktivieren