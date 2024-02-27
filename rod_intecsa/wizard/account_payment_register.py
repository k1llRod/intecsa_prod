from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    total_commission = fields.Float(string='Total Commission', digits=(16, 2))
    # def _create_payments(self):
    #     res = super(AccountPaymentRegister, self)._create_payment()
    #     return res
    def action_create_payments(self):
        res = super(AccountPaymentRegister, self).action_create_payments()
        if res:
            for payment in res:
                payment.move_id.commission_total = payment.move_id.sale_id.commission_total
        return res

    @api.onchange('amount')
    def _total_commission(self):
        for rec in self:
            id = self._context.get('active_ids', [])[0]
            sale_id = self.env['sale.order'].search([('ids', '=', self._context.get('active_ids', [])[0])])
            rec.total_commission = 10



