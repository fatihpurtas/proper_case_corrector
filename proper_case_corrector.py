import sys

def type_corrector(txt):
    txt = txt.lower()
    lines = txt.split('\n')
    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            words[j] = words[j][0].upper() + words[j][1:]
        lines[i] = ' '.join(words)
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python file.py <file_name>")
        return
    file_name = sys.argv[1]

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            txt = file.read()
    except FileNotFoundError:
        print(f"{file_name} file not found..")
        return

    output = type_corrector(txt)

    new_file_name = "edited_" + file_name
    with open(new_file_name, "w", encoding="utf-8") as file:
        file.write(output)

    print(f"New text file created: {new_file_name}")


if __name__ == "__main__":
    main()
