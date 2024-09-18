import random

quiz_questions = [
    ("What is the capital of Australia?", 
     ["Option A: Sydney", "Option B: Melbourne", "Option C: Canberra", "Option D: Brisbane"], 
     ["Canberra"]),
     
    ("The capital of the state of Louisiana is?", 
     ["Option A: New Orleans", "Option B: Baton Rouge", "Option C: Shreveport", "Option D: Lafayette"], 
     ["Baton Rouge"]),
     
    ("Who was the first man to step on the Moon?", 
     ["Option A: Buzz Aldrin", "Option B: Michael Collins", "Option C: Neil Armstrong", "Option D: Yuri Gagarin"], 
     ["Neil Armstrong"]),
     
    ("Which planet is known as the 'Red Planet'?", 
     ["Option A: Venus", "Option B: Mars", "Option C: Jupiter", "Option D: Saturn"], 
     ["Mars"]),
     
    ("What is the currency of Japan?", 
     ["Option A: Japanese Yen", "Option B: Chinese Yuan", "Option C: South Korean Won", "Option D: Indian Rupee"], 
     ["Japanese Yen"]),
     
    ("What is the chemical symbol for gold?", 
     ["Option A: Au", "Option B: Ag", "Option C: Fe", "Option D: Hg"], 
     ["Au"])
]

score = 0

while True:
    question, options, correct_answers = random.choice(quiz_questions)
    print(question)
    
    for option in options:
        print(option)
    
    user_answer = input("Your answer: ")
    
    if user_answer in correct_answers:
        print("Correct!")
        score += 5
    else:
        print(f"Wrong! The correct answer is: {correct_answers[0]}")
        score -= 1
    
    print("Your current score is:", score)
    
    continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_quiz != "yes":
        break

print("Final score:", score)
