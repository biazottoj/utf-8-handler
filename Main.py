from Codes import codes
from IOHandler import *


#code[0] ==  letter
#code[1] ==  code


for file in getFileList("input_files"):
    output_lines = []
    inputLines = getInputLines("input_files/"+file)
    removeDoneFile("input_files/"+file)
    for input_line in inputLines:
        output_line = input_line;
        isTrue = False;
        for code in codes:
            if code[1] in input_line:
                if(isTrue):
                    output_line = output_line.replace(code[1], code[0]);
                else:
                    isTrue = True
                    output_line = input_line.replace(code[1], code[0]);
        output_lines.append(output_line);
    writeOutputLines("output_files/"+file, output_lines);
