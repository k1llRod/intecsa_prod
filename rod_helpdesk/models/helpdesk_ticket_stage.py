from odoo import fields, models

class HelpdeskTicketStage(models.Model):
    _inherit = 'helpdesk.ticket.stage'

    ribon = fields.Boolean(string='Cinta')