from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_cancel(self):
        super(PurchaseOrder, self.with_context(cancel=True)).button_cancel()

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    """def update_cost_price(self, line):
        supplier_info = line.product_id.seller_ids.filtered(
            lambda r: r.name == line.partner_id
        )
        if supplier_info and line.price_unit != supplier_info.price:
            price_unit = line.price_unit
            if 'discount' in line and line.discount:
                price_unit = line.price_unit * (1 - line.discount / 100)
            supplier_info.price = price_unit
            line.product_id.standard_price = price_unit
            line.product_id.write({"label_to_be_printed": True})"""

    @api.model
    def create(self, values):
        line = super(PurchaseOrderLine, self).create(values)
        if self.env.context.get('cancel'):
            return line
        """self.update_cost_price(line)"""
        if line.product_id.first_purchased:
            line.product_id.label_to_be_printed = True
            line.product_id.first_purchased = False
        return line

    """def write(self, values):
        ret = super(PurchaseOrderLine, self).write(values)
        if self.env.context.get('cancel'):
            return ret
        for line in self:
            self.update_cost_price(line)
        return ret"""
