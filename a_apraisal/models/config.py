# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
from datetime import datetime,timedelta
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
_logger	 = logging.getLogger(__name__)

class DisciplinaryCategory(models.Model):
    _inherit = "discipline.category"

    categ_id =  fields.Many2one(string='Category Group', comodel_name='discipline.category.group', ondelete='restrict')
    weight = fields.Float(string='')
    max_point =  fields.Integer(string='')
    penalty = fields.Integer(string='Penalty per Accurance')

class DisciplinaryCategoryGroup(models.Model):
    _name = "discipline.category.group"

    name = fields.Char()



class DisciplinaryActionCreation(models.Model):
    _inherit = "disciplinary.action"

    job_id = fields.Many2one(string='Job Position', comodel_name='hr.job', ondelete='restrict')
    date = fields.Date(string='Date')
    desc = fields.Char(string='Description')
    categ_id =  fields.Many2one(string='Category Group', comodel_name='discipline.category.group', ondelete='restrict', related='discipline_reason.categ_id')
