from odoo import models, fields, api

class StockMove(models.Model):
    _inherit ='stock.move'

    cost_product = fields.Float(string='Costo del producto', compute='_compute_cost_product', store=True)
    # total_price_unit = fields.Float(string='Total', compute='_compute_total_price_unit', store=True)
    def _compute_cost_product(self):
        a = 1
        # for rec in self:
        #     rec.cost_product = rec.product_id.price_unit

    # def action_show_details(self):
        res = super(StockMove, self).action_show_details()

        return res