from odoo import models, fields, api


class ResPartners(models.Model):
    _name = 'university.res_partners'
    _description = 'Partners'
    _rec_name = 'display_name'
    display_name = fields.Char(string='Name', required=True)
    email = fields.Char('Email', required=True)
    mobile = fields.Char('Mobile', required=True)
    id = fields.Char()

    photoStudent = fields.Binary("Student photo", attachment=True, store=True)
