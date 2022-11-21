# dodyakj --- dodyakj
from typing import ValuesView
from odoo import api,fields,models,modules
from odoo.tools.translate import _
from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)

class competencyMap(models.Model):
    _name = 'competency.map'

    name =  fields.Char(string='Name')
    value =  fields.Integer(string='Value')


    hr_id  = fields.Many2one(string='Employee', comodel_name='hr.employee', ondelete='restrict')
    job_id  = fields.Many2one(string='Employee', comodel_name='hr.job', ondelete='restrict')



class HrEmployeeCompetencyMap(models.Model):
    _inherit = "hr.employee"

    topic_ids = fields.One2many('competency.map', 'hr_id')
    station_id  = fields.Many2one(string='Station', comodel_name='master.station', ondelete='restrict')

    @api.model
    def default_get(self, fields_list):
        res = super(HrEmployeeCompetencyMap, self).default_get(fields_list)
        vals = []
        station = self.env['training.topic'].search([], order="create_date asc")
        for s in station:
            vals.append((0, 0, {'name': s.name, 'value': 0}))
        res.update({'topic_ids': vals})
        return res

    t_mrt   =  fields.Integer(string='Tata tertib area MRTJ (I)', required=True, compute='competion_def')
    t_mrt_p =  fields.Integer(string='Tata tertib pegawai stasiun (J)', required=True, compute='competion_def')
    t_as    =  fields.Integer(string='Akses Stasiun (AQ)', required=True, compute='competion_def')
    t_psdm  =  fields.Integer(string='Pengelolaan SDM (K)', required=True, compute='competion_def')
    cr_mng   =  fields.Integer(string='Crowd Management 1', required=True, compute='competion_def')
    cr_mngae   =  fields.Integer(string='Crowd Management (AE)', required=True, compute='competion_def')
    t_p3k   =  fields.Integer(string='P3K', required=True, compute='competion_def')
    t_pew   =  fields.Integer(string='Prosedur Evakuasi (W)', required=True, compute='competion_def')
    t_ptd =  fields.Integer(string='Pelatihan Tanggap Darurat (Simulasi) (X)', required=True, compute='competion_def')
    t_pph   =  fields.Integer(string='Pelatihan Penggunaan Hydrant, APAR, dan APAB (Y)', required=True, compute='competion_def')
    t_ppfb   =  fields.Integer(string='Pelatihan Pengoperasian Flood Barier (Khusus Stasiun UG) (Z)', required=True, compute='competion_def')
    t_pses   =  fields.Integer(string='Pelatihan Safety Equipment Station (AA)', required=True, compute='competion_def')
    t_scba   =  fields.Integer(string='Pelatihan Penggunaan SCBA (AB)', required=True, compute='competion_def')
    t_ppwb   =  fields.Integer(string='Pelatihan Penggunaan Warden Box (AC)', required=True, compute='competion_def')
    t_pppt =  fields.Integer(string='Pelatihan P3K dan Penggunaan Tandu (AD)', required=True, compute='competion_def')
    t_pp =  fields.Integer(string='Pengumuman Penumpang (AS)', required=True, compute='competion_def')
    t_dh =  fields.Integer(string='Disability Handling (AU)', required=True, compute='competion_def')
    t_cash2 =  fields.Integer(string='Cash Handling Flow - Level 2 (S)', required=True, compute='competion_def')
    t_cash3 =  fields.Integer(string='Cash Handling Flow - Level 3 (S)', required=True, compute='competion_def')
    t_cash4 =  fields.Integer(string='Cash Handling Flow - Level 4 (S)', required=True, compute='competion_def')
    t_rev2 =  fields.Integer(string='Revanue Closing (prosedur dan formulir) - Level 2 (T)', required=True, compute='competion_def')
    t_rev3 =  fields.Integer(string='Revanue Closing (prosedur dan formulir) - Level 3 (T)', required=True, compute='competion_def')
    t_rev4 =  fields.Integer(string='Revanue Closing (prosedur dan formulir) - Level 4 (T)', required=True, compute='competion_def')
    t_iup =  fields.Integer(string='Identifikasi Uang Palsu (U)', required=True, compute='competion_def')
    t_brib =  fields.Integer(string='Bribery & Fraud Risk (V)', required=True, compute='competion_def')

    t_pcm3 =  fields.Integer(string='Pengoperasian CCTV Monitor - Level 3 (AF)', required=True, compute='competion_def')
    t_pcm4 =  fields.Integer(string='Pengoperasian CCTV Monitor - Level 4 (AF)', required=True, compute='competion_def')
    t_scuat3 =  fields.Integer(string='Pengoperasian SCUAT - Level 3 (AG)', required=True, compute='competion_def')
    t_scuat4 =  fields.Integer(string='Pengoperasian SCUAT - Level 4 (AG)', required=True, compute='competion_def')
    t_ppa =  fields.Integer(string='Pengoperasian PA System - (AH)', required=True, compute='competion_def')
    t_fscada4 =  fields.Integer(string='Pengoperasian FSCADA - Level 4 (AH)', required=True, compute='competion_def')
    t_bas =  fields.Integer(string='Pengoperasian BAS - Level 4 (AJ)', required=True, compute='competion_def')
    t_tvs =  fields.Integer(string='Pengoperasian TVS - Level 4 (AK)', required=True, compute='competion_def')
    t_gss =  fields.Integer(string='Pengoperasian GSS - Level 4 (AL)', required=True, compute='competion_def')
    t_psle2 =  fields.Integer(string='Pengoperasian SLE - Level 2 (PG, TVM, AVM) (AM)', required=True, compute='competion_def')
    t_psle3 =  fields.Integer(string='Pengoperasian SLE - Level 3 (PG, TVM, AVM) (AM)', required=True, compute='competion_def')
    t_psle4 =  fields.Integer(string='Pengoperasian SLE - Level 4 (PG, TVM, AVM) (AM)', required=True, compute='competion_def')
    t_tsle2 =  fields.Integer(string='Troubleshoot SLE - Level 2 (PG, TVM, AVM) (AN)', required=True, compute='competion_def')
    t_tsle3 =  fields.Integer(string='Troubleshoot SLE - Level 3 (PG, TVM, AVM) (AN)', required=True, compute='competion_def')
    t_tsle4 =  fields.Integer(string='Troubleshoot SLE - Level 4 (PG, TVM, AVM) (AN)', required=True, compute='competion_def')
    t_lift1 =  fields.Integer(string='Pengoperasian lift&eskalator - Level 1 (AT)', required=True, compute='competion_def')
    t_lift4 =  fields.Integer(string='Pengoperasian lift&eskalator - Level 4 (AT)', required=True, compute='competion_def')
    t_lift3 =  fields.Integer(string='Pengoperasian lift&eskalator - Level 3 (AT)', required=True, compute='competion_def')
    t_tom2 =  fields.Integer(string='Pengoperasian TOM - Level 2 (AO)', required=True, compute='competion_def')
    t_tom3 =  fields.Integer(string='Pengoperasian TOM - Level 3 (AO)', required=True, compute='competion_def')
    t_tom4 =  fields.Integer(string='Pengoperasian TOM - Level 4 (AO)', required=True, compute='competion_def')
    t_psd =  fields.Integer(string='Pengoperasian PSD (A)', required=True, compute='competion_def')
    t_fire =  fields.Integer(string='	Pengoperasian Fire System (B)', required=True, compute='competion_def')
 
    k_ticket    =  fields.Integer(string='Kebijakan Layanan Ticketing (L)', required=True, compute='competion_def')
    k_ticket_u  =  fields.Integer(string='Kebijakan Layanan Umum (M)', required=True, compute='competion_def')
    k_ticket_n  =  fields.Integer(string='Kebijakan layanan penumpang prioritas (N)', required=True, compute='competion_def')
    k_ticket_ap =  fields.Integer(string='Pengoperasian rolling door dan kunci stasiun (AP)', required=True, compute='competion_def')
    k_ticket_ar =  fields.Integer(string='Pengelolaan perlengkapan stasiun (AR)', required=True, compute='competion_def')
    k_ticket_o  =  fields.Integer(string='Pengetahuan fasilitas penumpang dan area sekitar stasiun (O)', required=True, compute='competion_def')
    k_ticket_p  =  fields.Integer(string='Lost&Found System (P)', required=True, compute='competion_def')

    p_ticket_2q =  fields.Integer(string='Effective Handling Complain - Level 2 (Q)', required=True, compute='competion_def')
    p_ticket_3q =  fields.Integer(string='Effective Handling Complain - Level 3 (Q)', required=True, compute='competion_def')
    p_ticket_4q =  fields.Integer(string='Effective Handling Complain - Level 4 (Q)', required=True, compute='competion_def')
    pp_ticket_1q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 1 (R)', required=True, compute='competion_def')
    pp_ticket_2q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 2 (R)', required=True, compute='competion_def')
    pp_ticket_3q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 3 (R)', required=True, compute='competion_def')
    pp_ticket_4q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 4 (R)', required=True, compute='competion_def')

    t_mrt_of   =  fields.Integer(string='Tata tertib area MRTJ (I)', required=True, compute='competion_def')
    t_mrt_p_of =  fields.Integer(string='Tata tertib pegawai stasiun (J)', required=True, compute='competion_def')
    t_as_of    =  fields.Integer(string='Akses Stasiun (AQ)', required=True, compute='competion_def')
    t_psdm_of  =  fields.Integer(string='Pengelolaan SDM (K)', required=True, compute='competion_def')
    cr_mng_of   =  fields.Integer(string='Crowd Management 1', required=True, compute='competion_def')
    cr_mngae_of   =  fields.Integer(string='Crowd Management (AE)', required=True, compute='competion_def')
    t_p3k_of   =  fields.Integer(string='P3K', required=True, compute='competion_def')
    t_pew_of   =  fields.Integer(string='Prosedur Evakuasi (W)', required=True, compute='competion_def')
    t_ptd_of =  fields.Integer(string='Pelatihan Tanggap Darurat (Simulasi) (X)', required=True, compute='competion_def')
    t_pph_of   =  fields.Integer(string='Pelatihan Penggunaan Hydrant, APAR, dan APAB (Y)', required=True, compute='competion_def')
    t_ppfb_of   =  fields.Integer(string='Pelatihan Pengoperasian Flood Barier (Khusus Stasiun UG) (Z)', required=True, compute='competion_def')
    t_pses_of   =  fields.Integer(string='Pelatihan Safety Equipment Station (AA)', required=True, compute='competion_def')
    t_scba_of   =  fields.Integer(string='Pelatihan Penggunaan SCBA (AB)', required=True, compute='competion_def')
    t_ppwb_of   =  fields.Integer(string='Pelatihan Penggunaan Warden Box (AC)', required=True, compute='competion_def')
    t_pppt_of   =  fields.Integer(string='Pelatihan P3K dan Penggunaan Tandu (AD)', required=True, compute='competion_def')
    t_pp_of   =  fields.Integer(string='Pengumuman Penumpang (AS)', required=True, compute='competion_def')
    t_dh_of   =  fields.Integer(required=True, compute='competion_def')
    t_cash2_of   =  fields.Integer(required=True, compute='competion_def')
    t_cash3_of   =  fields.Integer(required=True, compute='competion_def')
    t_cash4_of   =  fields.Integer(required=True, compute='competion_def')
    t_rev2_of   =  fields.Integer(required=True, compute='competion_def')
    t_rev3_of   =  fields.Integer(required=True, compute='competion_def')
    t_rev4_of   =  fields.Integer(required=True, compute='competion_def')
    t_iup_of   =  fields.Integer(required=True, compute='competion_def')
    t_brib_of   =  fields.Integer(required=True, compute='competion_def')

    t_pcm3_of   =  fields.Integer(required=True, compute='competion_def')
    t_pcm4_of   =  fields.Integer(required=True, compute='competion_def')
    t_scuat3_of   =  fields.Integer(required=True, compute='competion_def')
    t_scuat4_of   =  fields.Integer(required=True, compute='competion_def')
    t_ppa_of   =  fields.Integer(required=True, compute='competion_def')
    t_fscada4_of   =  fields.Integer(required=True, compute='competion_def')
    t_bas_of   =  fields.Integer(required=True, compute='competion_def')
    t_tvs_of   =  fields.Integer(required=True, compute='competion_def')
    t_gss_of   =  fields.Integer(required=True, compute='competion_def')
    t_psle2_of   =  fields.Integer(required=True, compute='competion_def')
    t_psle3_of   =  fields.Integer(required=True, compute='competion_def')
    t_psle4_of   =  fields.Integer(required=True, compute='competion_def')
    t_tsle2_of   =  fields.Integer(required=True, compute='competion_def')
    t_tsle3_of   =  fields.Integer(required=True, compute='competion_def')
    t_tsle4_of   =  fields.Integer(required=True, compute='competion_def')
    t_lift1_of   =  fields.Integer(required=True, compute='competion_def')
    t_lift4_of   =  fields.Integer(required=True, compute='competion_def')
    t_lift3_of   =  fields.Integer(required=True, compute='competion_def')
    t_tom2_of   =  fields.Integer(required=True, compute='competion_def')
    t_tom3_of   =  fields.Integer(required=True, compute='competion_def')
    t_tom4_of   =  fields.Integer(required=True, compute='competion_def')
    t_psd_of   =  fields.Integer(required=True, compute='competion_def')
    t_fire_of   =  fields.Integer(required=True, compute='competion_def')
    
 
    k_ticket_of    =  fields.Integer(string='Kebijakan Layanan Ticketing (L)', required=True, compute='competion_def')
    k_ticket_u_of  =  fields.Integer(string='Kebijakan Layanan Umum (M)', required=True, compute='competion_def')
    k_ticket_n_of  =  fields.Integer(string='Kebijakan layanan penumpang prioritas (N)', required=True, compute='competion_def')
    k_ticket_ap_of =  fields.Integer(string='Pengoperasian rolling door dan kunci stasiun (AP)', required=True, compute='competion_def')
    k_ticket_ar_of =  fields.Integer(string='Pengelolaan perlengkapan stasiun (AR)', required=True, compute='competion_def')
    k_ticket_o_of  =  fields.Integer(string='Pengetahuan fasilitas penumpang dan area sekitar stasiun (O)', required=True, compute='competion_def')
    k_ticket_p_of  =  fields.Integer(string='Lost&Found System (P)', required=True, compute='competion_def')

    p_ticket_2q_of =  fields.Integer(string='Effective Handling Complain - Level 2 (Q)', required=True, compute='competion_def')
    p_ticket_3q_of =  fields.Integer(string='Effective Handling Complain - Level 3 (Q)', required=True, compute='competion_def')
    p_ticket_4q_of =  fields.Integer(string='Effective Handling Complain - Level 4 (Q)', required=True, compute='competion_def')
    pp_ticket_1q_of =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 1 (R)', required=True, compute='competion_def')
    pp_ticket_2q_of =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 2 (R)', required=True, compute='competion_def')
    pp_ticket_3q_of =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 3 (R)', required=True, compute='competion_def')
    pp_ticket_4q_of =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 4 (R)', required=True, compute='competion_def')

    def competion_def(self):
        self.t_mrt = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Tata tertib area MRTJ (I)')]).id)\
                                                                ]).ids)
        self.cr_mng = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Crowd Management 1')]).id)\
                                                                ]).ids)
        self.cr_mngae = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Crowd Management (AE)')]).id)\
                                                                ]).ids)
        self.t_p3k = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','P3K')]).id)\
                                                                ]).ids)
        self.t_pew = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Prosedur Evakuasi (W)')]).id)\
                                                                ]).ids)
        self.t_ptd = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan Tanggap Darurat (Simulasi) (X)')]).id)\
                                                                ]).ids)
        self.t_pph = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan penggunaan hydrant, APAR, dan APAB (Y)')]).id)\
                                                                ]).ids)
        self.t_ppfb = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan pengoperasian flood barier (khusus stasiun UG) (Z)')]).id)\
                                                                ]).ids)
        self.t_pses = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan Safety Equipment Stasiun (AA)')]).id)\
                                                                ]).ids)
        self.t_scba = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan Penggunaan SCBA (AB)')]).id)\
                                                                ]).ids)
        self.t_ppwb = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan Penggunaan Warden Box (AC)')]).id)\
                                                                ]).ids)
        self.t_pppt = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelatihan P3K dan Penggunaan Tandu (AD)')]).id)\
                                                                ]).ids)
        self.t_pp = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pengumuman Penumpang (AS)')]).id)\
                                                                ]).ids)
        self.t_cash2 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Cash handling flow - Level 2 (S)')]).id)\
                                                                ]).ids)
        self.t_cash3 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Cash handling flow - Level 3 (S)')]).id)\
                                                                ]).ids)
        self.t_cash4 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Cash handling flow - Level 4 (S)')]).id)\
                                                                ]).ids)
        self.t_rev2 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Revanue Closing (prosedur dan formulir) - Leve 2 (T)')]).id)\
                                                                ]).ids)
        self.t_rev3 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Revanue Closing (prosedur dan formulir) - Leve 3 (T)')]).id)\
                                                                ]).ids)
        self.t_rev4 = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Revanue Closing (prosedur dan formulir) - Leve 4 (T)')]).id)\
                                                                ]).ids)
        self.t_iup = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Identifikasi uang palsu (U)')]).id)\
                                                                ]).ids)
        self.t_brib = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Bribery & Fraud Risk (V)')]).id)\
                                                                ]).ids)
        self.t_dh = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Disability Handling (AU)')]).id)\
                                                                ]).ids)

        self.t_pcm3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian CCTV Monitor - Level 3 (AF)')]).id)]).ids)
        self.t_pcm4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian CCTV Monitor - Level 4 (AF)')]).id)]).ids)
        self.t_scuat3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian SCUAT - Level 3 (AG)')]).id)]).ids)
        self.t_scuat4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian SCUAT - Level 4 (AG)')]).id)]).ids)
        self.t_ppa = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian PA System - (AH)')]).id)]).ids)
        self.t_fscada4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian FSCADA - Level 4 (AH)')]).id)]).ids)
        self.t_bas = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian BAS - Level 4 (AJ)')]).id)]).ids)
        self.t_tvs = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian TVS - Level 4 (AK)')]).id)]).ids)
        self.t_gss = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian GSS - Level 4 (AL)')]).id)]).ids)
        self.t_psle2 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian SLE - Level 2 (PG, TVM, AVM) (AM)')]).id)]).ids)
        self.t_psle3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian SLE - Level 3 (PG, TVM, AVM) (AM)')]).id)]).ids)
        self.t_psle4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian SLE - Level 4 (PG, TVM, AVM) (AM)')]).id)]).ids)
        self.t_tsle2 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Troubleshoot SLE - Level 2 (PG, TVM, AVM) (AN)')]).id)]).ids)
        self.t_tsle3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Troubleshoot SLE - Level 3 (PG, TVM, AVM) (AN)')]).id)]).ids)
        self.t_tsle4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Troubleshoot SLE - Level 4 (PG, TVM, AVM) (AN)')]).id)]).ids)
        self.t_lift1 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian lift&eskalator - Level 1 (AT)')]).id)]).ids)
        self.t_lift3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian lift&eskalator - Level 3 (AT)')]).id)]).ids)
        self.t_lift4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian lift&eskalator - Level 4 (AT)')]).id)]).ids)
        self.t_tom2 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian TOM - Level 2 (AO)')]).id)]).ids)
        self.t_tom3 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian TOM - Level 3 (AO)')]).id)]).ids)
        self.t_tom4 = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian TOM - Level 4 (AO)')]).id)]).ids)
        self.t_psd = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian PSD (A)')]).id)]).ids)
        self.t_fire = len(self.env['event.registration'].search([('employee_id','=',self.id),('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian Fire System (B)')]).id)]).ids)

        self.t_mrt_p = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Tata tertib pegawai stasiun (J)')]).id)\
                                                                ]).ids)
        self.t_as = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Akses Stasiun (AQ)')]).id)\
                                                                ]).ids)
        self.t_psdm = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pengelolaan SDM (K)')]).id)\
                                                                ]).ids)
        self.k_ticket = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Kebijakan Layanan Ticketing (L)')]).id)\
                                                                ]).ids)
        self.k_ticket_u = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Kebijakan Layanan Umum (M)')]).id)\
                                                                ]).ids)
        self.k_ticket_n = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Kebijakan layanan penumpang prioritas (N)')]).id)\
                                                                ]).ids)
        self.k_ticket_ap = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pengoperasian rolling door dan kunci stasiun (AP)')]).id)\
                                                                ]).ids)
        self.k_ticket_ar = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pengelolaan perlengkapan stasiun (AR)')]).id)\
                                                                ]).ids)
        self.k_ticket_o = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pengetahuan fasilitas penumpang dan area sekitar stasiun (O)')]).id)\
                                                                ]).ids)
        self.k_ticket_p = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Lost&Found System (P)')]).id)\
                                                                ]).ids)
        self.p_ticket_2q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Effective Handling Complain - Level 2 (Q)')]).id)\
                                                                ]).ids)
        self.p_ticket_3q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Effective Handling Complain - Level 3 (Q)')]).id)\
                                                                ]).ids)
        self.p_ticket_4q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Effective Handling Complain - Level 4 (Q)')]).id)\
                                                                ]).ids)
        self.pp_ticket_1q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelanggaran dan Penindakan Penumpang - Level 1 (R)')]).id)\
                                                                ]).ids)
        self.pp_ticket_2q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelanggaran dan Penindakan Penumpang - Level 2 (R)')]).id)\
                                                                ]).ids)
        self.pp_ticket_3q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelanggaran dan Penindakan Penumpang - Level 3 (R)')]).id)\
                                                                ]).ids)
        self.pp_ticket_4q = len(self.env['event.registration'].search([('employee_id','=',self.id),\
                                                                ('topic_id','=',self.env['training.topic'].search([('name','=','Pelanggaran dan Penindakan Penumpang - Level 4 (R)')]).id)\
                                                                ]).ids)
        self.t_mrt_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Tata tertib area MRTJ (I)')]).value)

        self.t_pcm3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian CCTV Monitor - Level 3 (AF)')]).value)
        self.t_pcm4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian CCTV Monitor - Level 4 (AF)')]).value)
        self.t_scuat3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian SCUAT - Level 3 (AG)')]).value)
        self.t_scuat4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian SCUAT - Level 4 (AG)')]).value)
        self.t_ppa_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian PA System - (AH)')]).value)
        self.t_fscada4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian FSCADA - Level 4 (AH)')]).value)
        self.t_bas_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian BAS - Level 4 (AJ)')]).value)
        self.t_tvs_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian TVS - Level 4 (AK)')]).value)
        self.t_gss_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian GSS - Level 4 (AL)')]).value)
        self.t_psle2_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian SLE - Level 2 (PG, TVM, AVM) (AM)')]).value)
        self.t_psle3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian SLE - Level 3 (PG, TVM, AVM) (AM)')]).value)
        self.t_psle4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian SLE - Level 4 (PG, TVM, AVM) (AM)')]).value)
        self.t_tsle2_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Troubleshoot SLE - Level 2 (PG, TVM, AVM) (AN)')]).value)
        self.t_tsle3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Troubleshoot SLE - Level 3 (PG, TVM, AVM) (AN)')]).value)
        self.t_tsle4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Troubleshoot SLE - Level 4 (PG, TVM, AVM) (AN)')]).value)
        self.t_lift1_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian lift&eskalator - Level 1 (AT)')]).value)
        self.t_lift3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian lift&eskalator - Level 3 (AT)')]).value)
        self.t_lift4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian lift&eskalator - Level 4 (AT)')]).value)
        self.t_tom2_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian TOM - Level 2 (AO)')]).value)
        self.t_tom3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian TOM - Level 3 (AO)')]).value)
        self.t_tom4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian TOM - Level 4 (AO)')]).value)
        self.t_psd_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian PSD (A)')]).value)
        self.t_fire_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian Fire System (B)')]).value)

        self.cr_mng_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Crowd Management 1')]).value)
        self.cr_mngae_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Crowd Management (AE)')]).value)
        self.t_p3k_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','P3K')]).value)
        self.t_pew_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Prosedur Evakuasi (W)')]).value)
        self.t_ptd_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan Tanggap Darurat (Simulasi) (X)')]).value)
        self.t_pph_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan penggunaan hydrant, APAR, dan APAB (Y)')]).value)
        self.t_ppfb_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan pengoperasian flood barier (khusus stasiun UG) (Z)')]).value)
        self.t_pses_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan Safety Equipment Stasiun (AA)')]).value)
        self.t_scba_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan Penggunaan SCBA (AB)')]).value)
        self.t_ppwb_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan Penggunaan Warden Box (AC)')]).value)
        self.t_pppt_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelatihan P3K dan Penggunaan Tandu (AD)')]).value)
        self.t_pp_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengumuman Penumpang (AS)')]).value)
        self.t_dh_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Disability Handling (AU)')]).value)
        self.t_cash2_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Cash handling flow - Level 2 (S)')]).value)
        self.t_cash3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Cash handling flow - Level 3 (S)')]).value)
        self.t_cash4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Cash handling flow - Level 4 (S)')]).value)
        self.t_rev2_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Revanue Closing (prosedur dan formulir) - Level 2 (T)')]).value)
        self.t_rev3_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Revanue Closing (prosedur dan formulir) - Level 3 (T)')]).value)
        self.t_rev4_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Revanue Closing (prosedur dan formulir) - Level 4 (T)')]).value)
        self.t_iup_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Identifikasi uang palsu (U)')]).value)
        self.t_brib_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Bribery & Fraud Risk (V)')]).value)
        self.t_mrt_p_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Tata tertib pegawai stasiun (J)')]).value)
        self.t_as_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Akses Stasiun (AQ)')]).value)
        self.t_psdm_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengelolaan SDM (K)')]).value)
        self.k_ticket_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Kebijakan Layanan Ticketing (L)')]).value)
        self.k_ticket_u_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Kebijakan Layanan Umum (M)')]).value)
        self.k_ticket_n_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Kebijakan layanan penumpang prioritas (N)')]).value)
        self.k_ticket_ap_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengoperasian rolling door dan kunci stasiun (AP)')]).value)
        self.k_ticket_ar_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengelolaan perintgkapan stasiun (AR)')]).value)
        self.k_ticket_o_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pengetahuan fasilitas penumpang dan area sekitar stasiun (O)')]).value)
        self.k_ticket_p_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Lost&Found System (P)')]).value)
        self.p_ticket_2q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Effective Handling Complain - Level 2 (Q)')]).value)
        self.p_ticket_3q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Effective Handling Complain - Level 3 (Q)')]).value)
        self.p_ticket_4q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Effective Handling Complain - Level 4 (Q)')]).value)
        self.pp_ticket_1q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelanggaran dan Penindakan Penumpang - Level 1 (R)')]).value)
        self.pp_ticket_2q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelanggaran dan Penindakan Penumpang - Level 2 (R)')]).value)
        self.pp_ticket_3q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelanggaran dan Penindakan Penumpang - Level 3 (R)')]).value)
        self.pp_ticket_4q_of = int(self.env['competency.map'].search([('job_id','=',self.job_id.id),('name','=','Pelanggaran dan Penindakan Penumpang - Level 4 (R)')]).value)



