def modify_list(l):
    for i in l:
        if i%2==1:
            l.remove(i)
        else:
            l.append(i/2)
    print(l)


print(modify_list([30, 63, 67, 29, 29, 54, 30, 29, 41, 0]))

