folder_word = open('tes.docx', 'w')
folder_word.write('Baris pertama aku tuh ganteng kali masbro -_- :v\n')
folder_word.write('siapa setuju aoaowkow\n')
folder_word.write('Aoakwokawo knotl')
folder_word.close()

# folder_word = open('tes.docx', 'r')
# for i in range(2):
#     print(str(i) + ': ' + folder_word.readline())

folder_word = open('tes.docx', 'r')
for i in folder_word.readlines():
    print("-%s" % i)