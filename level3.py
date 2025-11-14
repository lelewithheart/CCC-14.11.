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
        # Skip empty lines to find w h limit
        line = next(it)
        while not line.strip():
            line = next(it)
        w, h, limit = map(int, line.split())
        
        # Read asteroid lines
        asteroid = []
        for i in range(h + 2):
            line = next(it)
            while not line.strip() and i < h + 2:
                line = next(it)
            asteroid.append(line)
        
        # Find S position
        s_row = 0
        s_col = asteroid[0].find('S')
        
        # Minable grid: rows 1 to h, cols 0 to w-1
        grid = [list(asteroid[i+1]) for i in range(h)]
        
        # Create solution grid
        solution = [row[:] for row in grid]
        
        # Strategy: Since one dimension is 3, mine the middle and then expand
        dug = set()
        
        if h == 3:
            # Mine the middle row completely
            middle_row = 1
            for x in range(w):
                if grid[middle_row][x] in [':', 'S'] and len(dug) < limit:
                    solution[middle_row][x] = 'X'
                    dug.add((middle_row, x))
            
            # Mine the top row completely
            for x in range(w):
                if grid[0][x] in [':', 'S'] and len(dug) < limit:
                    solution[0][x] = 'X'
                    dug.add((0, x))
            
            # Mine the bottom row completely
            for x in range(w):
                if grid[2][x] in [':', 'S'] and len(dug) < limit:
                    solution[2][x] = 'X'
                    dug.add((2, x))
        
        elif w == 3:
            # Mine the middle column completely
            middle_col = 2
            for y in range(h):
                if grid[y][middle_col] in [':', 'S'] and len(dug) < limit:
                    solution[y][middle_col] = 'X'
                    dug.add((y, middle_col))
            
            # Mine the left column completely
            for y in range(h):
                if grid[y][0] in [':', 'S'] and len(dug) < limit:
                    solution[y][0] = 'X'
                    dug.add((y, 0))
            
            # Mine the right column completely
            for y in range(h):
                if grid[y][2] in [':', 'S'] and len(dug) < limit:
                    solution[y][2] = 'X'
                    dug.add((y, 2))
        
        # Reconstruct asteroid
        asteroid[1:h+1] = [''.join(row) for row in solution]
        results.append('\n'.join(asteroid))
    
    return '\n\n'.join(results)


def main():
    input_folder = Path("Inputs")
    output_folder = Path("Outputs")
    output_folder.mkdir(exist_ok=True)
    
    for input_file in sorted(input_folder.glob("level3_*.in")):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        result = solve(data)
        
        output_file = output_folder / input_file.name.replace('.in', '.out')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"Generiert: {output_file.name}")


if __name__ == "__main__":
    main()