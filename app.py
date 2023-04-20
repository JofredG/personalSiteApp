from distutils.file_util import write_file
from flask import Flask, render_template, request


app = Flask(__name__)
#app.config["TEMPLATES_AUTO_RELOAD"] = True # reloads the app without having to restart it

def readDetails(filename):
   with open(filename, 'r') as f:
      return [line for line in f]


@app.route("/")
def homePage():
   name = 'Jofred\'s Site'
   #details = ['This is my name', 'I am from earth'] #<- instead of this we'll use a function
   details = readDetails('static/details.txt')
   return render_template('base.html', name=name, aboutMe=details)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
   quote = None
   if request.method == 'POST':
      quote = request.form['nm']
   #ends with the above at 36:35 on panopto
   # if request.form['message']:
   #    write_file('Wk10\personalSiteApp\static\quotes.txt', request.form['quote'])

   return render_template('form.html', quote=quote)



if __name__ == "main":
    app.run(debug = True)

## Test Comment