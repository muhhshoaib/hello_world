from django.db import models


class UserInfo(models.Model):
    """
    Django model to save the user name in the database
    with the creation date/time
    """

    name = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        """
        How to serialize myself as a string
        """

        return "{name}: {created_date}".format(
            name=self.name,
            created_date=self.created.strftime('%l:%M%p %Z on %b %d, %Y')
        )

    @classmethod
    def get_all_users_info(cls):
        """
        returns all the users info objects
        """
        return cls.objects.all()