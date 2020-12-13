from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView
import urllib.parse as parse

from .models import Project, Process, Dataset, Task, Departmental, Skill, Schedule, Staff, Family, TaskSkill
from .forms import ProcessForm, DatasetForm, TaskForm, DepartmentalForm, SkillForm


POSITION_NAME = [
    '部長',
    '次長',
    '課長',
    '係長',
    '主任',
    '副主任',
    '一般社員'
]

PROFESSION = [
    'システムエンジニア',
    'プログラマー',
    'OA関連',
    'ユーザーサポート',
    'IT・エンジニアその他'
]

NATIONALITY = [
    '日本',
    'イタリア',
    'インド',
    'インドネシア',
    '韓国',
    'タイ',
    '台湾',
    '中国',
    'フランス',
    '米国',
    'ベトナム',
    'ロシア連邦',
    'その他の国・地域'
]

NATIVE_PLACE = [
    '北海道',
    '青森県',
    '岩手県',
    '宮城県',
    '秋田県',
    '山形県',
    '福島県',
    '茨城県',
    '栃木県',
    '群馬県',
    '埼玉県',
    '千葉県',
    '東京都',
    '神奈川県',
    '新潟県',
    '富山県',
    '石川県',
    '福井県',
    '山梨県',
    '長野県',
    '岐阜県',
    '静岡県',
    '愛知県',
    '三重県',
    '滋賀県',
    '京都府',
    '大阪府',
    '兵庫県',
    '奈良県',
    '和歌山県',
    '鳥取県',
    '島根県',
    '岡山県',
    '広島県',
    '山口県',
    '徳島県',
    '香川県',
    '愛媛県',
    '高知県',
    '福岡県',
    '佐賀県',
    '長崎県',
    '熊本県',
    '大分県',
    '宮崎県',
    '鹿児島県',
    '沖縄県'
]


# 部署リスト表示用Views
class DepartmentalListView(ListView):
    model = Departmental
    context_object_name = 'departments'
    template_name = 'office_info/departmental.html'

    def get_queryset(self):
        departments = Departmental.objects.filter(delete_flag=False).order_by('id')
        return departments


# 部署リスト削除用Views
class DepartmentalDeleteView(DeleteView):
    model = Departmental
    template_name = 'office_info/departmental.html'
    success_url = reverse_lazy('office_info:departmental_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# 部署新規登録用Views
class DepartmentalCreateView(CreateView):
    template_name = 'office_info/departmental.html'
    form_class = DepartmentalForm
    model = Departmental
    success_url = reverse_lazy('office_info:departmental_list')


# 部署更新用Views
class DepartmentalUpdateView(UpdateView):
    template_name = 'office_info/departmental.html'
    form_class = DepartmentalForm
    model = Departmental
    success_url = reverse_lazy('office_info:departmental_list')


# スキルリスト表示用Views
class SkillListView(ListView):
    model = Skill
    context_object_name = 'skills'
    template_name = 'office_info/skill.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departmental_id = self.kwargs.get('pk')
        departments = Departmental.objects.filter(id=departmental_id,
                                                  delete_flag=False).order_by('id')
        context['departmental_id'] = departmental_id
        context['departmental_name'] = departments[0].name

        return context

    def get_queryset(self):
        skills = Skill.objects.filter(departmental_id=self.kwargs.get('pk'),
                                      delete_flag=False).order_by('id')

        return skills


# スキルリスト全表示用Views
class SkillAllListView(ListView):
    model = Skill
    context_object_name = 'skills'
    template_name = 'office_info/skill.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Departmental.objects.filter(delete_flag=False).order_by('id')
        return context

    def get_queryset(self):
        skills = Skill.objects.filter(delete_flag=False).order_by('id')

        return skills


# スキルリスト削除用Views
class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'office_info/skill.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('office_info:skill_list',
                            kwargs={'pk': self.kwargs['departmental_id']})


# スキル新規登録用Views
class SKillCreateView(CreateView):
    template_name = 'office_info/skill.html'
    form_class = SkillForm
    model = Skill

    def form_valid(self, form):
        form.instance.departmental_id = self.kwargs.get('departmental_id')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:skill_list',
                            kwargs={'pk': self.kwargs['departmental_id']})


