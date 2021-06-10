# -*- coding: utf-8 -*-
{
    'name': "mylibrary",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': "Supports reStructuredText(RST) format",
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],

    'instalable': True,
    'application': True


    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
