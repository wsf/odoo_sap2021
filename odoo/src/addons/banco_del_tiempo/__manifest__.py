# -*- coding: utf-8 -*-
{
    'name': "bancodeltiempo",  # Module title
    'summary': "Gestion de prestamos de tiempo para voluntarios",  # Module subtitle phrase
    'description': """
El Banco del tiempo
==============
Modulo para la gestion de prestamos de tiempo voluntario
    """,  # Supports reStructuredText(RST) format
    'author': "GBT",
    'website': "http://www.example.com",
    'category': 'Test',
    'version': '14.0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not used in this example)
    # 'demo': [
    #     'data/demo.xml'
    # ],
    'instalable': True,
    'application': True
}
