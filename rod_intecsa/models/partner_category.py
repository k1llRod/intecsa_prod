from odoo import models, fields, api, _

class PartnerCategory(models.Model):
    name ='partner.category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    type = fields.Selection([('class_a', 'Clase A'),
                             ('class_b1', 'Clase B1'),
                             ('class_b2', 'Clase B2'),
                             ('class_b3', 'Clase B3')], string='Tipo de Cliente')
