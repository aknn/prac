def combo_gen():
    for c1 in range(3):
        for c2 in range(3):
            for c3 in range(3):
                yield (c1, c2, c3)

#Then, to actually make use of it:

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == (1,1,1):
        print('Found the combo:{}'.format((c1, c2, c3)))
        break