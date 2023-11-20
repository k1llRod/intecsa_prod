from odoo import models, fields, api

class Accesories(models.Model):
    _name = 'accesories'

    name = fields.Char(string='Accesorio')
