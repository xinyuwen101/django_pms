from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            # has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            # if has_contacted:
            #     messages.error(request, _('You have already made a contact for this listing'))
            #     return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)

        contact.save()

        # Send email
        # send_mail(
        #     'Property Notification',
        #     'There has been a message for ' + listing + '. Sign into the dashboard page for more information. Do not reply this email',
        #     'properties@xinyuwen.com',
        #     [realtor_email],
        #     fail_silently=False
        # )

        messages.success(request, _('Your message has been submitted'))
        return redirect('/listings/' + listing_id)
