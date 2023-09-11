from odoo import api, fields, models


class CancelWizard(models.TransientModel):
    _name = 'cancel.wizard'
    _description = 'Cancel Wizard'
    pr_id = fields.Many2one(
        comodel_name='purchase.request')

    rejection_reason = fields.Text(string='Rejection Reason')

    # rejection_reason = fields.Text(string='Rejection Reason', requierd='True')

    def confirm_rejection(self):
        purchase = self.env['purchase.request'].browse(self.env.context.get('active_id'))
        # results = self.env['cancel.wizard'].create(
        #     {'pr_id': purchase.id, 'rejection_reason': self.rejection_reason})

        for rec in self:
            print("request", purchase)
            print("request", purchase.rejection_reason)
            print("rec.rejection_reason", rec.rejection_reason)
            purchase.rejection_reason = rec.rejection_reason
            purchase.state = "reject"
            return {'type': 'ir.actions.act_window_close'}
#
#         return {
#     'type': 'ir.actions.act_window',
#     "res_model": "purchase.request",
#     'res_id': purchase_requests_.id,
#     "view_mode": "form",
#     "target": "main"
# }

# self.states = 'confirm'
