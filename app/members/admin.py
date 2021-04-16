from django.contrib import admin

from members.models import FranchiseeUser, PayGoUser, AgencyUser
from rangefilter.filter import DateRangeFilter

from owners.admin import ConnectPayGoUserManagerAdmin
from paymethod.admin import PaymentMethodInlineAdmin, SettlementInformationInlineAdmin
import nested_admin


class FranchiseeUserAdmin(admin.ModelAdmin):
    fields = ('email',)


class AgencyUserAdmin(admin.ModelAdmin):
    fields = ('email', ('owners', 'is_active'))


class AgencyUserInline(admin.ModelAdmin):
    model = AgencyUser

@admin.register(PayGoUser)
class PayGoUserAdmin(nested_admin.NestedModelAdmin):
    list_filter = ('user_type', ('store_joined_date', DateRangeFilter),)
    list_display = (
        'get_owner_name',
        'get_owner_number',
        'email',
        'merchant_id',

        'phone_number',

        'user_type',
        # 'store_status',
        'store_joined_date',

        # 수수료
        # 원가수수료
        # 대리점수수료
        # 총판수수료
        # 자사수수료
        # 영중소 구분(무엇?)

    )
    autocomplete_fields = ('agencies',)
    fieldsets = (
        ('회원정보', {
            "fields": (('gid', 'mid_name'), 'email', ('main_homepage', 'sub_homepage'),
                       ('user_type', 'is_active')
                       )
        }),
        ('가맹점 정보', {
            "fields": ("boss_name", "phone_number", "fax_number",)
        }),
        ("사업자 등록", {
            "fields": ("owners",)
        }),
        ("에이전트 등록", {
            "fields": ("agencies",)
        }),
        ('기타 사항', {
            "fields": (
                (
                    "transfer_or_not",
                    "published_or_not",
                    "pay_link_or_not",
                    "pg_info_auto_save_or_not",
                    "delivery_pay_or_not",
                )
            ),
        })
    )
    inlines = (
        ConnectPayGoUserManagerAdmin,
        PaymentMethodInlineAdmin,
        # AgencyUserInline,
        SettlementInformationInlineAdmin,
    )

    def get_owner_number(self, obj):
        if obj.owners is None:
            return 'not register'
        return obj.owners.business_license_number

    def get_owner_name(self, obj):
        if obj.owners is None:
            return 'not register'
        return obj.owners.business_name

    # agencies.short_description = '에이전시 등록'
    get_owner_number.short_description = '사업자번호'
    get_owner_name.short_description = '상호명'
    ordering = ('-store_joined_date', 'user_type',)
    list_editable = ('user_type',)
    list_per_page = 10

    # 주로 어떤걸 검색하는 걸까
    search_fields = ['email', ]
    empty_value_display = 'unknown'
    date_hierarchy = 'store_joined_date'

    # actions = ['request_send_message']

    # action 통해서 취소 api 날릴수 있는거 같아
    # def request_send_message(self, request, queryset):
    #     queryset.update(user_type="a")
    #     data = {
    #         "email": "django@gmail.com",
    #         "password": "a"
    #     }
    #     response = requests.post('http://localhost:8000/members/normal/login/', data=data)
    #     self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(response.json()))

    # request_send_message.short_description = '유저 타입 에이전시로 상태로 변경'


admin.site.register(AgencyUser, AgencyUserAdmin)
admin.site.register(FranchiseeUser, FranchiseeUserAdmin)
