from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for rec in self.sale_id.order_line:
            sum_total_cost = sum(self.move_line_ids_without_package.filtered(lambda x: x.product_id.id == rec.product_id.id).mapped('cost_product'))
            quant = len(self.move_line_ids_without_package.filtered(lambda x: x.product_id.id == rec.product_id.id))
            rec.purchase_price = sum_total_cost/quant
        return res


