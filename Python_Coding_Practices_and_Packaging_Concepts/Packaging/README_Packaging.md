# Python Packaging Beispielprojekt

Dieses Projekt demonstriert, wie man ein einfaches, strukturiertes Python-Paket mit Modulen, einem Einstiegspunkt (`__main__.py`) und Unit Tests erstellt.

---

## Projektstruktur

```
Python_Coding_Practices_and_Packaging_Concepts/
├── Packaging/
│   ├── __main__.py           # Einstiegspunkt zum Ausführen des Pakets
│   ├── basic.py              # Modul mit einfachen Funktionen
│   └── stats.py              # Modul mit Statistikfunktionen
├── tests/
│   ├── __init__.py
│   └── test_basic.py         # Unit Tests für basic.py
└── README.md                 # Diese Anleitung
```

---

## ⚙️ Installation (optional)

Du kannst das Paket lokal installieren:

```bash
pip install -e .
```

Oder du arbeitest einfach direkt im Projektordner mit `python3 -m Packaging`.

---

## Ausführen des Pakets

```bash
cd Python_Coding_Practices_and_Packaging_Concepts
python3 -m Packaging
```

Dies ruft `Packaging/__main__.py` auf.

---

## ✏️ Beispiel: Inhalt von `basic.py`

```python
def say_hello():
    print("Hallo aus basic.py!")
```

---

## ✏️ Beispiel: Inhalt von `stats.py`

```python
def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
```

---

## Tests mit `unittest`

Beispiel in `tests/test_basic.py`:

```python
import unittest
from Packaging import basic

class TestBasic(unittest.TestCase):
    def test_say_hello(self):
        self.assertIsNone(basic.say_hello())  # gibt nur Text aus

if __name__ == '__main__':
    unittest.main()
```

Tests ausführen mit:

```bash
python3 -m unittest discover -s tests
```

---

## ❗ Häufige Fehler

| Fehler | Ursache |
|-------|---------|
| `attempted relative import with no known parent package` | Du führst ein Modul direkt statt über `-m` aus |
| `cannot import name ... from partially initialized module` | Zirkulärer Import – vermeide Top-Level-Imports in `__init__.py` |

---

## Autorin

**Asmaa Hamami**  
*Junior Data Engineering*
