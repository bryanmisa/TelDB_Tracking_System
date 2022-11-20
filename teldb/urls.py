from django.urls import path, include
from teldb.views import *
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [

    path("login/", LoginView.as_view(template_name='login.html'), name="Login"),
    path('', TelephoneListView.as_view(), name='index'),

    path("select2/", include("django_select2.urls")),


    # LOCATION URLS
    path('location/list', LocationListView.as_view(), name='location_list'),
    path('location/update/<int:pk>',
         LocationUpdateView.as_view(), name='location_update'),
    path('location/create', LocationCreateView.as_view(), name='location_create'),
    path('location/delete/<int:pk>',
         LocationDeleteView.as_view(), name='location_delete'),

    # Code URLS
    path('code/list', CodeListView.as_view(), name='code_list'),
    path('code/update/<int:pk>', CodeUpdateView.as_view(), name='code_update'),
    path('code/create', CodeCreateView.as_view(), name='code_create'),
    path('code/delete/<int:pk>', CodeDeleteView.as_view(), name='code_delete'),

    # Organization URLS
    path('organization/list', OrganizationListView.as_view(),
         name='organization_list'),
    path('organization/update/<int:pk>',
         OrganizationUpdateView.as_view(), name='organization_update'),
    path('organization/create', OrganizationCreateView.as_view(),
         name='organization_create'),
    path('organization/delete/<int:pk>',
         OrganizationDeleteView.as_view(), name='organization_delete'),

    # Department URLS

    path('department/list', DepartmentListView.as_view(),
         name='department_list'),
    path('department/update/<int:pk>',
         DepartmentUpdateView.as_view(), name='department_update'),
    path('department/create', DepartmentCreateView.as_view(),
         name='department_create'),
    path('department/delete/<int:pk>',
         DepartmentDeleteView.as_view(), name='department_delete'),


    # region Employee Category URLS

    path('employee_category/list', EmployeeCategoryListView.as_view(),
         name='employee_category_list'),
    path('employee_category/update/<int:pk>',
         EmployeeCategoryUpdateView.as_view(), name='employee_category_update'),
    path('employee_category/create', EmployeeCategoryCreateView.as_view(),
         name='employee_category_create'),
    path('employee_category/delete/<int:pk>',
         EmployeeCategoryDeleteView.as_view(), name='employee_category_delete'),
    # endregion

    # region Employee URLS

    path('employee/list', EmployeeListView.as_view(), name='employee_list'),
    path('employee/create', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>',
         EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>',
         EmployeeDeleteView.as_view(), name='employee_delete'),
    # endregion Employee URLS

    # DID URLS
    path('did/list', DirectInwardDialInListViews.as_view(), name='did_list'),
    path('did/create', DirectInWardDialInCreateView.as_view(), name='did_create'),
    path('did/update/<int:pk>',
         DirectInWardDialInUpdateView.as_view(), name='did_update'),
    path('did/delete/<int:pk>',
         DirectInWardDialInDeleteView.as_view(), name='did_delete'),

    # DEVICE TYPE URLS
    path('device_type/list', DeviceTypeListView.as_view(), name='device_type_list'),
    path('device_type/create', DeviceTypeCreateView.as_view(),
         name='device_type_create'),
    path('device_type/update/<int:pk>',
         DeviceTypeUpdateView.as_view(), name='device_type_update'),
    path('device_type/delete/<int:pk>',
         DeviceTypeDeleteView.as_view(), name='device_type_delete'),

    # TELEPHONE URLS
    path('telephone/list', TelephoneListView.as_view(), name='telephone_list'),
    path('telephone/create', TelephoneCreateView.as_view(),
         name='telephone_create'),
    path('telephone/update/<int:pk>',
         TelephoneUpdateView.as_view(), name='telephone_update'),
    path('telephone/delete/<int:pk>',
         views.delete_telephone, name='telephone_delete'),
    path('telephone/details/<int:pk>',
         TelephoneDetailView.as_view(), name='telephone_details'),
    path('telephone/assign/<int:id>',
         views.assign_telephone, name='assign_telephone'),
    path('telephone/update_telphone/<int:id>',
         views.put_telephone_instock, name='put_telephone_instock'),


    # Export Text Files
    path('telephone/export_phone_profile/<int:id>',
         views.export_phone_profile, name='export_telephone_profile'),
    path('telephone/export_device_profile/<int:id>',
         views.export_device_profile, name='export_device_profile'),


]
