import csv


def DelNaN(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]
    new_lines = []
    for row in rows:
        new_row = row.copy()
        for i in row:
            if i == '':
                new_row.remove(i)
        new_lines.append(new_row)
    while new_lines[-1] == '':
        new_lines.pop(-1)
    with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(new_lines)
