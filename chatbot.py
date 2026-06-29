from difflib import get_close_matches
from faq_data import faq_data

print("=" * 55)
print("🤖 CodeAlpha FAQ Chatbot")
print("=" * 55)

questions = list(faq_data.keys())

while True:

    user_question = input("\nAsk your question (or type 'exit' to quit):\n")

    if user_question.lower() == "exit":
        print("\n👋 Thank you for using the FAQ Chatbot!")
        break

    match = get_close_matches(user_question, questions, n=1, cutoff=0.4)

    if match:
        print("\n✅ Answer:")
        print(faq_data[match[0]])
    else:
        print("\n❌ Sorry, I couldn't find an answer for that question.")