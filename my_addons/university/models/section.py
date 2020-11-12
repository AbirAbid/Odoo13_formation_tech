from odoo import models, fields, api


class UniversitySection(models.Model):
    _name = 'university.section'
    _rec_name = 'name_section'

    name_section = fields.Char(required="1")

    code = fields.Char(required="1")

    student_ids = fields.One2many('university.student', 'section_id', ondelete='cascade')
