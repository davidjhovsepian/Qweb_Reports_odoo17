from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleCustom(WebsiteSale):
    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        order_sudo = request.website.sale_get_order()

        redirection = self.checkout_redirection(order_sudo)
        if redirection:
            return redirection

        if order_sudo._is_public_order():
            return request.redirect('/shop/address')

        redirection = self.checkout_check_address(order_sudo)
        if redirection:
            return redirection

        values = self.checkout_values(order_sudo, **post)

        # Avoid useless rendering if called in ajax
        if post.get('xhr'):
            return 'ok'
        return request.render("website_sale.checkout", values)
