# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L.
# © 2015 Eezee-It, MONK Software, Vauxoo
# © 2013 Camptocamp
# © 2009-2013 Akretion,
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from openerp import fields, models


class RmaOperation(models.Model):
    _inherit = 'rma.operation'

    refund_policy = fields.Selection([
        ('no', 'No refund'), ('ordered', 'Based on Ordered Quantities'),
        ('received', 'Based on Received Quantities')], string="Refund Policy",
        default='no')
