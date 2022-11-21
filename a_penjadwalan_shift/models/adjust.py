# dodyakj --- dodyakj
from odoo import api, fields, models, modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger = logging.getLogger(__name__)


class MobileStaff(models.Model):
    _name = "mobile.staff"

    name = fields.Many2one(
        string='Station', comodel_name='master.station', ondelete='restrict')
    role = fields.Many2one(
        string='Role', comodel_name='shift.role', ondelete='restrict')
    date = fields.Date(string='Date')
    start_time = fields.Float(
        string='Start Time', related='shift_type.tanggal_mulai')
    end_time = fields.Float(
        string='End Time', related='shift_type.tanggal_selesai')
    shift_type = fields.Many2one(
        string='Shift Type ', comodel_name='shift.type', ondelete='restrict')
    shift_code = fields.Char(related='shift_type.code')
    # states = fields.Selection(string='Status', selection=[('tosubmit', 'To Submit'),('toapprove', 'To Approve'),('done', 'Done')], delault='tosubmit')
    states = fields.Selection(
        [
            ("toapprove", "To Approve"),
            ("approved", "Approved"),
            ('refuse', 'Refused')
        ],
        string='Status',
        default='toapprove',
        readonly=True,
        track_visibility="onchange"
    )

    available_ids = fields.One2many(
        string='Available Resouce', comodel_name='available.resource', inverse_name='mobile_id')

    def approve_mobile(self):
        self.write({"states": "approved"})

    @api.onchange('shift_type')
    def onchange_shift_type(self):
        self.update({'available_ids': False})
        _logger.warning(self.shift_type)
        _logger.warning(self.shift_type.id)
        shift = self.env['shift.shift'].search(
            [('shift_type_id', '=', self.shift_type.id)])
        _logger.warning(shift)
        vals = []
        for s in shift:
            _logger.warning(s.station.id)
            vals.append((0, 0,  {'station': s.station.id, 'name': s.employee_id.name or '',
                        'shift_type': s.shift_type_id.id, 'role': s.rules.id or ''}))
            # _logger.warning(vals)
        self.update({'available_ids': vals})
        # self.write({'available_ids': vals})
        _logger.warning(vals)
        _logger.warning(self.available_ids)


class AdjustStaff(models.Model):
    _name = "adjust.staff"

    name = fields.Many2one(
        string='Station', comodel_name='master.station', ondelete='restrict')
    role = fields.Many2one(
        string='Role', comodel_name='shift.role', ondelete='restrict')
    date = fields.Date(string='Date')
    start_time = fields.Float(
        string='Start Time', related='shift_type.tanggal_mulai')
    end_time = fields.Float(
        string='End Time', related='shift_type.tanggal_selesai')
    shift_type = fields.Many2one(
        string='Shift Type ', comodel_name='shift.type', ondelete='restrict')
    shift_code = fields.Char(related='shift_type.code')
    states = fields.Selection(string='Status', selection=[(
        'tosubmit', 'To Submit'), ('toapprove', 'To Approve'), ('done', 'Done')], delault='tosubmit')

    available_ids = fields.One2many(
        string='Available Resouce', comodel_name='available.resource', inverse_name='adjust_id')

    @api.onchange('shift_type')
    def onchange_shift_type(self):
        self.update({'available_ids': False})
        _logger.warning(self.shift_type)
        _logger.warning(self.shift_type.id)
        shift = self.env['shift.shift'].search(
            [('shift_type_id', '=', self.shift_type.id)])
        _logger.warning(shift)
        vals = []
        for s in shift:
            _logger.warning(s.station.id)
            vals.append((0, 0,  {'station': s.station.id, 'name': s.employee_id.name or '',
                        'shift_type': s.shift_type_id.id, 'role': s.rules.id or ''}))
            # _logger.warning(vals)
        self.update({'available_ids': vals})
        # self.write({'available_ids': vals})
        _logger.warning(vals)
        _logger.warning(self.available_ids)

        # self.env['available.resource'].create({'station': s.station.id, 'name': s.name, 'shift_type': s.shift_type_id.id,'role': s.rules,'adjust_id':self.id})


class AvailableResource(models.Model):
    _name = "available.resource"

    station = fields.Many2one(
        string='Station', comodel_name='master.station', ondelete='restrict')
    name = fields.Char('Name')
    shift_type = fields.Many2one(
        string='Shift Type ', comodel_name='shift.type', ondelete='restrict')
    role = fields.Many2one(
        string='Role', comodel_name='shift.role', ondelete='restrict')
    select = fields.Boolean()

    adjust_id = fields.Many2one(
        string='Adjust', comodel_name='adjust.staff', ondelete='restrict')
    mobile_id = fields.Many2one(
        string='Mobile', comodel_name='mobile.staff', ondelete='restrict')
