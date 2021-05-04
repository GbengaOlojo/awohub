from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Oluwo Fayemi',
        'title': 'Ifa Topics',
        'content': 'What is Ifa',
        'date_posted': 'May 4, 2021'
    },

        {
        'author': 'Oluwo Faniyi',
        'title': 'Spirituality',
        'content': 'Talking Spirituality',
        'date_posted': 'May 7, 2021'
    },

]

@app.route('/')
@app.route('/home')
def home():
    return  render_template('home.html', posts=posts)



@app.route('/about/')
def about():
    return  render_template('about.html', title='About')



if __name__ == '__name__':
    app.run(debug=True)