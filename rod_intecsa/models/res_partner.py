from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit ='res.partner'

    class_partner = fields.Selection([('class_a', 'Clase A'),
                                      ('class_b', 'Clase B'),
                                      ('class_c', 'Clase C')], string='Clase de contacto', compute='_compute_class_partner', store=True)
    reassigned = fields.Boolean(string='Reasignado', default=False)
    country_id = fields.Many2one('res.country', string='País', default=29)
    sale_order_count_expired = fields.Integer(string='Pedidos de venta vencidos', related='sale_order_count', store=True)
    sale_order_count = fields.Integer(compute='_compute_sale_order_count', string='Sale Order Count', store=True)
    def _compute_sale_order_count_expired(self):
        for record in self:
            record.sale_order_count_expired = len(self.env['sale.order'].search([('partner_id', '=', record.id), ('state', '=', 'draft')]))

    @api.depends('category_id')
    def _compute_class_partner(self):
        for record in self:
            if record.category_id:
                record.class_partner = record.category_id[-1].class_partner
            else:
                record.class_partner = False
    def assign_client(self):
        class_a = len(self.filtered(lambda x:x.class_partner == 'class_a'))
        class_b1 = len(self.filtered(lambda x:x.class_partner == 'class_b1'))
        class_b2 = len(self.filtered(lambda x:x.class_partner == 'class_b2'))
        class_b3 = len(self.filtered(lambda x:x.class_partner == 'class_b3'))

        user_class_a = len(self.env['res.users'].search([('class_partner', '=', 'class_a')]))
        user_class_b1 = len(self.env['res.users'].search([('class_partner', '=', 'class_b1')]))
        user_class_b2 = len(self.env['res.users'].search([('class_partner', '=', 'class_b2')]))
        user_class_b3 = len(self.env['res.users'].search([('class_partner', '=', 'class_b3')]))

        context = {
            'default_customer_class_a': class_a,
            'default_customer_class_b1': class_b1,
            'default_customer_class_b2': class_b2,
            'default_customer_class_b3': class_b3,
            'default_seller_class_a': user_class_a,
            'default_seller_class_b1': user_class_b1,
            'default_seller_class_b2': user_class_b2,
            'default_seller_class_b3': user_class_b3,
        }
        return {
            'name': 'Asignar clientes',
            'type': 'ir.actions.act_window',
            'res_model': 'reassign.customers',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': context,
        }

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        if not args:
            args = []
        if name:
            positive_operators6 = ['=', 'ilike', '=ilike', 'like', '=like']
            partners_ids = []
            args = ['|', ('name', operator, name), ('a_area', operator, name)] + args
            partners_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        else:
            partners_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return partners_ids