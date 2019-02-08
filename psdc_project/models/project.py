# -*- coding: utf-8 -*-
from odoo import models, fields, api, osv, tools
from openerp.tools.translate import _
from odoo.exceptions import UserError, ValidationError, Warning
import logging
_logger = logging.getLogger(__name__)


class Project(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'
    resident_id = fields.Many2one(
        'res.partner',
        string='Residente del proyecto',
        domain=[('is_resident','=','True')])
    addendum_ids = fields.One2many(
        'psdc_project.addendum',
        'project_id',
        string='Adenda')
    policy_ids = fields.One2many(
        'psdc_project.policy',
        'project_id',
        string='Póliza')
    bail_ids = fields.One2many(
        'psdc_project.bail',
        'project_id',
        string='Fianza')
