import re
for index in range(int(input())):
    string = input()
    x=re.findall('(#[a-fA-F0-9]{3,6})\S',string)
    [print(i) for i in x]


    
output:
    
 11
body {
  color: red;
}

h1 {
  color: #00ff00;
}

p.ex {
  color: rgb(0,0,255);
}

#00ff00
