from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    name = fields.Char(string="Number", compute="", store=True)