from django.db import models


# プロジェクトテーブル
class Project(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    background = models.TextField(verbose_name='背景', max_length=1000, blank=True, null=True)
    purpose = models.TextField(verbose_name='目的', max_length=1000, blank=True, null=True)
    start_date = models.DateField(verbose_name='開始日付')
    end_date = models.DateField(verbose_name='終了日付', blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'プロジェクト'

    def __str__(self):
        return self.name


# 工程テーブル
class Process(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    priority = models.IntegerField(verbose_name='優先度', default=1)
    remark = models.TextField(verbose_name='備考', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = '工程'

    def __str__(self):
        return self.name


# データセットテーブル
class Dataset(models.Model):
    process = models.ForeignKey(Process, verbose_name='工程', on_delete=models.CASCADE, related_name='dataset')
    name = models.CharField(verbose_name='名称', max_length=100)
    priority = models.IntegerField(verbose_name='優先度', default=1)
    remark = models.TextField(verbose_name='備考', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'データセット'

    def __str__(self):
        return self.name


# タスクテーブル
class Task(models.Model):
    dataset = models.ForeignKey(Dataset, verbose_name='データセット', on_delete=models.CASCADE, related_name='task')
    name = models.CharField(verbose_name='名称', max_length=100)
    priority = models.IntegerField(verbose_name='優先度', default=1)
    cost = models.DecimalField(verbose_name='工数', max_digits=4, decimal_places=2, default=1)
    remark = models.TextField(verbose_name='備考', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'タスク'

    def __str__(self):
        return self.name


# タスクスキルテーブル
class TaskSkill(models.Model):
    task = models.ForeignKey(Task, verbose_name='タスクスキル', on_delete=models.CASCADE, related_name='task_skill')
    skill_name = models.CharField(verbose_name='スキル名称', max_length=100, blank=True, null=True)
    ratio = models.IntegerField(verbose_name='割合', blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'タスクスキル'

    def __str__(self):
        return self.skill_name


# 部署テーブル
class Departmental(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    remark = models.TextField(verbose_name='備考', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = '部署'

    def __str__(self):
        return self.name


# スキルテーブル
class Skill(models.Model):
    departmental = models.ForeignKey(Departmental, verbose_name='部署', on_delete=models.CASCADE, related_name='skill')
    name = models.CharField(verbose_name='名称', max_length=100)
    remark = models.TextField(verbose_name='備考', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'スキル'

    def __str__(self):
        return self.name


# スケジュールテーブル
class Schedule(models.Model):
    project = models.OneToOneField(Project, verbose_name='プロジェクト', on_delete=models.CASCADE, related_name='schedule')
    process = models.ManyToManyField(Process, verbose_name='工程', related_name='schedule')
    dataset = models.ManyToManyField(Dataset, verbose_name='データセット', related_name='schedule')
    task = models.ManyToManyField(Task, verbose_name='タスク', related_name='schedule')
    cost = models.DecimalField(verbose_name='工数', max_digits=4, decimal_places=2)
    main_member = models.CharField(verbose_name='担当', max_length=40)
    sub_member = models.CharField(verbose_name='副担当', max_length=40)
    start_time = models.DateTimeField(verbose_name='開始時間')
    end_time = models.DateTimeField(verbose_name='終了時間', blank=True, null=True)
    reflections = models.TextField(verbose_name='振り返り内容', max_length=1000, blank=True, null=True)
    evaluation = models.TextField(verbose_name='評価内容', max_length=1000, blank=True, null=True)
    status = models.SmallIntegerField(verbose_name='ステータス')
    receptionist = models.CharField(verbose_name='対応者', max_length=40)
    plan_start_date = models.DateField(verbose_name='予定開始日')
    plan_end_date = models.DateField(verbose_name='予定終了日', blank=True, null=True)
    result_start_date = models.DateField(verbose_name='実績開始日', blank=True, null=True)
    result_end_date = models.DateField(verbose_name='実績予定日', blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'スケジュール'

    def __str__(self):
        return self.cost


# 社員テーブル
class Staff(models.Model):
    project = models.ManyToManyField(Project, verbose_name='プロジェクト', related_name='staff')
    departmental = models.ForeignKey(Departmental, verbose_name='部署', on_delete=models.CASCADE, related_name='staff')
    company_code = models.CharField(verbose_name='社員コード', max_length=10)
    password = models.CharField(verbose_name='パスワード', max_length=20, blank=True, null=True)
    name_kanji = models.CharField(verbose_name='氏名（漢字）', max_length=20, blank=True, null=True)
    name_romaji = models.CharField(verbose_name='氏名（ローマ字）', max_length=40, blank=True, null=True)
    name_kana = models.CharField(verbose_name='氏名（かな）', max_length=20, blank=True, null=True)
    birthdate = models.DateField(verbose_name='生年月日')
    age = models.SmallIntegerField(verbose_name='年齢')
    sex = models.CharField(verbose_name='性別', max_length=6)
    profile_image = models.BinaryField(verbose_name='プロフィール画像', blank=True, null=True)
    zip_code = models.CharField(verbose_name='郵便番号', max_length=7)
    state = models.CharField(verbose_name='都道府県', max_length=10)
    city = models.CharField(verbose_name='市区町村', max_length=200)
    address = models.CharField(verbose_name='番地、ビル名', max_length=200)
    tel = models.CharField(verbose_name='自宅', max_length=10, blank=True, null=True)
    mobile = models.CharField(verbose_name='携帯電話', max_length=11, blank=True, null=True)
    mail_address = models.CharField(verbose_name='メールアドレス', max_length=100)
    hire_date = models.DateField(verbose_name='雇用日')
    position_name = models.CharField(verbose_name='役職', max_length=50, blank=True, null=True)
    profession = models.CharField(verbose_name='職種', max_length=50, blank=True, null=True)
    employment = models.CharField(verbose_name='雇用', max_length=20)
    health_insurance_number = models.CharField(verbose_name='健康保険番号', max_length=8)
    basic_pension_numbers = models.CharField(verbose_name='基礎年金番号', max_length=10)
    my_number = models.CharField(verbose_name='マイナンバー', max_length=12)
    employment_insurance_number = models.CharField(verbose_name='雇用保険番号', max_length=11)
    nationality = models.CharField(verbose_name='国籍', max_length=30)
    native_place = models.CharField(verbose_name='出身地', max_length=10)
    blood_type = models.CharField(verbose_name='血液型', max_length=2, blank=True, null=True)
    academic_history = models.CharField(verbose_name='最終学歴', max_length=100, blank=True, null=True)
    basic_salary = models.IntegerField(verbose_name='基本給', blank=True, null=True)
    notices = models.TextField(verbose_name='特記事項', max_length=1000, blank=True, null=True)
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = '社員'

    def __str__(self):
        return self.company_code


# タグテーブル
class Tag(models.Model):
    staff = models.ForeignKey(Staff, verbose_name='社員', on_delete=models.CASCADE, related_name='tag')
    name = models.CharField(verbose_name='名称', max_length=100)
    type = models.SmallIntegerField(verbose_name='タイプ')
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.name


# 家族テーブル
class Family(models.Model):
    staff = models.ForeignKey(Staff, verbose_name='社員', on_delete=models.CASCADE, related_name='family')
    name = models.CharField(verbose_name='名称', max_length=100)
    connection = models.CharField(verbose_name='続柄', max_length=12)
    age = models.SmallIntegerField(verbose_name='年齢')
    create_user = models.CharField(verbose_name='作成者', max_length=40, blank=True, null=True)
    update_user = models.CharField(verbose_name='更新者', max_length=40, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name='作成日', blank=True, null=True)
    update_date = models.DateTimeField(verbose_name='更新日', blank=True, null=True)
    delete_flag = models.BooleanField(verbose_name='削除フラグ', default=False)

    class Meta:
        verbose_name_plural = '家族'

    def __str__(self):
        return self.name

