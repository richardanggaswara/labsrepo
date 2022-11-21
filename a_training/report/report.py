# denta

from odoo import http
from odoo.http import content_disposition, request
from io import StringIO
from odoo.tools.misc import xlwt
from dateutil import relativedelta
from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.exceptions import  ValidationError
import time
import base64
import io
import itertools
import calendar
import xlsxwriter
import logging
_logger = logging.getLogger(__name__)

class WizardOvertimeReport(models.TransientModel):
    _name = 'wizard.overtime.report'
    _description = 'Training Report'

    filename = fields.Char()
    data = fields.Binary()

    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    station_id = fields.Many2one('master.station', string="Station")

    def get_excel_report(self):
        # redirect ke controller /sale/excel_report untuk generate file excel
        return {
            'type': 'ir.actions.act_url',
            'url': '/a_overtime/report/%s' % (self.id),
            'target': 'new',
        }

    def get_data(self):
        # search_param = []
        query = """
                select
                	 he.id as id,
                	 he.name as name,
                	 ms.name as station,
                     dc.conversion_hour as conversion_hour,
                     dc.duration_type as duration_type,
                     he.identification_id as nip,
                     ms.code as area,
                     dc.conversion_hour as jam_konversi,
                     dc.days_no_tmp as jam_aktual,
                     dc.cash_hrs_amount as nominal_lembur,
                     hc.wage as gaji,
                     hj.name as unit
                from
                	public.hr_employee as he
                    left join hr_contract as hc on hc.employee_id = he.id
                    left join master_station ms on ms.id = he.station_id
                    left join hr_overtime dc on dc.employee_id  = he.id 
                    left join hr_job hj on hj.id = hc.job_id
                
                where
                    dc.date_from >= '%s'
                and
                    dc.date_to <= '%s'
                """% (str(self.start_date), str(self.end_date))
        if self.station_id:
            query = query + 'and dc.station_id = %s'%(self.station_id.id)



        self.env.cr.execute(query)
        result = self.env.cr.dictfetchall()
        return result


    def action_export(self):
        workbook = xlwt.Workbook(encoding="utf-8")
        get = self.get_data()
        col = 0
        judul = 'Overtime Summary'
        sheet = workbook.add_sheet('Overtime')
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
        row = 4
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

        period = str(self.start_date) + ' s.d ' + str(self.end_date)
        nama_penerima_jaminan = self.station_id.name if self.station_id else 'All Station'
        station = self.station_id.name

        sheet.write_merge(0, 0, 0, 8, judul, style_judul)
        sheet.write_merge(1, 1, 0, 8, 'Station {}'.format(nama_penerima_jaminan), style_judul)
        sheet.write_merge(2, 2, 0, 8, 'Periode: {}'.format(period), style_judul)
        # sheet.write_merge(3, 3, 0, 10, 'Station {}'.format(nama_penerima_jaminan), style_judul_2)

        plus = 2

        # judul tabel
        sheet.write(4, 0, 'No.', style_no_bold)
        sheet.write(4, 1, 'NIP', style_no_bold)
        sheet.write(4, 2, 'Nama', style_no_bold)
        sheet.write(4, 3, 'Unit', style_no_bold)
        sheet.write(4, 4, 'Area', style_no_bold)
        sheet.write(4, 5, 'Gaji & Tunjangan', style_no_bold)
        sheet.write(4, 6, 'Jam Actual', style_no_bold)
        sheet.write(4, 7, 'Jam Konversi', style_no_bold)
        sheet.write(4, 8, 'Nominal Lembur', style_no_bold)

        plus = 2
        no = 1
        row = 6
        
        # cari sale order untuk sales person terpilih pada rentang tanggal yang dipilih user
        overtimes = request.env['hr.overtime'].search([('station_id','=', self.station_id.id),('date_from','>=', self.start_date), ('date_to','<=', self.end_date)])
        for x in get:
            # content / isi report
            sheet.write(row, 0, format(no), style_no_bold) #no
            sheet.write(row, 1, x["nip"], style_no_bold) #NIP
            sheet.write(row, 2, x["name"], style_no_bold) #Nama
            sheet.write(row, 3, x["unit"], style_no_bold) #Unit
            sheet.write(row, 4, x["area"], style_no_bold) #Area
            sheet.write(row, 5, x["gaji"], style_no_bold) #Gaji & Tunjangan
            sheet.write(row, 6, x["jam_aktual"], style_no_bold) #Jam Actual
            sheet.write(row, 7, x["jam_konversi"], style_no_bold) #Jam Konversi
            sheet.write(row, 8, x["nominal_lembur"], style_no_bold) #Nominal Lembur
            
            row += 1
            no += 1

        file_data = io.BytesIO()
        workbook.save(file_data)
        self.write({
                'data': base64.encodestring(file_data.getvalue()),
                'filename': judul+' ' + station + ' ' + period + '.xls',
            })

        view = self.env.ref('a_overtime.wizard_report_overtime_view_form')
        return {
            'type': 'ir.actions.act_window',
            'name': 'Overtime Report ' + period,
            'res_model': 'wizard.overtime.report',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(view.id, 'form')],
            'target': 'new'
        }