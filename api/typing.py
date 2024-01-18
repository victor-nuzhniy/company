"""Typing module for api."""
import typing

from flask_sqlalchemy.extension import _FSAModel  # noqa WPS450

from api.apps.invoice import models as invoice_models
from api.apps.order import models as order_models
from api.apps.purchase import models as purchase_models
from api.apps.sale import models as sale_models
from api.apps.tax import models as tax_models


ModelType: typing.TypeAlias = typing.Type[_FSAModel]

GetLastNameModelType = typing.Union[
    order_models.Order,
    invoice_models.Invoice,
    purchase_models.PurchaseInvoice,
    sale_models.SaleInvoice,
    tax_models.TaxInvoice,
    None
]
