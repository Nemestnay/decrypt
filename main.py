import pandas as pd
f = open('dehash.txt', 'r')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_excel('text.xlsx', engine='openpyxl')
df.rename(columns=df.iloc[0])


def number(x):
    return f.readline()[-12:-1]


def ad(str):
    mesto = str.rfind(".")
    number = (ord(str[mesto-1]) - ord("в") + 32) % 32
    global sdvigi
    sdvigi.append(number)
    otvet = ''
    for i in range(len(str)):
        if str[i] != "." and str[i] != " " and str[i] != "-" and ord(str[i]) > 57:
           otvet += chr(((ord(str[i]) - 1071) + 32 - number) % 32 + 1071)
        else:
            otvet += str[i]
    return otvet


def email(str):
    global shetchic
    number = sdvigi[shetchic]
    shetchic += 1
    otvet = ''
    for i in range(len(str)):
        if str[i] != "." and str[i] != " " and str[i] != "@":
            otvet += chr(((ord(str[i]) - 96) + 26 - number) % 26 + 96)
        else:
            otvet += str[i]
    return otvet


#df['Телефон'] = df['Телефон'].apply(lambda x: number(x))
#df['Адрес'] = df["Адрес"].apply(lambda x: ad(x))
#df['email'] = df['email'].apply(lambda x: email(x))
#df['сдвиг'] = sdvigi
df.to_csv('filename.csv', index=False)
f.close()

