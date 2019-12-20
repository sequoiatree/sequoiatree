import flask

# from src.packages.todo import todo as todo

app = flask.Flask(__name__)

@app.route('/')
def root():
    return flask.render_template('index.html')

# TODO: Use bash scripts in package.json to build a chapter / all chapters?

if __name__ == '__main__':
    app.run()
