from question_modal import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_text = question['text']
    new_answer = question['answer']
    new_question = Question(new_text, new_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()
+print(f"you are successfully submitted the quiz\n you're final score was {quiz.score}/{len(question_data)}")
