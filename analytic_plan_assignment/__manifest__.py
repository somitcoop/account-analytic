# Copyright 2024 Som IT Cooperatiu SCCL - Nicolás Ramos <nicolas.ramos@somit.coop>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Analytic_plan_assignment",
    "version": "16.0.1.0.0",
    "summary": """ Assign analytic plans to products """,
    "author": "Som IT Cooperatiu SCCL, Odoo Community Association (OCA)",
    "website": "https://www.somit.coop",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "base",
        "sale_project",
    ],
    "data": [
        "views/product_template_views.xml",
    ],
    "installable": True,
    "maintainers": ["nramosdev"],
    "development_status": "Alpha",
}
