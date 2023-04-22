from django.shortcuts import render
from main.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a FirstTable object for the new user
            first_table = FirstTable.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:profile")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form })
