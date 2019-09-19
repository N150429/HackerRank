import re
for index in range(int(input())):
    string = input()
    x=re.findall('(#[a-fA-F0-9]{3,6})\S',string)
    [print(i) for i in x]
