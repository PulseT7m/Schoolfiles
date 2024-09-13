ww = "aaabbbbbbbaaabbbbbbb"
r = len(ww) // 2
# w1 = ww[:r]
# w2 = ww[r:]
i = a = 0
while i < len(ww)//2:
    if ww[i] == "a" or ww[i] == "b":
        a = "true"
        #print(f"{ww[i]} true")
        i += 1
    else:
        a = "false"
        i = len(ww)
if a == "true":
    if ww[:r] == ww[r:]:
        print(".")
    else:
        print("x")
else:
     print("false")