from odoo import models, fields, api

class Brand(models.Model):
    _name = 'brand'

    name = fields.Char(string='Marca')
