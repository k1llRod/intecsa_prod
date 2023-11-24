# -*- coding: utf-8 -*-
{
    'name': "rod_intecsa",

    'summary': """
        Adaptaciones para Intecsa""",

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
    'depends': ['base','contacts','sale','sale_management','base_vat','bi_professional_reports_templates','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/custom_channels.xml',
        'views/res_partner.xml',
        'views/res_partner_category.xml',
        'views/res_users.xml',
        'views/sale_order.xml',
        'views/stock_move.xml',
        'views/stock_move_line.xml',
        'views/stock_quant.xml',
        'views/stock_picking.xml',
        'report/report.xml',
        'report/report_sale_order_other.xml',
        'wizard/reassing_customer.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
}
