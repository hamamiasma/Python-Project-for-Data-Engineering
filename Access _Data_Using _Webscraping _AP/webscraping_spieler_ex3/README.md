
# Web Scraping – CSS Selector Cheat Sheet (für BeautifulSoup)

CSS-Selektoren sind eine mächtige Methode, um gezielt Elemente aus HTML mit BeautifulSoup zu extrahieren. Hier sind die häufigsten Beispiele:

---

## Basis-Selektoren

| Selektor              | Bedeutung                                | Beispiel HTML                         |
|-----------------------|------------------------------------------|----------------------------------------|
| `tag`                | Wählt alle Tags mit diesem Namen         | `div`, `table`, `tr`                  |
| `.class`             | Wählt alle Elemente mit dieser Klasse    | `.main`, `.content`                   |
| `#id`                | Wählt ein Element mit dieser ID          | `#header`, `#main-banner`             |

---

## Kombinationen

| Selektor                      | Bedeutung                                              |
|-------------------------------|--------------------------------------------------------|
| `div.content`                 | Alle `<div>` mit Klasse `content`                     |
| `table.items tbody tr`        | Alle `<tr>`-Zeilen im `<tbody>` eines `<table class="items">` |
| `ul > li`                     | Nur direkte `<li>`-Kinder innerhalb von `<ul>`        |
| `div > p.note`                | Alle `<p class="note">` direkt unter einem `<div>`    |
| `a[href]`                     | Alle `<a>`-Tags mit einem `href`-Attribut             |
| `img[alt="logo"]`             | `<img>`-Tag mit genau diesem `alt`-Text               |

---

## Attribut-Filter

| Selektor                  | Bedeutung                                  |
|---------------------------|--------------------------------------------|
| `a[href^="http"]`        | `href` beginnt mit „http“                  |
| `a[href$=".pdf"]`        | `href` endet auf „.pdf“                    |
| `a[href*="example"]`     | `href` enthält das Wort „example“          |

---

## Beispiel in BeautifulSoup

```python
# Alle Tabellenzeilen im Haupttabelle auf Transfermarkt
rows = soup.select("table.items tbody tr")

# Alle Links mit Klasse 'hauptlink'
links = soup.select("a.hauptlink")

# Alle Bilder mit alt-Text = 'Logo'
logos = soup.select("img[alt='Logo']")


soup.select("div.box > ul li.active")

# Erklärung: `soup.select("div.box > ul li.active")`


## Schrittweise erklärt:

| Teil         | Bedeutung                                                                 |
|--------------|---------------------------------------------------------------------------|
| `div.box`    | Ein `<div>`-Element mit der Klasse `box`                                  |
| `>`          | Bedeutet: **direktes Kind** – also keine Zwischenebene dazwischen         |
| `ul`         | Eine **ungeordnete Liste**, direkt innerhalb von `div.box`                |
| `li.active`  | Ein Listenelement `<li>` mit der Klasse `active`, das in der Liste liegt  |

---

## Beispiel-HTML:

```html
<div class="box">
  <ul>
    <li class="active">Startseite</li>
    <li>Kontakt</li>
  </ul>
</div>