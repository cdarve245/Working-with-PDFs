from array import array
from distutils.command.clean import clean
import os

with open('pdfInfo.txt', 'w') as text:
    pdfInfo = []
    listOfIDs = set()
    allTitles = []
    for filename in os.listdir("PDFs"):
        f = os.path.join("PDFs", filename)
        if os.path.isfile(f):

            with open(f, encoding="utf8") as pdf:
                newPDF = [filename]

                lines = pdf.read()

                # find title
                searchFor = len("CPM Specifications Document\n")
                indexOfTitle = lines.find("CPM Specifications Document\n")
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
                pdfInfo.append(newPDF)

    # for pdf in pdfInfo:
    #     text.write(pdf[0])
    #     text.write(pdf[1] + "\n")
    #     IDcount = 0
    #     for value in pdf:
    #         if value in listOfIDs:
    #             IDcount += 1
    #             text.write("\t" + value + "\n")
    #         if "Age: " in value:
    #             text.write("\t" + value + "\n")
    #         if "Gender: " in value:
    #             text.write("\t" + value + "\n\n")
    #     text.write("------------------------------\n")

    idInfo = []
    for pdf in pdfInfo:
        newIDS = []
        IDcount = 0
        for value in pdf:
            curCount = IDcount
            if value in listOfIDs:
                newID = ["ID: N/A", "PDF: N/A",
                         "Title: N/A", "Age: N/A", "Gender: N/A", "\n"]
                newID[0] = "ID:" + value + "\n"
                newID[1] = "File:" + pdf[0] + "\n"
                newID[2] = "Title:" + pdf[1] + "\n"
                newID[3] = "---------------------------\n"
                IDcount += 1
            if "Age: " in value:
                newID[3] = value + "\n"
            if "Gender: " in value:
                newID[4] = value + "\n"
                newID[5] = "---------------------------\n"
            if curCount != IDcount:
                newIDS.append(newID)
        idInfo.append(newIDS)

    idAdded = []
    cleanIdInfoList = []
    for info in idInfo:
        for i in info:
            if i[0] not in idAdded:
                idAdded.append(i[0])
                for e in i:
                    cleanIdInfoList.append(e)
            else:
                index = cleanIdInfoList.index(i[0])
                cleanIdInfoList.insert(index + 1, i[1])

    for i in cleanIdInfoList:
        text.write(i)
