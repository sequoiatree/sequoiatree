import flask
import jinja2
import os
import sys

from src.packages.chapter_parser import parse_chapters as pc
from src.packages.books import books as bk

SOURCE_CHAPTERS_PATH = './src/packages/books/chapters'
TARGET_CHAPTERS_PATH = './static/chapters'

def rename(name):
    def rename_decorator(function):
        function.__name__ = name
        return function
    return rename_decorator

def parse_chapters():
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

def render_endpoints():
    render_root()
    for chapter in pc.get_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, False):
        render_chapter(chapter)

def render_root():
    @app.route('/')
    def root_renderer():
        return flask.render_template(
            'index.html',
            nav_options=[
                ('about', 'About / Contact', 'template', None),
                ('textbooks', 'Textbooks', 'template', bk.books),
                ('pyagram', 'Pyagram', 'template', None),
                ('publications', 'Publications', 'template', None),
            ],
        )

def render_chapter(chapter):
    @app.route(f'/{chapter.id}')
    @rename(f'chapter_renderer:{chapter.id}')
    def chapter_renderer():
        return flask.render_template(
            chapter.target_file_name,
        )

if __name__ == '__main__':
    parse_chapters()
    app = flask.Flask(__name__)
    app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([
            TARGET_CHAPTERS_PATH,
        ]),
    ])
    render_endpoints()
    app.run()
