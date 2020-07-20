import requests
import random
from similar_text import similar_text

response = requests.get('http://jservice.io/api/clues?category=139').json()

def return_random_question():
    global random_integer
    random_integer = random.randint(0, len(response)-1)
    return response[random_integer]["question"]

def return_answer():
    return response[random_integer]["answer"]


# random.shuffle(response) 
# score = 0 
# for item in response:
#     question= (item['question'])
#     user_response = input(("Here is your question: " + question + " : ")) 
#     answer = (item['answer'])
#     hint = ("The answer starts with the letter " + item['answer'][0] + " and has a total of " + str(len(item['answer'])) + " characters")
#     value = (item['value'])
#     if user_response.lower() == answer.lower():
#         score += value
#         print("Congrats!! you are correct! Your score is " + str(score)) 
#     elif 100> (similar_text(user_response.lower(),answer.lower())) >75:
#         second_chance = input("Nope! you're close would you like a hint: yes or no: ")
#         if second_chance.lower() == "yes":
#             print(hint)
#             second_response = input("What is your final guess: " )
#             if second_response.lower() == answer.lower():
#                 score += value
#                 print("WOOHOO you got it! your score is " + str(score))
#             else: 
#                 score -= value
#                 print("Sorry even with a hint you're still incorrect! The correct answer is: " + answer + "your score is " + str(score))
#         else:
#             score -= value
#             print("ok suit yourself, the correct answer is: " + answer + "your score is " + str(score))
#     else:
#         score -= value
#         print("That's inncorrect!- the answer is " + answer + " and your score is " + str(score))