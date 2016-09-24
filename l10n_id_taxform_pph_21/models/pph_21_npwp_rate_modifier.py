# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class Pph21NpwpRateModifier(models.Model):
    _name = "l10n_id.pph_21_npwp_rate_modifier"
    _description = "PPh 21 NPWP Rate Modifier"

    name = fields.Char(
        string="Dasar Hukum",
        required=True,
        )
    date_start = fields.Date(
        string="Tanggal Mulai Berlaku",
        required=True,
        )
    pph_rate_modifier = fields.Float(
        string="PPh Rate Modifier",
        required=True,
        )

    @api.model
    def _find(self, dt=None):
        #TODO:
        result = False
        return result
