# -*- coding: utf-8 -*-

from odoo import models, fields, api

import dateutil.parser
import datetime


class UniversityStudent(models.Model):
    _name = 'university.student'
    _rec_name = 'f_name'

    f_name = fields.Char('First name')

    l_name = fields.Char('Last name')

    sex = fields.Selection([('male', "Male"), ("female", "Female")])

    identity_card = fields.Char('Identity Card')

    adress = fields.Text('Adresse')

    x = datetime.datetime(1999, 1, 1)

    birthday = fields.Date('Birthday', default=x)

    registration_date = fields.Datetime(default=fields.Date.today)
    email = fields.Char()
    phone = fields.Char()

    photoStudent = fields.Binary("Student photo", attachment=True, store=True)
    score = fields.Float('Score')

    state = fields.Selection([('l1', 'level1'), ('l2', 'level2'), ('l3', 'level3'), ('finished', 'Finished')],
                             default='l1')
    # manyToOne clé étrangére
    # department_id = fields.Many2one('university.department')

    section_id = fields.Many2one('university.section', 'Section for student')

    # (student-classroom)
    classroom_id = fields.Many2one('university.classroom')
    # pour que subject_ids est un champ relié
    # subject_ids pour avoir les subjects du classroom de l'etudiant
    # Many2many subject_classroom
    subject_ids = fields.Many2many('university.subject')

    # name_get lors de select student display class+name+last name
    def name_get(self):
        result = []
        for student in self:
            name = '[' + student.classroom_id.classroom_name + '] ' + student.f_name + ' ' + student.l_name
            result.append((student.id, name))
        return result

    # fonction verification birthday, registration_date

    @api.constrains('registration_date', 'birthday')
    def check_dates(self):
        if self.birthday > dateutil.parser.parse(self.registration_date.strftime("%m/%d/%Y, %H:%M:%S")).date():
            raise ValueError('the birthday date must be less than the registration date')

    def next_level(self):
        # le traitement s'execute une seule fois
        self.ensure_one()
        if self.state == 'l1':
            return self.write({'state': 'l2'})
        elif self.state == 'l2':
            return self.write({'state': 'l3'})
        elif self.state == 'l3':
            return self.write({'state': 'finished'})

    def previous_level(self):
        self.ensure_one()
        if self.state == 'l2':
            return self.write({'state': 'l1'})
        elif self.state == 'l3':
            return self.write({'state': 'l2'})
        elif self.state == 'finished':
            return self.write({'state': 'l3'})

    def calcul_score(self):
        print('subjects length', len(self.subject_ids))
        self.score = 0;
        for sub in self.subject_ids:
            print('self.subject_ids.subject_name', sub.subject_name)
