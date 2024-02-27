from odoo import api, fields, models

class DavidsTestModel(models.Model):
    _inherit="sale.order"
    thing=fields.Char("davids test field")
