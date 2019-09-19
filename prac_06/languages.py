
from prac_06.programming_languages import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
print([str(language) for language in languages])

print("\nThe dynamically typed languages are: ")
dynamic_languages = [dynamic.name for dynamic in languages if dynamic.is_dynamic()]
for i in dynamic_languages:
    print(i)
