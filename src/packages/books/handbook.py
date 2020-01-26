from . import utils

class Handbook:
    """
    """

    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters
    
    def __iter__(self):
        """
        summary # [id, title, encoding, context] as used in utils.html's decode_content

        :return:
        """
        return iter((
            utils.kebab_case(self.title),
            self.title,
            'handbook',
            self.chapters,
        ))
