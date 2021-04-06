from os import listdir, remove

def getInputLines(path):
    file = open(path, "r");
    inputLines = file.readlines();
    file.close();
    return inputLines;

def writeOutputLines(path, outputLines):
    file = open(path, "w", encoding='utf8');
    file.writelines(outputLines);
    file.close();

def getFileList(path):
    return listdir(path);

def removeDoneFile(path):
    remove(path)