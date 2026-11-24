"""Make the AI Judge Laugh: the Office Joke Open — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single-line joke about office life, at most 200 characters.
"""
import os

LINE = "My calendar says I'm free all day, which is how I know nobody actually read my calendar."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
