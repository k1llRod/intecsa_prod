from odoo import models, fields, api

class StockInventoryLine(models.Model):
    _inherit = 'stock.inventory.line'

    cost_product = fields.Float(string='Costo del producto')
