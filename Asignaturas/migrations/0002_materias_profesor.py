# Generated by Django 3.2.7 on 2021-10-04 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_docente'),
        ('Asignaturas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materias',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.docente'),
        ),
    ]