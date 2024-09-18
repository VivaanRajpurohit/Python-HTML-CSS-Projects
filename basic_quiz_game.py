quiz_answer = "Paris"

while True:
    quiz_question = input("What is the capital of France?: ")
    if quiz_question.lower() == quiz_answer.lower():
        print("Good job, you got it correct!")
        break
    else:
        print("Wrong answer, try again.")
