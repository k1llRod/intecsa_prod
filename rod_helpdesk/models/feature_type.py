from odoo import models, fields, api

class FeatureType(models.Model):
    _name = 'feature.type'
    _description = 'Tipo de caracteristica'

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripcion')
