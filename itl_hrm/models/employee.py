from odoo import fields, models

class Employee(models.Model):
    _name = 'itl.employee'
    _description = 'itl employee'

    name = fields.Char(string="Name")
    mobile = fields.Char(string="Mobile")
    department = fields.Many2one("itl.department", string="Department")
    assets = fields.Many2many("itl.assets", string="Allocated Assets")
    asset_given_date = fields.Date(string="Asset given at")
