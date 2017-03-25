from django.db import models

# Create your models here.
class Message(models.Model):
    """Stores messages for our bottles."""

    # Create a text column to store the message. Limit this to 120
    # characters as we this isn't "Essey in a Bottle"
    message = models.CharField(max_length=120)
    # Add a boolean column for marking messages as read, so we can
    # filter them to ensure users only get new messages.
    is_read = models.BooleanField(default=False)

    # This is meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'message'
 
    # Define what to output when the model is printed as a string.
    def __str__(self):
        # Return the message.
        return self.message
