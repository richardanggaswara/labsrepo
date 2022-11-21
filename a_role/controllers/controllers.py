# -*- coding: utf-8 -*-
from odoo import http

# class ARole(http.Controller):
#     @http.route('/a_role/a_role/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a_role/a_role/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a_role.listing', {
#             'root': '/a_role/a_role',
#             'objects': http.request.env['a_role.a_role'].search([]),
#         })

#     @http.route('/a_role/a_role/objects/<model("a_role.a_role"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a_role.object', {
#             'object': obj
#         })