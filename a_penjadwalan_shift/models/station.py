# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
# from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)


class StationMaster(models.Model):
    _name = "master.station"

    name = fields.Char('Nama', required=True)
    sequence = fields.Integer('Sequence', required=True)
    code = fields.Char('Code Station', required=True)
    departement = fields.Many2one(string='Department', comodel_name='hr.department', ondelete='restrict')
    master = fields.Boolean('Master')
    desc = fields.Text('Desc')