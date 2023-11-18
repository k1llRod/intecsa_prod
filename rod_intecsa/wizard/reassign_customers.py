from odoo import models, fields, api, _
from datetime import datetime, timedelta


class ReassignCustomers(models.TransientModel):
    _name = 'reassign.customers'
    _description = 'Reassign Customers'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', default='Reasignar clientes')
    customer_class_a = fields.Integer(string='Cliente clase A')
    customer_class_b1 = fields.Integer(string='Cliente clase B1')
    customer_class_b2 = fields.Integer(string='Cliente clase B2')
    customer_class_b3 = fields.Integer(string='Cliente clase B3')

    seller_class_a = fields.Integer(string='Vendedor clase A')
    seller_class_b1 = fields.Integer(string='Vendedor clase B1')
    seller_class_b2 = fields.Integer(string='Vendedor clase B2')
    seller_class_b3 = fields.Integer(string='Vendedor clase B3')

    no_movement = fields.Integer(string='Dias sin movimiento')
    customer_no_movement = fields.Integer(string='Clientes sin movimiento', compute='_compute_customer_no_movement',
                                          store=True)

    @api.depends('no_movement')
    def _compute_customer_no_movement(self):
        contact_cero = self.env['res.partner'].search([('sale_order_ids', '=', False)])
        date_days_ago = datetime.now() - timedelta(days=self.no_movement)
        customer = self.env['res.partner'].search([('sale_order_ids', '!=', False)])
        partner_ids = []
        if self.no_movement > 0:
            for record in customer:
                verify = record.sale_order_ids.filtered(lambda x: x.state == 'draft' and x.date_order < date_days_ago)
                if verify:
                    partner_ids.append(record.id)
        self.customer_no_movement = len(partner_ids)


    def assing(self):
        partner = self.env['res.users'].search([('name','ilike','Carla')])
        self.env['mail.message'].sudo().create({
            'author_id': self.env.user.partner_id.id,
            'model': 'mail.channel',
            # 'res_id': assignment.id,
            'body': f'Nueva asignación para ti: \nDescripción: Partner',
            'partner_ids': [(4, partner.partner_id.id)],
            'message_type': 'comment',
        })
        # user_id = self.env['res.users'].search([])[1]
        # return message
        # date_days_ago = datetime.now() - timedelta(days=self.no_movement)
        # customer = self.env['res.partner'].search([('sale_order_ids', '!=', False)])
        # partner_ids = []
        # if self.no_movement > 0:
        #     for record in customer:
        #         verify = record.sale_order_ids.filtered(lambda x: x.state == 'draft' and x.date_order < date_days_ago)
        #         if verify:
        #             partner_ids.append(record.id)
        #
        # for partner in partner_ids:
        #     create_lead = self.env['crm.lead'].create(
        #         {'name': 'Asignado: ' + partner.name, 'partner_id': partner.id, 'sale_order_id': datetime.now()})

    def inbox_message(self, message_text):
        # construct the message that is to be sent to the user
        message_text = f'<strong>Title</strong> ' \
                       f'<p>This picking has been validated!</p>'

        # odoo runbot
        odoobot_id = self.env['ir.model.data'].sudo().xmlid_to_res_id("base.partner_root")

        # find if a channel was opened for this user before
        channel = self.env['mail.channel'].sudo().search([
            ('name', '=', 'Picking Validated'),
            ('channel_partner_ids', 'in', [self.env.user.partner_id.id])
        ],
            limit=1,
        )

        if not channel:
            # create a new channel
            channel = self.env['mail.channel'].with_context(mail_create_nosubscribe=True).sudo().create({
                'channel_partner_ids': [(4, self.env.user.partner_id.id), (4, odoobot_id)],
                'public': 'public',
                'channel_type': 'chat',
                'email_send': False,
                'name': f'Picking Validated',
                'display_name': f'Picking Validated',
            })

        # send a message to the related user
        channel.sudo().message_post(
            body=message_text,
            author_id=odoobot_id,
            message_type="comment",
            subtype="mail.mt_comment",
        )