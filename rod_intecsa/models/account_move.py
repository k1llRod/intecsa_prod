from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_register_payment(self):
        a = 1
        ''' Open the account.payment.register wizard to pay the selected journal entries.
        :return: An action opening the account.payment.register wizard.
        '''
        form =  {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'context': {
                'active_model': 'account.move',
                'active_ids': self.ids,
                'total_commission': self.commission_total,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
        return form

