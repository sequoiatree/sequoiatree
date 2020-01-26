import os

from . import chapter
from . import utils

def parse_chapters(source_chapters_path, target_chapters_path, lazy_parsing_enabled):
    if not lazy_parsing_enabled:
        utils.clear_dir(target_chapters_path)
    chapters_to_parse = get_chapters(source_chapters_path, target_chapters_path, lazy_parsing_enabled)
    for chapter_to_parse in chapters_to_parse:
        chapter_to_parse.parse()

def get_chapters(source_chapters_path, target_chapters_path, only_new_chapters):
    source_chapter_names = os.listdir(source_chapters_path)
    parsed_chapter_names = os.listdir(target_chapters_path)
    chapters = {
        chapter.Chapter(
            source_chapter_name,
            source_chapters_path,
            target_chapters_path,
        )
        for source_chapter_name in source_chapter_names
    }
    for chapter_obj in chapters:
        if only_new_chapters and chapter_obj.target_file_name in parsed_chapter_names:
            chapters.remove(chapter_obj)
    return chapters
