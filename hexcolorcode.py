import re
'''txt = input()

print(re.findall('#[a-fA-F0-9]{3|6}',txt))
'''

'''for i in range(int(input())):
    s=input()
    x=s.split()
    
    if len(x)>1  and  '{' not in x:
        x=re.findall('(#[a-fA-F0-9]{3,6})\S',s)
        [print(i) for  i in x]
'''
for index in range(int(input())):
    string = input()
    x=re.findall('(#[a-fA-F0-9]{3,6})\S',string)
    [print(i) for i in x]
