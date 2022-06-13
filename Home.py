import os

with open('pdfInfo.txt', 'w') as text:
    # count = 0
    for filename in os.listdir("PDFs"):
        # print(filename)
        f = os.path.join("PDFs", filename)
        if os.path.isfile(f):

            with open(f, encoding="utf8") as pdf:
                # count += 1
                text.write(filename + "\n")
                # prints ids per file
                lines = pdf.read()
                indexOfOSMSC = lines.find("OSMSC")
                indexOfNewLine = lines.find("\n", indexOfOSMSC)
                idsOfPdf = lines[indexOfOSMSC + 5:indexOfNewLine].split()
                for id in idsOfPdf:
                    text.write("\t" + id + "\n")
    # text.write(str(count))
