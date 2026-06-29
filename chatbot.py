
from difflib import get_close_matches
from faq_data import faq_data
from datetime import datetime

questions = list(faq_data.keys())

questions_asked = 0
answers_found = 0
not_found = 0

print("="*60)
print("🤖 CodeAlpha Smart FAQ Chatbot")
print("="*60)
print("Type 'exit' anytime to quit.\n")

while True:

    user_question = input("You : ")

    if user_question.lower() == "exit":
        break

    questions_asked += 1

    match = get_close_matches(user_question, questions, n=3, cutoff=0.4)

    if match:

        answer = faq_data[match[0]]

        print("\n🤖", answer)

        answers_found += 1

        try:
            with open("chat_history.txt", "a", encoding="utf-8") as file:
                file.write("="*60 + "\n")
                file.write("Time : " + str(datetime.now()) + "\n")
                file.write("Question : " + user_question + "\n")
                file.write("Matched FAQ : " + match[0] + "\n")
                file.write("Answer : " + answer + "\n")
                file.write("="*60 + "\n\n")
        except Exception as e:
            print("\n⚠ Unable to save chat history.")
            print(e)

    else:

        print("\n❌ Sorry, I couldn't find an answer.")

        if len(match) > 0:
            print("\nDid you mean:")
            for item in match:
                print("•", item)

        not_found += 1

print("\n" + "="*60)
print("📊 SESSION SUMMARY")
print("="*60)
print("Questions Asked :", questions_asked)
print("Answers Found   :", answers_found)
print("Not Found       :", not_found)
print("="*60)
print("👋 Thank you for using CodeAlpha Smart FAQ Chatbot!"