from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# @app.route('/<username>')  # this is for the browser route
# def hello_world(username=None):
#     return render_template('index.html', name=username)  # render_template read html in the specific templates folder
# by using {{}} in html file, it is a flask variable, and by using <username> it is another flask variable

@app.route('/')
def my_home():
    return render_template('/index.html')


@app.route('/<string:page_name>')  # we can only have one route for the same name
def html_page(page_name):  # it will accept data in the url
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])  # methods are default, get means send to web, post means save
def submit_form():  # define an action for submit form in html
    if request.method == 'POST':  # grab the information in a dict
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'did not saved in database'
    else:
        return 'something went wrong, please try again'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a',encoding="utf-8") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # delimiter will separate and with quoting will quote those items with quote char
        csv_writer.writerow([email, subject, message])  # with writerow we give only variables we want as list


app.run(debug=True)  # with debug mode we can change realtime
