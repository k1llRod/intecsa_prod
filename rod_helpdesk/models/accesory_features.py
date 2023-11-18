from odoo import models, fields, api

class AccesoryFeatures(models.Model):
    _name = 'accesory.features'
    _description = 'caracteristicas de los accesorios'

    name = fields.Char(string='Codigo')
    description = fields.Text(string='Descripcion de la caracteristica')
    feature_type = fields.Many2one('feature.type', string='Tipo de caracteristica')
    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket')