# スキル新規登録用（部署選択）Views
class SKillSelectCreateView(CreateView):
    template_name = 'office_info/skill.html'
    form_class = SkillForm
    model = Skill

    def form_valid(self, form):
        form.instance.departmental_id = form.data['departmental_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:skill_all_list')


# スキル更新用Views
class SkillUpdateView(UpdateView):
    template_name = 'office_info/skill.html'
    form_class = SkillForm
    model = Skill

    def get_success_url(self):
        return reverse_lazy('office_info:skill_list',
                            kwargs={'pk': self.kwargs['departmental_id']})


# 工程リスト表示用Views
class ProcessListView(ListView):
    model = Process
    context_object_name = 'processes'
    template_name = 'office_info/process.html'

    def get_queryset(self):
        processes = Process.objects.filter(delete_flag=False).order_by('id')
        return processes


# 工程リスト削除用Views
class ProcessDeleteView(DeleteView):
    model = Process
    template_name = 'office_info/process.html'
    success_url = reverse_lazy('office_info:process_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# 工程新規登録用Views
class ProcessCreateView(CreateView):
    template_name = 'office_info/process.html'
    form_class = ProcessForm
    model = Process
    success_url = reverse_lazy('office_info:process_list')


# 工程更新用Views
class ProcessUpdateView(UpdateView):
    template_name = 'office_info/process.html'
    form_class = ProcessForm
    model = Process
    success_url = reverse_lazy('office_info:process_list')


# データセットリスト表示用Views
class DatasetListView(ListView):
    model = Dataset
    context_object_name = 'datasets'
    template_name = 'office_info/dataset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        process_id = self.kwargs.get('pk')
        processes = Process.objects.filter(id=process_id,
                                           delete_flag=False).order_by('id')
        context['process_id'] = process_id
        context['process_name'] = processes[0].name
        return context

    def get_queryset(self):
        datasets = Dataset.objects.filter(process_id=self.kwargs.get('pk'),
                                          delete_flag=False).order_by('id')
        return datasets


# データセットリスト全表示用Views
class DatasetAllListView(ListView):
    model = Dataset
    context_object_name = 'datasets'
    template_name = 'office_info/dataset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['processes'] = Process.objects.filter(delete_flag=False).order_by('id')
        return context

    def get_queryset(self):
        datasets = Dataset.objects.filter(delete_flag=False).order_by('id')
        return datasets


# データセットリスト削除用Views
class DatasetDeleteView(DeleteView):
    model = Dataset
    template_name = 'office_info/dataset.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('office_info:dataset_list',
                            kwargs={'pk': self.kwargs['process_id']})


# データセット新規登録用Views
class DatasetCreateView(CreateView):
    template_name = 'office_info/dataset.html'
    form_class = DatasetForm
    model = Dataset

    def form_valid(self, form):
        form.instance.process_id = self.kwargs.get('process_id')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:dataset_list',
                            kwargs={'pk': self.kwargs['process_id']})


# データセット新規登録用（工程選択）Views
class DatasetSelectCreateView(CreateView):
    template_name = 'office_info/dataset.html'
    form_class = DatasetForm
    model = Dataset

    def form_valid(self, form):
        form.instance.process_id = form.data['process_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:dataset_all_list')


# データセット更新用Views
class DatasetUpdateView(UpdateView):
    template_name = 'office_info/dataset.html'
    form_class = DatasetForm
    model = Dataset

    def get_success_url(self):
        return reverse_lazy('office_info:dataset_list',
                            kwargs={'pk': self.kwargs['process_id']})


# タスクスキル表示View
def task_skill_view():
    skills = Skill.objects.filter(delete_flag=False).order_by('id')
    task_skills = TaskSkill.objects.filter(delete_flag=False).order_by('id')

    task_skill_list = []
    for task_skill in task_skills:
        task_skill_dict = {
            'task_skill_id': task_skill.id,
            'skill_name': task_skill.skill_name,
            'ratio': task_skill.ratio,
            'task_id': task_skill.task_id
        }
        task_skill_list.append(task_skill_dict)

    skill_list = []
    for skill in skills:
        skill_dict = {
            'task_skill_id': '',
            'skill_name': skill.name,
            'ratio': 0,
            'task_id': ''
        }
        skill_list.append(skill_dict)

    return task_skill_list, skill_list


