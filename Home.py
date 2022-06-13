# from PyPDF2 import PdfReader
import os

with open('pdfInfo.txt', 'w') as text:
    for filename in os.listdir("PDFs"):
        # print(filename)
        f = os.path.join("PDFs", filename)
        if os.path.isfile(f):

            with open(f, encoding="utf8") as pdf:
                lines = pdf.read()
                indexOfOSMSC = lines.find("OSMSC")
                indexOfNewLine = lines.find("\n", indexOfOSMSC)
                # text.write(lines[indexOfOSMSC:indexOfNewLine])
                idsOfPdf = lines[indexOfOSMSC + 5:indexOfNewLine].split()
                text.write(filename + "\n")
                for id in idsOfPdf:
                    text.write("\t" + id + "\n")
