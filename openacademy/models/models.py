# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
   _name = 'openacademy.course'
   _description ='AQUI'

   name = fields.Char(string="Title", required=True)
   description = fields.Text()
