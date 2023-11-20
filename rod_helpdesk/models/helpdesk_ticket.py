from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    accesory_features = fields.One2many('accesory.features', 'ticket_id', string='Caracteristicas del equipo')
    equipment_conditions = fields.Selection([('nuevo', 'Nuevo'), ('mediouso', 'A medio uso')], string='Condiciones del equipo')
    accesories_ids = fields.One2many('accesory.list', 'ticket_id', string='Accesorios')
    type_contract = fields.Selection([('contrato', 'Contrato'), ('eventual', 'Eventual')], string='Tipo de contrato')
    ribon = fields.Boolean(string='Cinta', related='stage_id.ribon')