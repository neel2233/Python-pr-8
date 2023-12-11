import csv


def Info(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]
        print(f'Количество строк с данными: {len(rows)}')
        print(f'Количество колонок в таблице: {len(rows)}x{len(headers)}')
        for i in range(len(headers)):
            count = 0
            for row in rows:
                if not row[i]:
                    continue
                else:
                    count += 1
                tp = type(row[i]).__name__
            print(headers[i], '\t', count, '\t', tp)
