# Generated by Django 4.2.5 on 2023-11-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgekeep', '0002_papers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='type',
            field=models.CharField(choices=[('financeandeconomics', 'Finance & Economics'), ('mathematicsandstatistics', 'Mathematics and Statictics'), ('environmentalscience', 'Environmental Science'), ('computerscience', 'Computer Science')], default='financeandeconomics', max_length=25),
        ),
    ]
