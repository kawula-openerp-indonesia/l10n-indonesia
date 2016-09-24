# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    ptkp_category_id = fields.Many2one(
        string="PTKP Category",
        comodel_name="l10n_id.ptkp_category",
        )
    join_tax_period_id = fields.Many2one(
        string="Masa Pajak Bergabung",
        comodel_name="l10n_id.tax_period",
        )
    join_tax_year_id = fields.Many2one(
        string="Tahun Pajak Bergabung",
        comodel_name="l10n_id.tax_year",
        )
