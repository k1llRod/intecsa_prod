from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit ='sale.order'

    # sale_order_count = fields.Integer(string='Pedidos de venta', compute='_compute_sale_order_count', store=True)
    a_area = fields.Char(string='Area', related='partner_id.a_area')