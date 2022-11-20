from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from django.views.generic import *
from django.views import *
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import *

# relative import
from teldb.models import *
from teldb.forms import *
from teldb.filters import *

import datetime

# Create your views here.


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


@login_required
def index(request):
    context = {
    }
    return render(request, "telephone/telephone_list.html", context)


""" Locations Views"""


class LocationListView(LoginRequiredMixin, FilteredListView):
    model = Location
    template_name = 'location/location_list.html'
    context_object_name = 'locations'
    filterset_class = LocationFilter
    paginate_by = 10


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "location/location_form.html"

    def get_success_url(self):
        return reverse('location_list')


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = "location/location_form.html"

    def get_success_url(self):
        return reverse('location_list')


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    context_object_name = 'location'
    success_url = reverse_lazy('location_list')
    template_name = "location/location_delete.html"


""" Organization Views"""


class OrganizationListView(LoginRequiredMixin, FilteredListView):
    model = Organization
    paginate_by = 10
    filterset_class = OrganizationFilter
    template_name = 'organization/organization_list.html'
    context_object_name = 'organizations'


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization/organization_form.html"

    def get_success_url(self):
        return reverse('organization_list')


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization/organization_form.html"

    def get_success_url(self):
        return reverse('organization_list')


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    context_object_name = 'organization'
    success_url = reverse_lazy('organization_list')
    template_name = "organization/organization_delete.html"


""" Department """


class DepartmentListView(LoginRequiredMixin, FilteredListView):
    model = Department
    paginate_by = 10
    filterset_class = DepartmentFilter
    template_name = 'department/department_list.html'
    context_object_name = 'departments'


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/department_form.html"

    def get_success_url(self):
        return reverse('department_list')


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/department_form.html"

    def get_success_url(self):
        return reverse('department_list')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    context_object_name = 'department'
    success_url = reverse_lazy('department_list')
    template_name = "department/department_delete.html"


""" Code Views"""


class CodeListView(LoginRequiredMixin, FilteredListView):
    model = Code
    paginate_by = 10
    filterset_class = CodeFilter
    template_name = 'code/code_list.html'
    context_object_name = 'codes'


class CodeUpdateView(LoginRequiredMixin, UpdateView):
    model = Code
    form_class = CodeForm
    template_name = "code/code_form.html"

    def get_success_url(self):
        return reverse('code_list')


class CodeCreateView(LoginRequiredMixin, CreateView):
    model = Code
    form_class = CodeForm
    template_name = "code/code_form.html"

    # fields = ['location_name']

    def get_success_url(self):
        return reverse('code_list')


class CodeDeleteView(LoginRequiredMixin, DeleteView):
    model = Code
    context_object_name = 'code'
    success_url = reverse_lazy('code_list')
    template_name = "code/code_delete.html"


""" Employee Category """


class EmployeeCategoryListView(LoginRequiredMixin, FilteredListView):
    model = EmployeeCategory
    paginate_by = 10
    filterset_class = EmployeeCategoryFilter
    template_name = 'employee_category/employee_category_list.html'
    context_object_name = 'employee_categories'


class EmployeeCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeCategory
    form_class = EmployeeCategoryForm
    template_name = "employee_category/employee_category_form.html"

    def get_success_url(self):
        return reverse('employee_category_list')


class EmployeeCategoryCreateView(LoginRequiredMixin, CreateView):
    model = EmployeeCategory
    form_class = EmployeeCategoryForm
    template_name = "employee_category/employee_category_form.html"

    # fields = ['location_name']

    def get_success_url(self):
        return reverse('employee_category_list')


class EmployeeCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = EmployeeCategory
    context_object_name = 'employee_category'
    success_url = reverse_lazy('employee_category_list')
    template_name = "employee_category/employee_category_delete.html"


""" Employee Views """


