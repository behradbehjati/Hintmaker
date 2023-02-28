from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number,name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('You should set your email')



        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            name=name,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number,name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            phone_number=phone_number,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
