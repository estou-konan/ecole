# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EcoleClasse(models.Model):
    _name = 'ecole.classe'
    
    name = fields.Char()
    code = fields.Char()