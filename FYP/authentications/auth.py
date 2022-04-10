from django.shortcuts import redirect


# To check if USER is LOGGED in or not
def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function


# check User role ADMIN or NOT
# and if the user is ADMIN, it gives access to ADMIN PAGES
# and if the user is NOT ADMIN, it redirects to USER DASHBOARD
def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function



# Check User role NORMAL or ADMIN
# and if the user is NORMAL USER, it gives access to USER PAGES
# and if the user is not NORMAL USER, it redirects to ADMIN DASHBOARD
def employee_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admins/dashboard')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function