from odoo import api, fields, models


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = "Purchase Request"
    name = fields.Char(string='Name', required=True)
    requested_by_id = fields.Many2one("res.users", String='Requested By', defult=lambda self: self.env.user)
    start_date = fields.Date(string='Start Date', default=fields.Date.today())
    end_date = fields.Date(string='End Date')
    rejection_reason = fields.Text(string='Rejection Reason')
    rejection_ids = fields.One2many(comodel_name='cancel.wizard', inverse_name='pr_id', string='Rejection_ids')
    order_lines_ids = fields.One2many('order.lines', 'purchase_requests_id', String='Purchase Request')
    total = fields.Float(String='Total')
    state = fields.Selection(string='States',
                             selection=[('draft', 'Draft'), ('approve', 'Approve'), ('reject', 'Reject'),
                                        ('cancel', 'Cancel'),
                                        ("to_be_approved", 'To Be Approved')], default='draft')

    @api.depends('order_lines_ids.sub_total')
    def _total_sum(self):
        self.total = 0
        self.total += self.sub_total

    def to_approve_purchase(self):
        self.state = "to_be_approved"

    def approve(self):
        self.state = "approve"
        self.send_approval_email()

    def get_purchase_manager_users(self):
        group_purchase_manager = self.env.ref('purchase.group_purchase_manager')
        users = self.env['res.users'].search([('groups_id', 'in', group_purchase_manager.id)])
        user_ids = users.ids
        return user_ids

    def send_approval_email(self):
        template = self.env.ref('task_1.email_template_purchase')
        if template:
            print(self.get_purchase_manager_users())
            for user in self.get_purchase_manager_users():
                template.send_mail(user, force_send=True)

    def to_cancel(self):
        self.state = "cancel"

    def reset_to_draft(self):
        self.state = "draft"

# def reject(self):
# self.state = "reject"
