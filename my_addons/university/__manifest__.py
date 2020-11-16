# -*- coding: utf-8 -*-

{
    'name': "university",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Mangement',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail',
                'base_setup',
                'resource',
                'web',
                'mail_bot' ],

    # always loaded
    'data': [
        'views/student_views.xml',
        'views/professor_views.xml',
        'views/classroom_views.xml',
        'views/subject_views.xml',
        'views/department_views.xml',
        'views/contact_views.xml',
        'views/section_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
