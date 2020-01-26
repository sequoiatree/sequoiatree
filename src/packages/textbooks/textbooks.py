from . import textbook

textbooks = [
    textbook.Textbook(
        'Fundamental Computer Science',
        {
            'name of part one': [
                'welcome',
                'terminal',
            ],
            'name of part two': [
                'terminal',
            ],
        },
    ),
    textbook.Textbook(
        'A Fake Textbook',
        {
            'name of this part one': [
                'terminal',
            ],
            'name of this part two': [
                'welcome',
                'terminal',
            ],
        },
    ),
]
