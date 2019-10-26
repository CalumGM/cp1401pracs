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
    category = input("What category would you like to store {} files into: ".format(doctype))
    try:
        os.mkdir(category)
    except FileExistsError:
        pass
    for file in files:
        for index, char in enumerate(file):
            if file[index] == ".":
                doc_type = file[index + 1:]
        if doctype == doc_type:
            shutil.move(file, category + '/' + file)