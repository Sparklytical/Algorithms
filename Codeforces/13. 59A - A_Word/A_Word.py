val = input()
cap = []
low = []

for i in val:
    if(i.isupper()):
        cap.append(i)
    else:
        low.append(i)
if(len(cap) > len(low)):
    print(val.upper())
else:
    print(val.lower())
