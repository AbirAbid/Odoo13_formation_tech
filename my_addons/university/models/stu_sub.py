from odoo import models, fields, api


class UniversityStuSub(models.Model):
    _name = 'university.stu_sub'
    subject_id = fields.Many2one('university.subject')
    student_id = fields.Many2one('university.student')
    score_subj = fields.Float('Subject score')
