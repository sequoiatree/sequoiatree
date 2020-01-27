import flask
import flask_frozen
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

def render_endpoints():
    chapters, chapter_titles = pc.get_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, False)
    render_root(chapter_titles)
    render_page_not_found()
    for chapter in chapters:
        render_chapter(chapter)

def render_root(chapter_titles):
    @app.route('/')
    def root():
        return flask.render_template(
            'index.html',
            nav_options=[
                ('about', 'About / Contact', 'template', None),
                ('textbooks', 'Textbooks', 'template', bk.books),
                ('pyagram', 'Pyagram', 'template', None),
                ('publications', 'Publications', 'template', None),
            ],
            chapter_titles=chapter_titles,
        )

def render_page_not_found():
    @app.errorhandler(404)
    def page_not_found(exception):
        return flask.redirect(flask.url_for('root'))

def render_chapter(chapter_obj):
    @app.route(f'/{chapter_obj.target_file_name}')
    @rename(f'chapter:{chapter_obj.id}')
    def chapter():
        return flask.render_template(chapter_obj.target_file_name)

if __name__ == '__main__':
    app = flask.Flask(__name__)
    app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([
            TARGET_CHAPTERS_PATH,
        ]),
    ])
    freeze_app = False
    run_app = True
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'build':
            freeze_app = True
            run_app = False
        elif sys.argv[1] == 'parse-new':
            pc.parse_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, True)
        elif sys.argv[1] == 'parse-all':
            pc.parse_chapters(SOURCE_CHAPTERS_PATH, TARGET_CHAPTERS_PATH, False)
        else:
            assert False
    else:
        assert False
    render_endpoints()
    if freeze_app:
        freezer = flask_frozen.Freezer(app)
        freezer.freeze()
    if run_app:
        app.run()
