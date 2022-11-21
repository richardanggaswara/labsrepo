# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
import time
import base64
import io
import itertools
import calendar
from io import StringIO
from odoo.tools.misc import xlwt
import xlsxwriter
from dateutil import relativedelta
from datetime import date, datetime, timedelta
import logging
_logger	 = logging.getLogger(__name__)

class MultiChannelSale(models.Model):
    _inherit = "hr.overtime"


    type = fields.Selection([('cash', 'Cash'),
                             ('leave', 'Leave ')], default='cash')
    station_id = fields.Many2one(string='Station', comodel_name='master.station', ondelete='restrict')
    conversion_hour = fields.Float('Conversion Hours (Rate)', compute='onchange_day_no_tmp')

    @api.one
    def onchange_day_no_tmp(self):
        if self.overtime_type_id:
            for o in self.overtime_type_id:
                for c in o.rule_line_ids:
                    if ((self.days_no_tmp >= c.to_hrs and self.days_no_tmp <= c.to_hrs) or (self.days_no_tmp >= c.from_hrs and self.days_no_tmp <= c.from_hrs) or (self.days_no_tmp >= c.from_hrs and self.days_no_tmp <= c.from_hrs)) :
                        self.conversion_hour = c.hrs_amount 

