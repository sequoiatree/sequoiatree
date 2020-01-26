import os

from . import postprocess
from . import preprocess
from . import utils

TITLE_FILE_NAME = 'title'
CONTENT_FILE_NAME = 'content'

TITLE_FILE_EXT = 'txt'

class Chapter:
    """
    """

    def __init__(self, source_chapters_path, target_chapters_path, chapter_dir_name):
        self.id = chapter_dir_name
        self.source_path = os.path.join(source_chapters_path, chapter_dir_name)
        self.target_path = os.path.join(target_chapters_path, chapter_dir_name)

    def resource_path(self, dir_type, resource_name, resource_ext=None):
        if dir_type == 'source':
            dir_path = self.source_path
            default_ext = 'md'
        elif dir_type == 'target':
            dir_path = self.target_path
            default_ext = 'html'
        else:
            assert False
        if resource_ext is None:
            resource_ext = default_ext
        return os.path.join(dir_path, f'{resource_name}.{resource_ext}')

    def parse(self):
        os.mkdir(self.target_path)
        source_title_path = self.resource_path('source', TITLE_FILE_NAME, TITLE_FILE_EXT)
        target_title_path = self.resource_path('target', TITLE_FILE_NAME, TITLE_FILE_EXT)
        source_content_path = self.resource_path('source', CONTENT_FILE_NAME)
        target_content_path = self.resource_path('target', CONTENT_FILE_NAME)
        utils.copy(source_title_path, target_title_path)
        content = utils.read(source_content_path)
        content = preprocess.preprocess(content)
        # content = convert md to html # TODO
        content = postprocess.postprocess(content)
        utils.write(target_content_path, content)