class HrJobCompetencyMap(models.Model):
    _inherit = "hr.job"


    topic_ids = fields.One2many('competency.map', 'job_id')



    @api.onchange('name')
    def onchange_company_id(self):
        self.update({'topic_ids': False})  
        vals = []
        station = self.env['training.topic'].search([], order="create_date asc")
        for s in station:
            vals.append((0, 0, {'name': s.name, 'value': 0, 'job_id':self.id}))
        self.update({'topic_ids': vals})



    @api.model
    def default_get(self, fields_list):
        res = super(HrJobCompetencyMap, self).default_get(fields_list)
        vals = []
        station = self.env['training.topic'].search([], order="create_date asc")
        for s in station:
            vals.append((0, 0, {'name': s.name, 'value': 0, 'job_id':self.id}))
        res.update({'topic_ids': vals})
        return res


    # t_mrt   =  fields.Integer(string='Tata tertib area MRTJ (I)', required=True)
    # t_mrt_p =  fields.Integer(string='Tata tertib pegawai stasiun (J)', required=True)
    # t_as    =  fields.Integer(string='Akses Stasiun (AQ)', required=True)
    # t_psdm  =  fields.Integer(string='Pengelolaan SDM (K)', required=True)
 
    # k_ticket    =  fields.Integer(string='Kebijakan Layanan Ticketing (L)', required=True)
    # k_ticket_u  =  fields.Integer(string='Kebijakan Layanan Umum (M)', required=True)
    # k_ticket_n  =  fields.Integer(string='Kebijakan layanan penumpang prioritas (N)', required=True)
    # k_ticket_ap =  fields.Integer(string='Pengoperasian rolling door dan kunci stasiun (AP)', required=True)
    # k_ticket_ar =  fields.Integer(string='Pengelolaan perlengkapan stasiun (AR)', required=True)
    # k_ticket_o  =  fields.Integer(string='Pengetahuan fasilitas penumpang dan area sekitar stasiun (O)', required=True)
    # k_ticket_p  =  fields.Integer(string='Lost&Found System (P)', required=True)

    # p_ticket_2q =  fields.Integer(string='Effective Handling Complain - Level 2 (Q)', required=True)
    # p_ticket_3q =  fields.Integer(string='Effective Handling Complain - Level 3 (Q)', required=True)
    # p_ticket_4q =  fields.Integer(string='Effective Handling Complain - Level 4 (Q)', required=True)
    # pp_ticket_1q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 1 (R)', required=True)
    # pp_ticket_2q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 2 (R)', required=True)
    # pp_ticket_3q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 3 (R)', required=True)
    # pp_ticket_4q =  fields.Integer(string='Pelanggaran dan Penindakan Penumpang - Level 4 (R)', required=True)

    



