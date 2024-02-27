from odoo import _, api, fields, models

class SellerCommission(models.Model):
    _name = 'seller.commission'

    agent_id = fields.Many2one('res.partner', string='Agent')
    sale_id = fields.Many2one('sale.order', string='Sale Order')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    total = fields.Float(string='Total')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], string='State')

    def action_confirm(self):
        self.state = 'done'
