# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SendEmailNotification(models.AbstractModel):
    _name = 'send.email.notification'
    _description = 'Send Email Notification'
    
    def send(self, id, model, status, type, receiver, name):
        self = self.sudo()
        url = self.env['ir.config_parameter'].get_param('web.base.url') + '/web#id=%s&model=%s&view_type=form' % (id, model)
        template_id = self.env.ref('a_send_email.reminder_notification')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'name': name, 'status': status, 'url': url, 'email': sendto}).send_mail(self.id, force_send=True)

    def send_load_req(self, id, model, type, receiver, name):
        self = self.sudo()
        url = self.env['ir.config_parameter'].get_param('web.base.url') + '/web#id=%s&model=%s&view_type=form' % (id, model)
        template_id = self.env.ref('a_send_email.load_requirment_notification')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'name': name, 'url': url, 'email': sendto}).send_mail(self.id, force_send=True)
    
    def send_load_mon(self, id, model, type, receiver):
        self = self.sudo()
        url = self.env['ir.config_parameter'].get_param('web.base.url') + '/web#id=%s&model=%s&view_type=form' % (id, model)
        template_id = self.env.ref('a_send_email.load_monitoring_notification')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'url': url, 'email': sendto}).send_mail(self.id, force_send=True)

    def send_project(self, project, pl, type, receiver):
        self = self.sudo()
        template_id = self.env.ref('a_send_email.template_assign_project')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'email': sendto, 'project': project, 'pl': pl}).send_mail(self.id, force_send=True)
    
    def send_contract_project(self, judul_kontrak, nama_kontrak, 
        customer, date_from, date_to, type, receiver):
        self = self.sudo()
        template_id = self.env.ref('a_send_email.template_contract_project')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'email': sendto, 'judul_kontrak': judul_kontrak, 'nama_kontrak': nama_kontrak, 'customer':customer,
        'date_from': date_from, 'date_to': date_to}).send_mail(self.id, force_send=True)

    def send_bast(self, judul_kontrak, no_kontrak, 
        pihak_pertama, date, type, receiver):
        self = self.sudo()
        template_id = self.env.ref('a_send_email.template_bast')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'email': sendto, 'judul_kontrak': judul_kontrak, 
        'no_kontrak': no_kontrak, 'pihak_pertama':pihak_pertama,'date': date}).send_mail(self.id, force_send=True)

    def send_cs(self, judul_kontrak, no_kontrak, 
        organization, type, receiver):
        self = self.sudo()
        template_id = self.env.ref('a_send_email.template_cs')
        if type == 'group':
            email = self.env['ir.model.data'].xmlid_to_object(receiver).users
        elif type == 'user':
            email = self.env['res.users'].search([('id', '=', receiver.id)])
        email_list = [i.email for i in email if i.email]
        sendto = ', '.join(email_list)
        template_id.with_context({'email': sendto, 'judul_kontrak': judul_kontrak, 
        'no_kontrak': no_kontrak, 'organization': organization}).send_mail(self.id, force_send=True)    
    