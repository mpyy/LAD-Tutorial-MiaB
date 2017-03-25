from random import randint

from django.shortcuts import render
from django.db.models import Count

from rest_framework import views
from rest_framework.response import Response

from . import serializers, models

# Create your views here.
class MessageView(views.APIView):
    """View to managing messages through the API."""

    # The 'serializer' class takes out input and turns it into
    # a Python object we can play with.
    serializer_class = serializers.MessageSerializer

    # This is what happens when we receive a HTTP POST request to the API.
    def post(self, request, format=None):
        """Receive the post of the new message and return a random one."""

        # First, let's get a random message.
        # (We do this first to avoid getting the same message the users posts.)
        random_message = self._get_random_message()

        # Send the users input to the serializer class.
        serializer = self.serializer_class(data=request.data)
        # Check that the users input is valid. Raise an exception if it's not,
        # as DjangoRestFramework will automatically display the error to the
        # user.
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # If we got this far, no exception was raised and the input is valid.
        # So let's mark the "random_message" as read.
        random_message.is_read = True
        # Now save the updates to the 'random_message' in the database.
        random_message.save()

        # Now return the data of the serializer class.
        return Response(self.serializer_class(random_message).data)

    # This is our method that will get a random message.
    def _get_random_message(self):
        """Get a Random Message from the Database."""

        # Get the count of un-read random messages in the database.
        count = models.Message.objects.filter(
            is_read=False
        ).aggregate(
            count=Count('id')
        )['count']

        # Get a random number between the count.
        random_index = randint(0, count - 1)
        # Select the unread message for the random number that was selected.
        random_message = models.Message.objects.filter(
            is_read=False)[random_index]

        # Return the random_message.
        return random_message
