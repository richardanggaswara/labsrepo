# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)


class MyShiftGroup(models.Model):
    _name = "shift.group"
    _rec_name = 'name'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    desc = fields.Char()
    station = fields.Many2one('master.station')
    department = fields.Many2one('hr.department')
    period_start = fields.Date('Date', required=True)
    period_end = fields.Date('Date', required=True)
    responsible = fields.Many2one('res.users')
    approver = fields.Many2one('res.users')

    shift_ids =  fields.Many2many('shift.shift', compute='shift_many')
    states = fields.Selection([("toapprove","To Approve"),("approved","Approved"),('refuse','Refused')], string='Status', default='toapprove')

    def shift_many(self):
        self.shift_ids = self.env['shift.shift'].search([('shift_group_id','=',self.id)]).ids

    def approve(self):
        self.states = 'approved'
        self.responsible = self.env.user.id
        self.approver = self.env.user.id

    def refuse(self):
        self.states = 'refuse'
        self.responsible = self.env.user.id
        self.approver = self.env.user.id
        

    def reset(self):
        self.states = 'toapprove'
        self.responsible = False
        self.approver = False

class MyShift(models.Model):
    _name = "shift.shift"
    
    name = fields.Char(string='Shift')
    states = fields.Selection([("toapprove","To Approve"),("approved","Approved"),('refuse','Refused')], string='Status', default='toapprove')
    type_shift = fields.Selection([("days","Days"),("hours","Hours")], string='Type', default='days')
    shift_type_id = fields.Many2one(string='Shift Type', comodel_name='shift.type', ondelete='restrict', required=True)
    duration = fields.Float(string='Duration')
    tanggal_mulai = fields.Datetime(string='Date')
    # date_start = fields.Date(string='Date')
    tanggal_selesai = fields.Datetime(string='Date')
    date_end = fields.Date(string='Date')
    desc = fields.Char(string='Description')
    # mode_id = fields.Many2one(string='Mode', comodel_name='shift.mode', ondelete='restrict', required=False)
    employee_id = fields.Many2one(string='Employee', comodel_name='hr.employee', ondelete='restrict', required=True)
    department_id = fields.Many2one(string='Department', comodel_name='hr.department', ondelete='restrict', related='employee_id.department_id')
    flag = fields.Boolean(string='Payslip')
    comment = fields.Text(string='Comment')
    job_position = fields.Many2one(string='Job Position', comodel_name='hr.job', ondelete='restrict', related='employee_id.job_id')
    rules = fields.Many2one(string='Role', comodel_name='shift.role', ondelete='restrict')
    shift_group_id =  fields.Many2one(string='Shift Group', comodel_name='shift.group', ondelete='restrict')
    station =  fields.Many2one(string='Station', comodel_name='master.station', ondelete='restrict')


    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} on {} ".format(record.employee_id.name, record.shift_type_id.name)))
        return result

    def approve(self):
        self.states = 'approved'

    def refuse(self):
        self.states = 'refuse'

    def reset(self):
        self.states = 'toapprove'

    @api.onchange('shift_type_id')
    def onchange_shift_type_id(self):
        _logger.warning('self.shift_type_id.tanggal_mulai')
        _logger.warning(self.shift_type_id.tanggal_mulai)
        _logger.warning('self.shift_type_id.tanggal_selesai')
        _logger.warning(self.shift_type_id.tanggal_selesai)
        
        _logger.warning('self.tanggal_mulai')
        _logger.warning(self.tanggal_mulai)
        _logger.warning('self.tanggal_selesai')
        _logger.warning(self.tanggal_selesai)
        try:
            mulai = str(self.shift_type_id.tanggal_mulai).split('.')
            self.tanggal_mulai.replace(minute=int(mulai[1]), hour=int(mulai[0]))
            selesai = str(self.shift_type_id.tanggal_selesai).split('.')
            self.tanggal_selesai.replace(minute=int(selesai[1]), hour=int(selesai[0]))
        except:
            pass

        # self.tanggal_mulai = self.shift_type_id.tanggal_mulai
        # self.tanggal_selesai = self.shift_type_id.tanggal_selesai
    
    

class MyRoles(models.Model):
    _name = "shift.role"

    name = fields.Char(string='Roles Name', required=True)
    desc = fields.Char(string='Description')
    

class MyShiftType(models.Model):
    _name = "shift.type"

    name = fields.Char(string='Shift Name', required=True)
    code = fields.Char(string='Shift Code')
    desc = fields.Char(string='Description')
    tanggal_mulai = fields.Float(string='Time')
    tanggal_selesai = fields.Float(string='End Date')
    color = fields.Char(string='Color')


    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}  ".format(record.code)))
        return result


class MyShiftMode(models.Model):
    _name = "shift.mode"

    name = fields.Char(string='Mode Name')