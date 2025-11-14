from pathlib import Path

def solve(input_data):
    lines = input_data.strip().split('\n')
    it = iter(lines)
    
    try:
        n = int(next(it))
    except StopIteration:
        return ""
    
    results = []
    for _ in range(n):
        # Skip empty lines to find w h
        w_h_line = next(it)
        while not w_h_line.strip():
            w_h_line = next(it)
        w_h = w_h_line.split()
        w, h = int(w_h[0]), int(w_h[1])
        
        # Read asteroid lines
        asteroid = []
        for i in range(h + 2):
            line = next(it)
            while not line.strip() and i < h + 2:  # skip empty if any, but shouldn't
                line = next(it)
            asteroid.append(line)
        
        # Find S position in first row (index 0)
        first_row = asteroid[0]
        s_pos = first_row.find('S')
        
        # Dig tunnel from row 1 to row h (indices 1 to h)
        for r in range(1, h + 1):
            row = list(asteroid[r])
            if row[s_pos] == ':':
                row[s_pos] = 'X'
            asteroid[r] = ''.join(row)
        
        results.append('\n'.join(asteroid))
    
    return '\n\n'.join(results)


def main():
    input_folder = Path("Inputs")
    output_folder = Path("Outputs")
    output_folder.mkdir(exist_ok=True)
    
    for input_file in sorted(input_folder.glob("level2_*.in")):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        result = solve(data)
        
        output_file = output_folder / input_file.name.replace('.in', '.out')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"Generiert: {output_file.name}")


if __name__ == "__main__":
    main()