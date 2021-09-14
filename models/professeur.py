# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EcoleProfesseur(models.Model):
    _name = 'ecole.professeur'
    
    first_name = fields.Char('Nom')
    last_name = fields.Char('Prenoms')
    sexe = fields.Selection([('homme', 'Homme'),('femme', 'Femme')])
    identity_card = fields.Char('Carte d intentidé')
    address = fields.Text('Adresse')
    birthday = fields.Datetime('Anniversaire')
    start_date = fields.Char('Start Date')
    email = fields.Char()
    phone = fields.Char()
