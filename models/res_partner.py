from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        result = []
        for partner in self:
            name = partner.name or ""

            phones = []
            if partner.phone:
                phones.append(partner.phone)


            if phones:
                display_name = f"{name} ({', '.join(phones)})"
            else:
                display_name = name

            result.append((partner.id, display_name))
        return result
