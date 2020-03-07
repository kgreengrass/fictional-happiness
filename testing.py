import csv

###CSV READER####
with open('ks-projects-201801.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    iterable_csv = iter(csv_reader)  ##### gets rid of the headers, skips the first row
    next (iterable_csv)  ## part of the above line
    for row in iterable_csv:
        try:
            print(row)
        except UnicodeDecodeError:
            print('Error for row')
            pass


# with open('user_details.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     print(list(csv_reader))