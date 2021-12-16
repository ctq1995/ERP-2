from extensions.common.base import *
from extensions.serializers import *
from extensions.exceptions import *
from apps.system.models import *
from apps.data.models import *
from apps.goods.models import *


# System
class RoleOptionSerializer(ModelSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name']


class UserOptionSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'name']


# Data
class WarehouseOptionSerializer(ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ['id', 'number', 'name', 'is_locked']


class ClientCategoryOptionSerializer(ModelSerializer):

    class Meta:
        model = ClientCategory
        fields = ['id', 'name']


class ClientOptionSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'number', 'name', 'level']


class SupplierCategoryOptionSerializer(ModelSerializer):

    class Meta:
        model = SupplierCategory
        fields = ['id', 'name']


class SupplierOptionSerializer(ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id', 'number', 'name']


class AccountOptionSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'number', 'name']


class ChargeItemOptionSerializer(ModelSerializer):

    class Meta:
        model = ChargeItem
        fields = ['id', 'name']


# Goods
class GoodsCategoryOptionSerializer(ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']


class GoodsUnitOptionSerializer(ModelSerializer):

    class Meta:
        model = GoodsUnit
        fields = ['id', 'name']


class GoodsOptionSerializer(ModelSerializer):
    
    class Meta:
        model = Goods
        fields = ['id', 'number', 'name', 'barcode', 'enable_batch_control', 'shelf_life_days',
                  'purchase_price', 'retail_price', 'level_price1', 'level_price2', 'level_price3']


class BatchOptionSerializer(ModelSerializer):
    unit_name = CharField(source='goods.unit.name', read_only=True, label='单位名称')

    class Meta:
        model = Batch
        fields = ['id', 'number', 'remain_quantity', 'unit_name', 'production_date', 'expiration_date']


__all__ = [
    'RoleOptionSerializer', 'UserOptionSerializer',
    'WarehouseOptionSerializer',
    'ClientCategoryOptionSerializer', 'ClientOptionSerializer',
    'SupplierCategoryOptionSerializer', 'SupplierOptionSerializer',
    'AccountOptionSerializer', 'ChargeItemOptionSerializer',
    'GoodsCategoryOptionSerializer', 'GoodsUnitOptionSerializer', 'GoodsOptionSerializer',
    'BatchOptionSerializer',
]
