from odoo import models, fields, api, _

class ResPartnerCategory(models.Model):
    _inherit ='res.partner.category'

    class_partner = fields.Selection([('class_a', 'Clase A'),
                             ('class_b1', 'Clase B1'),
                             ('class_b2', 'Clase B2'),
                             ('class_b3', 'Clase B3')],string='Clase de contacto')

