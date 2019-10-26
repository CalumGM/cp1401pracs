import shutil
import os

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
files = os.listdir('.')
doctypes = []
for file in files:
    for index, char in enumerate(file):
        if file[index] == ".":
            doc_type = file[index + 1:]
            doctypes.append(doc_type)
doctypes = list(dict.fromkeys(doctypes))

for doctype in doctypes:
    try:
        os.mkdir(doctype)
    except FileExistsError:
        pass
    for file in files:
        for index, char in enumerate(file):
            if file[index] == ".":
                doc_type = file[index + 1:]
                print("{} is {}".format(file, doctype))
        if doctype == doc_type:
            print("Should make file")
            shutil.move(file, doctype + '/' + file)
