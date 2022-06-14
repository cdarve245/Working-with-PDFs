import os

with open('pdfInfo.txt', 'w') as text:
    pdfInfo = []
    listOfIDs = set()
    allText = []
    allTitles = []
    for filename in os.listdir("PDFs"):
        f = os.path.join("PDFs", filename)
        if os.path.isfile(f):

            with open(f, encoding="utf8") as pdf:
                newPDF = [filename]

                lines = pdf.read()

                indexOfOSMSC = lines.find("OSMSC")
                indexOfNewLine = lines.find("\n", indexOfOSMSC)
                idsOfPdf = lines[indexOfOSMSC + 5:indexOfNewLine].split()

                for id in idsOfPdf:
                    newPDF.append(id)
                    listOfIDs.add(id)

                searchFor = len("CPM Specifications Document")
                indexOfTitle = lines.find("CPM Specifications Document")
                indexOfNewLine = lines.find(":", indexOfTitle)
                title = lines[indexOfTitle + searchFor:indexOfNewLine]

                newPDF.append(title)
                pdfInfo.append(newPDF)

    for pdf in pdfInfo:
        text.write("\n" + pdf[0])
        text.write("\n" + pdf[len(pdf) - 1] + "\n")
        for value in pdf:
            if value in listOfIDs:
                text.write("\t" + value + "\n")
        text.write("NEW PDF \n")
    print(len(listOfIDs))
    print(len(pdfInfo))
