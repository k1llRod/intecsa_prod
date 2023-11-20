from odoo import models, fields, api

class Model(models.Model):
    _name = 'model.machine'

    name = fields.Char(string='Modelo')
