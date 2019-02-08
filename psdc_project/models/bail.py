# -*- coding: utf-8 -*-
from odoo import models, fields, api, osv, tools
from openerp.tools.translate import _
from odoo.exceptions import UserError, ValidationError, Warning
import logging
_logger = logging.getLogger(__name__)


class Bail(models.Model):
    _name = 'psdc_project.bail'
    _rec_name = 'number'
    number = fields.Char(
        string='N de Fianza',
        required=True)
    issue_date = fields.Date(
        string='Fecha de Emisión',
        required=True)
    expired_at = fields.Date(
        string='Fecha de Fencimiento',
        required=True)
    insurer_id = fields.Many2one(
        'res.partner',
        string='Aseguradora',
        required=True,
        domain=[('is_insurer', '=', 'True')])
    endorsement_ids = fields.One2many(
        'psdc_project.endorsement',
        'bail_id',
        string='Endozos')
    project_id = fields.Many2one(
        'project.project',
        string='Proyecto')
