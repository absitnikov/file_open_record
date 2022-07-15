import os


def txt_files(sort):
    files = os.listdir(sort)
    print(files)
    temp_dict = {}
    for file in files:
        if file.endswith('.txt'):
            with open(file, encoding='utf-8') as folder:
                file_list = []
                file_1 = folder.readlines()
                file_list.append(file_1)
                file_list.append(len(file_1))
                temp_dict[file] = file_list
    dict_sort = list(sorted(temp_dict.items(), key=lambda x: x[1][1]))
    print(dict_sort)
    with open('sort.txt', 'w', encoding="utf-8") as output:
        for file in dict_sort:
            print(file[0], file[1][-1], *file[1][0], sep='\n', file=output)


txt_files(os.getcwd())