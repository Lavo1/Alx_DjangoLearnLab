from django.shortcuts import render

# after creating a user
user = CustomUser.objects.create_user(...)
UserProfile.objects.create(user=user, role='Member')
 Create your views here.
