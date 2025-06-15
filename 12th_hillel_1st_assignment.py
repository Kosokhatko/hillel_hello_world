import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        text_without_tags = re.sub(r'<[^>]+>', '', line)
        stripped_line = text_without_tags.strip()
        if stripped_line:
            cleaned_lines.append(stripped_line)

    with open(result_file, 'w', encoding='utf-8') as result:
        for line in cleaned_lines:
            result.write(line + '\n')
