from . import handbook
from . import textbook

books = {
    'textbooks': [
        textbook.Textbook(
            'Fundamental Computer Science',
            {
                'Part I: Lorem Ipsum': [
                    'welcome-to-computer-science',
                    'setup',
                ],
                'Part II: Dolor Sit Amet': [
                    'variables',
                    'functions',
                    'booleans',
                    'iteration',
                    'higher-order-functions',
                    'lambda-functions',
                    'recursion',
                    'counting-problems',
                    'objects',
                    'orders-of-growth',
                    'iterators-and-generators',
                    'scheme',
                ],
            },
        ),
        textbook.Textbook(
            'Relational Databases',
            {
                'Part I: Lorem Ipsum': [
                    'sql:-data-manipulation',
                ],
            },
        ),
    ],
    'handbooks': [
        handbook.Handbook(
            'Lorem Ipsum',
            [
                'welcome-to-computer-science',
            ],
        ),
    ],
}
