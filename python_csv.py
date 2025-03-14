import csv

data = open('username.csv', encoding='utf-8')
csv_data = csv.reader(data, delimiter=';')

data_lines = list(csv_data)


# for line in data_lines:
#     print(line)


# print(data_lines)

# all_names = []
# for line in data_lines[1:]:
#     if line:
#         all_names.append(line[2] + ' ' + line[3])

# print(all_names)

file_to_output = open('to_save_file .csv', 'w') # 'w' - write mode
csv_writer = csv.writer(file_to_output, delimiter=';')

csv_writer.writerow(['first name', 'last name'])

for line in data_lines[1:]:
    if line:
        csv_writer.writerow([line[2], line[3]])

file_to_output.close()

f = open('to_save_file .csv', 'a') # 'a' - append mode
csv_writer = csv.writer(f, delimiter=';')

csv_writer.writerow(['Fulano', 'da Silva'])

f.close()


f = open('to_save_file .csv', 'r') # 'r' - read mode
csv_f = csv.reader(f, delimiter=';')

for line in csv_f:
    print(line)

f.close()
