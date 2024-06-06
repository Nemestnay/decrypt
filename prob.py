import xlsxwriter
import hashlib
workbook = xlsxwriter.Workbook('prob.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'Хеш')
worksheet.write(0, 1, 'Номер телефона')
worksheet.write(1, 2, '89638730193')
worksheet.write(2, 2, '89179144668')
worksheet.write(3, 2, '89839655342')
worksheet.write(4, 2, '89158111588')
worksheet.write(5, 2, '89858713871')
f = open('desol.txt', 'r')
sol = 0
i = 0
while True:
    line = f.readline()[-12:]
    if not line:
        break
    i += 1
    number = str(int(line[-12:-1]) - sol) + 'a'
    md5 = str(hashlib.sha1(number.encode()).hexdigest())
    worksheet.write(i, 0, md5)
    worksheet.write(i, 1, number)
    if i < 10:
        print(line[-12:-1], number)
workbook.close()
f.close()
