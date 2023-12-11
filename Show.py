import random
import csv


def Show(file_path, output_type='top', num_strings=5, separator=','):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]

        print(*headers, sep=separator)

        if output_type == 'top':
            output_rows = rows[:num_strings]
        elif output_type == 'bottom':
            output_rows = rows[-num_strings:]
        elif output_type == 'random':
            output_rows = random.sample(rows, num_strings)

        for row in output_rows:
            print(*row, sep=separator)
