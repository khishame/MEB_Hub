from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name="admin_home"),
    path('events_menu', views.events_menu, name="events_menu"),
    # URL patterns for the bus
    path('bus_menu', views.bus_menu, name="bus_menu"),
    path('add_all_campus_view', views.add_all_campuses_view, name="add_all_campus_view"),
    path('add_bus_schedule/<int:code>/', views.add_bus_schedule, name="add_bus_schedule"),
    path('bus_stats', views.bus_schedule_stats, name='bus_schedule_stats'),
    # URL patterns for admin home
    path("view_all_actions", views.view_all_actions, name="view_all_actions"),
    # URL patterns for bus
    path("add_bus", views.add_bus, name="add_bus"),
    path("remove_bus", views.remove_bus, name="remove_bus"),
    # Dashboard pages
    path("user_management", views.user_management, name="user_management"),
    path("analytics", views.analytics, name="analytics"),
    path('student-report/', views.student_report, name='student_report'),
    path('student-report/pdf/', views.student_report_pdf, name='student_report_pdf'),
    path('student-report/docx/', views.student_report_docx, name='student_report_docx'),
    path('student-report/csv/', views.student_report_csv, name='student_report_csv'),
    path('full-report/', views.full_report, name='full_report'),
    path('full-report/pdf/', views.full_report_pdf, name='full_report_pdf'),
    path('full-report/docx/', views.full_report_docx, name='full_report_docx'),
    path('full-report/csv/', views.full_report_csv, name='full_report_csv'),
]
