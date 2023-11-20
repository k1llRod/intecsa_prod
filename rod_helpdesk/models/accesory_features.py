from odoo import models, fields, api

class AccesoryFeatures(models.Model):
    _name = 'accesory.features'
    _description = 'caracteristicas de los accesorios'

    # name = fields.Char(string='Descripcion')
    name = fields.Many2one('machine', string='Equipo')
    brand_id = fields.Many2one('brand', string='Marca')
    model_id = fields.Many2one('model.machine', string='Modelo')
    serial_number = fields.Char(string='Serial')
    # description = fields.Text(string='Descripcion de la caracteristica')
    # feature_type = fields.Many2one('feature.type', string='Tipo de caracteristica')
    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket')


