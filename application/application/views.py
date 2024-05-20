from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.cache import cache


def home(request):
    return render(request, 'index.html')

def add_day(request):
    return render(request, 'add_day.html')

def add_day_submit(request):
    if request.method == 'POST':
        cache.clear()

        context = dict()
        names = ['sleep', 'health', 'study']
        months = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                  'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']

        day = request.POST.get('day')
        month = request.POST.get('month')

        bool = True

        for name in names:
            start_hour = request.POST.get(name + '_start_hour')
            start_minute = request.POST.get(name + '_start_minute')
            end_hour = request.POST.get(name + '_end_hour')
            end_minute = request.POST.get(name + '_end_minute')
            bool = bool and check_dates(start_hour, start_minute, end_hour, end_minute)

        if month not in months:
            context['success'] = False

        elif (int(day) <= 0) or (int(day) > 31) or (int(day) % 1 != 0):
            context['success'] = False

        elif bool == False:
            context['success'] = False

        else:
            context['success'] = True
            context['day'] = day
            context['month'] = month

        if context['success']:
            for name in names:
                start_hour = request.POST.get(name + '_start_hour')
                start_minute = request.POST.get(name + '_start_minute')
                end_hour = request.POST.get(name + '_end_hour')
                end_minute = request.POST.get(name + '_end_minute')

                activity = Activity(name, day, month, start_hour, start_minute, end_hour, end_minute)
                activity.write_in_db()

        return render(request, 'add_day_respond.html', context)


def info_day(request):
    return render(request, 'info_day.html')

def info_day_submit(request):
    if request.method == 'POST':
        cache.clear()

        context = dict()
        names = ['sleep', 'health', 'study']
        months = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                  'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']

        day = request.POST.get('day')
        month = request.POST.get('month')


        if month not in months:
            context['success'] = False

        elif (int(day) <= 0) or (int(day) > 31) or (int(day) % 1 != 0):
            context['success'] = False

        else:
            context['success'] = True
            context['day'] = day
            context['month'] = month

        if context['success']:
            conn = sqlite3.connect('regime.db')


            for name in names:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM ' + name + ' WHERE day=' + str(day) + ' AND month="' + str(month)+'"')
                result = cursor.fetchone()
                context[name] = str(result[2]) + ':' + str(result[3]) + ' - ' + str(result[4]) + ':' + str(result[5])

            conn.commit()
            conn.close()

        return render(request, 'info_day_respond.html', context)


def info_activity(request):
    return render(request, 'info_activity.html')

def info_activity_submit(request):
    if request.method == 'POST':
        cache.clear()

        context = dict()
        names = ['sleep', 'health', 'study']
        months = ['Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
                  'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь']

        activity = request.POST.get('activity')
        month = request.POST.get('month')


        if month not in months:
            context['success'] = False

        elif activity not in names:
            context['success'] = False

        else:
            context['success'] = True
            context['activity'] = activity
            context['month'] = month


        if context['success']:

            days = []

            for i in range(1, 32):
                conn = sqlite3.connect('regime.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM ' + activity + ' WHERE day=' + str(i) + ' AND month="' + str(month)+'"')
                result = cursor.fetchone()
                if result != None:
                    days.append(str(result[2]) + ':' + str(result[3]) + ' - ' + str(result[4]) + ':' + str(result[5]))

                conn.commit()
                conn.close()

            context['days'] = days

        return render(request, 'info_activity_respond.html', context)


def check_dates(start_hour, start_minute, end_hour, end_minute):
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)

    if start_hour*60 + start_minute > end_hour*60 + end_minute:
        return False
    elif (start_hour < 0) or (start_hour > 23):
        return False
    elif (start_minute < 0) or (start_minute > 59):
        return False
    elif (end_hour < 0) or (end_hour > 23):
        return False
    elif (end_minute < 0) or (end_minute > 59):
        return False

    else:
        return True





