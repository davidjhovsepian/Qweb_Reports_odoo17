# -*- coding: utf-8 -*-

from odoo import models, fields

class VetAppAnimal(models.Model):
    _name = 'vetapp.animal'
    _description = 'Vet App Animal'

    name = fields.Char(string='Name')
    value = fields.Integer(string='Value')
    breed = fields.Char(string='Breed')
    birthdate = fields.Date(string='Birthdate')
    notes = fields.Text(string='Notes')
    other = fields.Text(string='Other')

   
   

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

