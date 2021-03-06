from odoo import models, fields, api


class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    # pour chatter
    _inherit = 'mail.thread'
    _rec_name = 'classroom_name'
    classroom_name = fields.Char(required="1")

    code = fields.Char(required="1")

    # inverse_name = champs qui relie 2 objects
    student_ids = fields.One2many('university.student', 'classroom_id')
    # relation = classe associative / col1 et col 2 =ids de la class associ
    # manytomany (professor-classroom)

    professor_ids = fields.Many2many('university.professor')

    # for graphe
    prof_count = fields.Integer(string="Count professor",
                                     compute='get_professor_count',
                                     store=True)

    def name_get(self):
        result = []
        for classroom in self:
            name = classroom.classroom_name
            result.append((classroom.id, name))
        return result

    # manytomany (subject-classroom)

    subject_ids = fields.Many2many('university.subject')

    num_prof = fields.Integer(string="Number of professor", compute='comp_prof')
    num_sub = fields.Integer(string="Number of subjects", compute='comp_sub')
    num_stu = fields.Integer(string="Number of students", compute='comp_stu')

    def comp_prof(self):
        self.num_prof = len(self.professor_ids)

    def comp_sub(self):
        self.num_sub = len(self.student_ids)

    def comp_stu(self):
        self.num_stu = len(self.student_ids)

    # pour vérifier nombre de subjects (en changant subject_ids)
    @api.onchange('subject_ids')
    def check_number_of_subjects(self):
        if len(self.subject_ids) > 3:
            return {'warning': {'title': 'Warning', 'message': 'The number must be less than 3'}}

    # function for count graph
    @api.depends('professor_ids')
    def get_professor_count(self):
        for p in self:
            p.prof_count = len(p.professor_ids)

