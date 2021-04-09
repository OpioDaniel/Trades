from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from django.contrib import messages
from .forms import (RegistrationForm, EditUserForm, UserProfileForm)
from .models import (GlobUser)


def home(request):
    return render(request, 'main/home.html', {'title':  'Main Page'})


def email_message(semail, type):
    if type == 'register':
        email_from = 'noreply@drbaranes.com'
        subject = 'Registration to Trading Program'
        body = 'Your registration has been accepted. Please login and update your profile in Edit your profile.' \
               ' http://127.0.0.1:8010/.'
    elif type == 'instructor_confirmed':
        email_from = 'noreply@drbaranes.com'
        subject = 'Confirmation on instructor status'
        body = 'Your status as instructor has been confirmed. You can create a new games:  http://127.0.0.1:8010/'

    send_mail(subject, body, email_from, [semail], fail_silently=False)


# Registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            semail = cd['email']
            email_message(semail, 'register')
            form.save()

            return redirect(reverse('main:home'))
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'main/reg_form.html', args)


# Portfolios
def view_profile(request, pk=None):
    if pk:
        user = GlobUser.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'main/profile.html', args)


def edit_user_profile(request):
    if request.method == 'POST':
        # print("edit_user_profile1000: \n\n", request.POST, '\n\n')
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        # print("edit_user_profile1001: \n\n", user_form, '\n\n')
        # print("edit_user_profile1001: \n\n", profile_form, '\n\n')
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'User profile updated successfully.')
            return redirect(reverse('main:view_profile'))
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'main/edit_user_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('main:view_profile'))
        else:
            return redirect(reverse('main:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'main/change_password.html', args)


class MyPasswordResetView(PasswordResetView):
    # form_class = PasswordResetForm
    template_name = 'main/reset_password.html'
    success_url = reverse_lazy('main:password_reset_done')
    # subject_template_name = 'accounts/emails/password-reset-subject.txt'
    email_template_name = 'main/reset_password_email.html'


class MyPasswordResetDoneView(PasswordResetDoneView):
    # form_class = PasswordResetForm
    template_name = 'main/reset_password_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    # form_class = PasswordResetForm
    template_name = 'main/reset_password_confirm.html'
    success_url = reverse_lazy('main:password_reset_complete')


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/reset_password_complete.html'



