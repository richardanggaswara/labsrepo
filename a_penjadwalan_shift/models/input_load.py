# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.addons.a_role.models.models import _get_uid_from_group
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)


class LoadRequirment(models.Model):
    _name = "input.load"
    _inherit = ['mail.thread']

    name = fields.Char('Description')
    date = fields.Date()
    tanggal_mulai = fields.Datetime(string='Period')
    tanggal_selesai = fields.Datetime(string='Date')

    type_load =  fields.Selection([('weekday', 'Weekday'),('weekend', 'Weekend'),('holiday', 'Holiday')], default='weekday')

    weekday_ids = fields.One2many('man.power', 'wd_id', copy=True,)
    weekend_ids = fields.One2many('man.power', 'we_id', copy=True,)
    holiday_ids = fields.One2many('man.power', 'hl_id', copy=True,)

    @api.model
    def default_get(self, fields_list):
        res = super(LoadRequirment, self).default_get(fields_list)
        vals_weekday = []
        vals_weekend = []
        vals_holiday = []
        station = self.env['master.station'].search([], order="sequence asc")
        for s in station:
            vals_weekday.append((0, 0, {'name': s.code, 'type_load': 'weekday'}))
            vals_weekend.append((0, 0, {'name': s.code, 'type_load': 'weekend'}))
            vals_holiday.append((0, 0, {'name': s.code, 'type_load': 'holiday'}))
        res.update({'weekday_ids': vals_weekday})
        res.update({'weekend_ids': vals_weekend})
        res.update({'holiday_ids': vals_holiday})
        return res

    def email_to_sm(self):
        user_ids = _get_uid_from_group(self, self.env.ref("a_role.group_station_manager").id)
        partner_ids = [self.env["res.users"].browse(uid).partner_id.id for uid in user_ids]
        self.message_post(
            email_from="gaas@jakartamrt.co.id",
            body="[THIS IS AUTOMATIC MESSAGING SYSTEM. NO REPLY] \n Dear User, Load requirements has been updated. \n Please custom the scheduling refer to this change. \n Thanks",
            subject=self.name,
            partner_ids=partner_ids,
            message_type="email",
            subtype="mail.mt_comment",
        )

    
class ManPower(models.Model):
    _name = "man.power"

    name =  fields.Char(string='Code', required=True)

    type_load =  fields.Selection([('weekday', 'Weekday'),('weekend', 'Weekend'),('holiday', 'Holiday')], default='weekday')

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

    wd_id = fields.Many2one(string='Weekday', comodel_name='input.load')
    we_id = fields.Many2one(string='Weekend', comodel_name='input.load')
    hl_id = fields.Many2one(string='Holiday', comodel_name='input.load')

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

