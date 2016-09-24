# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class Pph21TunjanganJabatan(models.Model):
    _name = "l10n_id.pph_21_biaya_jabatan"
    _description = "Biaya Jabatan"

    name = fields.Char(
        string="Dasar Hukum",
        required=True,
        )
    date_start = fields.Date(
        string="Tanggal Mulai Berlaku",
        required=True,
        )
    rate_biaya_jabatan = fields.Float(
        string="Rate Biaya Jabatan",
        required=True,
        )

    @api.model
    def _find(self, dt=None):
        #TODO
        result = False
        return True