class EmployeeListView(LoginRequiredMixin, FilteredListView):
    model = Employee
    paginate_by = 10
    template_name = "employee/employee_list.html"
    context_object_name = 'employees'
    filterset_class = EmployeeFilter


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')
    template_name = 'employee/employee_form.html'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'

    def get_success_url(self):
        return reverse('employee_list')


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee/employee_delete.html'

    def get_success_url(self):
        return reverse('employee_list')


""" Direct Inward DialIn Views """


class DirectInwardDialInListViews(LoginRequiredMixin, FilteredListView):
    model = DirectInwardDialIn
    paginate_by = 20
    filterset_class = DirectInwardDialInFilter
    template_name = 'did/did_list.html'
    context_object_name = 'dids'


class DirectInWardDialInUpdateView(LoginRequiredMixin, UpdateView):
    model = DirectInwardDialIn
    template_name = 'did/did_form.html'
    form_class = DirectInwardDialInForm

    def get_success_url(self):
        return reverse('did_list')


class DirectInWardDialInCreateView(LoginRequiredMixin, CreateView):
    model = DirectInwardDialIn
    template_name = 'did/did_form.html'
    form_class = DirectInwardDialInForm

    def get_success_url(self):
        return reverse('did_list')


class DirectInWardDialInDeleteView(LoginRequiredMixin, DeleteView):
    model = DirectInwardDialIn
    context_object_name = 'did'
    template_name = 'did/did_delete.html'

    def get_success_url(self):
        return reverse('did_list')


""" DeviceType Views"""


class DeviceTypeListView(LoginRequiredMixin, FilteredListView):
    model = DeviceType
    paginate_by = 10
    filterset_class = DeviceTypeFilter
    context_object_name = 'device_types'
    template_name = 'device_type/device_type_list.html'


class DeviceTypeCreateView(LoginRequiredMixin, CreateView):
    model = DeviceType
    template_name = 'device_type/device_type_form.html'
    form_class = DeviceTypeForm

    def get_success_url(self):
        return reverse('device_type_list')


class DeviceTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DeviceType
    template_name = 'device_type/device_type_form.html'
    form_class = DeviceTypeForm

    def get_success_url(self):
        return reverse('device_type_list')


class DeviceTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DeviceType
    template_name = 'device_type/device_type_delete.html'
    context_object_name = 'device_type'

    def get_success_url(self):
        return reverse('device_type_list')


""" Telephone Views """


class TelephoneListView(LoginRequiredMixin, FilteredListView):
    model = Telephone
    filterset_class = TelephoneFilter
    paginate_by = 25
    context_object_name = 'telephones'
    template_name = 'telephone/telephone_list.html'


class TelephoneCreateView(LoginRequiredMixin, CreateView):
    model = Telephone
    context_object_name = 'telephone'
    template_name = 'telephone/telephone_form.html'
    form_class = TelephoneForm

    def get_success_url(self):
        return reverse('telephone_list')


class TelephoneUpdateView(LoginRequiredMixin, UpdateView):
    model = Telephone
    template_name = 'telephone/telephone_form.html'
    form_class = TelephoneForm
    success_url = reverse_lazy('telephone_list')


class TelephoneDetailView(LoginRequiredMixin, DetailView):
    model = Telephone
    context_object_name = 'telephone'
    template_name = 'telephone/telephone_details.html'


# class TelephoneDeleteView(DeleteView):
#     model = Telephone
#     template_name = 'telephone/telephone_delete.html'
#     context_object_name = 'telephone'

#     def get_success_url(self):
#         return reverse('telephone_list')

#     def post(self, request, *args, **kwargs):

#         self.object = self.get_object()
#         form = self.get_form()

#         if form.is_valid():
#             did = DirectInwardDialIn.objects.get(id=object.extension_number.id)
#             did.status = 'Free'
#             did.save()
#             return self.form_valid(form)

#         else:
#             return self.form_invalid(form)

@login_required
def delete_telephone(request, pk):

    telephone = Telephone.objects.get(id=pk)

    if request.method == 'POST':
        if telephone.extension_number == None:
            telephone.delete()
        else:
            did = DirectInwardDialIn.objects.get(
                id=telephone.extension_number.id)
            did.status = 'Free'
            did.save()
            telephone.delete()
        return redirect('telephone_list')

    context = {'telephone': telephone}

    return render(request, 'telephone/telephone_delete.html', context)


