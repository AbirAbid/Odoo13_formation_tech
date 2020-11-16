from odoo import models, fields, api


class UniversityDepartment(models.Model):
    _name = 'university.department'
    _rec_name = 'name_department'

    name_department = fields.Char('Department name', required="1")

    code_dep = fields.Char('Code of department', required="1")

    professor_ids = fields.One2many('university.professor', 'department_id')

    # for graphe
    prof_count = fields.Integer(string="Count professor",
                                compute='get_professor_count',
                                store=True)

    # function for count graph
    @api.depends('professor_ids')
    def get_professor_count(self):
        for p in self:
            p.prof_count = len(p.professor_ids)
