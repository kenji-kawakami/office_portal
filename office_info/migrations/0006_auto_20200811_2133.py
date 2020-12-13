# Generated by Django 3.0.8 on 2020-08-11 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office_info', '0005_auto_20200811_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='task',
        ),
        migrations.CreateModel(
            name='TaskSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('ratio', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='割合')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_skill', to='office_info.Task', verbose_name='タスクスキル')),
            ],
            options={
                'verbose_name_plural': 'タスクスキル',
            },
        ),
    ]
