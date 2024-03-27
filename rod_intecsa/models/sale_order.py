from odoo import models, fields, api, _
from datetime import datetime

class SaleOrder(models.Model):
    _inherit ='sale.order'

    # sale_order_count = fields.Integer(string='Pedidos de venta', compute='_compute_sale_order_count', store=True)
    a_area = fields.Char(string='Area', related='partner_id.a_area')
    payment_comision = fields.Boolean(string='Pago de comisión', default=False)

    def action_create_payment(self):
        for rec in self:
            rec.payment_comision = True
            create_payment = self.env['seller.commission'].create({
                'agent_id': rec.user_id.id,
                'sale_id': rec.id,
                'amount_untaxed': rec.amount_untaxed,
                'amount_tax': rec.amount_tax,
                'amount_total': rec.amount_total,
                'discount_total': rec.discount_total,
                'total': self.commission_total,
                'date_from': datetime.today(),
                'state': 'draft',
            })