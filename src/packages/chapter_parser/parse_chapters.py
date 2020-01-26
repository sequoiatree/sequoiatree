import os

from . import chapter
from . import utils

def parse_chapters(source_chapters_path, target_chapters_path, lazy_parsing_enabled):
    if not lazy_parsing_enabled:
        utils.clear_dir(target_chapters_path)
    chapters_to_parse = get_new_chapters(source_chapters_path, target_chapters_path)
    for chapter_to_parse in chapters_to_parse:
        chapter_to_parse.parse()

def get_new_chapters(source_chapters_path, target_chapters_path):
    new_chapters = set()
    chapter_dir_names = os.listdir(source_chapters_path)
    parsed_chapter_dir_names = os.listdir(target_chapters_path)
    for chapter_dir_name in chapter_dir_names:
        if not chapter_dir_name in parsed_chapter_dir_names:
            new_chapters.add(chapter.Chapter(
                source_chapters_path,
                target_chapters_path,
                chapter_dir_name,
            ))
    return new_chapters