class EventRegistrasion(models.Model):
    _inherit = "event.registration"
    
    employee_id  = fields.Many2one(string='Employee', comodel_name='hr.employee', ondelete='restrict')
    pre_test_ids = fields.Many2many(string='Pre-Test Form', comodel_name='survey.survey')
    post_test_ids = fields.Many2many(string='Post-Test Form', comodel_name='survey.survey')
    topic_id  = fields.Many2one(string='Topic', comodel_name='traning.topic', compute='test_many')

    def button_test(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'survey.survey',
            'views': [(False, 'tree')],
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {},
            'domain': ['|',('id', 'in', self.pre_test_ids.ids),('id', 'in', self.post_test_ids.ids)],
        }


    def test_many(self):
        try:
            self.pre_test_ids = [self.event_id.pre_test_id.id]
            self.post_test_ids = [self.event_id.post_test_id.id]
            self.topic_id = self.event_id.training_id.id
        except:
            pass

class EventEvent(models.Model):
    _inherit = "event.event"

    training_id  = fields.Many2one(string='Training Topic', comodel_name='training.topic', ondelete='restrict')
    trainer_id  = fields.Many2one(string='Trainer', comodel_name='res.partner', ondelete='restrict')
    pre_test_id = fields.Many2one(string='Pre-Test Form', comodel_name='survey.survey', ondelete='restrict')
    post_test_id = fields.Many2one(string='Post-Test Form', comodel_name='survey.survey', ondelete='restrict')

