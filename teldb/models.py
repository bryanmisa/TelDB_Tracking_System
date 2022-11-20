from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Location(models.Model):

    location_name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('location_name',)

    def __str__(self):
        return self.location_name


class Organization(models.Model):
    organization_name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('organization_name',)

    def __str__(self):
        return self.organization_name


class Department(models.Model):
    department_name = models.CharField(max_length=150, unique=True)

    code = models.ForeignKey('Code',
                             on_delete=models.SET_NULL,
                             related_name='department_code',
                             null=True,
                             blank=True)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        return self.department_name


class Code(models.Model):
    code = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code


class EmployeeCategory(models.Model):
    employee_category = models.CharField(
        max_length=250, unique=True)

    class Meta:
        ordering = ('employee_category',)
        verbose_name_plural = 'Employee Categories'

    def __str__(self):
        return self.employee_category


class Employee(models.Model):
    employee_number = models.CharField(max_length=50, unique=True)
    employee_name = models.CharField(max_length=250, unique=True)
    department = models.ForeignKey('Department',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='department')
    organization = models.ForeignKey('Organization',
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     related_name='employee_organization')
    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='employee_location')
    employee_category = models.ForeignKey('EmployeeCategory',
                                          on_delete=models.SET_NULL,
                                          null=True,
                                          blank=True,)
    EMPLOYEE_STATUS = [
        ('Active', 'Active'),
        ('In Active', 'In Active')
    ]

    employee_status = models.CharField(max_length=15,
                                       choices=EMPLOYEE_STATUS, )

    class Meta:
        ordering = ('-employee_name',)

    def __str__(self):
        return self.employee_name


class DirectInwardDialIn(models.Model):
    did = models.IntegerField(unique=True)

    STATUS = [
        ('Active', 'Active'),
        ('Free', 'Free'),
        ('Inactive', 'Inactive'),
    ]

    status = models.CharField(max_length=20,
                              choices=STATUS,
                              default='Free')

    class Meta:
        ordering = ('-did',)

    def __str__(self):
        return str(self.did)


class DeviceType(models.Model):
    device_type = models.CharField(max_length=100,
                                   unique=True)

    class Meta:
        ordering = ('-device_type',)

    def __str__(self):
        return self.device_type


class Telephone(models.Model):
    mac_address = models.CharField(max_length=20, unique=True)
    device_name = models.CharField(max_length=100, unique=True)
    telephone_device_type = models.ForeignKey('DeviceType',
                                              on_delete=models.SET_NULL,
                                              related_name='telephone_device_type',
                                              null=True,
                                              blank=True)
    assigned_to = models.ForeignKey('Employee',
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name='assigned_to')
    connection_date = models.DateField(blank=True, null=True, )
    disconnection_date = models.DateField(blank=True, null=True)
    updated_at = models.DateField(auto_now_add=True)

    STATUS = [
        ('Installed', 'Installed'),
        ('In Stock', 'In Stock'),
        ('In Repair', 'In Repair'),
        ('Disposed', 'Disposed'),
    ]

    status = models.CharField(max_length=20,
                              choices=STATUS,
                              default='In Stock')
    extension_number = models.ForeignKey('DirectInwardDialIn',
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='extension_number')

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return str(self.device_name)
