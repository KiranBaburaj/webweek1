from django.contrib.auth import authenticate, login as adlogin
from django.contrib.auth import authenticate, logout as adlogout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required






@never_cache
def superuser_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            adlogin(request, user)
            # Redirect to the custom admin panel homepage
            return redirect('custom_admin_homepage')
        else:
            # Display invalid login error
            error_message = 'Invalid username or password.'
            return render(request, 'superuser_login.html', {'error_message': error_message})
    else:
        return render(request, 'superuser_login.html')





@never_cache
@login_required(login_url='superuser_login')
def create_user(request):
    if request.method == 'POST':
      
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username, email, password)  # Assuming password hashing is handled
        return redirect('user_list')  # Redirect to user list
    else:
        return render(request, 'create_user.html')


@never_cache
@login_required(login_url='superuser_login')
def custom_admin_homepage(request):

    context = {} 
    return render(request, 'custom_admin_homepage.html', context)

@never_cache
@login_required(login_url='superuser_login')
def user_list(request):
    users = User.objects.all()  
    context = {'users': users}
    return render(request, 'user_list.html', context)

    

@never_cache
@login_required(login_url='superuser_login')
def search_users(request):
    # Same logic as the user_list function, but with a different name
    query = request.GET.get('query')
    print(query)
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()

    context = {'users': users}
    return render(request, 'user_list.html', context)




@never_cache
@login_required(login_url='superuser_login')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Handle form data
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        user.save()
        return redirect('user_list')  # Redirect to user list upon success
    
    else:
        # Render the edit form for GET requests
        context = {'user': user}
        return render(request, 'edit_user.html', context)






@never_cache
@login_required(login_url='superuser_login')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Redirect to user list
    else:
        context = {'user': user}
        return render(request, 'delete_user.html', context)


@never_cache
@login_required(login_url='superuser_login')
def logout_view(request):
    adlogout(request)
    return redirect('superuser_login')  # Redirect to your login page after logout

