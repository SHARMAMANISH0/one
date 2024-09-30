from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my-page')
def my_page():
    return render_template('my_page1.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

