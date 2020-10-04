import docx2txt


path = 'D:\\projects\\bazyabi\\paragraphs.docx'
text = docx2txt.process(path)
write_text_file = open("allGroupstext.txt","wb")
write_text_file.write(text.encode("utf-8"))
write_text_file.close()