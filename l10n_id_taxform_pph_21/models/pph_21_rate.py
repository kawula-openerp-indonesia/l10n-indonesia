# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class Pph21Rate(models.Model):
    _name = "l10n_id.pph_21_rate"
    _description = "PPh 21 Rate"

    name = fields.Char(
        string="Dasar Hukum",
        required=True,
        )
    date_start = fields.Date(
        string="Tanggal Mulai Berlaku",
        required=True,
        )
    line_ids = fields.One2many(
        string="PPh 21 Rate Detail",
        comodel_name="l10n_id.pph_21_rate_line",
        inverse_name="rate_id",
        )

    @api.model
    def _find(self, dt=None):
        #TODO:
        result = False
        return result

class Pph21RateLine(models.Model):
    _name = "l10n_id.pph_21_rate_line"
    _description = "PPh 21 Rate Line"

    rate_id = fields.Many2one(
        string="PPh 21 Rate",
        comodel_name="l10n_id.pph_21_rate",
        ondelete="cascade",
        )
    min_income = fields.Float(
        string="Min. Income",
        required=True,
        )
    pph_rate = fields.Float(
        string="PPh 21 Rate",
        )
