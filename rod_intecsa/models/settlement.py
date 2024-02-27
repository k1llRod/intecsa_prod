from odoo import _, api, fields, models

class Settlement(models.Model):
    _inherit = "sale.commission.settlement"

    sale_id = fields.Many2one('sale.order', string="Sale Order")
