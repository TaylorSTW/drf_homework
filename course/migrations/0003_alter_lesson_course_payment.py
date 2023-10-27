# Generated by Django 4.2.4 on 2023-08-19 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.course', verbose_name='курс'),
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateTimeField(auto_now=True, verbose_name='дата платежа')),
                ('pay_sum', models.IntegerField(verbose_name='сумма платежа')),
                ('payment_type', models.CharField(choices=[('Card', 'карта'), ('CASH', 'наличка')], verbose_name='тип оплаты')),
                ('course_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
                ('lesson_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.lesson')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'оплата',
                'verbose_name_plural': 'оплаты',
            },
        ),
    ]