from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit ='stock.quant'

    # def _cost_product(self):
    #     search_lot = self.env['stock.production.lot'].search([('name','=','NS07')]).purchase_order_ids.picking_ids.move_ids_without_package
    #     return search_lot.price_unit
    cost_product = fields.Float(string='Costo', store=True)
    @api.onchange('lot_id')
    def _compute_cost_product(self):
        for rec in self:
            rec.cost_product = self.env['stock.production.lot'].search([('name','=','NS07')]).purchase_order_ids.picking_ids.move_ids_without_package



