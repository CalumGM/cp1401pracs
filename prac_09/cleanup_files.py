"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')  # make temp inside of christmas
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    for index, char in enumerate(filename):
        if filename[index - 1].islower() and filename[index].isupper():
            filename = filename[:index] + '_' + filename[index:]
        elif filename[index - 1] == "_":
            text = filename[index].upper()
            filename = filename[:index] + text + filename[index + 1:]
    new_name = filename[1:]
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(full_name, new_name)


main()
