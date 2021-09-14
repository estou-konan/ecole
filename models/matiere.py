# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EcoleMatiere(models.Model):
    _name = 'ecole.matiere'
    
    name = fields.Char()
    code = fields.Char()