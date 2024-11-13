# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    analytic_plan_id = fields.Many2one(
        "account.analytic.plan",
        string="Analytic Plan",
        help="When creating a project from this product, this analytic plan will be automatically "
        "assigned to the project's analytic account. This is useful for automatically "
        "categorizing and organizing your project's analytical accounting.",
        domain=lambda self: [("company_id", "in", [self.env.company.id, False])],
    )
