# Generated by Django 4.1.5 on 2023-05-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecom", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="discrition", new_name="discription",
        ),
    ]
