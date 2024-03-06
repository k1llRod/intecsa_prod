from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError

class CommissionPayment(models.Model):
    _name = 'commission.payment'

    name = fields.Char(string='Name', default='New')
    total_commission = fields.Float(string='Total Commission', digits=(16, 2))
    user_id = fields.Many2one('res.users', string='Agent')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], string='State', default='draft')
    seller_ids = fields.One2many('seller.commission', 'commission_id', string='Comisiones')

    def action_payment(self):
        self.ensure_one()
        return {
            'name': 'Liquidar Comisión',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.commission.payment',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_user_id': self.agent_id.id,
                'default_total_commission': self.total_commission,
            },
        }
