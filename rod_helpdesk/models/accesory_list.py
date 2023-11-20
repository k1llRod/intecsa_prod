from odoo import fields, models

class AccesoryList(models.Model):
    _name = 'accesory.list'
    _description = 'Accessory List'

    name = fields.Many2one('accesories', string='Accesorio')
    description = fields.Char(string='Descripcion')
    imagen = fields.Binary(string='Imagen')
    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket')