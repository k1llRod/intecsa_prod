from odoo import models, fields, api
from odoo.tools.float_utils import float_is_zero

class StockQuant(models.Model):
    _inherit ='stock.quant'

    cost_product = fields.Float(string='Costo', store=True)

    def update_cost_product(self, res):
        try:
            for rec in res:
                price_unit = self.env['stock.move.line'].search([('product_id', '=', rec.product_id.id)]).filtered(lambda x:x.lot_id == rec.lot_id).picking_id.move_ids_without_package.filtered(lambda x:x.product_id == rec.product_id).price_unit
                rec.cost_product = price_unit
            return price_unit
        except:
            return 0

    def update_cost_product_massive(self):
        for rec in self:
            price_unit = self.env['stock.move.line'].search([('product_id', '=', rec.product_id.id)]).filtered(lambda x:x.lot_id == rec.lot_id).picking_id.move_ids_without_package.filtered(lambda x:x.product_id == rec.product_id).price_unit
            rec.cost_product = price_unit

    def create(self, vals_list):
        res = super(StockQuant, self).create(vals_list)
        # lot = res.lot_id.name
        price_unit = self.update_cost_product(res)
        res.cost_product = price_unit
        return res
    # @api.depends('lot_id')
    # def _compute_cost_product(self):
    #     for rec in self:
    #         rec.cost_product = self.env['stock.production.lot'].search([('name','=','NS07')]).purchase_order_ids.picking_ids.move_ids_without_package



