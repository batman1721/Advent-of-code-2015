#Day 4 - The Ideal Stocking Stuffer

import hashlib

code='iwrupvqb'

def get_hash(x):
    return hashlib.md5(x.encode('utf-8')).hexdigest()

#Part 1
ans=''
i=0
while ans[:5]!='00000':
    i+=1
    ans=get_hash(code+str(i))
        
print i

#Part 2
ans=''
i=0
while ans[:6]!='000000':
    i+=1
    ans=get_hash(code+str(i))
        
print i
