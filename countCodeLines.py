import glob

countLinesFiles = 0

types = ['**/*.java', '**/*.js']

for type_of_files in types:
    for path in glob.glob(type_of_files, recursive=True):
        with open(path) as file:
            linesInFile = len(file.readlines())
            print("Number of lines " + path + " - " + str(linesInFile))
            countLinesFiles += linesInFile

print("Total number lines of code: " + str(countLinesFiles))