class TrainingCompetency(models.Model):
    _name = "training.competency"

    name = fields.Char(string='Name')
    # planned_date = fields.Char(string="Planed Date")

class TrainingTopic(models.Model):
    _name = "training.topic"

    name = fields.Char(string='Name', required=True)
    desc = fields.Char(string='Desc')
    competency_id = fields.Many2one(string='Competency', comodel_name='training.competency')
    code = fields.Char(string='Training Code', required=True)

    @api.constrains('code')
    @api.one
    def _code_karakter(self):
        if len(self.code) > 3 :
            raise ValidationError("Code Training tidak boleh melebihi dari 3 Karakter")
    

class TrainingRecomendation(models.Model):
    _name = "training.recomendation"
    
    employee_id = fields.Many2one('hr.employee', string='Employee', default=lambda self: self.env['hr.employee'].search([('user_id','=',self.id)], limit=1).id)    
    station_id = fields.Many2one(string='Station', comodel_name='master.station', ondelete='restrict')
    department_id = fields.Many2one(string='Department', comodel_name='hr.department', ondelete='restrict', related='employee_id.department_id')
    job_id = fields.Many2one(string='Job Position', comodel_name='hr.job', ondelete='restrict', related='employee_id.job_id')
    training_topic = fields.Many2one(string='Competency', comodel_name='training.competency')
    planned_date = fields.Date(string="Planned Date")
    
    remarks = fields.Text('Remarks')
    # employee = fields.Many2one('hr.employee', string='Employee', default=lambda self: self.env['hr.employee'].search([('user_id','=',self.id)], limit=1).id)    
    # station = fields.Many2one('master.station', string='Station')
    # department = fields.Many2one('hr.department', string='Department', related="employee_id.department_id")
    # job_id = fields.Many2one('hr.job', string="Job", related="employee_id.job_id")
    # post_date = datetime(String='Posted Date')

class SurveyLabel(models.Model):
    _inherit = 'survey.label'

class SurveyQuestion(models.Model):  
    _inherit = 'survey.question'