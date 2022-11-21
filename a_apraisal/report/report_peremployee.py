# dodyakj --- dodyakj
import time
import base64
import io
import itertools
import calendar
from io import StringIO
from odoo.tools.misc import xlwt
import xlsxwriter
from dateutil import relativedelta
from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.exceptions import  ValidationError
import logging
_logger = logging.getLogger(__name__)


class WizardPerEmployee(models.TransientModel):
    _name = 'wizard.apraisal.peremployee'
    _description = 'Pelanggaran per Frontliners'

    filename = fields.Char()
    data = fields.Binary()

    month  = fields.Selection([\
                                ('1', 'January'),\
                                ('2', 'February'),\
                                ('3', 'Maret'),\
                                ('4', 'April'),\
                                ('5', 'Mei'),\
                                ('6', 'Juni'),\
                                ('7', 'Juli'),\
                                ('8', 'Agustus'),\
                                ('9', 'September'),\
                                ('10', 'Oktober'),\
                                ('11', 'November'),\
                                ('12', 'Desember')\
                                ], required=True)
    year = fields.Integer(required=True, default=2021)
    station_id = fields.Many2one('master.station', string="Station")

    # @api.multi
    # @api.constrains('startdate', 'enddate')
    # def date_constrains(self):
    #     for rec in self:
    #         if rec.enddate < rec.startdate:
    #             raise ValidationError(_('Sorry, End Date Must be greater Than Start Date...'))


    def get_data(self):
        # search_param = []
        query = """
                select
                	 he.id as id,
                	 he.name as name,
                	 ms.name as station
                from
                	public.hr_employee as he
                    left join master_station ms on ms.id = he.station_id
                    left join disciplinary_action dc on dc.employee_name  = he.id 
                
                where
                    dc.date >= '%s-1-%s'
                and
                    dc.date <= '%s-%s-%s'
                """% (str(self.year), str(self.month), str(self.year), str(self.month), str(calendar.monthrange(self.year, int(self.month))[1]))
        if self.station_id:
            query = query + 'and ms.id = %s'%(self.station_id.id)



        self.env.cr.execute(query)
        result = self.env.cr.dictfetchall()
        return result


    def action_export(self):
        workbook = xlwt.Workbook(encoding="utf-8")
        get = self.get_data()
        col = 0
        judul = 'Pelanggaran Per Frontliners'
        sheet = workbook.add_sheet('Pelanggaran')
        sheet.normal_magn = 80
        sheet.show_grid = False
        style_no_bold = xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin;'
            'align: vert centre, horz center; font: name Helvetica Neue;')
        style_header_no = xlwt.easyxf('font: colour black, bold 1, name Helvetica Neue; borders: left thin, right thin, top thin,'
            'bottom thin; align: vert centre, horz center; pattern: pattern solid, fore_colour yellow;')
        style_header = xlwt.easyxf('font: colour black, bold 1, name Helvetica Neue; borders: left thin, right thin, top thin,'
            'bottom thin; align: vert centre, horz center; pattern: pattern solid, fore_colour green;')
        style_header5 = xlwt.easyxf('font: colour black, bold 1, name Helvetica Neue; borders: left thin, right thin, top thin,'
            'bottom thin; align: vert centre, horz center; pattern: pattern solid, fore_colour white;')
        style_headerblue= xlwt.easyxf('font: colour black, bold 1, name Helvetica Neue; borders: left thin, right thin, top thin,'
            'bottom thin; align: vert centre, horz center; pattern: pattern solid, fore_colour aqua;')
        style_judul = xlwt.easyxf('font: colour black, bold 1, height 280, name Helvetica Neue; align: vert centre, horz center;')
        style_judul_2 = xlwt.easyxf('font: colour black, bold 1, height 180, name Helvetica Neue; align: vert center, horz left;')

        col_width = 256 * 25
        row = 6
        try:
            for i in itertools.count():
                sheet.col(i).width = col_width
                sheet.col(0).width = 256 * 5
                # sheet.col(1).width = 256 * 45
                # sheet.col(2).width = 256 * 20
                # sheet.col(3).width = 256 * 30
                # sheet.col(5).width = 256 * 55
                sheet.row(i).height = 5 * 75
                sheet.set_panes_frozen(True)
                sheet.set_horz_split_pos(row + 1)
                sheet.set_remove_splits(True)
        except ValueError:
            pass

        period = self.month + ' - ' + str(self.year)
        nama_penerima_jaminan = self.station_id.name if self.station_id else 'All Station'

        sheet.write_merge(0, 0, 0, 10, judul, style_judul)
        sheet.write_merge(1, 1, 0, 10, "LOGBOOK PELANGGARAN", style_judul)
        sheet.write_merge(2, 2, 0, 10, 'Periode: {}'.format(period), style_judul)
        sheet.write_merge(3, 3, 0, 10, 'Station {}'.format(nama_penerima_jaminan), style_judul_2)

        plus = 4
        no = 0
        for x in get:
            sheet.write_merge(8+no, 8+no, 0, 10, 'Name : {}'.format(x['name']), style_judul_2)
            sheet.write_merge(5+plus, 10+plus-2, 0, 0, 'No', style_header_no)
            sheet.write_merge(5+plus, 9+no, 1, 6, 'Attitude', style_header)
            sheet.write_merge(5+plus+1, 9+1+no, 1, 2, '5%', style_header5)
            sheet.write_merge(5+plus+1, 9+1+no, 3, 4, '5%', style_header5)
            sheet.write_merge(5+plus+1, 9+1+no, 5, 6, '5%', style_header5)
            sheet.write_merge(5+plus+2, 9+2+no, 1, 2, 'Kesopanan', style_header)
            sheet.write_merge(5+plus+2, 9+2+no, 3, 4, 'Kerapihan', style_header)
            sheet.write_merge(5+plus+2, 9+2+no, 5, 6, 'Kebersihan', style_header)
            sheet.write_merge(5+plus+3, 9+3+no, 1, 1, 'Tgl', style_header_no)
            sheet.write_merge(5+plus+3, 9+3+no, 2, 2, 'Keterangan', style_header_no)
            sheet.write_merge(5+plus+3, 9+3+no, 3, 3, 'Tgl', style_header_no)
            sheet.write_merge(5+plus+3, 9+3+no, 4, 4, 'Keterangan', style_header_no)
            sheet.write_merge(5+plus+3, 9+3+no, 5, 5, 'Tgl', style_header_no)
            sheet.write_merge(5+plus+3, 9+3+no, 6, 6, 'Keterangan', style_header_no)
            
            sheet.write_merge(5+plus+4, 9+4+no, 0, 0, '1', style_header5)
            sheet.write_merge(5+plus+5, 9+5+no, 0, 0, '2', style_header5)
            sheet.write_merge(5+plus+6, 9+6+no, 0, 0, '3', style_header5)
            sheet.write_merge(5+plus+7, 9+7+no, 0, 0, '4', style_header5)
            sheet.write_merge(5+plus+8, 9+8+no, 0, 0, '5', style_header5)
            
            for y in range(6):
                sheet.write_merge(5+plus+4, 9+4+no, y+1, y+1, '', style_header5)
                sheet.write_merge(5+plus+5, 9+5+no, y+1, y+1, '', style_header5)
                sheet.write_merge(5+plus+6, 9+6+no, y+1, y+1, '', style_header5)
                sheet.write_merge(5+plus+7, 9+7+no, y+1, y+1, '', style_header5)
                sheet.write_merge(5+plus+8, 9+8+no, y+1, y+1, '', style_header5)
            
            
            sheet.write_merge(5+plus+9, 9+9+no, 1, 2, '0', style_headerblue)
            sheet.write_merge(5+plus+10, 9+10+no, 1, 2, '5', style_header_no)
            sheet.write_merge(5+plus+9, 9+9+no, 3, 4, '0', style_headerblue)
            sheet.write_merge(5+plus+10, 9+10+no, 3, 4, '5', style_header_no)
            sheet.write_merge(5+plus+9, 9+9+no, 5, 6, '0', style_headerblue)
            sheet.write_merge(5+plus+10, 9+10+no, 5, 6, '5', style_header_no)
            sheet.write_merge(5+plus+9, 9+9+no, 0, 0, 'Jumlah', style_headerblue)
            sheet.write_merge(5+plus+10, 9+10+no, 0, 0, 'POINT', style_header_no)

            


            plus += 14
            no += 14

        # col1 = 11 + plus
        # no = 0
        # for x in get:
        #     no += 1
        #     sheet.write(col1, 0, no, style_no_bold)
        #     sheet.write(col1, 1, x['name'], style_no_bold)
        #     sheet.write(col1, 2, x['station'], style_no_bold)

        #     col1 += 1

        file_data = io.BytesIO()
        workbook.save(file_data)
        self.write({
                'data': base64.encodestring(file_data.getvalue()),
                'filename': judul+' ' + period + '.xls',
            })

        view = self.env.ref('a_apraisal.wizard_report_peremployee_view_form')
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pelanggaran per Frontliners ' + period,
            'res_model': 'wizard.apraisal.peremployee',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(view.id, 'form')],
            'target': 'new'
        }
