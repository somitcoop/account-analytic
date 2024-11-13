# -*- coding: utf-8 -*-
from odoo import models


class Project(models.Model):
    _inherit = "project.project"

    def _create_analytic_account(self):
        analytic_account = super()._create_analytic_account()
        if self.sale_line_id and self.sale_line_id.product_id.analytic_plan_id:
            plan = self.sale_line_id.product_id.analytic_plan_id
            if plan.company_id == self.company_id or not plan.company_id:
                analytic_account.plan_id = plan.id
        return analytic_account
