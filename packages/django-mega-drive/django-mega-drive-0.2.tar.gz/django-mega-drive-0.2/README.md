settins.py
``` 
MEGA_ACCOUNTS = {
    'default': {
        'email': 'mega drive account email here',
        'password': "mega drive account password"
    },

    # define another account  with anothers alias
}
```

models.py
```
from mega_drive.storage import MegaDriveStorage
from django.db import model

drive_storage = MegaDriveStorage(account_alias='default')
second_drive_storage = MegaDriveStorage(
    account_alias="another_mega_drive_alias")

class Profile(models.Model):
    image = models.ImageField(
        upload_to='upload_destination', storage=drive_storage)
    image = models.FileField(
        upload_to='upload_destination', storage=second_drive_storage)
    ...

```
