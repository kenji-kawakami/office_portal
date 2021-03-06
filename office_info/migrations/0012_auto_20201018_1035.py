# Generated by Django 3.0.8 on 2020-10-18 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office_info', '0011_auto_20200821_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='first_name_kana',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='first_name_kanji',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name_kana',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name_kanji',
        ),
        migrations.AddField(
            model_name='staff',
            name='name_kana',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='氏名（かな）'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name_kanji',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='氏名（漢字）'),
        ),
        migrations.AddField(
            model_name='staff',
            name='name_romaji',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='氏名（ローマ字）'),
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='パスワード'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('type', models.SmallIntegerField(verbose_name='タイプ')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='office_info.Staff', verbose_name='社員')),
            ],
            options={
                'verbose_name_plural': 'タグ',
            },
        ),
    ]
