from flask import Flask
#web "micro" framework for building web applications using Python
from flask import jsonify, render_template


#creating an instance of Flask called:
app = Flask(__name__)
#named after my package(__name__)

#Flask uses a routing system to map URLs to specific view functions
#which generate the HTTP response
#Routing is done using decorators:
@app.route('/')
def home():
    return jsonify({'message': "Hello, world!"})
#defined the root of the URL"/"
#home function is the view function associated with the route
#when a user visits the root URL, this function is executed

#jsonify returns a JSON response
#jsonify converts the Python dict into a JSON response object

#defined another route to hold an about section
@app.route('/about')
def about():
    #imported render_template, which is a function provided by Flask
    #which allows the user to render HTML templates
    #and pass data to them for dynamic content generation:
    return render_template('about.html')
    #the function takes the name of the template file ('about.html')
    #and returns the rendered HTML content
    #it automatically looks for template files in a directory named:
    #"templates" located in the root dir of the Flask app


if __name__ == '__main__':
    app.run()