@login_required
def assign_telephone(request, id):

    telephone = get_object_or_404(Telephone, id=id)
    form = AssignTelephoneForm(instance=telephone)
    if request.method == 'POST':
        form.save(commit=False)
        form = AssignTelephoneForm(request.POST, instance=telephone)
        if form.is_valid():
            did = DirectInwardDialIn.objects.get(
                id=telephone.extension_number.id)
            telephone.status = 'Installed'
            telephone.connection_date = datetime.date.today()
            did.status = 'Active'
            did.save()
            form.save()
            return redirect('telephone_list')
    context = {
        'form': form,
        'telephone': telephone
    }

    return render(request, 'telephone/telephone_assign_form.html', context)


@login_required
def put_telephone_instock(request, id):

    telephone = get_object_or_404(Telephone, id=id)
    form = PutTelephoneInStock(instance=telephone)
    if request.method == 'POST':
        form = PutTelephoneInStock(request.POST, instance=telephone)
        did = DirectInwardDialIn.objects.get(id=telephone.extension_number.id)
        if form.is_valid():
            telephone.assigned_to = None
            telephone.connection_date = None
            telephone.disconnection_date = None
            telephone.status = 'In Stock'
            telephone.extension_number = None
            did.status = 'Free'
            did.save()
            form.save()
            return redirect('telephone_list')
    context = {
        'form': form,
        'telephone': telephone,
    }

    return render(request, 'telephone/telephone_instock_form.html', context)


@login_required
def export_phone_profile(request, id):

    telephone = Telephone.objects.get(id=id)
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = telephone_profile.txt'

    lines = ["MAC ADDRESS, DESCRIPTION, DIRECTORY NUMBER  1, LINE DESCRIPTION  1, ALERTING NAME  1, ASCII ALERTING NAME  1, DISPLAY  1, ASCII DISPLAY  1, LINE TEXT LABEL  1", "\n"]
    lines.append(
        f'{telephone.mac_address},{telephone.assigned_to.organization}-{telephone.extension_number},{telephone.extension_number},{telephone.assigned_to.organization}-{telephone.extension_number},{telephone.assigned_to},{telephone.assigned_to},{telephone.assigned_to},{telephone.assigned_to},{telephone.assigned_to}')

    # Write to text File
    response.writelines(lines)
    return response


@login_required
def export_device_profile(request, id):

    telephone = Telephone.objects.get(id=id)
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = telephone_profile.txt'

    lines = ["DEVICE PROFILE NAME,DESCRIPTION,DIRECTORY NUMBER  1,LINE DESCRIPTION  1,ALERTING NAME  1,ASCII ALERTING NAME  1,FORWARD BUSY EXTERNAL DESTINATION  1,FORWARD BUSY INTERNAL DESTINATION  1,FORWARD NO ANSWER EXTERNAL DESTINATION  1,FORWARD NO ANSWER INTERNAL DESTINATION  1,FORWARD UNREGISTERED EXTERNAL DESTINATION  1,FORWARD UNREGISTERED INTERNAL DESTINATION  1,DISPLAY  1,ASCII DISPLAY  1,LINE TEXT LABEL  1", "\n"]
    lines.append(
        f'{telephone.assigned_to.organization}-{telephone.extension_number},{telephone.assigned_to.organization}-{telephone.extension_number},{telephone.extension_number},{telephone.assigned_to.organization}-{telephone.extension_number},*{telephone.assigned_to},*{telephone.assigned_to},{telephone.extension_number},{telephone.extension_number},{telephone.extension_number},{telephone.extension_number},{telephone.extension_number},{telephone.extension_number},*{telephone.assigned_to},*{telephone.assigned_to},*{telephone.assigned_to}')

    # Write to text File
    response.writelines(lines)
    return response
