# python imports
import ast

# django
from django.db import models
from localflavor.us.us_states import US_STATES

# lfs imports
import lfs.customer.utils
from lfs.criteria.models import Criterion


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class USStatesCriterion(Criterion):
    value = ListField()

    def get_operators(self):
        return self.SELECTION_OPERATORS

    def get_value_type(self):
        return self.MULTIPLE_SELECT

    def get_selectable_values(self, request):
        states = []
        for state in US_STATES:
            states.append({
                "id": state[0],
                "name": state[1],
                "selected": state[0] in self.value,
            })
        return states

    def is_valid(self):
        customer = lfs.customer.utils.get_customer(self.request)
        if customer:
            address = customer.get_selected_shipping_address()
            return address.state in self.value
        else:
            return False
