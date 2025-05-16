import os
import sys

def generate_c_code(brainfuck_source):
    # Шаблон C-программы
    c_template = """
#include<stdio.h>
#define ARRAY_SIZE 30000 // размер массива памяти

int main() {{
    char array[ARRAY_SIZE];
    int ptr = 0;
    
    {code}
    
    return 0;
}}
"""

    code_segments = []
    for ch in brainfuck_source.strip():
        if ch == '>':
            code_segments.append("ptr++;")
        elif ch == '<':
            code_segments.append("ptr--;")
        elif ch == '+':
            code_segments.append("array[ptr]++;")
        elif ch == '-':
            code_segments.append("array[ptr]--;")
        elif ch == '.':
            code_segments.append('putchar(array[ptr]);')
        elif ch == ',':
            code_segments.append('array[ptr] = getchar();')
        elif ch == '[':
            code_segments.append('while(array[ptr]) {')
        elif ch == ']':
            code_segments.append('}')

    generated_code = '\n'.join(code_segments)
    final_code = c_template.format(code=generated_code)
    return final_code


if __name__ == "__main__":
    if len(sys.argv) != 2 or not (sys.argv[1].endswith('.bf') or sys.argv[1].endswith('.b')):
        print("Usage: python bf_compiler.py <filename.bf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_filename = os.path.splitext(input_file)[0] + ".c"

    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    c_code = generate_c_code(source_code)

    with open(output_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(c_code)

    print(f"C-code written to '{output_filename}' successfully.")
