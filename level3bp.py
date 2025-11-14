import os
import sys
from typing import List, TypeVar

T = TypeVar("T")

# -----------------------------
# Utility: 2D Array
# -----------------------------
def make_2d_array(x: int, y: int, fill: T = 0) -> List[List[T]]:
    if x < 0 or y < 0:
        raise ValueError("x und y müssen >= 0 sein")
    return [[fill for _ in range(y)] for _ in range(x)]


# -----------------------------
# Mining Pointer (UNVERÄNDERT)
# -----------------------------
class IntPointer:
    def __init__(self, array, row: int = 0, col: int = 0):
        self.array = array
        self.set_pos(row, col)

    def _check(self, row, col):
        if row < 0 or col < 0 or row >= len(self.array) or col >= len(self.array[0]):
            raise IndexError("Koordinate außerhalb des Arrays")

    def set_pos(self, row: int, col: int):
        self._check(row, col)
        self.row = row
        self.col = col

    def get(self) -> int:
        return self.array[self.row][self.col]

    def set(self, value: int):
        self.array[self.row][self.col] = value

    def move(self, drow: int = 0, dcol: int = 0):
        self.set_pos(self.row + drow, self.col + dcol)

    def coords(self):
        return (self.row, self.col)


# -----------------------------
# Mining-Logik (UNVERÄNDERT)
# -----------------------------
def process_asteroid(h_actual, w_actual, diglimit, grid):
    # minable Feld extrahieren (ohne Rand)
    h = h_actual - 2   # number of minable rows
    w = w_actual - 2   # number of minable cols

    # Feld für deine Logik
    mine = make_2d_array(h, w, ":")

    start_r = None
    start_c = None

    # S dynamisch im gesamten Grid suchen
    for r in range(h_actual):
        for c in range(w_actual):
            if grid[r][c] == "S":
                start_r = r - 1
                start_c = c - 1
                break
        if start_r is not None:
            break

    # Anpassen, falls außerhalb minable Bereich
    if start_r is not None:
        if start_r < 0:
            start_r = 0
        if start_c < 0:
            start_c = 0
        if start_r >= h:
            start_r = h - 1
        if start_c >= w:
            start_c = w - 1

    # Übernehme nur Zellen innerhalb des minable rectangles
    for r in range(h):
        for c in range(w):
            cell = grid[r+1][c+1]
            mine[r][c] = cell

    # --- Deine Original Mining Logik: UNVERÄNDERT ---
    ptr = IntPointer(mine, 0, 0)
    x, y = h, w

    if x == 3:
        start_col = start_c  # Dynamisch von S
        ptr.set_pos(0, start_col)
        ptr.set("X")
        ptr.move(1, 0)
        ptr.set("X")
        middle_row = x // 2
        for c in range(y):
            ptr.set_pos(middle_row, c)
            ptr.set("X")
    elif y == 3:
        start_col = start_c  # Dynamisch von S
        ptr.set_pos(0, start_col)
        ptr.set("X")

        if start_col == 0:
            ptr.set_pos(0, 1)
            ptr.set("X")
            for r in range(x):
                ptr.set_pos(r, 1)
                ptr.set("X")
        elif start_col == y - 1:
            ptr.set_pos(0, 1)
            ptr.set("X")
            for r in range(x):
                ptr.set_pos(r, 1)
                ptr.set("X")
        else:
            for r in range(x):
                ptr.set_pos(r, start_col)
                ptr.set("X")

    # S muss wieder gesetzt werden (Logik überschreibt ihn evtl.)
    # Da S im Rand ist, nicht im minable Feld setzen

    # --- Ergebnis wieder in das volle Raster einsetzen ---
    out = []
    for r in range(h_actual):
        row = []
        for c in range(w_actual):
            if r == 0 or r == h_actual - 1 or c == 0 or c == w_actual - 1:
                row.append(grid[r][c])
            else:
                row.append(mine[r-1][c-1])
        out.append("".join(row))

    return out


# -----------------------------
# Input Parser (für CCC & lokal)
#  Erwartetes Format in einer Asteroiden-Zeile:  <width> <height> <diglimit>
#  Wir wandeln intern in (h = height, w = width)
# -----------------------------
def parse_input_lines(lines):
    idx = 0

    # Leading Leerzeilen ignorieren
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1

    if idx >= len(lines):
        return []

    n = int(lines[idx])
    idx += 1

    asteroids = []

    for _ in range(n):

        # <width> <height> <diglimit> (bezogen auf das MINABLE RECTANGLE)
        w_mine, h_mine, dig = map(int, lines[idx].split())
        idx += 1

        # Tatsächliche Breite/Höhe inkludieren den # Rand
        h_actual = h_mine + 2
        w_actual = w_mine + 2

        grid = []
        for _ in range(h_actual):
            row = list(lines[idx])
            if len(row) != w_actual:
                raise ValueError(
                    f"Zeile hat nicht erwartete Breite {w_actual}: '{lines[idx]}'"
                )
            grid.append(row)
            idx += 1

        # optionale Leerzeile
        if idx < len(lines) and lines[idx].strip() == "":
            idx += 1

        asteroids.append((h_actual, w_actual, dig, grid))

    return asteroids


# -----------------------------
# CCC Mode: STDIN → STDOUT
# -----------------------------
def run_ccc_mode():
    lines = [l.rstrip("\n") for l in sys.stdin.readlines()]
    asteroids = parse_input_lines(lines)

    first = True
    for (h, w, dig, grid) in asteroids:
        if not first:
            print()
        first = False

        result = process_asteroid(h, w, dig, grid)
        for line in result:
            print(line)


# -----------------------------
# Local Batch Mode: /Inputs → /Outputs
# -----------------------------
def run_local_mode():
    input_dir = "Inputs"
    output_dir = "Outputs"

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.isdir(input_dir):
        print(f"Input-Ordner '{input_dir}' existiert nicht. Lege ihn an und pack deine .in Dateien rein.")
        return

    for filename in sorted(os.listdir(input_dir)):
        if not filename.endswith(".in"):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(
            output_dir,
            filename.replace(".in", ".out")
        )

        with open(input_path, "r") as f:
            lines = [l.rstrip("\n") for l in f.readlines()]

        asteroids = parse_input_lines(lines)

        out_lines = []
        first = True

        for (h, w, dig, grid) in asteroids:
            if not first:
                out_lines.append("")
            first = False

            result = process_asteroid(h, w, dig, grid)
            out_lines.extend(result)

        with open(output_path, "w") as f:
            f.write("\n".join(out_lines))

        print(f"✓ {filename} → {output_path}")


# -----------------------------
# Main: Automatische Erkennung
# -----------------------------
def main():
    if sys.stdin.isatty():
        # kein STDIN → lokaler Batch-Modus
        run_local_mode()
    else:
        # CCC Modus (STDIN vorhanden)
        run_ccc_mode()


if __name__ == "__main__":
    main()
