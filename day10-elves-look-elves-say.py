#Day 10 - Elves Look, Elves Say

code='1113122113'

def translate(x):
    a=str(len(x))
    b=x[0]
    return a+b

def lookup(x):
    ans=[]
    var=[]
    ans.append(0)
    n_code=''
    for i in xrange(len(x)-1):
        if x[i]!=x[i+1]:
            ans.append(i+1)
    ans.append(len(x))
    
    for j in xrange(len(ans)-1):
        var.append(x[ans[j]:ans[j+1]])

    for k in xrange(len(var)):
        n_code+=translate(var[k])

    return n_code

for p in xrange(0,50):
    code=lookup(code)

print len(code)
