from django import forms
from .models import *
from django.core.validators import RegexValidator
from django_select2 import forms as s2forms


# region Widgets
class EmployeeWidget(s2forms.ModelSelect2Widget):
    queryset = Employee.objects.all().filter(employee_status='Active')
    search_fields = [
        'employee_name__icontains'
    ]


class DIDWidget(s2forms.ModelSelect2Widget):
    queryset = DirectInwardDialIn.objects.filter(status='Free')
    search_fields = [
        'did__icontains'
    ]


class DeviceTypeWidget(s2forms.ModelSelect2Widget):

    search_fields = [
        'device_type__icontains'
    ]


class LocationWidget(s2forms.ModelSelect2Widget):

    search_fields = ['location_name__icontains']


class DepartmentWidget(s2forms.ModelSelect2Widget):
    search_fields = ['department_name__icontains']


class EmployeeCategoryWidget(s2forms.ModelSelect2Widget):
    search_fields = ['employee_category__icontains']


class OrganizationWidget(s2forms.ModelSelect2Widget):
    search_fields = ['organization_name__icontains']


class CodeWidget(s2forms.ModelSelect2Widget):
    search_fields = ['code__icontains']
# endregion Widgets


class LocationForm(forms.ModelForm):
    location_name = forms.CharField(
        label='Enter a New Location Name : ',
        widget=forms.TextInput(attrs={'placeholder': 'Location Name'}),
        error_messages={'unique': u'Location already exists'})

    class Meta:
        model = Location
        fields = [
            "location_name",
        ]


class CodeForm(forms.ModelForm):
    code = forms.CharField(
        label='Enter a new Code : ',
        widget=forms.TextInput(attrs={'placeholder': 'Code'}),
        error_messages={'unique': u'Code already exists'}
    )

    class Meta:
        model = Code
        fields = [
            "code",
        ]


class OrganizationForm(forms.ModelForm):
    organization_name = forms.CharField(
        label='Enter the name of the new organization: ',
        widget=forms.TextInput(
            attrs={'placeholder': 'Organization / Company'}),
        error_messages={'unique': u' Organization already exists'}
    )

    class Meta:
        model = Organization
        fields = [
            "organization_name",
        ]


class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField(
        label='Enter a new Department : ',
        widget=forms.TextInput(attrs={'placeholder': 'Department'}),
        error_messages={'unique': u'Department already exists'}
    )
    code = forms.ModelChoiceField(queryset=Code.objects.all())

    class Meta:
        model = Department
        fields = [
            "department_name",
            "code",
        ]


class EmployeeCategoryForm(forms.ModelForm):
    employee_category = forms.CharField(
        label='Enter a new Employee Category : ',
        widget=forms.TextInput(attrs={'placeholder': 'Employee Category'}),
        error_messages={'unique': u'Employee Category already exists'}
    )

    class Meta:
        model = EmployeeCategory
        fields = [
            "employee_category",
        ]


class DeviceTypeForm(forms.ModelForm):
    device_type = forms.CharField(
        label='Enter a new Device Type : ',
        widget=forms.TextInput(attrs={'placeholder': 'Employee Category'}),
        error_messages={'unique': u'Employee Category already exists'}
    )

    class Meta:
        model = DeviceType
        fields = [
            "device_type",
        ]

# region EmployeeForm


class EmployeeForm(forms.ModelForm):
    employee_number = forms.CharField(
        label='Enter a Employee Number : ',
        widget=forms.TextInput(attrs={'placeholder': 'Employee Number'}),
        error_messages={'unique': u'Employee Number already exists'}
    )
    employee_name = forms.CharField(
        label='Enter a Employee Name : ',
        widget=forms.TextInput(attrs={'placeholder': 'Employee Name'}),
        error_messages={'unique': u'Employee Name already exists'}
    )

    EMPLOYEE_STATUS = [
        ('Active', 'Active'),
        ('In Active', 'In Active')
    ]

    employee_status = forms.ChoiceField(
        choices=EMPLOYEE_STATUS,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'location': LocationWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Location Name', }),
            'department': DepartmentWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Department Name', }),
            'organization': OrganizationWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Organization Name', }),
            'employee_category': EmployeeCategoryWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Employee Category', }),
        }

# endregion EmployeeForm


class DirectInwardDialInForm(forms.ModelForm):
    did = forms.CharField(
        label='Enter a new extension number : ',
        widget=forms.TextInput(attrs={'placeholder': 'Extension Number'}),
        error_messages={'unique': u'DID already exists'}
    )

    STATUS = [
        ('Active', 'Active'),
        ('Free', 'Free'),
        ('Out of Service', 'Out of Service'),
    ]
    status = forms.ChoiceField(
        choices=STATUS,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = DirectInwardDialIn
        fields = '__all__'

# region TelephoneForm


class TelephoneForm(forms.ModelForm):
    mac_address = forms.CharField(validators=[RegexValidator('([0-9a-fA-F]{2}){5}([0-9a-fA-F]{2})', message="Enter a valid mac address, format as e.g. 8fed76191b75 or 3D55FE0981AF")],
                                  label='Enter a new mac address : ',
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'MAC address'}),
                                  error_messages={
                                      'unique': u'MAC Address already exists'}
                                  )
    device_name = forms.CharField(
        label='Enter the device name : ',
        widget=forms.TextInput(attrs={'placeholder': 'Device Name'}),
        error_messages={'unique': u'Device Name already exists'}
    )

    STATUS = [
        ('In Stock', 'In Stock'),

    ]

    status = forms.ChoiceField(
        choices=STATUS,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Telephone

        fields = ['mac_address',
                  'device_name',
                  'telephone_device_type']
        widgets = {
            'telephone_device_type': DeviceTypeWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Enter Device Type', }),
        }
# endregion TelephoneForm


""" Telephone Assignment Form"""


class AssignTelephoneForm(forms.ModelForm):

    extension_number = DirectInwardDialIn.objects.all().filter(status='Free')

    class Meta:
        model = Telephone
        fields = [
            'assigned_to',
            'extension_number'
        ]

        widgets = {
            'assigned_to': EmployeeWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Enter Employee Name', }),
            'extension_number': DIDWidget(
                attrs={'data-width': '100%',
                       'data-placeholder': 'Assign Extension Number', }),

        }


class PutTelephoneInStock(forms.ModelForm):

    STATUS = [
        ('In Stock', 'In Stock'),
    ]

    status = forms.ChoiceField(
        choices=STATUS,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Telephone
        fields = [
            'status'
        ]
