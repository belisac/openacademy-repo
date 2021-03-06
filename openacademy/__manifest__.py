# -*- coding: utf-8 -*-
{
    'name': "Open Academy",
    'summary': "Manage Trainings",
    'description': """Open Academy module for managing trainings""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/
    # base/data/ir_module_category_data.xml  for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml'
        'views/openacademy.xml',
        'views/templates.xml',
        'views/partner.xml',
        'reports.xml',
        'views/session_board.xml'
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml', ],
    'application': True,
    'installable': True,
}
