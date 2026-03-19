ja klar

* Config dateien erstellen (einmal geheim und nicht im repo, einmal im repo und "öffentlich" sichtbar)
* sqlite-Datenbanken zu supabase migrieren



Stellen: 
    * news
    * counter
    * quizdatenbank mit den fragen
  
* Benutzerverwaltung einrichten (bisher in JSON)
    Dann: 
    * quiz komplett migrieren


* DB-Funktionen so umschreiben, dass sie die REST-Api von supabase abfragen
* git-Aufrufe entfernen




ggf. nach Tabellenimport sowas wie: 

SELECT setval(
  pg_get_serial_sequence('quotes', 'id'), 
  (SELECT MAX(id) FROM quotes)
);