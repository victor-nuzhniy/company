"""Init module for api."""
from api.app import api, app
from api.apps.common.account import routes as account_routes
from api.apps.common.auth import routes as auth_routes
from api.apps.common.special import routes as common_special_routes
from api.apps.counterparty.base import routes as counterparty_base_routes
from api.apps.counterparty.base.models import Agreement, Counterparty, Discount
from api.apps.counterparty.special import routes as counterparty_special_routes
from api.apps.invoice.base import routes as invoice_base_routes
from api.apps.invoice.base.models import Invoice, InvoiceProduct
from api.apps.invoice.special import routes as invoice_special_routes
from api.apps.order.base import routes as order_base_routes
from api.apps.order.base.models import Order, OrderProduct
from api.apps.order.special import routes as order_special_routes
from api.apps.product.base import routes as product_base_routes
from api.apps.product.base.models import Product, ProductType
from api.apps.purchase.base import routes as purchase_base_routes
from api.apps.purchase.base.models import PurchaseInvoice, PurchaseInvoiceProduct
from api.apps.purchase.special import routes as purchase_special_routes
from api.apps.sale.base import routes as sale_base_routes
from api.apps.sale.base.models import SaleInvoice, SaleInvoiceProduct
from api.apps.sale.special import routes as sale_special_routes
from api.apps.tax.base import routes as tax_base_routes
from api.apps.tax.base.models import TaxInvoice, TaxInvoiceProduct
from api.apps.tax.special import routes as tax_special_routes
from api.apps.user.base import routes as user_base_routes
from api.apps.user.base.models import User
from api.apps.user.special import routes as user_special_routes

...  # noqa WPS428

__all__ = (  # noqa WPS410
    "api",
    "app",
    "Agreement",
    "Counterparty",
    "Discount",
    "Invoice",
    "InvoiceProduct",
    "Order",
    "OrderProduct",
    "Product",
    "ProductType",
    "PurchaseInvoice",
    "PurchaseInvoiceProduct",
    "SaleInvoice",
    "SaleInvoiceProduct",
    "TaxInvoice",
    "TaxInvoiceProduct",
    "User",
)
