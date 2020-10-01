from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.models import Q
from django.db.utils import NotSupportedError
from django.test import TestCase

import eav
from eav.models import Attribute, EnumGroup, EnumValue, Value
from eav.registry import EavConfig

from tests.models import Encounter, Patient


class Queries(TestCase):
    def setUp(self):
        eav.register(Encounter)
        eav.register(Patient)

        Attribute.objects.create(name='age', datatype=Attribute.TYPE_INT)
        Attribute.objects.create(name='height', datatype=Attribute.TYPE_FLOAT)
        Attribute.objects.create(name='weight', datatype=Attribute.TYPE_FLOAT)
        Attribute.objects.create(name='city', datatype=Attribute.TYPE_TEXT)
        Attribute.objects.create(name='country', datatype=Attribute.TYPE_TEXT)

        self.yes = EnumValue.objects.create(value='yes')
        self.no = EnumValue.objects.create(value='no')
        self.unknown = EnumValue.objects.create(value='unknown')

        ynu = EnumGroup.objects.create(name='Yes / No / Unknown')
        ynu.values.add(self.yes)
        ynu.values.add(self.no)
        ynu.values.add(self.unknown)

        Attribute.objects.create(name='fever', datatype=Attribute.TYPE_ENUM, enum_group=ynu)

        self.cashback = EnumValue.objects.create(value='cashback')
        self.petrol = EnumValue.objects.create(value='petrol')
        self.lounge = EnumValue.objects.create(value='lounge')

        cardfacilities = EnumGroup.objects.create(name='cardfacilities')
        cardfacilities.values.add(self.cashback)
        cardfacilities.values.add(self.petrol)
        cardfacilities.values.add(self.lounge)

        Attribute.objects.create(name='card_facilities', datatype=Attribute.TYPE_M2M, enum_group=cardfacilities)

    def init_data(self):
        yes = self.yes
        no = self.no
        cashback = self.cashback
        petrol = self.petrol
        lounge = self.lounge

        data = [
            # Name,    age, fever, city,       country, card_facilities
            ['Anne', 3, no, 'New York', 'USA', [cashback, lounge]],
            ['Bob', 15, no, 'Bamako', 'Mali', [lounge, petrol]],
            ['Cyrill', 15, yes, 'Kisumu', 'Kenya', []],
            ['Daniel', 3, no, 'Nice', 'France', [cashback, lounge, petrol]],
            ['Eugene', 2, yes, 'France', 'Nice', []]
        ]

        for row in data:
            patient = Patient.objects.create(
                name=row[0],
                eav__age=row[1],
                eav__fever=row[2],
                eav__city=row[3],
                eav__country=row[4]
            )

            if len(row[5]):
                patient.eav.card_facilities.add(*row[5])
