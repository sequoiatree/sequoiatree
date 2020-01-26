from . import handbook
from . import textbook

books = {
    'textbooks': [
        textbook.Textbook(
            'Fundamental Computer Science',
            {
                'name of part one': [
                    'welcome-to-computer-science',
                    'the-terminal',
                ],
                'name of part two': [
                    'the-terminal',
                ],
            },
        ),
        textbook.Textbook(
            'A Fake Textbook',
            {
                'name of this part one': [
                    'the-terminal',
                ],
                'name of this part two': [
                    'welcome-to-computer-science',
                    'the-terminal',
                ],
            },
        ),
    ],
    'handbooks': [
        handbook.Handbook(
            'A Fake Handbook',
            [
                'the-terminal',
                'welcome-to-computer-science',
                'the-terminal',
            ],
        ),
    ],
}
