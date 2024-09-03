from flask import Flask, request, make_response, render_template,jsonify
from flask_ckeditor import CKEditor
from helper import save_file_to_local
from git_setup import check_git, commit_changes
import os

app = Flask(__name__)
ckeditor = CKEditor(app)

app.config.from_pyfile('settings.py')
repo_path = os.getcwd()  

commit_message = 'Added notes'

@app.route("/")
def home():
    response = make_response({"success": "true", "message": "Base URL"})
    response.status_code = 200
    return response

@app.route("/create", methods=['GET', 'POST'])
def createNote():
    if request.method == 'POST':
        data = request.form.get('ckeditor')
        print(data)
        if data:
            save_file_to_local(data)
            repo = check_git(repo_path)
            commit_changes(repo, commit_message)
        
            

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
