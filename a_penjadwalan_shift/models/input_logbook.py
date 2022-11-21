# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)


class LoadLoogbook(models.Model):
    _name = "input.logbook"

    name = fields.Date('Date')
    act = fields.Text('Activity / Event / Report')
    states =  fields.Selection([('open', 'Open'),('close', 'Close'),('pending', 'Pending'),('information', 'Information'),], string="Status", default='open')
    dept_id = fields.Many2one(string='Related Dept', comodel_name='hr.department')
    sm_id = fields.Many2one(string='SM Name', comodel_name='hr.employee')
    shift =  fields.Selection([('pagi', 'Pagi'),('siang', 'Siang'),('malam', 'Malam')], string="Shift", default="pagi")
    notes = fields.Text('Notes')
    stat_handover =  fields.Selection([('open', 'Open'),('pending', 'Pending'),('close', 'Close')], string="Status Hand Over", default='open')
    closed_by = fields.Many2one(string='Closed By', comodel_name='res.users')
    link_form = fields.Text('Link Form Patrol Share Point')