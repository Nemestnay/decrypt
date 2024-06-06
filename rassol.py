import xlsxwriter
workbook = xlsxwriter.Workbook('table.xlsx')
worksheet = workbook.add_worksheet()
f = open('desol.txt', 'r')

mas = {89638730193, 89179144668, 89839655342, 89158111588, 89858713871}
a = 89638730193
bigset = set()
while True:
    line = f.readline()[-12:]
    if not line:
        break
    bigset.add(int(line))
sol = 0
newmas = set()
for el in mas:
    newmas.add(el+sol)
for elem in bigset:
    sol = elem - a
    newmas = set()
    for el in mas:
        newmas.add(el + sol)
    if len(newmas & bigset) == 5:
        break
f.close()
f = open('desol.txt', 'r')
worksheet.write(0, 0, 'Хеш')
worksheet.write(0, 1, 'Номер телефона')
worksheet.write(1, 2, '89638730193')
worksheet.write(2, 2, '89179144668')
worksheet.write(3, 2, '89839655342')
worksheet.write(4, 2, '89158111588')
worksheet.write(5, 2, '89858713871')
i=1
while True:
    line = f.readline()
    if not line:
        break
    worksheet.write(i, 0, line[:-13])
    worksheet.write(i, 1, int(line[-12:-1]) - sol)
    i+=1
print(sol)
workbook.close()
f.close()
