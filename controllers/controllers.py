# from odoo import http


# class PartnerPhoneSearch(http.Controller):
#     @http.route('/partner_phone_search/partner_phone_search', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_phone_search/partner_phone_search/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_phone_search.listing', {
#             'root': '/partner_phone_search/partner_phone_search',
#             'objects': http.request.env['partner_phone_search.partner_phone_search'].search([]),
#         })

#     @http.route('/partner_phone_search/partner_phone_search/objects/<model("partner_phone_search.partner_phone_search"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_phone_search.object', {
#             'object': obj
#         })