# タスクリスト表示用Views
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'office_info/task.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        process_id = self.kwargs.get('process_id')
        dataset_id = self.kwargs.get('pk')
        processes = Process.objects.filter(id=process_id,
                                           delete_flag=False).order_by('id')
        datasets = Dataset.objects.filter(id=dataset_id,
                                          delete_flag=False).order_by('id')

        context['process_id'] = process_id
        context['process_name'] = processes[0].name
        context['dataset_id'] = dataset_id
        context['dataset_name'] = datasets[0].name

        task_skill_list, skill_list = task_skill_view()
        context['task_skills'] = task_skill_list
        context['skills'] = skill_list

        return context

    def get_queryset(self):
        tasks = Task.objects.filter(dataset_id=self.kwargs.get('pk'),
                                    delete_flag=False).order_by('id')
        return tasks


# タスクリスト全表示用Views
class TaskAllListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'office_info/task.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['processes'] = Process.objects.filter(delete_flag=False).order_by('id')
        context['datasets'] = Dataset.objects.filter(delete_flag=False).order_by('id')

        task_skill_list, skill_list = task_skill_view()
        context['task_skills'] = task_skill_list
        context['skills'] = skill_list

        return context

    def get_queryset(self):
        tasks = Task.objects.filter(delete_flag=False).order_by('id')
        return tasks


# タスクリスト削除用Views
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'office_info/task.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('office_info:task_list',
                            kwargs={
                                'process_id': self.kwargs['process_id'],
                                'pk': self.kwargs['dataset_id']
                            })


# タスク新規登録用Views
class TaskCreateView(CreateView):
    template_name = 'office_info/task.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        form.instance.dataset_id = self.kwargs.get('dataset_id')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:task_list',
                            kwargs={
                                'pk': self.kwargs['dataset_id'],
                                'process_id': self.kwargs['process_id']})


# タスク新規登録用（工程・データセット選択）Views
class TaskSelectCreateView(CreateView):
    template_name = 'office_info/task.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        form.instance.dataset_id = form.data['dataset_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('office_info:task_all_list')


# タスク更新用Views
class TaskUpdateView(UpdateView):
    template_name = 'office_info/task.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse_lazy('office_info:task_list',
                            kwargs={
                                'process_id': self.kwargs['process_id'],
                                'pk': self.kwargs['dataset_id']
                            })


# タスクスキル登録or更新用Views
def task_skill_create_or_update_view(request, process_id, dataset_id, pk):

    if request.method == 'POST':
        post_data = request.POST.getlist('data')
        data_list = parse.unquote(post_data[0]).split('&')

        post_id = []
        post_name = []
        post_ratio = []
        for data in data_list:
            if 'ratio=' in data:
                post_ratio.append(data.replace('ratio=', ''))
            elif 'id=' in data:
                post_id.append(data.replace('id=', ''))
            elif 'name=' in data:
                post_name.append(data.replace('name=', ''))

        for task_skill_id, skill_name, ratio in zip(post_id, post_name, post_ratio):
            if not task_skill_id:
                task_skill_id = None
            TaskSkill.objects.update_or_create(
                id=task_skill_id,
                defaults={'skill_name': skill_name, 'ratio': ratio, 'task_id': pk})

        return redirect('office_info:task_list', process_id=process_id, pk=dataset_id)


# 社員リスト表示用Views
class StaffListView(ListView):
    model = Staff
    context_object_name = 'staffs'
    template_name = 'office_info/staff.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['length'] = len(context['staffs'])

        return context

    def get_queryset(self):
        staffs = Staff.objects.filter(delete_flag=False).order_by('id')
        return staffs


# 社員フォーム表示用Views
class StaffDetailView(ListView):
    model = Staff
    context_object_name = 'staffs'
    template_name = 'office_info/staff_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Departmental.objects.filter(delete_flag=False).order_by('id')
        context['skills'] = Skill.objects.filter(delete_flag=False).order_by('id')
        context['position_name'] = POSITION_NAME
        context['profession'] = PROFESSION
        context['nationality'] = NATIONALITY
        context['native_place'] = NATIVE_PLACE

        return context

    def get_queryset(self):
        staffs = Staff.objects.filter(delete_flag=False).order_by('id')
        return staffs

