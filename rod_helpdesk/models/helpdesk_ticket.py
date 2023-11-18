from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    accesory_features = fields.One2many('accesory.features', 'ticket_id', string='Caracteristicas de los accesorios')