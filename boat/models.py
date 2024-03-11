from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=150,verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True) #unique - второй такой почты не может быть

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = "Владельцы"

class Boat(models.Model):
    name = models.CharField(max_length=50,verbose_name='название')
    year = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name='год выпуска')
    price = models.IntegerField(null=True,blank=True,verbose_name='цена')
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,verbose_name='владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Лодка"
        verbose_name_plural = "Лодки"


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat,on_delete=models.CASCADE,verbose_name='лодка')
    start_year = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name='владел с')
    stop_year = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name='владел по')
    owner = models.ForeignKey(Owner,on_delete=models.SET_NULL,verbose_name='владелец',null=True,blank=True)


    def __str__(self):
        return f'{self.boat} {self.start_year}--{self.stop_year}'

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"
