from flask import Flask, render_template, request, redirect, url_for

#########################################
# creating a flask application instance
app = Flask(__name__)

# intializing an empty list to store notes
notes = []   

#########################################
# route number one
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        note = request.form.get("note")     # get the note from the user
        notes.append(note) # add the note to the list
        return redirect(url_for('index')) # to redirect the user back to the home page
    return render_template("home.html", notes=enumerate(notes)) # if the GET request has been received, that is the page has loaded, render the home page template

#########################################
# route number two
@app.route('/edit/<int:note_index>', methods = ['GET', 'POST'])
def edit(note_index):
    try:
        note_to_edit = notes[note_index]
    except IndexError:
        return "Invalid note index. Please go back and try again."

    if request.method == 'POST':
        edited_note = request.form.get('edited_note') # get the edited note from the form
        notes[note_index] = edited_note     # update the note in the list
        return redirect(url_for('index'))   #redirects the user back to the home page
        
    return render_template('edit_note.html', note_index=note_index, note_to_edit=note_to_edit)
 
#########################################
# to start the flask development server
if __name__ == '__main__':
    app.run(debug=True)