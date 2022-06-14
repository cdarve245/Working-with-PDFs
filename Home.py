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

                # find title
                searchFor = len("CPM Specifications Document")
                indexOfTitle = lines.find("CPM Specifications Document")
                indexOfNewLine = lines.find(":", indexOfTitle)
                title = lines[indexOfTitle + searchFor:indexOfNewLine]
                newPDF.append(title)

                # find ids
                indexOfOSMSC = lines.find("OSMSC")
                indexOfNewLine = lines.find("\n", indexOfOSMSC)
                idsOfPdf = lines[indexOfOSMSC + 5:indexOfNewLine].split()

                for id in idsOfPdf:
                    firstPartID = id[0:4]
                    secondPartID = id[5:9]

                    listOfIDs.add(firstPartID + "_" + secondPartID)
                    newPDF.append(firstPartID + "_" + secondPartID)

                    searchFor = len("ID: OSMSC" + firstPartID +
                                    "\nsubID: " + secondPartID + "\n Age: ")
                    indexOfAge = lines.find(
                        "ID: OSMSC" + firstPartID + "\nsubID: " + secondPartID + "\nAge: ")
                    indexOfNewLine = lines.find("\nGe", indexOfAge + searchFor)
                    if indexOfAge != - 1 and indexOfNewLine != -1:
                        age = lines[indexOfAge +
                                    searchFor - 2:indexOfNewLine]
                    newPDF.append("Age: " + str(age))

                    searchFor = len("ID: OSMSC" + firstPartID + "\nsubID: " +
                                    secondPartID + "\nAge: " + str(age) + "\nGender: ")
                    indexOfGender = lines.find(
                        "ID: OSMSC" + firstPartID + "\nsubID: " + secondPartID + "\nAge: " + str(age) + "\nGender: ")
                    indexOfNewLine = lines.find("\n", indexOfAge + searchFor)
                    if indexOfAge != - 1 and indexOfNewLine != -1:
                        gender = lines[indexOfAge +
                                       searchFor - 2:indexOfNewLine]
                    newPDF.append("Gender: " + gender)
                newPDF.append(title)

                pdfInfo.append(newPDF)

    for pdf in pdfInfo:
        text.write("\n" + pdf[0])
        text.write("\n" + pdf[1] + "\n")
        for value in pdf:
            if value in listOfIDs:
                text.write("\t" + value + "\n")
            if "Age: " in value:
                text.write("\t" + value + "\n")
            if "Gender: " in value:
                text.write("\t" + value + "\n")
        text.write("NEW PDF \n")
