readfile = open('quiz.html', 'ra')
writefile = open('quizNew.html', 'rw')
endfile = open('quizEnd.html', 'r')


count = len(open('quiz.html', 'r').readlines(  ))

print(readfile.readline())

readfile.write(writefile.read())
readfile.write(endfile.read())
readfile.close()

loopNum = int(input("How much questions you want to write?: "))
for a in range(1, loopNum):
    questionNum = int(input("How much questions do you have so far?: "))
    questionLine = str(input("please type the question line: ")).replace('<', '&lt;').replace('>', '&gt;')
    writefile.write('<p class = "questions">'+str(questionNum+a)+'.'+questionLine +'</p>\n')
    for i in range(1,5):
        answer = str(input("please type answer number " + str(i) + ": ")).replace('<', '&lt;').replace('>', '&gt;')
        correct = int(input("is it the correct answer (1 for yes, 0 for no)?: "))
        writefile.write('<input type="radio" id="mc" name="q'+str(i)+'" value="'+str(correct)+'">' + answer +'<br>\n')


readfile.write(str(writefile))
readfile.write(endfile)