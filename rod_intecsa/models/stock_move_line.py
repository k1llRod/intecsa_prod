from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit ='stock.move.line'

    cost_product = fields.Float(string='Costo del productos', compute='_compute_cost_product', store=True)
    @api.depends('lot_id')
    def _compute_cost_product(self):
        for record in self:
            for r in record.lot_id.purchase_order_ids.picking_ids.move_lines:
                if r.lot_ids.filtered(lambda x: x.name == record.lot_id.name):
                    record.cost_product = r.price_unit
            # try:
            #     record.cost_product = record.lot_id.purchase_order_ids.picking_ids.move_ids_without_package.price_unit
            # except:
            #     record.cost_product = 0
        # for line in self:
        #     line.cost_product = line.product_id.cost_price