string = 'шалаш'
list_string = list(string)
flag = True

for i in range(0,len(list_string)):
    if list_string[i] != list_string[-(i+1)]:
        flag = False

if (flag):
    print('polindrom')
else:
    print('not polindrom')
