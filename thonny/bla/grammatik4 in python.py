string="bbaab"
i=0
def q0(string, i):
    if i >= len(string):
        print("ableitbar")
    elif "a" == string[i]:
        i += 1
        q0(string, i)
    elif "b" == string[i]:
        i += 1
        q1(string, i)
    
def q1(string, i):
    if i >= len(string):
        print("nicht ableitbar")
    elif "a" == string[i]:
        i += 1
        q1(string, i)
    elif "b" == string[i]:
        i += 1
        q0(string, i)
        
q0(string, i)