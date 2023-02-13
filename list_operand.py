

def list_extract(data,value):
    out = []

    for i in data:
        if i == value:
            out.append(i)
            break
        else:
            if i == value:
                out.append(i)
                break
    print(out)

d = ['ram','tom','jhon','om']
list_extract(d,'jhon')