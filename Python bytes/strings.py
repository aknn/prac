names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there ' + name
    print(statement)


"""  right way below """

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)