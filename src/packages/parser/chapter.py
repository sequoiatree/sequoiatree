import os

from . import io

TITLE_FILE_NAME = 'title.txt'
CONTENT_FILE_NAME = 'content.md'

class Chapter:
    """
    """

    def __init__(self, source_chapters_path, target_chapters_path, chapter_dir_name):
        self.id = chapter_dir_name
        self.source_path = os.path.join(source_chapters_path, chapter_dir_name)
        self.target_path = os.path.join(target_chapters_path, chapter_dir_name)

    @property
    def title(self):
        title_path = os.path.join(self.source_path, TITLE_FILE_NAME)
        return io.read(title_path)

    @property
    def content(self):
        content_path = os.path.join(self.source_path, CONTENT_FILE_NAME)
        return io.read(content_path)

    def parse(self):
        # os.mkdir(self.target_path)
        pass # TODO
