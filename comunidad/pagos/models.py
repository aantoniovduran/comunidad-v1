from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

PAGADO_ADEUDADO_CHOICES = (
    (True, 'Pagado'),
    (False, 'Adeudado')
)
SEXO_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('N', 'No_declarado')
)

###################perfil usuario##########################
class Profile(models.Model):
    """Model definition for Socio."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    numsocio = models.CharField(max_length=15, null=True)
    nombre1 = models.CharField(max_length=15)
    nombre2 = models.CharField(max_length=15, null=True)
    apellido1 = models.CharField(max_length=15)
    apellido2 = models.CharField(max_length=15, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    direccion = models.CharField(max_length=60, null=True)
    comuna = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    telefono = models.IntegerField(null=True)
    celular = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    cumple = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='foto_socios', null=True, blank=True)
    valoracion = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_nombre_completo(self):
        full_name = '%s %s %s %s' % (self.nombre1, self.nombre2, self.apellido1, self.apellido2)
        return full_name.strip()

    def get_primer_nombre(self):
        return self.nombre1

    def get_direccion(self):
        return self.direccion

    def get_comuna(self):
        return self.comuna

    def get_email(self):
        return self.email

    def get_bio(self):
        return self.bio
        
    def get_telefonos(self):
        telefonos = '%s %s' % (self.telefono, self.celular)
        return telefonos.strip()


    
    class Meta:
        """Meta definition for Socio."""
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        """Unicode representation of PerfilUsuario."""
        return 'Socio N° %s %s %s'%(self.numsocio, self.nombre1, self.apellido1)
        pass

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


###############################################
############## sys cuotas #####################
###############################################

class Cuota(models.Model):
    """Model definition for Cuota."""
    socio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cuotas_socio')
    cuotames = models.CharField(max_length=5)
    multa1 = models.IntegerField(blank=True, null=True)
    multa2 = models.IntegerField(blank=True, null=True)
    cuota1 = models.IntegerField(blank=True, null=True)
    cuota2 = models.IntegerField(blank=True, null=True)
    fechapub = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        """Meta definition for Cuota."""
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas'
   
    def __str__(self):
        """Unicode representation of Cuotas."""
        return 'la cuota %s para %s se registro'%(self.cuotames, self.socio)
        pass

class Pagos(models.Model):
    """Model definition for Pagos."""

    socio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos_socio')
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE, related_name='cuotas_sociales')
    fechapago = models.DateTimeField(default=timezone.now)
    estadocuota = models.BooleanField(choices=PAGADO_ADEUDADO_CHOICES, default='Adeudado')

    class Meta:
        """Meta definition for Cuota."""

        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
    def __str__(self):
        """Unicode representation of Pagos."""
        return ' El pago de %s %s '%(self.cuota, self.get_estadocuota_display())
        pass