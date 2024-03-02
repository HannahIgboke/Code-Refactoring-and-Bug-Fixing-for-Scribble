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

The words 'GET' and 'POST' are used frequently in the course of this project. Here is what they mean:

**GET** refers to requests used to retrieve data from a system. In this case, the GET request is expected to respond to the user who inputted the URL by loading the note-taking page.

**POST** refers to requests used to submit data to be processed; in this case, the notes or scribbles are the data. Clicking on the add note button by the user initiates a POST request.

You can find the comprehensive report of this project here.

## Objectives

The objectives for this project are twofold, namely:
 
- To refactor the existing codebase and ensure the proper functioning of the note-taking application,

- Document all identified bugs during the debugging process.


# Workflow🤹‍♀️

## Create a virtual environment to install flask and activate the environment

First, using Visual Studio code, I created a virtual environment called '.env_flask_scribble' on which to install the flask framework. Thereafter, I activated the environment for use.

![virtual environmnet](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Virtual%20envrionment%20and%20activation.JPG)



## Install flask

The flask installation was successful.

![Installation](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Installed%20flask.JPG)


## Run the initial codebase

When I ran the codebase a 405 error occured.

![Client error](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Client%20error.JPG)


## Issues/bugs 🐛 identified

1. Route method mismatch

The route in the Python code is setup to only handle POST requests. Also, based on the app's functionality, we need to first be able to access the page (i.e., get data from it), but the ‘GET’ method has not been defined here. This leads to the method error when the app is run.

![Bug 1 - python](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%201%20-%20python.JPG)


On the other hand, the HTML code contains no corresponding method, which sets it to the default method of ‘GET’, resulting in the data not being sent to the server correctly.

![Bug 1 - html](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%201%20-%20html.JPG)


### Bug fix

The 'POST' method is included in the HTML code, 

![Bug fix - html](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%203.JPG)


And the 'GET' method is included as well in the Python code. This resolves the 405 error.

![Bug fix - python](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%20fix%201%20-%20python.JPG)


2. Data retrieval issues

Now that we have the Python code and the HTML files communicating properly, we have another issue: data retrieval.

Here, after entering a note, the user cannot see his or her notes as the application is expected to work, instead we see ‘None’.

![2nd error](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/2nd%20error.JPG)

### Bug fix

The issue here is that the Python code cannot correctly retrieve the notes already submitted via the form. This is because the note variable is stored using `request.args.get("note")`, which matches a GET request. We ought to use `request.form.get()` for POST requests, as form data is usually accessed this way to match the POST request in the HTML code.

Previous code:

![Bug 2](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%202%20-%20python.JPG)


Corrected code:

![Bug fix 2](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%20fix%202.JPG)


3. No action is specified

In this application, the form is intended to submit the data to the root URL (‘/’) when the user adds a new note. Since it wasn’t stated in the action attribute, the form data was not sent to the correct route (which is the homepage, so they could see previous notes they had made) for processing, and since it wasn't processed, we ended up with ‘None’ instead of the notes we entered.

![Bug 3](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%203.JPG)

### Bug fix

![Bug fix](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Bug%20fix%203.JPG)


All bugs are fixed ✅.


## Add-ons

I added some features that extend the functionality of the Scribble app, namely:

- Users can edit already-created notes.

- The ‘Enter note’ field is wider to enable users to have an enhanced view of their notes as they type.


## Final output

![Final output](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Final%20output.JPG)


## Conclusion

![Conclusion](https://github.com/HannahIgboke/Code-Refactoring-and-Bug-Fixing-for-Scribble/blob/main/Files/Images/Conclusion.jpg)

This project uses HTTP request methods to connect to data sources like APIs or web servers, enabling data retrieval, submission, and updating. These interactions are essential for data collection, preprocessing, and analysis workflows in data science.

By refactoring the flask route, I was able to resolve the mismatch in the route methods used, include the GET method to allow us access the page, specify the needed action in the html file, and handle the data retrieval issues. The app now functions as intended. The app's features were also extended for an improved user experience.

