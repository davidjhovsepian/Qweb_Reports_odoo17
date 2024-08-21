from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class InventoryQRController(http.Controller):

    @http.route('/inventory_qr/validate_transfer', type='http', auth='user')
    def validate_transfer(self, **kw):
        # Extract URL parameters
        action_id = kw.get('action')
        active_id = kw.get('active_id')
        model = kw.get('model')
        view_type = kw.get('view_type')
        cids = kw.get('cids')
        menu_id = kw.get('menu_id')

        _logger.info(f"Received parameters - Action: {action_id}, Active ID: {active_id}, Model: {model}, View Type: {view_type}, CIDs: {cids}, Menu ID: {menu_id}")

        try:
            transfer_id = int(active_id)
            picking = request.env['stock.picking'].browse(transfer_id)
            if picking.exists() and picking.state not in ['done', 'cancel']:
                picking.action_confirm()
                picking.action_assign()
                picking.button_validate()

                # Run additional method here
                self.run_additional_method(picking)

                return "Stock transfer validated and additional method executed successfully."
            else:
                return "Invalid or already processed stock transfer."
        except Exception as e:
            _logger.error(f"Error processing stock transfer: {str(e)}")
            return "Error processing stock transfer."

    def run_additional_method(self, picking):
        # Add your custom method logic here
        _logger.info(f"Running additional method for picking: {picking.id}")
        # Example: Updating a field on the stock picking
        picking.write({'additional_field': 'value'})
        # You can add more logic here as needed

    @http.route('/inventory_qr/open_action', type='http', auth='user')
    def open_action(self, **kw):
        # Redirect to the desired action
        url = f"/web#action={kw.get('action')}&active_id={kw.get('active_id')}&model={kw.get('model')}&view_type={kw.get('view_type')}&cids={kw.get('cids')}&menu_id={kw.get('menu_id')}"
        return request.redirect(url)
