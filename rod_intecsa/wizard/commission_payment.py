from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError

class CommissionPayment(models.TransientModel):
    _name = 'wizard.commission.payment'
    _description = 'Commission Payment'

    name = fields.Char(string='Name', default='New')
    total_commission = fields.Float(string='Total Commission', digits=(16, 2))
    user_id = fields.Many2one('res.users', string='Partner')
    seller_ids = fields.Many2many('seller.commission', string='Seller')

    def action_payment(self):
        self.ensure_one()
        for rec in self.seller_ids:
            rec.state = 'done'
        pay_commission = self.env['commission.payment'].create({
            'name': self.name,
            'total_commission': self.total_commission,
            'user_id': self.user_id.id,
            'state': 'done',
        })

