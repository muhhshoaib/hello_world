from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from .models import UserInfo
from django.template.context_processors import csrf


def home(request):
    """
    GET returns the html for with post url in the context dictionary
    to render the home.html page

    POST creates a new UserInfo object and renders the name of the user
    in the user_info.html page
    """
    if request.method == 'GET':
        url = reverse('helloworld.views.home')
        context_dict = {'url': url}
        context_dict.update(csrf(request))

        # call render_to_response method
        return render_to_response('home.html', context=context_dict)

    if request.method == "POST":
        name = request.POST['name']

        # save the name in the UserInfo table
        user_info = UserInfo.objects.create(name=name)

        # call render_to_response method
        return render_to_response('user_info.html', context={'name': user_info.name})
