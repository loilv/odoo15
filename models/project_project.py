from odoo import fields, api, models, _


class InheritProjectProject(models.Model):
    _inherit = 'project.project'

    def act_detail(self):
        return {
            'name': '%s' % self.name,
            'view_mode': 'form',
            'res_model': 'project.project',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'view_id': self.env.ref('project.edit_project').id,
            'target': 'current',
        }