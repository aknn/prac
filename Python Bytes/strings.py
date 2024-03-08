names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there ' + name
    print(statement)


"""  right way below """

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)

""" The reason for this is it scales better. When we use the +, we're creating new strings.
 A more impactful example of this might be if we're just trying to print out a string list
  of all of the names:"""

#Another fairly common string joining task is with file paths. It can be very tempting to do something like:

# /starting/file/path + '/' + filename
# As you may have guessed, this is not the correct method. Instead, we use os.path.join. For example:

#             double back-slash for window's nonsense.
location_of_files = 'C:\\Users\\H\\Desktop\\Intermediate Python'
file_name = 'example.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())