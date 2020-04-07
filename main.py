 import os
    import comtypes.client
    import time


    wdFormatPDF = 17


  #user should enter path
  
    in_file=r'absolute path of input docx file 1'
    out_file=r'absolute path of output pdf file 1'

    in_file2=r'absolute path of input docx file 2'
    out_file2=r'absolute path of outputpdf file 2'

   
    print in_file
    print out_file
    print in_file2
    print out_file2


t
    word = comtypes.client.CreateObject('Word.Application')
    # make word visible before open a new document
    word.Visible = True
# wait for the COM Server to prepare well.
    time.sleep(3)

    # convert docx file 1 to pdf file 1
    doc=word.Documents.Open(in_file) # open docx file 1
    doc.SaveAs(out_file, FileFormat=wdFormatPDF) # conversion
    doc.Close() # close docx file 1
    word.Visible = False
    # convert docx file 2 to pdf file 2
    doc = word.Documents.Open(in_file2) # open docx file 2
    doc.SaveAs(out_file2, FileFormat=wdFormatPDF) # conversion
    doc.Close() # close docx file 2   
    word.Quit() # close Word Application
