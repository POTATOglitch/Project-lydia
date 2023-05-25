import time
import random
from tkinter import *
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3

# Initialize speech synthesis engine
engine = pyttsx3.init()

# Create a dictionary for storing knowledge
knowledge = {
    "variable": "a named storage location in a program that holds a value",
    "data type": "a classification of data that determines the operations that can be performed on it",
    "function": "a block of reusable code that performs a specific task",
    "argument": "a value passed to a function or method when it is called",
    "conditional statement": "a programming construct that executes different actions based on a condition",
    "loop": "a control flow statement that repeats a block of code until a certain condition is met",
    "list": "an ordered collection of items that can be of different data types",
    "string": "a sequence of characters",
    "integer": "a whole number without a fractional part",
    "float": "a number with a decimal point",
    "boolean": "a data type that represents either true or false",
    "dictionary": "an unordered collection of key-value pairs",
    "module": "a file containing Python definitions and statements",
    "class": "a blueprint for creating objects that define their properties and behaviors",
    "object": "an instance of a class that encapsulates data and methods",
    "attribute": "a value associated with an object, accessed using dot notation",
    "method": "a function that belongs to a class and operates on its objects",
    "inheritance": "a mechanism in which one class inherits properties and behaviors from another",
    "exception": "an event that occurs during the execution of a program, disrupting the normal flow",
    "try-except": "a block of code used to catch and handle exceptions",
    "file": "a named location on disk used to store related information",
    "input": "a function that prompts the user to enter data",
    "output": "the result or value produced by a program",
    "algorithm": "a step-by-step procedure for solving a problem",
    "debugging": "the process of identifying and fixing errors or defects in a program",
    "comment": "text that provides explanations or annotations in a program's source code",
    "syntax": "the set of rules that define the structure and organization of a programming language",
    "IDE": "Integrated Development Environment, a software application for coding and development",
    "say": "to speak or utter words",
    "hello": "a common greeting",
    "world": "the earth, together with all its countries and peoples",
    "import": "to bring in or introduce from one source to another",
    "os": "a module in Python providing functions for interacting with the operating system",
    "time": "a module in Python providing functions for working with time-related operations",
    "random": "a module in Python providing functions for generating random numbers and choices",
    "tkinter": "a standard Python library for creating GUI applications",
    "scrolledtext": "a module in tkinter for creating scrollable text areas",
    "speech_recognition": "a library in Python for performing speech recognition",
    "pyttsx3": "a library in Python for text-to-speech conversion",
    "dictionary": "a collection of words and their definitions",
    "knowledge": "information or understanding acquired through learning or experience",
    "function": "a named block of code that performs a specific task",
    "query": "a request for information or an action to be performed",
    "response": "a reply or answer to a query or request",
    "greeting": "a polite or friendly message to someone",
    "module": "a file containing Python definitions and statements",
    "operating system": "the software that manages computer hardware and software resources",
    "GUI": "Graphical User Interface, a visual way of interacting with computer programs",
    "library": "a collection of pre-written code that can be used by programmers",
    "text-to-speech": "the conversion of written text into spoken words",
    "speech recognition": "the technology that converts spoken language into written text",
    "loop": "a programming construct that repeats a set of instructions",
    "microphone": "an input device used to record sound",
    "phrases": "groups of words that express a single idea",
    "unknown value error": "an error that occurs when speech recognition cannot understand the input",
    "request error": "an error that occurs when there is a problem with the speech recognition service",
}


# Function to add knowledge
def learn():
    global knowledge
    query = input_textbox.get(1.0, END)
    query = query.strip().lower()
    if query:
        response = input('What should I say in response to "{}"? '.format(query))
        knowledge[query] = response
        input_textbox.delete(1.0, END)
        print('Learned: "{}" => "{}"\n'.format(query, response))

# Function to get a response
def respond(query):
    global knowledge
    response = knowledge.get(query.strip().lower(), None)
    if response:
        return response
    else:
        return None
        
# Function to process incoming audio
def process_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source, phrase_time_limit=5)
    try:
        query = r.recognize_google(audio)
        print('Heard: "{}"'.format(query))
        response = respond(query)
        if response:
            print('Saying:', response)
            engine.say(response)
            engine.runAndWait()
        else:
            print('Sorry, I do not know how to respond to "{}"'.format(query))
            engine.say('I am sorry, I do not know how to respond to that')
            engine.runAndWait()
    except sr.UnknownValueError:
        print('Sorry, could not understand what you said')
        engine.say('Sorry, could not understand what you said')
        engine.runAndWait()
    except sr.RequestError:
        print('Sorry, could not process your request')
        engine.say('Sorry, could not process your request')
        engine.runAndWait()

# Set up user interface using tkinter
root = Tk()
root.title('Lydia')
root.geometry('500x500')

# Create input textbox
input_label = Label(root, text='Enter your command:')
input_label.pack()
input_textbox = scrolledtext.ScrolledText(root, height=5, wrap=WORD)
input_textbox.pack()
input_textbox.focus()

# Create submit button
submit_button = Button(root, text='Submit', command=learn)
submit_button.pack()

# Start processing incoming audio
while True:
    process_audio()

root.mainloop()