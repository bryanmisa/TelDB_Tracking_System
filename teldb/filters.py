import django_filters

from django import forms

from teldb.models import *


from django_select2 import forms as s2forms
from django_select2.forms import Select2Widget

""" Telephone Filters"""

# region Widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class OrganizationWidget(s2forms.ModelSelect2Widget):
    queryset = Organization.objects.all()
    search_fields = [
        "assigned_to_organization_name__icontains",
    ]


class ExtensionNumberWidget(s2forms.ModelSelect2Widget):
    queryset = DirectInwardDialIn.objects.all()
    search_fields = [
        "did__icontains",
    ]


# endregion Widgets

# region Filters

""" Location Filter"""


class LocationFilter(django_filters.FilterSet):

    location_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Location Name'
    )

    class Meta:
        model = Location
        fields = ['location_name']


""" Organization Filter """


class OrganizationFilter(django_filters.FilterSet):
    organization_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Organization Name'
    )

    class Meta:
        model = Organization
        fields = ['organization_name']


""" Department Filter"""


class DepartmentFilter(django_filters.FilterSet):
    department_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Department Name'
    )
    code__code = django_filters.CharFilter(
        lookup_expr='icontains', field_name='code__code',
        label='Department Code'
    )

    class Meta:
        model = Department
        fields = ['department',
                  'code__code']


""" Code Filter """


class CodeFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains', label='Code')

    class Meta:
        model = Code
        fields = ['code']


""" Employee Category Filter """


class EmployeeCategoryFilter(django_filters.FilterSet):
    employee_category = django_filters.CharFilter(
        lookup_expr='icontains', label='Employee Category')

    class Meta:
        model = EmployeeCategory
        fields = ['employee_category']


""" Device Type Filter"""


class DeviceTypeFilter(django_filters.FilterSet):
    device_type = django_filters.CharFilter(
        lookup_expr='icontains', label='Device Type'
    )

    class Meta:
        model = DeviceType
        fields = ['device_type']


""" DirectInwardDialIn Filter"""


class DirectInwardDialInFilter(django_filters.FilterSet):
    did = django_filters.CharFilter(
        lookup_expr='icontains', label='DID Number'
    )

    class Meta:
        model = DirectInwardDialIn
        fields = ['did']


""" Telephone Filter """


class TelephoneFilter(django_filters.FilterSet):

    mac_address = django_filters.CharFilter(
        lookup_expr='icontains', label='MAC Address')

    device_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Device Name')

    telephone_device_type = django_filters.CharFilter(
        lookup_expr='icontains', field_name='telephone_device_type__device_type', label='Device Type')

    assigned_to = django_filters.CharFilter(
        lookup_expr='icontains', field_name='assigned_to__employee_name', label='Employee Name')

    assigned_to__organization = django_filters.CharFilter(
        lookup_expr='icontains', field_name='assigned_to__organization__organization_name', label='Organization')

    assigned_to__department__code__code = django_filters.CharFilter(
        lookup_expr='icontains', field_name='assigned_to__department__code__code', label='Code')

    connection_date = django_filters.DateFilter(
        widget=DateInput(attrs={'type': 'date'}))

    disconnection_date = django_filters.DateFilter(
        widget=DateInput(attrs={'type': 'date'}))

    extension_number = django_filters.CharFilter(
        lookup_expr='icontains', field_name='extension_number__did', label='Extension Number')

    TELEPHONE_STATUS = [
        ('Installed', 'Installed'),
        ('In Stock', 'In Stock'),
        ('In Repair', 'In Repair'),
        ('Disposed', 'Disposed'),
    ]

    status = django_filters.ChoiceFilter(
        choices=TELEPHONE_STATUS, label='Status', )

    class Meta:
        model = Telephone
        fields = [
            'mac_address',
            'device_name',
            'telephone_device_type',
            'assigned_to',
            'assigned_to__organization',
            'assigned_to__department__code__code',
            'connection_date',
            'disconnection_date',
            'status',
            'extension_number'
        ]


class EmployeeFilter(django_filters.FilterSet):
    employee_number = django_filters.CharFilter(
        lookup_expr='icontains', label='Employee Number')
    employee_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Employee Name')
    department = django_filters.CharFilter(
        lookup_expr='icontains', field_name='department__department_name', label='Department')
    organization = django_filters.CharFilter(
        lookup_expr='icontains', field_name='organization__organization_name', label='Organization')
    location = django_filters.CharFilter(
        lookup_expr='icontains', field_name='location__location_name', label='Location')
    employee_category = django_filters.CharFilter(
        lookup_expr='icontains', field_name='employee_category__employee_category', label='Employee Category')

    FILTER_EMPLOYEE_STATUS = [
        ('Active', 'Active'),
        ('In Active', 'In Active')
    ]
    employee_status = django_filters.ChoiceFilter(
        choices=FILTER_EMPLOYEE_STATUS, label='Status', )

    class Meta:

        model = Employee
        fields = [
            'employee_number',
            'employee_name',
            'department',
            'organization',
            'location',
            'employee_category',
            'employee_status',
        ]

# endregion Filters
