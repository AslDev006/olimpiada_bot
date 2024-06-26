from django.urls import path, register_converter
from .views import *


class TelegramIDConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
register_converter(TelegramIDConverter, 'telegram_id')

urlpatterns = [
    path('users/', UserList),
    path('excel-olimpiada-users/', ExcelOlimpiadaUserList),
    path('excel-no-olimpiada-users/', ExcelNoOlimpiadaUserList),
    path('excel-grand-users/', ExcelGrandUserList),
    path('olimpiada-users/', OlimpiadaUserList),
    path('no-olimpiada-users/', NoOlimpiadaUserList),
    path('top-users/', TopSoreUserList),
    path('count-users/', UserCountList),
    path('admin-user/', UserAdminList),
    path('super-admin-user/', UserSuperAdminList),
    path('next-top-users/', NextTopSoreUserList),
    path('users/<telegram_id:telegram_id>/', UserDetail),
    path('users/<telegram_id:telegram_id>/olimpiada/', OlimpiadaDetail),
    path('users/<telegram_id:telegram_id>/scores/', ScoreDetail),
    path('users/<telegram_id:telegram_id>/permissions/', PermissionDetail),
    path('users/<telegram_id:telegram_id>/ban/', UserBanDetail),
    path('users/<telegram_id:telegram_id>/active/', UserActiveDetail),
    path('users/<telegram_id:telegram_id>/personal-data/', PersonalDataDetail),
    path('users/<telegram_id:telegram_id>/first-name/', FirstNameDetail),
    path('users/<telegram_id:telegram_id>/last-name/', LastNameDetail),
    path('users/<telegram_id:telegram_id>/region/', RegionDetail),
    path('users/<telegram_id:telegram_id>/district/', DistrictDetail),
    path('users/<telegram_id:telegram_id>/phone-number/', PhoneNumberDetail),
]