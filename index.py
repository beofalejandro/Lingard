from flask import Flask as fk, render_template as rt
from pytube import YouTube # Soon proyect

# Method to pytube library dowloader
# def downloader:

# Start Flask
app = fk(__name__)

# Create a route for create url - its important to create more pages
@app.route('/')
# Insert content to index
def index():
    return rt('index.html')

@app.route('/about') # Remember do this because home is already use
def about():
    return rt('about.html')

# Start the app
if __name__ == '__main__':
    app.run(debug=True)