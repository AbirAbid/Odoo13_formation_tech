from odoo import models, fields, api


class UniversitySubject(models.Model):
    _name = 'university.subject'
    _rec_name = 'subject_name'

    subject_name = fields.Char()

    code = fields.Char()

    coef = fields.Integer(default=1)

    # many subject to one department
    # chaque subject apprtient à un seule department

    professor_ids = fields.One2many('university.professor', 'subject_id')

    # manytomany (subject-classroom)

    classroom_ids = fields.Many2many('university.classroom')

    student_ids = fields.Many2many('university.student')
