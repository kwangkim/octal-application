from django.db import models

from apps.user_management.models import Profile

class Participants(models.Model):
    """
    Stores valid participant IDs
    """
    pid = models.CharField(max_length=5, unique=True)
    linear = models.BooleanField(default=False)
    presurvey = models.BooleanField(default=False)
    postsurvey = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%d' % (int(self.pid))

class ParticipantLogins(models.Model):
    """
    Stores information about participants
    A participant might use multiple browsers
    """
    uprofile = models.OneToOneField(Profile)
    participant = models.ForeignKey(Participants)
    timestamp = models.DateTimeField(auto_now_add=True)