from odoo import models, fields

class Employee(models.Model):
    _name = 'itl.employee'
    _description = 'ITL Employee'

    name = fields.Char(string="Name")
    mobile = fields.Char(string="Mobile")
    user_id = fields.Many2one('res.users', string="Linked User")  # Add this line
    department_id = fields.Many2one("itl.department", string="Department")
    asset_given_date = fields.Date(string="Asset given at")
