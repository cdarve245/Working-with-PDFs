import os

with open('pdfInfo.txt', 'w') as text:
    # count = 0
    listOfIDs = []
    allText = []
    for filename in os.listdir("PDFs"):
        # print(filename)
        f = os.path.join("PDFs", filename)
        if os.path.isfile(f):

            with open(f, encoding="utf8") as pdf:
                newPDF = [filename]
                lines = pdf.read()
                indexOfOSMSC = lines.find("OSMSC")
                indexOfNewLine = lines.find("\n", indexOfOSMSC)
                idsOfPdf = lines[indexOfOSMSC + 5:indexOfNewLine].split()
                for id in idsOfPdf:
                    if id not in allText:
                        listOfIDs.append(id)
                        allText.append(id)
                        allText.append(filename)
                    else:
                        allText.insert(allText.index(id) + 1, filename)
    for line in allText:
        if line in listOfIDs:
            text.write(line + "\n")
        else:
            text.write("\t" + line + "\n")
