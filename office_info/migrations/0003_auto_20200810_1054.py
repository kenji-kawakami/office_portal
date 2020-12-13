# Generated by Django 3.0.8 on 2020-08-10 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office_info', '0002_auto_20200803_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('priority', models.IntegerField(default=1, verbose_name='優先度')),
                ('remark', models.TextField(blank=True, max_length=1000, null=True, verbose_name='備考')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
            ],
            options={
                'verbose_name_plural': 'データセット',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('priority', models.IntegerField(default=1, verbose_name='優先度')),
                ('remark', models.TextField(blank=True, max_length=1000, null=True, verbose_name='備考')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
            ],
            options={
                'verbose_name_plural': '工程',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('background', models.TextField(blank=True, max_length=1000, null=True, verbose_name='背景')),
                ('purpose', models.TextField(blank=True, max_length=1000, null=True, verbose_name='目的')),
                ('start_date', models.DateField(verbose_name='開始日付')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='終了日付')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
            ],
            options={
                'verbose_name_plural': 'プロジェクト',
            },
        ),
        migrations.AlterField(
            model_name='skill',
            name='departmental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='office_info.Departmental', verbose_name='部署'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('priority', models.IntegerField(default=1, verbose_name='優先度')),
                ('cost', models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='工数')),
                ('remark', models.TextField(blank=True, max_length=1000, null=True, verbose_name='備考')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='office_info.Dataset', verbose_name='データセット')),
            ],
            options={
                'verbose_name_plural': 'タスク',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.IntegerField(verbose_name='社員コード')),
                ('last_name_kanji', models.CharField(max_length=20, verbose_name='姓（漢字）')),
                ('first_name_kanji', models.CharField(max_length=20, verbose_name='名（漢字）')),
                ('last_name_kana', models.CharField(max_length=20, verbose_name='姓（かな）')),
                ('first_name_kana', models.CharField(max_length=20, verbose_name='名（かな）')),
                ('birthdate', models.DateField(verbose_name='生年月日')),
                ('age', models.SmallIntegerField(verbose_name='年齢')),
                ('sex', models.SmallIntegerField(default=0, verbose_name='性別')),
                ('profile_image', models.BinaryField(blank=True, null=True, verbose_name='プロフィール画像')),
                ('zip_code', models.IntegerField(verbose_name='郵便番号')),
                ('state', models.CharField(max_length=10, verbose_name='都道府県')),
                ('city', models.CharField(max_length=200, verbose_name='市区町村')),
                ('address', models.CharField(max_length=200, verbose_name='番地、ビル名')),
                ('tel', models.IntegerField(blank=True, null=True, verbose_name='自宅')),
                ('mobile', models.IntegerField(blank=True, null=True, verbose_name='携帯電話')),
                ('mail_address', models.CharField(max_length=100, verbose_name='メールアドレス')),
                ('hire_date', models.DateField(verbose_name='雇用日')),
                ('position_name', models.SmallIntegerField(blank=True, null=True, verbose_name='役職区分')),
                ('profession', models.SmallIntegerField(blank=True, null=True, verbose_name='職種区分')),
                ('employment', models.SmallIntegerField(verbose_name='雇用区分')),
                ('health_insurance_number', models.IntegerField(verbose_name='健康保険番号')),
                ('basic_pension_numbers', models.CharField(max_length=10, verbose_name='基礎年金番号')),
                ('my_number', models.IntegerField(verbose_name='マイナンバー')),
                ('employment_insurance_number', models.IntegerField(verbose_name='雇用保険番号')),
                ('nationality', models.CharField(max_length=30, verbose_name='国籍')),
                ('native_place', models.CharField(max_length=10, verbose_name='出身地')),
                ('blood_type', models.CharField(blank=True, max_length=2, null=True, verbose_name='血液型')),
                ('academic_history', models.CharField(blank=True, max_length=100, null=True, verbose_name='最終学歴')),
                ('basic_salary', models.IntegerField(blank=True, null=True, verbose_name='基本給')),
                ('notices', models.TextField(blank=True, max_length=1000, null=True, verbose_name='特記事項')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('project', models.ManyToManyField(related_name='staff', to='office_info.Project', verbose_name='プロジェクト')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='office_info.Departmental', verbose_name='部署')),
            ],
            options={
                'verbose_name_plural': '社員',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='工数')),
                ('main_member', models.CharField(max_length=40, verbose_name='担当')),
                ('sub_member', models.CharField(max_length=40, verbose_name='副担当')),
                ('start_time', models.DateTimeField(verbose_name='開始時間')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='終了時間')),
                ('reflections', models.TextField(blank=True, max_length=1000, null=True, verbose_name='振り返り内容')),
                ('evaluation', models.TextField(blank=True, max_length=1000, null=True, verbose_name='評価内容')),
                ('status', models.SmallIntegerField(verbose_name='ステータス')),
                ('receptionist', models.CharField(max_length=40, verbose_name='対応者')),
                ('plan_start_date', models.DateField(verbose_name='予定開始日')),
                ('plan_end_date', models.DateField(blank=True, null=True, verbose_name='予定終了日')),
                ('result_start_date', models.DateField(blank=True, null=True, verbose_name='実績開始日')),
                ('result_end_date', models.DateField(blank=True, null=True, verbose_name='実績予定日')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('dataset', models.ManyToManyField(related_name='schedule', to='office_info.Dataset', verbose_name='データセット')),
                ('process', models.ManyToManyField(related_name='schedule', to='office_info.Process', verbose_name='工程')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='office_info.Project', verbose_name='プロジェクト')),
                ('task', models.ManyToManyField(related_name='schedule', to='office_info.Task', verbose_name='タスク')),
            ],
            options={
                'verbose_name_plural': 'スケジュール',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('connection', models.CharField(max_length=12, verbose_name='続柄')),
                ('age', models.SmallIntegerField(verbose_name='年齢')),
                ('create_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='作成者')),
                ('update_user', models.CharField(blank=True, max_length=40, null=True, verbose_name='更新者')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='更新日')),
                ('delete_flag', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family', to='office_info.Staff', verbose_name='社員')),
            ],
            options={
                'verbose_name_plural': '家族',
            },
        ),
        migrations.AddField(
            model_name='dataset',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='office_info.Process', verbose_name='工程'),
        ),
    ]