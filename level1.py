from pathlib import Path

def solve(input_data):
    lines = input_data.strip().split()
    if not lines:
        return ""
    
    it = iter(map(int, lines))
    try:
        n = next(it)
    except StopIteration:
        return ""
    
    results = []
    for _ in range(n):
        try:
            w = next(it)
            h = next(it)
        except StopIteration:
            break
        
        total_w = w + 2
        top_bottom = '#' * total_w
        middle = '#' + ':' * w + '#'
        asteroid = [top_bottom] + [middle] * h + [top_bottom]
        results.append('\n'.join(asteroid))
    
    return '\n\n'.join(results)


def main():
    input_folder = Path("Inputs")
    output_folder = Path("Outputs")
    output_folder.mkdir(exist_ok=True)
    
    for input_file in sorted(input_folder.glob("level1_*.in")):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        result = solve(data)
        
        output_file = output_folder / input_file.name.replace('.in', '.out')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(result))
        print(f"Generiert: {output_file.name}")


if __name__ == "__main__":
    main()