import os
import sys

from . import chapter
from . import utils

if __name__ == '__main__':
    assert len(sys.argv) == 4
    source_chapters_path = sys.argv[1]
    target_chapters_path = sys.argv[2]
    lazy_parsing_enabled = bool(sys.argv[3])

    if not lazy_parsing_enabled:
        utils.clear_dir(target_chapters_path)

    chapter_dir_names = os.listdir(source_chapters_path)
    parsed_chapter_dir_names = os.listdir(target_chapters_path)
    for chapter_dir_name in chapter_dir_names:
        if chapter_dir_name not in parsed_chapter_dir_names:
            chapter.Chapter(
                source_chapters_path,
                target_chapters_path,
                chapter_dir_name,
            ).parse()
