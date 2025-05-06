# Static Code Analysis with Pylint

Statische Codeanalyse (engl. Static Code Analysis) ist eine Methode zur Überprüfung der Effizienz von Anwendungscode. Dabei wird der Quellcode auf Qualität, Zuverlässigkeit und Sicherheit analysiert – ohne ihn auszuführen. Die statische Codeanalyse ist ein wesentlicher Bestandteil des Entwicklungszyklus von Software und wird in vielen Python-Frameworks unterstützt.

Eines der bekanntesten Tools hierfür ist PyLint. PyLint überprüft den Code auf Einhaltung der PEP8-Stilrichtlinien und gibt Hinweise an den Stellen, wo Verstöße festgestellt werden.

## Projektbeschreibung

Dieses Projekt demonstriert, wie man statische Codeanalyse mit [`pylint`](https://pylint.pycqa.org/) durchführt, um die Codequalität zu überprüfen, häufige Fehler zu erkennen und den Python-Code stilistisch zu verbessern.

---

## Verwendete Technologien

- **Python 3.11+**
- **pylint 2.11.1** (oder höher empfohlen)

---

## ⚙️ Setup

### 1. Virtuelle Umgebung (empfohlen)
```bash
python3 -m venv .venv
source .venv/bin/activate  # oder .venv\Scripts\activate auf Windows
```

### 2. Installation von pylint
```bash
pip install pylint
```

---

## ▶️ Beispielcode (`static_code.py`)

```python
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

# Initialize the variable 'num1' with the value 4.
num1 = 4

# Initialize the variable 'num2' with the value 5.
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))
```

## Linting ausführen

Um den Code zu prüfen:

```bash
pylint static_code.py
```

### Ausgabe:

************* Module static_code
static_code.py:16:0: C0301: Line too long (110/100) (line-too-long)
static_code.py:17:0: C0304: Final newline missing (missing-final-newline)
static_code.py:1:0: C0114: Missing module docstring (missing-module-docstring)
static_code.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
static_code.py:8:0: C0103: Constant name "num1" doesn't conform to UPPER_CASE naming style (invalid-name)
static_code.py:11:0: C0103: Constant name "num2" doesn't conform to UPPER_CASE naming style (invalid-name)
static_code.py:14:0: C0103: Constant name "total" doesn't conform to UPPER_CASE naming style (invalid-name)
static_code.py:17:6: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------------------------------------
Your code has been rated at 0.00/10


---

## Interpretation

| Code    | Bedeutung                                                |
|---------|-----------------------------------------------------------|
| C0301   | Zeile ist zu lang (mehr als 100 Zeichen)                 |
| C0304   | Es fehlt eine Leerzeile am Ende der Datei                |
| C0114   | Modul-Dokumentation fehlt                                |
| C0116   | Funktions-Dokumentation fehlt                            |
| C0103   | Variablennamen folgen nicht dem UPPER_CASE-Stil          |
| C0209   | Verwende f-Strings anstelle von .format()              |

---

## ▶️ Beispiel 2(static_code_analysis.py)

```python
"""This script defines a simple add function and demonstrates usage with constants."""

def add(number1, number2):
    """Return the sum of two numbers."""
    return number1 + number2

NUM1 = 4
NUM2 = 5

TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
```

---

## Linting ausführen

Um den Code zu prüfen:

```bash
pylint static_code_analysis.py
```

# Ausgabe:
```
------------------------------------------------------------------
Your code has been rated at 10.00/10
```

---

## Ziel

Ein sauberer, gut dokumentierter Python-Code mit einem `pylint`-Score von **10.00/10**.

---

## Autorin

**Asmaa Hamami**  
>Junior Data Engineer 

---
