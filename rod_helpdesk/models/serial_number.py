from odoo import models, fields, api

class SerialNumber(models.Model):
    _name ='serial.number'

    name = fields.Char(string='Numero de serie')
