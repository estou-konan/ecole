# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EcoleDepartement(models.Model):
    _name = 'ecole.departement'
    
    name = fields.Char()
    code = fields.Char()