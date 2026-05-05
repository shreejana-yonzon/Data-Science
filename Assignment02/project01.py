#Scenario: Create a MathTutor class that generates random math questions using random and math operators.

#Track correct and incorrect answers.
#Provide a score at the end.
#Handle invalid input using exception handling.
#Concepts: Random, Math, Exception Handling, Classes



import random
class MathTutor:
    def __init__(self, total_questions: int = 5):
        self.correct = 0
        self.incorrect = 0
        self.total_questions = total_questions
        self.operators = ['+', '-', '*', '/']
        
    
    def ques_generator(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(self.operators)
        
        if operator == '/':
            num2 = random.randint(1,20)
            correct_answer = round(num1/num2, 2)
        elif operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        return num1, num2, operator, correct_answer
    
    def run_question(self):
        print("---------Math Tutor-------")
        
        for question in range(1, self.total_questions + 1):
            num1, num2, operator, correct_answer = self.ques_generator()
            
            print(f"Question {question}: {num1} {operator} {num2}")
            
            # For file Handling
            try:
                user = float(input("Your answer: "))
            
            except ValueError as exc:
                print(f"Invalid input! {exc} is not an whole number.")
                self.incorrect += 1 
                continue
            
            if user == correct_answer:
                print(f"Congratulation! Your answer is correct!")
                self.correct += 1
            else:
                print(f"Incorrect! Your answer is: {correct_answer}")
                self.incorrect += 1
        
        #Final Score
        print("\n -----------Result-----------")
        print("Correct:", self.correct)
        print("Incorrect:", self.incorrect)
        print("Score:", (self.correct/self.total_questions)*100,"%")
        

# Running Program 
if __name__ == "__main__":
    tutor = MathTutor(5)
    tutor.run_question()