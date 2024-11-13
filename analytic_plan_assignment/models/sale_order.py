# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_analytic_account_data(self, prefix=None):
        result = super()._prepare_analytic_account_data(prefix=prefix)

        if self.order_line:
            product = self.order_line[0].product_id
            if product.analytic_plan_id:
                if (
                    product.analytic_plan_id.company_id == self.company_id
                    or not product.analytic_plan_id.company_id
                ):
                    result["plan_id"] = product.analytic_plan_id.id

        return result
