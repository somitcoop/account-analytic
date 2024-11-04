# -*- coding: utf-8 -*-
from odoo import models


class Project(models.Model):
    _inherit = "project.project"

    def _create_analytic_account(self):
        analytic_account = super()._create_analytic_account()

        if self.sale_line_id and self.sale_line_id.product_id.analytic_plan_id:
            analytic_account.plan_id = self.sale_line_id.product_id.analytic_plan_id.id

        return analytic_account
