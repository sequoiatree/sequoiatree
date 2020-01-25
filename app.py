import flask
import jinja2

from src.packages.parser import parse as ps

# SOURCE_CHAPTERS_PATH = './src/chapters'
# TARGET_CHAPTERS_PATH = './static/chapters'

app = flask.Flask(__name__)

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    # jinja2.FileSystemLoader([
    #     ?
    #     for chapter in ps.get_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, False),
    # ]),
])

# TODO: Figure out how to get a set of Chapter objects from the parser package into this file.

# TODO: Typora -> Markdown -> Jinja {% extends 'chapter.html' %} -> HTML
# Typora (./src/chapters/{chapter id}/content.md)                                   \
# Markdown (RAM)                                                                    | This packagae
# Jinja {% extends 'chapter.html' %} (./static/chapters/{chapter id}/content.html) /
# HTML (./build)                                                                   <- FrozenFlask

@app.route('/')
def root():
    return flask.render_template(
        'index.html',
        nav_options=[
            ('about', 'About / Contact', None),
            ('textbooks', 'Textbooks', None),
            ('pyagram', 'Pyagram', None),
            ('publications', 'Publications', None),
        ],
    )

if __name__ == '__main__':
    app.run()
