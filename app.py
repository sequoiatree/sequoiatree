import flask
import jinja2
import sys

from src.packages.chapter_parser import parse_chapters as pc
from src.packages.textbooks import textbooks as tb

SOURCE_CHAPTERS_PATH = './src/packages/textbooks/chapters'
TARGET_CHAPTERS_PATH = './static/chapters'

app = flask.Flask(__name__)

app.jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    # jinja2.FileSystemLoader([
    #     ?
    #     for chapter in pc.get_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, False),
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
            ('about', 'About / Contact', 'template', None),
            ('textbooks', 'Textbooks', 'template', tb.textbooks),
            ('pyagram', 'Pyagram', 'template', None),
            ('publications', 'Publications', 'template', None),
        ],
    )

if __name__ == '__main__':
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        lazy_parsing_arg = sys.argv[1]
        if lazy_parsing_arg == 'parse-new':
            lazy_parsing_enabled = True
        elif lazy_parsing_arg == 'parse-all':
            lazy_parsing_enabled = False
        else:
            assert False
        pc.parse_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, lazy_parsing_enabled)
    else:
        assert False
    app.run()
