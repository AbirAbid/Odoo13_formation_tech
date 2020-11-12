from odoo import models, fields, api

import datetime


class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    f_name = fields.Char('First name', required="1", tracking=True)
    l_name = fields.Char('Last name', required="1")
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], required="1")
    identity_card = fields.Char('Identity card', required="1")
    address = fields.Text('Address', required="1")
    x = datetime.datetime(1999, 1, 1)
    birthday = fields.Date('Birthday', default=x, required="1")
    start_date = fields.Datetime('Start Date', default=fields.Date.today)
    email = fields.Char(required="1")
    phone = fields.Char(required="1")

    department_id = fields.Many2one('university.department', required=True)

    subject_id = fields.Many2one('university.subject')

    classroom_ids = fields.Many2many('university.classroom')

    classroom_count = fields.Integer(string="count classroom",
                                     compute='get_classroom_count',
                                     store=True
                                     )

    def name_get(self):
        result = []
        for professor in self:
            name = '[' + professor.identity_card + ']' + professor.f_name + ' ' + professor.l_name
            result.append((professor.id, name))
        return result

    @api.depends('classroom_ids')
    def get_classroom_count(self):
        for p in self:
            p.classroom_count = len(p.classroom_ids)
