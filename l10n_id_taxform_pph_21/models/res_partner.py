# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    # @api.multi
    # def compute_pph_21_2110001(
    #         self,
    #         bulan_bergabung,
    #         ptkp_category,
    #         tanggal_pemotongan,
    #         jumlah_penghasilan_rutin,
    #         jumlah_penghasilan_non_rutin,
    #         tunjangan_jabatan,
    #         pensiun,
    #         ):
    #     #TODO
    #     self.ensure_one()
    #     result = {
    #         "biaya_jabatan_rutin": 0.0,
    #         "penghasilan_bruto_rutin_setahun": 0.0,
    #         "penghasilan_bruto_non_rutin_setahun": 0.0,
    #         "penghasilan_bruto_setahun": 0.0,
    #         "ptkp": 0.0,
    #         "pkp_rutin_setahun": 0.0,
    #         "pkp_setahun": 0.0,
    #         "pph_rutin_setahun": 0.0,
    #         "pph_non_rutin_setahun": 0.0,
    #         "pph_setahun": 0.0,
    #         "pph": 0.0,
    #         }

    #     obj_biaya_jabatan = self.env["l10n_id.pph_21_biaya_jabatan"]

    #     biaya_jabatan = obj_biaya_jabatan.get_biaya_jabatan(
    #         jumlah_penghasilan_rutin,
    #         jumlah_penghasilan_non_rutin,
    #         tunjangan_jabatan,
    #         tanggal_pemotongan,
    #         )
    #     result["jumlah_pengurangan"] = biaya_jabatan["biaya_jabatan"] + \
    #             pensiun
    #     result["jumlah_penghasilan_netto"] = jumlah_penghasilan_rutin + \
    #         jumlah_penghasilan_non_rutin - result["jumlah_pengurang"]
    #     penghasilan_netto_rutin_disetahunkan = jumlah_penghasilan_rutin * \
    #         (12 - bulan_bergabung + 1)



    #     npwp = len(self.vat) > 0 and self.vat or False
    #     result["ptkp"] = ptkp_category._get_rate(tanggal_pemotongan)



    #     return result

        
