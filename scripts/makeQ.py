firstfile = open('quiz.html', 'rw')
secondfile = open('quizNew.html', 'w')
endfile = open('quizEnd.html', 'r')

linecount = len(firstfile.readlines())
firstfile.close()
firstfile = open("./quiz.html", "rw")
string = ''
for i in range(linecount):
    line = firstfile.readline()
    string += line
    if i == linecount-6:
        break


loopNum = int(raw_input("How much questions you want to write?: "))
for a in range(1, loopNum+1):
    questionNum = int(raw_input("How much questions do you have so far?: "))
    questionLine = str(raw_input("please type the question line: ")).replace('<', '&lt;').replace('>', '&gt;')
    string += '<p class = "questions">'+str(questionNum+a)+'.'+questionLine +'</p><br>\n'
    for i in range(1,5):
        answer = str(raw_input("please type answer number " + str(i) + ": ")).replace('<', '&lt;').replace('>', '&gt;')
        correct = int(raw_input("is it the correct answer (1 for yes, 0 for no)?: "))
        string += '<input type="radio" id="mc" name="q'+str(i)+'" value="'+str(correct)+'">' + answer +'<br>\n'

firstfile.close()
firstfile = open('quiz.html', 'w')
firstfile.write(string)
firstfile.write(endfile.read())
