# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    analytic_plan_id = fields.Many2one("account.analytic.plan", string="Plan Analítico")
