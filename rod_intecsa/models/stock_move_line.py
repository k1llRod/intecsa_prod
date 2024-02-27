from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit ='stock.move.line'

    def create(self, vals_list):
        res = super(StockMoveLine, self).create(vals_list)
        for rec in res:
            stock_quant = rec.env['stock.quant'].search([('lot_id','=',rec.lot_id.id)])
            for record in stock_quant:
                if record.cost_product > 0:
                    rec.cost_product = record.cost_product
        return res
    cost_product = fields.Float(string='Costo del producto', store=True)
    # @api.onchange('lot_id')
    # def _compute_cost_product(self):
    #     for rec in self:
    #         stock_quant = rec.env['stock.quant'].search([('lot_id','=',rec.lot_id.id)])
    #         for record in stock_quant:
    #             if record.cost_product > 0:
    #                 rec.cost_product = record.cost_product
            # try:
            #     record.cost_product = record.lot_id.purchase_order_ids.picking_ids.move_ids_without_package.price_unit
            # except:
            #     record.cost_product = 0
        # for line in self:
        #     line.cost_product = line.product_id.cost_price