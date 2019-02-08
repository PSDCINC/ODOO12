# -*- coding: utf-8 -*-
from odoo import models, fields, api, osv, tools
from openerp.tools.translate import _
from odoo.exceptions import UserError, ValidationError, Warning
import logging
_logger = logging.getLogger(__name__)


class AddendumDescription(models.Model):
    _name = 'psdc_project.addendum_description'
    _rec_name = 'name'
    name = fields.Char(
        string='Nombre',
        required=True)


class Addendum(models.Model):
    _name = 'psdc_project.addendum'
    _rec_name = 'number'
    number = fields.Char(
        string='N de Adenda',
        required=True)
    comments = fields.Text(
        string='Comentarios',
        required=False)
    start_at = fields.Date(
        string='Fecha Inicial',
        required=True)
    end_at = fields.Date(
        string='Fecha Final',
        required=True)
    addendum_date = fields.Date(
        string='Fecha por Adenda',
        required=True)
    project_id = fields.Many2one(
        'project.project',
        string='Proyecto')
    addendum_description_id = fields.Many2one(
        'psdc_project.addendum_description',
        string='Descripción',
        required=True)
