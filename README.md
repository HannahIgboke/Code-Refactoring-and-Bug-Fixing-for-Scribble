# Code Refactoring and Bug Fixing for Scribble✍

<p align="center">
    <img width="300" src="https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Scribble.jpg" alt="Scribble">
</p>

## Background 📃

A team of enthusiastic data scientists identified a need to develop a personalized Note Taking Application called **Scribble**. To build this, they have to utilize Python, HTML and Flask framework to create the application server. While at the development stage, the team ran into some **challenges** with the backend which prevented it from being fully functional. Recognizing my proficiency in backend development, I have been tasked with fixing the broken code to ensure the application works seamlessly.

## How it is supposed to work

The Scribble application is such that the home route or page contains a text field and a button. And users can add a note, and all the notes will be displayed as an unordered list below the text field on the same page.


## Tech Stack used🛠

- Python
- Flask
- HTML

## Knowledge Check

The words 'GET' and 'POST' are used frequently in the course of this project. Here are what they mean:

GET - refers to requests used to retrieve data from a system. In this case, the GET request is expected to respond to the user who inputted the url by loading the note taking page

POST - refers to requests used to submit data to be processed, in this case - the notes/scribbles is the data, clicking in the add note button by the user initiates a POST request

You can find the comprehensive report of this project here.


# Workflow

## Create a virtual environment to install flask and activate the environment

First, using visual studio code, I created a virtual environment called '.env_flask_scribble' on which to install the flask framework. Thereafter, I activated the environment for use.
![virtual environmnet](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Virtual%20envrionment%20and%20activation.JPG)



## Install flask

The flask installation was successful.

![Installation](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Installed%20flask.JPG)


## Run the initial codebase

When I ran the code base a 405 error occured.

![Client error](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Client%20error.JPG)


## Issues/bugs 🐛 identified

1. Route method mismatch

