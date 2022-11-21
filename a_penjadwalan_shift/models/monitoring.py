# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
import calendar
_logger	 = logging.getLogger(__name__)

class LoadMonitoring(models.Model):
    _name = "input.monitoring"

    name = fields.Char('Description')
    date = fields.Date()
    tanggal_mulai = fields.Date(string='Period')
    tanggal_selesai = fields.Date(string='Date')

    load_date =  fields.Integer(string='Date')

    tanggal_1 = fields.One2many('man.hour', 'tanggal_1_id', copy=True)
    tanggal_2 = fields.One2many('man.hour', 'tanggal_2_id', copy=True)
    tanggal_3 = fields.One2many('man.hour', 'tanggal_3_id', copy=True)
    tanggal_4 = fields.One2many('man.hour', 'tanggal_4_id', copy=True)
    tanggal_5 = fields.One2many('man.hour', 'tanggal_5_id', copy=True)
    tanggal_6 = fields.One2many('man.hour', 'tanggal_6_id', copy=True)
    tanggal_7 = fields.One2many('man.hour', 'tanggal_7_id', copy=True)
    tanggal_8 = fields.One2many('man.hour', 'tanggal_8_id', copy=True)
    tanggal_9 = fields.One2many('man.hour', 'tanggal_9_id', copy=True)
    tanggal_10 = fields.One2many('man.hour', 'tanggal_10_id', copy=True)
    tanggal_11 = fields.One2many('man.hour', 'tanggal_11_id', copy=True)
    tanggal_12 = fields.One2many('man.hour', 'tanggal_12_id', copy=True)
    tanggal_13 = fields.One2many('man.hour', 'tanggal_13_id', copy=True)
    tanggal_14 = fields.One2many('man.hour', 'tanggal_14_id', copy=True)
    tanggal_15 = fields.One2many('man.hour', 'tanggal_15_id', copy=True)
    tanggal_16 = fields.One2many('man.hour', 'tanggal_16_id', copy=True)
    tanggal_17 = fields.One2many('man.hour', 'tanggal_17_id', copy=True)
    tanggal_18 = fields.One2many('man.hour', 'tanggal_18_id', copy=True)
    tanggal_19 = fields.One2many('man.hour', 'tanggal_19_id', copy=True)
    tanggal_20 = fields.One2many('man.hour', 'tanggal_20_id', copy=True)
    tanggal_21 = fields.One2many('man.hour', 'tanggal_21_id', copy=True)
    tanggal_22 = fields.One2many('man.hour', 'tanggal_22_id', copy=True)
    tanggal_23 = fields.One2many('man.hour', 'tanggal_23_id', copy=True)
    tanggal_24 = fields.One2many('man.hour', 'tanggal_24_id', copy=True)
    tanggal_25 = fields.One2many('man.hour', 'tanggal_25_id', copy=True)
    tanggal_26 = fields.One2many('man.hour', 'tanggal_26_id', copy=True)
    tanggal_27 = fields.One2many('man.hour', 'tanggal_27_id', copy=True)
    tanggal_28 = fields.One2many('man.hour', 'tanggal_28_id', copy=True)
    tanggal_29 = fields.One2many('man.hour', 'tanggal_29_id', copy=True)
    tanggal_30 = fields.One2many('man.hour', 'tanggal_30_id', copy=True)
    tanggal_31 = fields.One2many('man.hour', 'tanggal_31_id', copy=True)


    # @api.onchange('tanggal_selesai')
    # def onchange_field(self):
        # last_day_of_month = calendar.monthrange(2019,8)[1]
        # _logger.warning(self.tanggal_selesai.year)
        # _logger.warning(self.tanggal_selesai.month)
        # _logger.warning(self.tanggal_selesai.day)
        # self.load_date = self.tanggal_selesai.day
    
    @api.model
    def default_get(self, fields_list):
        res = super(LoadMonitoring, self).default_get(fields_list)
        vals= []
        station = self.env['master.station'].search([], order="sequence asc")
        for s in station:
            vals.append((0, 0, {'name': s.code}))
        for seq in range(1,32):
            res.update({'tanggal_'+str(seq): vals})
        return res

    
class ManHour(models.Model):
    _name = "man.hour"

    name =  fields.Char(string='Code', required=True)
    
    hours  = fields.Integer(string='Hour')

    empat  = fields.Integer(string='4')
    lima  = fields.Integer(string='5')
    enam  = fields.Integer(string='6')
    tujuh  = fields.Integer(string='7')
    delapan  = fields.Integer(string='8')
    sembilan  = fields.Integer(string='9')
    sepuluh  = fields.Integer(string='10')
    sebelas  = fields.Integer(string='11')
    duabelas  = fields.Integer(string="12")
    tigabelas  = fields.Integer(string='13')
    empatbelas  = fields.Integer(string='14')
    limabelas  = fields.Integer(string='15')
    enambelas  = fields.Integer(string='16')
    tujuhbelas  = fields.Integer(string='17')
    delapanbelas  = fields.Integer(string='18')
    sembilanbelas  = fields.Integer(string='19')
    duapuluh  = fields.Integer(string='20')
    duasatu  = fields.Integer(string='21')
    duadua  = fields.Integer(string='22')
    duatiga  = fields.Integer(string='23')
    
    
    total  = fields.Integer(string='Total', compute='total_manpower')

    tanggal_1_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_2_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_3_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_4_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_5_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_6_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_7_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_8_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_9_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_10_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_11_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_12_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_13_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_14_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_15_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_16_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_17_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_18_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_19_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_20_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_21_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_22_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_23_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_24_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_25_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_26_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_27_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_28_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_29_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_30_id = fields.Many2one(string='Load', comodel_name='input.monitoring')
    tanggal_31_id = fields.Many2one(string='Load', comodel_name='input.monitoring')

    @api.one
    def total_manpower(self):
        self.total = \
                    self.empat + \
                    self.lima + \
                    self.enam + \
                    self.tujuh + \
                    self.delapan + \
                    self.sembilan + \
                    self.sepuluh + \
                    self.sebelas + \
                    self.duabelas + \
                    self.tigabelas + \
                    self.empatbelas + \
                    self.limabelas + \
                    self.enambelas + \
                    self.tujuhbelas + \
                    self.delapanbelas + \
                    self.sembilanbelas + \
                    self.duapuluh + \
                    self.duasatu + \
                    self.duadua + \
                    self.duatiga \



