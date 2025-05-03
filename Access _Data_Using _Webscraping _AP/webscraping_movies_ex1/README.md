
# Web Scraping Projekt: Top 50 Filme

## Projektbeschreibung

Dieses Python-Projekt extrahiert automatisch die 50 höchstbewerteten Filme von einer archivierten Webseite und speichert diese lokal als CSV-Datei sowie in einer SQLite-Datenbank.

---

## Technologien

- **Python 3.x**
- **BeautifulSoup** – HTML-Parser
- **requests** – Webseiten-Anfrage
- **pandas** – Datenverarbeitung
- **sqlite3** – Speicherung in Datenbank

---

## Struktur

- `webscraping_movies.py` – Hauptskript zum Extrahieren und Speichern
- `top_50_films.csv` – Enthält die Ergebnisse als CSV
- `Movies.db` – SQLite-Datenbank mit der Tabelle `Top_50`

---

##  Ausführung

```bash
python3 webscraping_movies.py
