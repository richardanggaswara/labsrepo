# -*- coding: utf-8 -*-
from odoo import http

# class ASendEmail(http.Controller):
#     @http.route('/a_send_email/a_send_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a_send_email/a_send_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a_send_email.listing', {
#             'root': '/a_send_email/a_send_email',
#             'objects': http.request.env['a_send_email.a_send_email'].search([]),
#         })

#     @http.route('/a_send_email/a_send_email/objects/<model("a_send_email.a_send_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a_send_email.object', {
#             'object': obj
#         })