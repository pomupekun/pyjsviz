# -*- coding: utf-8 -*-

nobel_winners = [
    {
        'category': 'Physics',
        'name': 'Albert Einstein',
        'nationality': 'Swiss',
        'sex': 'male',
        'year': 1921,
    },
    {
        'category': 'Physics',
        'name': 'Paul Dirac',
        'nationality': 'British',
        'sex': 'male',
        'year': 1933
    },
    {
        'category': 'Chemistry',
        'name': 'Marie Curie',
        'nationality': 'Polish',
        'sex': 'female',
        'year': 1911
    }
]

# print('dict data', nobel_winners)


def simple_csv_write(data, filename):
    cols = data[0].keys()
    cols.sort()
    print("cols", cols)
    print("sorted", cols)
    print("join", ',' . join(cols))

    with open(filename, 'w') as f:
        # join: phpのimplode。csvのヘッダ用文字列を作成
        f.write(','.join(cols) + '\n')

        for o in data:
            row = [str(o[col]) for col in cols]
            f.write(',' . join(row) + '\n')


def simple_csv_read(filename):
    with open(filename) as r:
        for line in r.readlines():
            print(line),


def mod_csv_write(data, filename):
    import csv
    with open(filename, 'wb') as f:
        fieldnames = data[0].keys()
        fieldnames.sort()
        print('fieldnames', fieldnames)
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for w in data:
            writer.writerow(w)


def mod_csv_read(filename):
    import csv
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def mod_csv_dict_read(filename):
    import csv
    with open(filename) as f:
        reader = csv.DictReader(f)
        dict = list(reader)
        print(dict)
        for w in dict:
            w['year'] = int(w['year'])
            print(w)




# simple_csv_write(nobel_winners, 'data/test1.csv')
# simple_csv_read('data/test1.csv')
# mod_csv_write(nobel_winners, 'data/test2.csv')
# mod_csv_read('data/test2.csv')
winners = mod_csv_dict_read('data/nobel_winners.csv')


