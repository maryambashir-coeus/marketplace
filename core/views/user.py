from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms.profile import ProfileForm, UserForm
from .models import Profile


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
