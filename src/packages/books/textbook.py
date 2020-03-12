from . import utils

class Textbook:
    """
    """

    def __init__(self, title, parts):
        self.title = title
        self.parts = parts
    
    def __iter__(self):
        """
        summary # [id, title, encoding, context] as used in utils.html's decode_content

        :return:
        """
        return iter((
            utils.kebab_case(self.title),
            self.title,
            'textbook',
            self.parts,
        ))
