# -*- coding: utf-8 -*-
{
    'name': "quan_ly_du_an",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/du_an_cong_viec.xml',
        'views/du_an_quan_ly_nhan_su.xml',
        'views/du_an_quan_ly.xml',
        'views/du_an_rui_ro.xml',
        'views/du_an_tai_nguyen.xml',
        'views/du_an_tien_do.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}