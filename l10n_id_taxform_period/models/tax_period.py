# -*- coding: utf-8 -*-
# Copyright 2016 Prime Force Indonesia
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class TaxYear(models.Model):
    _name = "l10n_id.tax_year"
    _description = "Tax Year"

    name = fields.Char(
        string="Tax Year",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_end = fields.Date(
        string="Date End",
        required=True,
    )
    period_ids = fields.One2many(
        string="Periods",
        comodel_name="l10n_id.tax_period",
        inverse_name="year_id",
    )

    @api.multi
    def action_create_period(self):
        for year in self:
            self._create_period()

    @api.multi
    def _create_period(self):
        self.ensure_one()
        # TODO

    @api.model
    def _find_year(self, dt=None):
        self.ensure_one()
        # TODO
        result = False
        return result


class TaxPeriod(models.Model):
    _name = "l10n_id.tax_period"
    _description = "Tax Period"

    name = fields.Char(
        string="Tax Period",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_end = fields.Date(
        string="Date End",
        required=True,
    )
    year_id = fields.Many2one(
        string="Tax Year",
        comodel_name="l10n_id.tax_year",
        ondelete="cascade",
    )

    @api.multi
    def _next_period(self, step):
        # TODO
        self.ensure_one()
        result = False
        return result

    @api.model
    def _find_period(self, dt=None):
        # TODO
        result = False
        return result
