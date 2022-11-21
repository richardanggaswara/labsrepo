# dodyakj --- dodyakj
from odoo import api,fields,models,modules
from odoo.tools.translate import _
from datetime import datetime,timedelta
from odoo.addons.odoo_multi_channel_sale.tools import extract_list as EL
from odoo.exceptions import Warning, ValidationError, UserError
import base64
import logging
import pyshopee
_logger	 = logging.getLogger(__name__)

class MultiChannelSale(models.Model):
    _inherit = "multi.channel.sale"
