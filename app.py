from flask import Flask, render_template, request
import csv
import random
from datetime import datetime

app = Flask(__name__)

# Load dataset from CSV file
def load_dataset():
    file_path = 'C:\\Users\\Kaivalya\\BG INTERN\\ChatBot\\dataset.csv'
    dataset = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append({'question': row[0], 'answer': row[1]})
    return dataset


responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "Feeling great!", "All good!"],
    "time": ["The current time is {time}.", "It's {time} right now.", "Right now, it's {time}."],
    "date": ["Today's date is {date}.", "It's {date} today.", "Today is {date}."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm sorry, I don't understand.", "Could you please repeat that?", "I'm still learning!"],
}

# Function to get a response from the chatbot
def get_response(user_input, dataset):
    user_input = user_input.lower()
    for data in dataset:
        if data['question'].lower() == user_input:
            return data['answer']
    if user_input in responses:
        if user_input == "time":
            current_time = datetime.now().strftime("%I:%M:%S %p")
            return random.choice(responses[user_input]).format(time=current_time)
        elif user_input == "date":
            current_date = datetime.now().strftime("%Y-%m-%d")
            return random.choice(responses[user_input]).format(date=current_date)
        else:
            return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    dataset = load_dataset()
    user_input = request.form['user_input']
    response = get_response(user_input, dataset)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, render_template, request
# import csv
# import random
# from datetime import datetime
# import pyttsx3

# app = Flask(__name__)

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Load dataset from CSV file
# def load_dataset():
#     file_path = 'C:\\Users\\Kaivalya\\BG INTERN\\ChatBot\\dataset.csv'
#     dataset = []
#     with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             dataset.append({'question': row[0], 'answer': row[1]})
#     return dataset

# responses = {
#     "hi": ["Hello!", "Hi there!", "Hey!"],
#     "how are you": ["I'm good, thanks for asking!", "Feeling great!", "All good!"],
#     "time": ["The current time is {time}.", "It's {time} right now.", "Right now, it's {time}."],
#     "date": ["Today's date is {date}.", "It's {date} today.", "Today is {date}."],
#     "bye": ["Goodbye!", "See you later!", "Bye!"],
#     "default": ["I'm sorry, I don't understand.", "Could you please repeat that?", "I'm still learning!"],
# }

# # Function to get a response from the chatbot
# def get_response(user_input, dataset):
#     user_input = user_input.lower()
#     for data in dataset:
#         if data['question'].lower() == user_input:
#             return data['answer']
#     if user_input in responses:
#         if user_input == "time":
#             current_time = datetime.now().strftime("%I:%M:%S %p")
#             return random.choice(responses[user_input]).format(time=current_time)
#         elif user_input == "date":
#             current_date = datetime.now().strftime("%Y-%m-%d")
#             return random.choice(responses[user_input]).format(date=current_date)
#         else:
#             return random.choice(responses[user_input])
#     else:
#         return random.choice(responses["default"])

# # Function to speak the response using pyttsx3
# def speak_response(response):
#     engine.say(response)
#     engine.runAndWait()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     dataset = load_dataset()
#     user_input = request.form['user_input']
#     response = get_response(user_input, dataset)
#     speak_response(response)  # Speak the response
#     return {'response': response}

# if __name__ == '__main__':
#     app.run(debug=True)













# from flask import Flask, render_template, request, jsonify
# import csv
# import random
# from datetime import datetime
# import pyttsx3

# app = Flask(__name__)

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Load dataset from CSV file
# def load_dataset():
#     file_path = 'C:\\Users\\Kaivalya\\BG INTERN\\ChatBot\\dataset.csv'
#     dataset = []
#     with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             dataset.append({'question': row[0], 'answer': row[1]})
#     return dataset

# responses = {
#     "hi": ["Hello!", "Hi there!", "Hey!"],
#     "how are you": ["I'm good, thanks for asking!", "Feeling great!", "All good!"],
#     "time": ["The current time is {time}.", "It's {time} right now.", "Right now, it's {time}."],
#     "date": ["Today's date is {date}.", "It's {date} today.", "Today is {date}."],
#     "bye": ["Goodbye!", "See you later!", "Bye!"],
#     "default": ["I'm sorry, I don't understand.", "Could you please repeat that?", "I'm still learning!"],
# }

# # Function to get a response from the chatbot
# def get_response(user_input, dataset):
#     user_input = user_input.lower()
#     for data in dataset:
#         if data['question'].lower() == user_input:
#             return data['answer']
#     if user_input in responses:
#         if user_input == "time":
#             current_time = datetime.now().strftime("%I:%M:%S %p")
#             return random.choice(responses[user_input]).format(time=current_time)
#         elif user_input == "date":
#             current_date = datetime.now().strftime("%Y-%m-%d")
#             return random.choice(responses[user_input]).format(date=current_date)
#         else:
#             return random.choice(responses[user_input])
#     else:
#         return random.choice(responses["default"])

# # Function to speak the response using pyttsx3
# def speak_response(response):
#     engine.say(response)
#     engine.runAndWait()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     dataset = load_dataset()
#     user_input = request.form['user_input']
#     response = get_response(user_input, dataset)
#     speak_response(response)  # Speak the response
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)

