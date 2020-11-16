from odoo import models, fields, api


class UniversitySection(models.Model):
    _name = 'university.section'
    _rec_name = 'name_section'

    name_section = fields.Char(required="1")

    code = fields.Char(required="1")

    student_ids = fields.One2many('university.student', 'section_id', ondelete='cascade')

    stu_co = fields.Integer(compute="count_student_by_section",
                                   store=True)

    @api.depends('student_ids')
    def count_student_by_section(self):
        for s in self:
            s.stu_co = len(s.student_ids)
