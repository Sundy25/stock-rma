# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from openerp import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    rma_approval_policy = fields.Selection(
        selection=[('one_step', 'One step'), ('two_step', 'Two steps')],
        string="RMA Approval Policy", required=True, default='one_step',
        help="Options: \n "
             "* One step: Always auto-approve RMAs that only contain "
             "products within categories with this policy.\n"
             "* Two steps: A RMA containing a product within a category with "
             "this policy will request the RMA manager approval.")
    rma_operation_id = fields.Many2one(
        comodel_name="rma.operation", string="RMA Operation")
