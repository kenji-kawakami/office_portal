from django.urls import path

from . import views


app_name = 'office_info'
urlpatterns = [


    # 部署
    path('departmental/',
         views.DepartmentalListView.as_view(), name='departmental_list'),
    path('departmental_delete/<int:pk>/',
         views.DepartmentalDeleteView.as_view(), name='departmental_delete'),
    path('departmental_create/',
         views.DepartmentalCreateView.as_view(), name='departmental_create'),
    path('departmental_update/<int:pk>/',
         views.DepartmentalUpdateView.as_view(), name='departmental_update'),


    # スキル
    path('skill_list/<int:pk>/',
         views.SkillListView.as_view(), name='skill_list'),
    path('skill_all_list/',
         views.SkillAllListView.as_view(), name='skill_all_list'),
    path('skill_delete/<int:departmental_id>/<int:pk>/',
         views.SkillDeleteView.as_view(), name='skill_delete'),
    path('skill_create/<int:departmental_id>/',
         views.SKillCreateView.as_view(), name='skill_create'),
    path('skill_select_create/',
         views.SKillSelectCreateView.as_view(), name='skill_select_create'),
    path('skill_update/<int:departmental_id>/<int:pk>/',
         views.SkillUpdateView.as_view(), name='skill_update'),


    # 工程
    path('process/',
         views.ProcessListView.as_view(), name='process_list'),
    path('process_delete/<int:pk>/',
         views.ProcessDeleteView.as_view(), name='process_delete'),
    path('process_create/',
         views.ProcessCreateView.as_view(), name='process_create'),
    path('process_update/<int:pk>/',
         views.ProcessUpdateView.as_view(), name='process_update'),


    # データセット
    path('dataset_list/<int:pk>/',
         views.DatasetListView.as_view(), name='dataset_list'),
    path('dataset_all_list/',
         views.DatasetAllListView.as_view(), name='dataset_all_list'),
    path('dataset_delete/<int:process_id>/<int:pk>/',
         views.DatasetDeleteView.as_view(), name='dataset_delete'),
    path('dataset_create/<int:process_id>/',
         views.DatasetCreateView.as_view(), name='dataset_create'),
    path('dataset_select_create/',
         views.DatasetSelectCreateView.as_view(), name='dataset_select_create'),
    path('dataset_update/<int:process_id>/<int:pk>/',
         views.DatasetUpdateView.as_view(), name='dataset_update'),


    # タスク
    path('task_list/<int:process_id>/<int:pk>/',
         views.TaskListView.as_view(), name='task_list'),
    path('task_all_list/',
         views.TaskAllListView.as_view(), name='task_all_list'),
    path('task_delete/<int:process_id>/<int:dataset_id>/<int:pk>/',
         views.TaskDeleteView.as_view(), name='task_delete'),
    path('task_create/<int:process_id>/<int:dataset_id>/',
         views.TaskCreateView.as_view(), name='task_create'),
    path('task_select_create/',
         views.TaskSelectCreateView.as_view(), name='task_select_create'),
    path('task_update/<int:process_id>/<int:dataset_id>/<int:pk>/',
         views.TaskUpdateView.as_view(), name='task_update'),


    # タスクスキル
    path('task_skill_create_update/<int:process_id>/<int:dataset_id>/<int:pk>/',
         views.task_skill_create_or_update_view, name='task_skill_create_update'),


    # 社員
    path('staff_list/',
         views.StaffListView.as_view(), name='staff_list'),
    path('staff_detail/',
         views.StaffDetailView.as_view(), name='staff_detail'),

]
