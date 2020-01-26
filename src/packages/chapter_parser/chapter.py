import os
import re

from . import postprocess
from . import preprocess
from . import utils

SOURCE_EXT = 'md'
TARGET_EXT = 'html'

class Chapter:
    """
    """

    def __init__(self, source_chapter_name, source_chapters_path, target_chapters_path):
        match = re.fullmatch(rf'(.+)\.{SOURCE_EXT}', source_chapter_name)
        self.title = match[1]
        self.id = utils.kebab_case(self.title)
        self.source_path = os.path.join(source_chapters_path, self.source_file_name)
        self.target_path = os.path.join(target_chapters_path, self.target_file_name)

    @property
    def source_file_name(self):
        return f'{self.title}.{SOURCE_EXT}'

    @property
    def target_file_name(self):
        return f'{self.id}.{TARGET_EXT}'

    def parse(self):
        content = utils.read(self.source_path)
        content = preprocess.preprocess(content)
        # content = convert md to html # TODO
        content = postprocess.postprocess(content)
        utils.write(self.target_path, content)
