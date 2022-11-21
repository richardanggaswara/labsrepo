# -*- coding: utf-8 -*-
from odoo import http

# class PropertekTeamHide(http.Controller):
#     @http.route('/hr_hide_recruitment/hr_hide_recruitment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_hide_recruitment/hr_hide_recruitment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_hide_recruitment.listing', {
#             'root': '/hr_hide_recruitment/hr_hide_recruitment',
#             'objects': http.request.env['hr_hide_recruitment.hr_hide_recruitment'].search([]),
#         })

#     @http.route('/hr_hide_recruitment/hr_hide_recruitment/objects/<model("hr_hide_recruitment.hr_hide_recruitment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_hide_recruitment.object', {
#             'object': obj
#         })