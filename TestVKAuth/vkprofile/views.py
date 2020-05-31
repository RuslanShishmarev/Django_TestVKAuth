
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests

def index(request):

    return render(
        request,
        'index.html',
        context={"user": request.user},
    )

def profile_detail(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    #Если админ или не зарегестрированный пользователь, то отправлю на страницу ошибки
    try:
        soc_user = SocialAccount.objects.get(user=request.user)

        social_account = SocialAccount.objects.get(provider='vk', user=request.user.pk)
        social_token = SocialToken.objects.get(account=social_account)

        #На всякий случай ловим аватарку пользователя
        try:
            avatar = soc_user.get_avatar_url()

        except:
            avatar = "no"

        friend_list = requests.get("https://api.vk.com/method/friends.get?user_id="
                                    + str(soc_user.uid) +
                                    "&count=5&fields=nickname,photo_200_orig&v=5.52&access_token="
                                    + str(social_token)).json()["response"]["items"]

        #Проверяем наличие друзей
        f_count = len(friend_list)
        if f_count == 0:
            friend_list = "no"

        args = {"user": user, "name": user.first_name, "last_name": user.last_name, "avatar": avatar, "friend_list": friend_list, "f_count": f_count}

        return render(
            request,
            'vkprofile/profile.html',
            args,
        )

    except:
        return render(
            request,
            'vkprofile/error.html',
            context={"user": request.user},
        )

