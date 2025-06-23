from odoo import models, fields

class Department(models.Model):
    _name = 'itl.department'
    _description = 'ITL Department'

    name = fields.Char("Name")
    manager_user_id = fields.Many2one('res.users', string="Department Manager (User)")
