from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'


    @api.depends('move_id.name', 'state')
    def _compute_name(self):
        for payment in self:
            payment.name = "Hello"
            # if payment.id and (not payment.name or payment.move_id and payment.name != payment.move_id.name) and payment.state in ('in_process', 'paid'):
            #     payment.name = (
            #         payment.move_id.name
            #         or self.env['ir.sequence'].with_company(payment.company_id).next_by_code(
            #             'account.payment',
            #             sequence_date=payment.date,
            #         )
            #     )