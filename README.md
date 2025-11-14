**Projektübersicht**

Dieses kleine Repo enthält zwei Python-Skripte für einen einfachen "CCC"-Workflow mit optionaler AI-Unterstützung.

- **`ccc_simple.py`**: Hauptskript zum Vorbereiten, Generieren von Templates und Ausführen von Lösungen (interaktiv, automatisch oder nur Template).
- **`setup_simple.py`**: Einmaliges Setup-Skript, das Verzeichnisse anlegt und die benötigte Abhängigkeit `pdfplumber` installiert.

**Voraussetzungen**

- **Python**: Version 3.6 oder neuer wird empfohlen.
- **pip**: Zum Installieren von `pdfplumber` (wird auch von `setup_simple.py` installiert).

**Wichtig: Inputs & Aufgaben-Angabe herunterladen**

- Lade vor dem Ausführen des Workflows unbedingt zunächst die Input-Dateien (ZIP/Archiv) und die Aufgaben-PDF von der Contest-/Aufgaben-Seite herunter.
- Platzieren/Benenne die Dateien so, dass `ccc_simple.py` sie findet:
  - ZIP-Archiv: `level{n}.zip` (oder im `Downloads`-Ordner). Das Skript prüft zuerst `Downloads/`, dann den Projektordner und zuletzt `infos/`.
  - PDF-Aufgabe: `Level {n}.pdf`, `level{n}.pdf` oder `Level{n}.pdf` — ebenfalls entweder im `Downloads`-Ordner oder in `infos/`.
- Alternativ kannst du die ZIP lokal entpacken und die enthaltenen `.in`-Dateien direkt nach `Inputs/` kopieren.
- Ohne die Inputs/PDF kann `ccc_simple.py` nicht automatisch extrahieren oder den AI-Prompt korrekt erzeugen.

**Schnellstart (Windows PowerShell)**

1. Setup ausführen (legt Ordner an und installiert Abhängigkeiten):

```powershell
python .\setup_simple.py
```

2. `ccc_simple.py` verwenden:

```powershell
# Interaktiver Modus (empfohlen für manuellen Ablauf)
python .\ccc_simple.py 5

# Vollautomatisch (so weit möglich, verwendet generierten AI-Prompt)
python .\ccc_simple.py 5 --auto

# Nur Template erzeugen (erstellt level5.py mit Platzhalter solve())
python .\ccc_simple.py 5 --template
```

Ersetze `5` durch die gewünschte Level-Nummer.

**Ordner & Dateien (wichtig)**

- **`Inputs/`**: Erwartete Input-Dateien für Lösungen. Format-Beispiel: `level5_example.in`.
- **`Outputs/`**: Hier schreibt die Lösung die erzeugten Output-Dateien (z. B. `level5_example.out`).
- **`infos/`**: Temporärer Ort; `ccc_simple.py` extrahiert ZIPs und sammelt dort Dateien.
- **ZIP/PDF**: `ccc_simple.py` sucht nach `level{n}.zip` oder nach PDF-Dateien im `Downloads`-Ordner oder im `infos/`-Ordner.

**Wie `ccc_simple.py` funktioniert (Kurzfassung)**

- Moduswahl per Kommandozeilen-Argumenten:
  - `--auto`: Versucht, einen AI-gestützten Workflow zu unterstützen (erzeugt Prompt-/Request-Dateien). Manche Schritte bleiben manuell.
  - `--template`: Nur Template erzeugen (Datei `level{n}.py` mit Platzhalter `solve()`).
  - Standard (keine Option): Interaktiver Modus mit Pausen für manuelle Schritte.

- Wichtige Ausgaben/Artefakte:
  - `level{n}_prompt.txt` — AI-Prompt, den du z. B. in GitHub Copilot Chat oder ChatGPT einfügen kannst.
  - `level{n}_workflow.md` / `level{n}_ai_request.md` — Hilfen für den AI-Workflow.
  - `level{n}.py` — automatisch erzeugtes Template (bei `--template`) oder durch AI generierte Lösung.

**AI-Workflow (Kurz)**

1. Skript extrahiert Aufgabe und erstellt `level{n}_prompt.txt`.
2. Öffne den Prompt in einem AI-Tool (z. B. GitHub Copilot Chat, ChatGPT) und bitte um eine vollständige Python-Lösung.
3. Speichere die generierte Lösung als `level{n}.py` im Projektordner.
4. Teste die Lösung mit `python level{n}.py` oder führe anschließend `python ccc_simple.py {n}` aus, um den kompletten Ablauf fortzusetzen.

Hinweis: Die AI-Ausgabe muss geprüft und ggf. an die Problemstellung angepasst werden. `ccc_simple.py` erzeugt nur Hilfsdateien — den finalen Code musst du ggf. manuell kontrollieren.

**Fehlerbehebung & häufige Hinweise**

- Wenn `pdfplumber` nicht installiert ist, wird die PDF-Analyse übersprungen. Installiere es manuell oder führe `setup_simple.py` aus:

```powershell
python -m pip install pdfplumber
```

- Wenn ZIP/PDF nicht gefunden werden: stelle sicher, dass die ZIP-Datei `level{n}.zip` heißt oder dass die PDF in `Downloads` bzw. `infos/` liegt.
- Bei Permission- oder Pfadproblemen: Starte PowerShell mit ausreichenden Rechten und prüfe, ob der Pfad Leerzeichen enthält.

**Beispiele**

- Interaktiv (manuelle Pausen, Kontrolle durch den Nutzer):

```powershell
python .\ccc_simple.py 3
```

- Vollautomatisch (führt so viel wie möglich automatisiert durch):

```powershell
python .\ccc_simple.py 3 --auto
```

**Weiteres / Nächste Schritte**

- Wenn du möchtest, ergänze eine `requirements.txt` mit `pdfplumber` oder erweitere `setup_simple.py` für weitere Abhängigkeiten.
- Soll ich die `README.md` committen und einen Vorschlag für `requirements.txt` erstellen? Sag kurz Bescheid.

---
Dateien referenziert: `ccc_simple.py`, `setup_simple.py` (erstellt am Projekt-Root)
