from odoo import models, fields, api


class UniversityDepartment(models.Model):
    _name = 'university.department'
    _rec_name = 'name_department'

    name_department = fields.Char('Department name')

    code_dep = fields.Char('Code of department')

    professor_ids = fields.One2many('university.professor', 'department_id')

