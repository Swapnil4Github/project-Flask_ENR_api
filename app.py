# packages required for the project
from flask import Flask, jsonify
import spacy
from spacy import displacy
import wikipedia


nlp = spacy.load('en_core_web_lg')

app = Flask(__name__)

@app.route('/<user_input>')
def mmain(user_input):
    raw_text = user_input.replace(" ", "_")
    complete_content = wikipedia.summary(raw_text)
    docx = nlp(complete_content)
    d = displacy.render(docx,style="ent")
    return {"html_data" : d}

if __name__ == "__main__":
    app.run(debug=True)
