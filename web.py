import requests
url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"

response = requests.get(url).json()

questions = list()
incorect = list()

count = 0;



correct = list()
for i in response["results"]:
    questions.append(i["question"])
    correct.append(i["correct_answer"])
    incorect.append(i["incorrect_answers"])


for i in range(0 , len(incorect)):
    print(questions[i])
    print("1 {}".format(incorect[i][0]))
    print("2 {}".format(incorect[i][1]))
    print("3 {}".format(incorect[i][2]))
    print("4 {}".format(correct[i]))
    answer =int(input("Your Answer\n"))
    if answer not in range(1,4):
        count+=10






print(count)











