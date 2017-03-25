from rest_framework import serializers

from api import models
 

# The serializer class takes the users input and converts it to a Python
# object that we can work with (and vica versa).
class MessageSerializer(serializers.ModelSerializer):
    """A serializer for our message model."""

    class Meta:
        # Tell the serializer class that the data should match our
        # "Message" database model.
        model = models.Message
        # Tell it we only expect to see the 'message' field (as all other
        # fields will be automatically generated).
        fields = ('message',)
