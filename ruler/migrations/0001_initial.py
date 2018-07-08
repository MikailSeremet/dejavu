# Generated by Django 2.0.6 on 2018-07-04 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntervalApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_description', models.CharField(max_length=200)),
                ('interval_counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Intervals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_name', models.CharField(max_length=200)),
                ('interval_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='intervalapply',
            name='interval_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruler.Intervals'),
        ),
    ]