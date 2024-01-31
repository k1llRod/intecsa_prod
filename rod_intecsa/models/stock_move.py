from odoo import models, fields, api

class StockMove(models.Model):
    _inherit ='stock.move'

    cost_product = fields.Float(string='Costo del producto')
    # total_price_unit = fields.Float(string='Total', compute='_compute_total_price_unit', store=True)
