from odoo import fields, models

class Department(models.Model):
    _name = 'itl.department'
    _description = 'itl department'

    name = fields.Char("Name")