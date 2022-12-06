import csv
import os
import matplotlib.pyplot as plt

def read_csv(fold):
    interval = 360

    fold_walk = os.walk(fold)
    for path, dir_list, file_list in fold_walk:
       for file in file_list:
           if file != '.DS_Store':
               file_path = os.path.join(path, file)

               tg_fold = os.path.join(path, 'epoch_data')
               if not os.path.exists(tg_fold):
                   os.mkdir(tg_fold)

               if file[1] == 'r':
                   tg_file = file[0:5] + '_epoch.csv'
               elif file[1] == 'e':
                   tg_file = file[0:4] + '_epoch.csv'
               tg_file_path = os.path.join(tg_fold, tg_file)

               w = open(tg_file_path, 'w', newline='')
               writer = csv.writer(w)

               r = open(file_path, 'r')
               reader = csv.reader(r)

               for idx, row in enumerate(reader):
                   if idx % interval == 0:
                       writer.writerow(row)

               w.close()
               r.close()

def draw_chart(fold):
    dic = {'reward': 3,
           'att': 4,
           'throughput': 5,
           'lay_delay': 6}

    fold_walk = os.walk(fold)
    for path, dir_list, file_list in fold_walk:
        for file in file_list:
            if file.find('epoch') > -1 and file.find('csv') > -1:
                file_path = os.path.join(path, file)

                tg_fold_path = os.path.join(path, 'epoch_figure')
                if not os.path.exists(tg_fold_path):
                   os.mkdir(tg_fold_path)

                r = open(file_path, 'rt')
                reader = csv.reader(r)
                epoch_column = [int(row[1]) for row in reader if row[0] != 'env_id']

                for key, id in dic.items():
                    r = open(file_path, 'rt')
                    reader = csv.reader(r)
                    data_column = [float(row[id]) for row in reader if row[0] != 'env_id']

                    plt.plot(epoch_column, data_column)
                    plt.xlabel('epoch')
                    plt.ylabel(key)

                    if file[1] == 'r':
                        tg_file = file[0:5] + '_epoch_' + key + '_figure.png'
                    elif file[1] == 'e':
                        tg_file = file[0:4] + '_epoch_' + key + '_figure.png'

                    tg_file_path = os.path.join(tg_fold_path, tg_file)
                    plt.savefig(tg_file_path)
                    #plt.show()
                    plt.close()

                r.close()

def draw_chart_multi(fold, tg_fold):
    dic = {'reward': 3,
           'att': 4,
           'throughput': 5,
           'lay_delay': 6}

    count = 1
    fold_walk = os.walk(fold)
    for path, dir_list, file_list in fold_walk:
        for file in file_list:
            if file.find('epoch') > -1 and file.find('csv') > -1:
                file_path = os.path.join(path, file)

                #tg_fold = os.path.join(path, 'epoch_figure')
                #if not os.path.exists(tg_fold):
                #   os.mkdir(tg_fold)

                r = open(file_path, 'rt')
                reader = csv.reader(r)
                epoch_column = [int(row[1]) for row in reader if row[0] != 'env_id']

                for key, id in dic.items():
                    r = open(file_path, 'rt')
                    reader = csv.reader(r)
                    data_column = [float(row[id]) for row in reader if row[0] != 'env_id']

                    if count == 1:
                        plt.figure(figsize=(25, 10))
                    plt.subplot(2, 4, count, )
                    plt.plot(epoch_column, data_column)
                    #plt.xlabel('epoch')
                    #plt.ylabel(key)

                    if file[1] == 'r':
                        title = file[0:5] + '_' + key
                    elif file[1] == 'e':
                        title = file[0:4] + '_' + key
                    plt.title(title)

                    count = (count + 1) % 9
                    if count == 0:
                        str_start = path.find('data') + (len(fold) - 2) + 1
                        str_end = path.find('1h') + 2
                        tg_title = path[str_start : str_end]
                        tg_file = tg_title + '.png'
                        tg_file_path = os.path.join(tg_fold, tg_file)

                        plt.suptitle(tg_title)
                        plt.savefig(tg_file_path)
                        #plt.show()
                        plt.close()

                        count = 1

                r.close()

if __name__ == '__main__':

   fold_path = './data_1x1_14'
   tg_fold_path = './data_1x1_14/figures'

   #read_csv(fold_path)
   #draw_chart(fold_path)
   draw_chart_multi(fold_path, tg_fold_path)
