# 🧪 Unit Testing in Python mit `unittest`

Diese Anleitung zeigt, wie man **Unit Tests** in Python schreibt, verwendet und ausführt – mit dem Standardmodul [`unittest`](https://docs.python.org/3/library/unittest.html).

---

## 📌 Was ist Unit Testing?

**Unit Tests** (Einheitstests) sind automatisierte Tests, die einzelne Bestandteile (Funktionen, Klassen, Methoden) eines Programms isoliert überprüfen. Sie helfen, Fehler frühzeitig zu erkennen und sorgen für stabile, wartbare Software.

---

## 🛠️ Voraussetzungen

- Python 3.x (ab Version 3.6 empfohlen)
- Keine externen Bibliotheken notwendig – `unittest` ist Teil der Standardbibliothek

---

## 📁 Projektstruktur

```
projekt/
│
├── mymodule.py             # Modul mit Funktionen
├── test_mymodule.py        # Test-Datei für Unit Tests
└── README.md               # Diese Anleitung
```

---

## ✏️ Beispiel: Modul mit Funktionen (`mymodule.py`)

```python
def square(x):
    return x * x

def double(x):
    return x * 2
```

---

## 🧪 Beispiel: Unit Tests (`test_mymodule.py`)

```python
# Importiere das unittest-Modul, um Tests zu schreiben
import unittest

# Importiere die zu testenden Funktionen
from mymodule import square, double

# Testklasse für die square-Funktion
class TestSquare(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(3), 9)

    def test_negative(self):
        self.assertEqual(square(-2), 4)

    def test_float(self):
        self.assertEqual(square(2.5), 6.25)

# Testklasse für die double-Funktion
class TestDouble(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(double(4), 8)

    def test_negative_float(self):
        self.assertEqual(double(-3.1), -6.2)

    def test_zero(self):
        self.assertEqual(double(0), 0)

# Wenn die Datei direkt ausgeführt wird, starte alle Tests
if __name__ == '__main__':
    unittest.main()
```

---

## ▶️ So führst du die Tests aus

Im Terminal/Command Line:

```bash
python test_mymodule.py
```

Beispielausgabe:

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

✅ Alle Tests wurden erfolgreich ausgeführt.

---

## ℹ️ Nützliche `unittest`-Methoden

| Methode                    | Beschreibung                                   |
|---------------------------|------------------------------------------------|
| `assertEqual(a, b)`       | Prüft, ob `a == b`                             |
| `assertNotEqual(a, b)`    | Prüft, ob `a != b`                             |
| `assertTrue(x)`           | Prüft, ob `x` wahr ist                         |
| `assertFalse(x)`          | Prüft, ob `x` falsch ist                       |
| `assertRaises(Error)`     | Erwartet, dass ein Fehler ausgelöst wird      |

---

## 🎯 Ziel

Ziel ist es, zuverlässigen, getesteten und wartbaren Python-Code zu schreiben. Mit `unittest` kannst du kleine Bausteine deiner Software regelmäßig automatisch prüfen lassen.

---

## 👩‍💻 Autorin

**Asmaa Hamami**  
*Data Engineering | Python Enthusiast*

*Letztes Update: 2025-05-05*
