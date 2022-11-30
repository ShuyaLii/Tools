import csv

def read_csv(file, tg_file):
    w = open(tg_file, 'w')
    writer = csv.writer(w)

    r = open(file, 'r')
    reader = csv.reader(r)

    for idx, row in enumerate(reader):
        if idx % 360 == 0:
            writer.writerow(row)

    w.close()
    r.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_data_path = 'train_data.csv'
    test_data_path = 'test_data.csv'
    train_epoch_path = 'train_epoch.csv'
    test_epoch_path = 'test_epoch.csv'

    #read_csv(train_data_path, train_epoch_path)
    read_csv(test_data_path, test_epoch_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
