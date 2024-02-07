from django.db.models import Model,CharField,ImageField,CASCADE,DecimalField, FloatField



class UserModel(Model):
    title=CharField(max_length=255)
    price=DecimalField(max_digits=10,decimal_places=4)
    old_price=DecimalField(max_digits=10,decimal_places=4)
    sale=FloatField(max_length=255)
    image = ImageField(upload_to='user/')

    def __str__(self):
        return self.title