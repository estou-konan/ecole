# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EcoleEtudiant(models.Model):
    _name = 'ecole.etudiant'
    
    first_name = fields.Char('Nom')
    last_name = fields.Char('Prenoms')
    sexe = fields.Selection([('homme', 'Homme'),('femme', 'Femme')])
    identity_card = fields.Char('Carte d intentidé')
    address = fields.Text('Adresse')
    birthday = fields.Datetime('Anniversaire')
    inscription_date = fields.Char('Date de linscription')
    email = fields.Char()
    phone = fields.Char()
