# Generated by Django 4.1.7 on 2023-02-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0008_alter_employeeleave_date_back_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeleave",
            name="date_back",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="employeeleave",
            name="date_leave",
            field=models.DateTimeField(),
        ),
    ]
