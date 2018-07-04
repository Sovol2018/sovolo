from django.shortcuts import redirect
from requests.utils import quote
from social_core.pipeline.partial import partial
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import uuid
import urllib
import random
import string

from .models import User

@partial
def get_profile_image(strategy, details, response,
                      user=None, is_new=False, *args, **kwargs):
    backend = kwargs.get('backend')
    if is_new:
        if backend.name == 'facebook':
            url = "http://graph.facebook.com/%(id)s/picture?type=large" % {
                'id': response['id'],
            }
        elif backend.name == 'twitter':
            url = response.get('profile_image_url', '').replace('_normal', '')
        if url:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib.request.urlopen(url).read())
            img_temp.flush()

            user.image.save(str(uuid.uuid4()), File(img_temp))
            pass


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    # backend = kwargs.get('backend')
    if user and user.email:
        # The user we're logging in already has their email attribute set
        return

    if is_new:
        # print ('kwargs:', kwargs)
        # quick fix: check if username is registered, add random string if so
        # todo: rethink about username uniqueness
        # todo: only check when form is posted (token cache will be reloaded, this will run twice)

        posted = (strategy.request_data().get('posted') == '1')
        if not posted:
            ## first time
            # userName in kwargs overwrites details
            #  should check username in pre-processed string, i.e. after pipeline getusername
            #  (for some reason? pre-processed string is only in kwargs, not in details?)
            userNameDetails = details.get('username', None)
            userName = kwargs.get('username', userNameDetails)
            # userName = strategy.request_data().get('userName')
            if userName:
                existingUser = User.objects.filter(username=userName)
                if existingUser.exists():
                    randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
                    details['username'] = userName + randomString

            userEmailDetails = details.get('email', None)
            userEmail = kwargs.get('email', userEmailDetails)

            # if userEmail:
            #     findUser = User.objects.filter(email=userEmail)
            #     if findUser.exists():
            #         emailexists = 1
            current_partial = kwargs.get('current_partial')
            return strategy.redirect('/user/email_required?partial_token={0}&username={1}&email={2}'.format(
                current_partial.token, quote(userName), quote(userEmail)))

        # posted, check all
        userName = strategy.request_data().get('username')
        isallright = 1
        userexists = 0
        emailexists = 0
        if userName:
            existingUser = User.objects.filter(username=userName)
            if existingUser.exists():
                userexists = 1
                isallright = 0
        else: # name empty
            isallright = 0

        # if email is used by some user
        # (in facebook case): it seems facebook will come in this branch, not the following strategy email one
        userEmail = strategy.request_data().get('email')
        if userEmail:
            # first check if email exists
            findUser = User.objects.filter(email=userEmail)
            if findUser.exists():
                # seems we cannot set details['email'] directly here, maybe return is not good?
                # We should process strategy request for email input here, or will be caught in a loop
                emailexists = 1
                isallright = 0
        else: # email empty
            isallright = 0

        if not isallright:
            # If there's no email information to be had, we need to ask the
            # user to fill it in.  This should redirect us to a view
            current_partial = kwargs.get('current_partial')
            # return strategy.redirect('/user/email_required?partial_token={0}&emailexists=1'.format(current_partial.token))
            return strategy.redirect('/user/email_required?partial_token={0}&username={1}&email={2}&userexists={3}&emailexists={4}'.format(
                current_partial.token, quote(userName), quote(userEmail), userexists, emailexists))


        details['username'] = userName
        details['email'] = userEmail

        return {
            'username': userName,
            'email': userEmail
        }

    # if is_new and not details.get('email'):
    #     # If we're creating a new user, and we can't find the email in the
    #     # details.  we'll attempt to request it from the data returned from our
    #     # backend strategy
    #     userEmail = strategy.request_data().get('email')
    #     if userEmail:
    #         # first check if email exists
    #         findUser = User.objects.filter(email=userEmail)
    #         if findUser.exists():
    #             current_partial = kwargs.get('current_partial')
    #             return strategy.redirect('/user/email_required?partial_token={0}&emailexists=1'.format(current_partial.token))
    #         else:
    #             details['email'] = userEmail

    #     else:
    #         # If there's no email information to be had, we need to ask the
    #         # user to fill it in.  This should redirect us to a view
    #         current_partial = kwargs.get('current_partial')
    #         return strategy.redirect('/user/email_required?partial_token={0}'.format(current_partial.token))


# full pipeline func, check if is anonymous
def check_anonymous(strategy, details, request, user=None, *args, **kwargs):
    if request and request.user and request.user.is_authenticated:
        return redirect("/")
