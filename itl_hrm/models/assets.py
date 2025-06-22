from odoo import fields, models

class Assets(models.Model):
    _name = 'itl.assets'
    _description = 'itl assets'

    name = fields.Char("Name")
    date = fields.Date("Stock date")