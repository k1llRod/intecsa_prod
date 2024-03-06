from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_register_payment(self):
        a = 1
        sale_id = self.env['sale.order'].search([('name','=',self.invoice_origin)])
        ''' Open the account.payment.register wizard to pay the selected journal entries.
        :return: An action opening the account.payment.register wizard.
        '''
        form =  {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'context': {
                'total_commission': self.commission_total,
                'sale_id': sale_id,
                'active_model': 'account.move',
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
        return form

