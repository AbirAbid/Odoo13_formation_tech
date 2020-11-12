from odoo import models, fields, api


class UniversitySubject(models.Model):
    _name = 'university.subject'
    _rec_name = 'subject_name'

    subject_name = fields.Char(required="1")

    code = fields.Char(required="1")

    coef = fields.Integer(default=1,required="1")

    # many subject to one department
    # chaque subject apprtient à un seule department

    professor_ids = fields.One2many('university.professor', 'subject_id')

    # manytomany (subject-classroom)

    classroom_ids = fields.Many2many('university.classroom')

    student_ids = fields.Many2many('university.student')
    sub_stu_id = fields.One2many('university.stu_sub', 'subject_id')
