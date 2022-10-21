from django.db import models
import uuid

# Should have a uuid, but didn't for certain reasons
class Organisation(models.Model):
    organisation_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=100)
    group_password = models.CharField(max_length=100)

    
