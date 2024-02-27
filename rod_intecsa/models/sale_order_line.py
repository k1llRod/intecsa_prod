from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit ='sale.order.line'

    sum_cost = fields.Float(string='Suma de costos', compute='_compute_sum_cost', store=True)

    @api.depends('price_unit')
    def _compute_sum_cost(self):
        for rec in self:
            rec.sum_cost = rec.price_unit * rec.product_uom_qty