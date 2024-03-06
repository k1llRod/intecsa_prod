from odoo import _, api, fields, models
from odoo.exceptions import UserError
class SellerCommission(models.Model):
    _name = 'seller.commission'

    agent_id = fields.Many2one('res.users', string='Agent')
    sale_id = fields.Many2one('sale.order', string='Sale Order')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    total = fields.Float(string='Total')
    commission_id = fields.Many2one('commission.payment', string='Commission')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], string='State')
    def action_confirm(self):
        sum_commission = 0
        seller_ids = []
        agent = self.agent_id[0]
        for rec in self:
            if agent.id == rec.agent_id.id:
                sum_commission = sum_commission + rec.total
                seller_ids.append(rec.id)
            else:
                raise UserError(_('No puede liquidar a dos agentes diferentes'))
        return {
            'name': 'Liquidar Comisión',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.commission.payment',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_user_id': agent.id,
                'default_total_commission': sum_commission,
                'default_seller_ids': seller_ids,
            }
        }
