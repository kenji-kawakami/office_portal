from django.forms import ModelForm
from .models import Project, Process, Dataset, Task, Departmental, Skill, Schedule, Staff, Family, TaskSkill


# 部署登録、更新用のフォーム
class DepartmentalForm(ModelForm):
    class Meta:
        model = Departmental
        fields = [
            'name',
            'remark',
        ]


# スキル登録、更新用のフォーム
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            'name',
            'remark',
        ]


# 工程登録、更新用のフォーム
class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = [
            'name',
            'priority',
            'remark',
        ]


# データセット登録、更新用のフォーム
class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = [
            'name',
            'priority',
            'remark',
        ]


# タスク登録、更新用のフォーム
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'priority',
            'cost',
            'remark',
        ]

