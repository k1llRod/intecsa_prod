from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    total_commission = fields.Float(string='Total Commission', digits=(16, 2))
    sale_id = fields.Char(string='Sale Order')
    # def _create_payments(self):
    #     res = super(AccountPaymentRegister, self)._create_payment()
    #     return res
    def action_create_payments(self):
        sale = self.env['sale.order'].search([('name', '=', self.sale_id)])
        res = super(AccountPaymentRegister, self).action_create_payments()
        if res:
            create_payment = self.env['seller.commission'].create({
                'agent_id': sale.user_id.id,
                'sale_id': sale.id,
                'amount_untaxed': sale.amount_untaxed,
                'amount_tax': sale.amount_tax,
                'amount_total': sale.amount_total,
                'discount_total': sale.discount_total,
                'total': self.total_commission,
                'date_from': datetime.today(),
                'state': 'draft',
            })
        return res

    @api.model
    def default_get(self, fields_list):
        res = super(AccountPaymentRegister, self).default_get(fields_list)
        if self._context.get('active_model') == 'account.move':
            active_id = self._context.get('active_id')
            move = self.env['account.move'].browse(active_id)
            res['total_commission'] = move.commission_total
            res['sale_id'] = move.invoice_origin
        return res

    # @api.onchange('amount')
    # def _total_commission(self):
    #     for rec in self:
    #         id = self._context.get('active_ids', [])[0]
    #         # sale_id = self.env['sale.order'].search([('ids', '=', self._context.get('active_ids', [])[0])])
    #         rec.total_commission = 10



