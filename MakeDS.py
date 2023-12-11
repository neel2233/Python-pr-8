import random
import os
import csv


def MakeDS(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)

    random.shuffle(data)
    split_index = int(0.7 * len(data))
    train_data = data[:split_index]
    test_data = data[split_index:]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    workdata_dir = os.path.join(base_dir, 'workdata')
    learning_dir = os.path.join(workdata_dir, 'Learning')
    testing_dir = os.path.join(workdata_dir, 'Testing')
    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    train_file_path = os.path.join(learning_dir, 'train.csv')
    with open(train_file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(train_data)

    test_file_path = os.path.join(testing_dir, 'test.csv')
    with open(test_file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(test_data)

