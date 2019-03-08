from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Valentina Sánchez',
        'title': 'First dummy post',
        'content': 'Content for the first post.',
        'date_posted': 'Mar 7, 2019'
    },
    {
        'author': 'Paulina Sánchez',
        'title': 'Second dummy post',
        'content': 'Content for the second post.',
        'date_posted': 'Mar 8, 2019'
    }
]

@app.route("/")
@app.route("/Home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
