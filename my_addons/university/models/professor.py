from odoo import models, fields, api

import datetime


class UniversityProfessor(models.Model):
    _name = 'university.professor'
    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    x = datetime.datetime(1999, 1, 1)

    birthday = fields.Date('Birthday', default=x)
    start_date = fields.Datetime('Start Date', default=fields.Date.today)
    email = fields.Char()
    phone = fields.Char()

    department_id = fields.Many2one('university.department', required=True)

    subject_id = fields.Many2one('university.subject')

    classroom_ids = fields.Many2many('university.classroom')

    def name_get(self):
        result = []
        for professor in self:
            name = '[' + professor.identity_card + ']' + professor.f_name + ' ' + professor.l_name
            result.append((professor.id, name))
        return result
