from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-##################################' #replace with your API
messages = []

chat = {
    "Hi": "Hello! How can I assist you today?",
    "How are you?": "I'm doing well, thank you! How can I help you?",
    "what is eziline": "Eziline software house is a tech company which provides various solutions like web development, app development and, SEO ect.",
    "What can you tell me about Eziline?": "Eziline is a software development and IT consulting company that specializes in providing innovative solutions for businesses.",
    "What services does Eziline offer?": "Eziline offers a wide range of services, including web development, mobile app development, software testing, UI/UX design, and IT consulting.",
    "Where is Eziline located?": "Eziline is located at following locations \nPK Office:304-G, Amna Plaza Pesh Rd Rawalpindi \nUS Office: 16192 Coastal Highway Lewes, DE \nUK Office: Intl. House, 776-778 Barking Rd London \nFR Office:5 avenue Pierre Salvi 95500 Gonesse Paris.",
    "What industries does Eziline cater to?": "Eziline caters to various industries such as healthcare, e-commerce, finance, education, and more.",
    "Who is CEO of Eziline?": "CEO of eziline is Ismail Shah.",
    "What is the mission of Eziline?": "The mission of Eziline is to empower businesses with cutting-edge technology solutions and exceptional customer service.",
    "What sets Eziline apart from other companies?": "Eziline stands out for its commitment to quality, innovation, and client satisfaction. We strive to deliver customized solutions that meet our clients' unique requirements.",
    "How can I contact Eziline?": "You can contact Eziline by filling out the contact form on our website or by calling our phone number at [phone number].",
    "What are Eziline's office hours?": "Eziline's office hours are 9am to 5pm.",
    "Is there a support email for Eziline?": "Yes, you can reach out to our support team by emailing info@eziline.com.",
    "Can I schedule a meeting with Eziline?": "Certainly! We would be happy to schedule a meeting with you. Please provide your preferred date and time, and we will get back to you to confirm."
}


def chat_bot(user_input):
    messages.append({"role": "user", "content": user_input})
    for key, value in chat.items():
        if user_input.lower() in key.lower():
            messages.append({"role": "assistant", "content": value})
            return value
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json["user_input"]
    response = chat_bot(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run()
