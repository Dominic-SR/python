
ans = 1996
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                if(str(a)+str(b)+str(c)+str(d) == str(ans)):
                    print("RES--->,",str(a)+str(b)+str(c)+str(d))
                    break
