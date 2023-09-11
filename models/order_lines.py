from odoo import api, fields, models


class OrderLines(models.Model):
    _name = 'order.lines'
    purchase_requests_id = fields.Many2one('purchase.request', String='Purchase Request')
    product_id = fields.Many2one('product.product', required=True)
    description = fields.Char(String='Description')
    quantity = fields.Float(String="Quantity", defult=1)
    cost_price = fields.Float(String='Cost Price', readonly=True)
    sub_total = fields.Float(Strig='Sub Total')

    def sub_total_(self):
        self.sub_total = self.quantity * self.cost_price
