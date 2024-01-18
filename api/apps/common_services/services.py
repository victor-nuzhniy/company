"""Services for common_services apps."""
import inspect
import typing

from flask import abort
from sqlalchemy import Row

from api.apps.invoice import models as invoice_models
from api.apps.order import models as order_models
from api.apps.purchase import models as purchase_models
from api.apps.sale import models as sale_models
from api.apps.tax import models as tax_models

GetLastNameModelType = typing.Union[
    order_models.Order,
    invoice_models.Invoice,
    purchase_models.PurchaseInvoice,
    sale_models.SaleInvoice,
    tax_models.TaxInvoice,
    None,
]


def get_last_name(model_name: str) -> Row:
    """Get last model name."""
    model_names_set: set = {
        "Order",
        "Invoice",
        "PurchaseInvoice",
        "SaleInvoice",
        "TaxInvoice",
    }
    if model_name not in model_names_set:
        abort(
            409,
            "".join(
                (
                    "'{name}' is not in ".format(name=model_name),
                    "Order, Invoice, PurchaseInvoice, SaleInvoice, TaxInvoice models.",
                ),
            ),
        )
    caller_globals = inspect.stack()[1][0].f_globals
    model: GetLastNameModelType = caller_globals.get(model_name)
    if model:
        query = model.query.with_entities(model.name)
        return query.order_by(model.id.desc()).first()
    abort(500, "{name} not in globals".format(name=model_name))
