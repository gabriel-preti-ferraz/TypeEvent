# Generated by Django 4.2 on 2023-04-15 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0005_certificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
