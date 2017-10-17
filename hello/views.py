from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import datetime
from firebase import firebase
from collections import Counter
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from .models import Greeting

#render data from google analytics
analytics_data = pd.ExcelFile('https://docs.google.com/spreadsheets/d/e/2PACX-1vTHlxEh7V0BItjq3sCKcDgnlnNfRSRLwCUMwSD_RZJeHLwkaT60qzm8SOpI0Ha__FER56PbttXRYkOu/pub?output=xlsx')
app_data = pd.ExcelFile('https://docs.google.com/spreadsheets/d/e/2PACX-1vTf5ODR80vFXY6rfcae4235qkk4EUPN-RiHFiX66Hb5w2mJPh09EoHrHM8Co9st4BearEtGw79q4vHH/pub?output=xlsx')

#FIREBASE DATA

posts = firebase.FirebaseApplication('https://dysco-2509c.firebaseio.com/posts', None)
app_result = posts.get('/posts', None)

users = firebase.FirebaseApplication('https://dysco-2509c.firebaseio.com/users', None)
users = users.get('/users', None)

firebase = firebase.FirebaseApplication('https://dysco-2509c.firebaseio.com/users', None)
result = firebase.get('/users', None)


# Create your views here.
@login_required(login_url='login')
def index(request):
    # return HttpResponse('Hello from Python!')
    date_time = analytics_data.parse('Test Dysco')
    date_time = date_time.loc[0, 'Unnamed: 1']
    return render(request, 'index.html', {'last_update' : date_time})

@login_required(login_url='login')
def test(request):

    apple_data = [12, 19, 3, 17, 6, 3, 7]
    orange_data = [2, 29, 5, 5, 2, 3, 10]
    labels = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
    my_colors = ['bg-primary', 'bg-secondary', 'bg-success']


    return render(request, 'test.html', locals())

@login_required(login_url='login')
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def base(request):

    date_time = analytics_data.parse('Test Dysco')
    date_time = date_time.loc[0, 'Unnamed: 1']
    today = datetime.datetime.now()
    return render(request, 'index.html', {'last_update': date_time, 'today' : today})

@login_required(login_url='login')
def blog(request):

    return render(request, 'blog.html')

@login_required(login_url='login')
def app(request):

    return render(request, 'app.html')

#BLOG DATA

@login_required(login_url='login')
def bloggender(request):
    gender = analytics_data

    # 7 DAYS DATA


    gender = analytics_data.parse('Gender  last 7 days')

    gender = gender.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]

    total_users = gender.loc[10, 'Unnamed: 1']
    new_users = gender.loc[10, 'Unnamed: 2']
    total_sessions = gender.loc[10, 'Unnamed: 3']
    avg_session_duration = gender.loc[10, 'Unnamed: 4']
    page_views = gender.loc[10, 'Unnamed: 5']



    # FEMALE_DATA

    f_total_users = gender.loc[14, 'Unnamed: 1']
    f_new_users = gender.loc[14, 'Unnamed: 2']
    f_total_sessions = gender.loc[14, 'Unnamed: 3']
    f_avg_session_duration = gender.loc[14, 'Unnamed: 4']
    f_page_views = gender.loc[14, 'Unnamed: 5']

    # MALE

    m_total_users = gender.loc[15, 'Unnamed: 1']
    m_new_users = gender.loc[15, 'Unnamed: 2']
    m_total_sessions = gender.loc[15, 'Unnamed: 3']
    m_avg_session_duration = gender.loc[15, 'Unnamed: 4']
    m_page_views = gender.loc[15, 'Unnamed: 5']

    # dict

    ref7 = {'total_users': total_users, 'f_total_users': f_total_users, 'm_total_users': m_total_users,
             'new_users': new_users,
             'f_new_users': f_new_users, 'm_new_users': m_new_users, 'total_sessions': total_sessions,
             'f_total_sessions': f_total_sessions, 'm_total_sessions': m_total_sessions,
             'avg_session_duration': int(avg_session_duration), 'f_avg_session_duration': int(f_avg_session_duration),
             'm_avg_session_duration': int(m_avg_session_duration), 'page_views': float(round(page_views,2)), 'f_page_views': float(round(f_page_views,2)),
             'm_page_views': float(round(m_page_views,2))}


    # 14 DAYS DATA

    gender_14 = analytics_data

    gender_14 = analytics_data.parse('Gender  last 14 days')

    gender_14 = gender_14.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]

    total_users = gender_14.loc[10, 'Unnamed: 1']
    new_users = gender_14.loc[10, 'Unnamed: 2']
    total_sessions = gender_14.loc[10, 'Unnamed: 3']
    avg_session_duration = gender_14.loc[10, 'Unnamed: 4']
    page_views = gender_14.loc[10, 'Unnamed: 5']



    # FEMALE_DATA

    f_total_users = gender_14.loc[14, 'Unnamed: 1']
    f_new_users = gender_14.loc[14, 'Unnamed: 2']
    f_total_sessions = gender_14.loc[14, 'Unnamed: 3']
    f_avg_session_duration = gender_14.loc[14, 'Unnamed: 4']
    f_page_views = gender_14.loc[14, 'Unnamed: 5']

    # MALE

    m_total_users = gender_14.loc[15, 'Unnamed: 1']
    m_new_users = gender_14.loc[15, 'Unnamed: 2']
    m_total_sessions = gender_14.loc[15, 'Unnamed: 3']
    m_avg_session_duration = gender_14.loc[15, 'Unnamed: 4']
    m_page_views = gender_14.loc[15, 'Unnamed: 5']

    # dict

    ref14 = {'total_users': total_users, 'f_total_users': f_total_users, 'm_total_users': m_total_users,
             'new_users': new_users,
             'f_new_users': f_new_users, 'm_new_users': m_new_users, 'total_sessions': total_sessions,
             'f_total_sessions': f_total_sessions, 'm_total_sessions': m_total_sessions,
             'avg_session_duration': int(avg_session_duration), 'f_avg_session_duration': int(f_avg_session_duration),
             'm_avg_session_duration': int(m_avg_session_duration), 'page_views': float(round(page_views,2)), 'f_page_views': float(round(f_page_views,2)),
             'm_page_views': float(round(m_page_views,2))}



    #THIS MONTH

    gender_30 = analytics_data

    gender_30 = analytics_data.parse('Gender  this month')

    gender_30 = gender_30.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]

    total_users = gender_30.loc[10, 'Unnamed: 1']
    new_users = gender_30.loc[10, 'Unnamed: 2']
    total_sessions = gender_30.loc[10, 'Unnamed: 3']
    avg_session_duration = gender_30.loc[10, 'Unnamed: 4']
    page_views = gender_30.loc[10, 'Unnamed: 5']



    # FEMALE_DATA

    f_total_users = gender_30.loc[14, 'Unnamed: 1']
    f_new_users = gender_30.loc[14, 'Unnamed: 2']
    f_total_sessions = gender_30.loc[14, 'Unnamed: 3']
    f_avg_session_duration = gender_30.loc[14, 'Unnamed: 4']
    f_page_views = gender_30.loc[14, 'Unnamed: 5']

    # MALE

    m_total_users = gender_30.loc[15, 'Unnamed: 1']
    m_new_users = gender_30.loc[15, 'Unnamed: 2']
    m_total_sessions = gender_30.loc[15, 'Unnamed: 3']
    m_avg_session_duration = gender_30.loc[15, 'Unnamed: 4']
    m_page_views = gender_30.loc[15, 'Unnamed: 5']

    # dict

    ref30 = {'total_users': total_users, 'f_total_users': f_total_users, 'm_total_users': m_total_users,
             'new_users': new_users,
             'f_new_users': f_new_users, 'm_new_users': m_new_users, 'total_sessions': total_sessions,
             'f_total_sessions': f_total_sessions, 'm_total_sessions': m_total_sessions,
             'avg_session_duration': int(avg_session_duration), 'f_avg_session_duration': int(f_avg_session_duration),
             'm_avg_session_duration': int(m_avg_session_duration), 'page_views': float(round(page_views,2)), 'f_page_views': float(round(f_page_views,2)),
             'm_page_views': float(round(m_page_views,2))}



#LAST MONTH

    gender_lm = analytics_data

    gender_lm = analytics_data.parse('Gender  last month')

    gender_lm = gender_lm.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]

    total_users = gender_lm.loc[10, 'Unnamed: 1']
    new_users = gender_lm.loc[10, 'Unnamed: 2']
    total_sessions = gender_lm.loc[10, 'Unnamed: 3']
    avg_session_duration = gender_lm.loc[10, 'Unnamed: 4']
    page_views = gender_lm.loc[10, 'Unnamed: 5']



    # FEMALE_DATA

    f_total_users = gender_lm.loc[14, 'Unnamed: 1']
    f_new_users = gender_lm.loc[14, 'Unnamed: 2']
    f_total_sessions = gender_lm.loc[14, 'Unnamed: 3']
    f_avg_session_duration = gender_lm.loc[14, 'Unnamed: 4']
    f_page_views = gender_lm.loc[14, 'Unnamed: 5']

    # MALE

    m_total_users = gender_lm.loc[15, 'Unnamed: 1']
    m_new_users = gender_lm.loc[15, 'Unnamed: 2']
    m_total_sessions = gender_lm.loc[15, 'Unnamed: 3']
    m_avg_session_duration = gender_lm.loc[15, 'Unnamed: 4']
    m_page_views = gender_lm.loc[15, 'Unnamed: 5']

    # dict

    reflm = {'total_users': total_users, 'f_total_users': f_total_users, 'm_total_users': m_total_users,
             'new_users': new_users,
             'f_new_users': f_new_users, 'm_new_users': m_new_users, 'total_sessions': total_sessions,
             'f_total_sessions': f_total_sessions, 'm_total_sessions': m_total_sessions,
             'avg_session_duration': int(avg_session_duration), 'f_avg_session_duration': int(f_avg_session_duration),
             'm_avg_session_duration': int(m_avg_session_duration), 'page_views': float(round(page_views,2)), 'f_page_views': float(round(f_page_views,2)),
             'm_page_views': float(round(m_page_views,2))}



#LIFETIME DATA

    gender_lt = analytics_data

    gender_lt = analytics_data.parse('Gender  lifetime')

    gender_lt = gender_lt.loc[:, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]

    total_users = gender_lt.loc[10, 'Unnamed: 1']
    new_users = gender_lt.loc[10, 'Unnamed: 2']
    total_sessions = gender_lt.loc[10, 'Unnamed: 3']
    avg_session_duration = gender_lt.loc[10, 'Unnamed: 4']
    page_views = gender_lt.loc[10, 'Unnamed: 5']



    # FEMALE_DATA

    f_total_users = gender_lt.loc[14, 'Unnamed: 1']
    f_new_users = gender_lt.loc[14, 'Unnamed: 2']
    f_total_sessions = gender_lt.loc[14, 'Unnamed: 3']
    f_avg_session_duration = gender_lt.loc[14, 'Unnamed: 4']
    f_page_views = gender_lt.loc[14, 'Unnamed: 5']

    # MALE

    m_total_users = gender_lt.loc[15, 'Unnamed: 1']
    m_new_users = gender_lt.loc[15, 'Unnamed: 2']
    m_total_sessions = gender_lt.loc[15, 'Unnamed: 3']
    m_avg_session_duration = gender_lt.loc[15, 'Unnamed: 4']
    m_page_views = gender_lt.loc[15, 'Unnamed: 5']

    # dict

    reflt = {'total_users': total_users, 'f_total_users': f_total_users, 'm_total_users': m_total_users,
             'new_users': new_users,
             'f_new_users': f_new_users, 'm_new_users': m_new_users, 'total_sessions': total_sessions,
             'f_total_sessions': f_total_sessions, 'm_total_sessions': m_total_sessions,
             'avg_session_duration': int(avg_session_duration), 'f_avg_session_duration': int(f_avg_session_duration),
             'm_avg_session_duration': int(m_avg_session_duration), 'page_views': float(round(page_views,2)), 'f_page_views': float(round(f_page_views,2)),
             'm_page_views': float(round(m_page_views,2))}





    ref = {'ref7': ref7, 'ref14' : ref14, 'reflm' : reflm, 'ref30' : ref30, 'reflt' : reflt}


    '''
    ANALYTICS
    '''

    #weekly report

    male_total7 = float(100* ref7['m_total_sessions'] / ref7['total_sessions'])
    female_total7 = float(100 * ref7['f_total_sessions'] / ref7['total_sessions'])

    male_total14 = float(100 * ref14['m_total_sessions'] / ref14['total_sessions'])
    female_total14 = float(100 * ref14['f_total_sessions'] / ref14['total_sessions'])

    #monthly report

    male_totallm = float(100* reflm['m_total_sessions'] / reflm['total_sessions'])
    female_totallm = float(100 * reflm['f_total_sessions'] / reflm['total_sessions'])

    male_total30 = float(100 * ref30['m_total_sessions'] / ref30['total_sessions'])
    female_total30 = float(100 * ref30['f_total_sessions'] / ref30['total_sessions'])

    #lifetime worth data

    male_totallt = float(100 * reflt['m_total_sessions'] / reflt['total_sessions'])
    female_totallt = float(100 * reflt['f_total_sessions'] / reflt['total_sessions'])



    return render(request,'blogFiles/gender.html', locals())


##AGE GROUPS
##IGNORE THE NAME 'GENDER', ITS JUST A REPLICATION OF VARIABLES FROM DIFFERENT SHEET

@login_required(login_url='login')
def blogagegroup(request):

    dict7 = analytics_data.parse('Age group  last 7 days')
    dict7 = dict7.loc[8:,
            ['Age group : last 7 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']]
    dict7 = dict7.dropna()


    while True:

        try:
            dict7 = {'age':
                         {'18':
                              {'users': dict7.loc[14, 'Unnamed: 1'], 'newusers': dict7.loc[14, 'Unnamed: 2'],
                               'sessions': dict7.loc[14, 'Unnamed: 3'], 'avgsd': int(dict7.loc[14, 'Unnamed: 4']),
                               'pgvps': float(round(dict7.loc[14, 'Unnamed: 5'], 2))},
                          '25': {'users': dict7.loc[15, 'Unnamed: 1'], 'newusers': dict7.loc[15, 'Unnamed: 2'],
                                 'sessions': dict7.loc[15, 'Unnamed: 3'], 'avgsd': int(dict7.loc[15, 'Unnamed: 4']),
                                 'pgvps': float(round(dict7.loc[15, 'Unnamed: 5'], 2))},
                          '35': {'users': dict7.loc[16, 'Unnamed: 1'], 'newusers': dict7.loc[16, 'Unnamed: 2'],
                                 'sessions': dict7.loc[16, 'Unnamed: 3'], 'avgsd': int(dict7.loc[16, 'Unnamed: 4']),
                                 'pgvps': float(round(dict7.loc[16, 'Unnamed: 5'], 2))}, }}
            break


        except:
            dict7 = {'age':
                         {'18':
                              {'users': dict7.loc[14, 'Unnamed: 1'], 'newusers': dict7.loc[14, 'Unnamed: 2'],
                               'sessions': dict7.loc[14, 'Unnamed: 3'], 'avgsd': int(dict7.loc[14, 'Unnamed: 4']),
                               'pgvps': float(round(dict7.loc[14, 'Unnamed: 5'], 2))},
                          '25': {'users': dict7.loc[15, 'Unnamed: 1'], 'newusers': dict7.loc[15, 'Unnamed: 2'],
                                 'sessions': dict7.loc[15, 'Unnamed: 3'], 'avgsd': int(dict7.loc[15, 'Unnamed: 4']),
                                 'pgvps': float(round(dict7.loc[15, 'Unnamed: 5'], 2))},
                          '35': {'users': 0, 'newusers': 0,
                                 'sessions': 0, 'avgsd': 0,
                                 'pgvps': 0}, }}
            break

    dict14 = analytics_data.parse('Age group  last 14 days')
    dict14 = dict14.loc[8:,
             ['Age group : last 14 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', ]]
    dict14 = dict14.dropna()

    dict14 = {'age':
                  {'18':
                       {'users': dict14.loc[14, 'Unnamed: 1'], 'newusers': dict14.loc[14, 'Unnamed: 2'],
                        'sessions': dict14.loc[14, 'Unnamed: 3'], 'avgsd': int(dict14.loc[14, 'Unnamed: 4']),
                        'pgvps': float(round(dict14.loc[14, 'Unnamed: 5'], 2))},
                   '25': {'users': dict14.loc[15, 'Unnamed: 1'], 'newusers': dict14.loc[15, 'Unnamed: 2'],
                          'sessions': dict14.loc[15, 'Unnamed: 3'], 'avgsd': int(dict14.loc[15, 'Unnamed: 4']),
                          'pgvps': float(round(dict14.loc[15, 'Unnamed: 5'], 2))},
                   '35': {'users': dict14.loc[16, 'Unnamed: 1'], 'newusers': dict14.loc[16, 'Unnamed: 2'],
                          'sessions': dict14.loc[16, 'Unnamed: 3'], 'avgsd': int(dict14.loc[16, 'Unnamed: 4']),
                          'pgvps': float(round(dict14.loc[16, 'Unnamed: 5'], 2))},

                   }}

    # MONTHLY DATA

    dictlm = analytics_data.parse('Age group  last month')
    dictlm = dictlm.loc[8:,
             ['Age group : last month', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', ]]

    dictlm = {'age':
                  {'18':
                       {'users': dictlm.loc[14, 'Unnamed: 1'], 'newusers': dictlm.loc[14, 'Unnamed: 2'],
                        'sessions': dictlm.loc[14, 'Unnamed: 3'], 'avgsd': int(dictlm.loc[14, 'Unnamed: 4']),
                        'pgvps': float(round(dictlm.loc[14, 'Unnamed: 5'], 2))},
                   '25': {'users': dictlm.loc[15, 'Unnamed: 1'], 'newusers': dictlm.loc[15, 'Unnamed: 2'],
                          'sessions': dictlm.loc[15, 'Unnamed: 3'], 'avgsd': int(dictlm.loc[15, 'Unnamed: 4']),
                          'pgvps': float(round(dictlm.loc[15, 'Unnamed: 5'], 2))},
                   '35': {'users': dictlm.loc[16, 'Unnamed: 1'], 'newusers': dictlm.loc[16, 'Unnamed: 2'],
                          'sessions': dictlm.loc[16, 'Unnamed: 3'], 'avgsd': int(dictlm.loc[16, 'Unnamed: 4']),
                          'pgvps': float(round(dictlm.loc[16, 'Unnamed: 5'], 2))}, }}

    dicttm = analytics_data.parse('Age group  this month')
    # dicttm = dicttm.dropna()

    while True:

        try:
            dicttm = {'age':
                          {'18':
                               {'users': dicttm.loc[14, 'Unnamed: 1'], 'newusers': dicttm.loc[14, 'Unnamed: 2'],
                                'sessions': dicttm.loc[14, 'Unnamed: 3'], 'avgsd': int(dicttm.loc[14, 'Unnamed: 4']),
                                'pgvps': float(round(dicttm.loc[14, 'Unnamed: 5'], 2))},
                           '25': {'users': dicttm.loc[15, 'Unnamed: 1'], 'newusers': dicttm.loc[15, 'Unnamed: 2'],
                                  'sessions': dicttm.loc[15, 'Unnamed: 3'], 'avgsd': int(dicttm.loc[15, 'Unnamed: 4']),
                                  'pgvps': float(round(dicttm.loc[15, 'Unnamed: 5'], 2))},
                           '35': {'users': dicttm.loc[16, 'Unnamed: 1'], 'newusers': dicttm.loc[16, 'Unnamed: 2'],
                                  'sessions': dicttm.loc[16, 'Unnamed: 3'], 'avgsd': int(dicttm.loc[16, 'Unnamed: 4']),
                                  'pgvps': float(round(dicttm.loc[16, 'Unnamed: 5'], 2))}, }}
            break


        except:
            dicttm = {'age':
                          {'18':
                               {'users': dicttm.loc[14, 'Unnamed: 1'], 'newusers': dicttm.loc[14, 'Unnamed: 2'],
                                'sessions': dicttm.loc[14, 'Unnamed: 3'], 'avgsd': int(dicttm.loc[14, 'Unnamed: 4']),
                                'pgvps': float(round(dicttm.loc[14, 'Unnamed: 5'], 2))},
                           '25': {'users': dicttm.loc[15, 'Unnamed: 1'], 'newusers': dicttm.loc[15, 'Unnamed: 2'],
                                  'sessions': dicttm.loc[15, 'Unnamed: 3'], 'avgsd': int(dicttm.loc[15, 'Unnamed: 4']),
                                  'pgvps': float(round(dicttm.loc[15, 'Unnamed: 5'], 2))},
                           '35': {'users': 0, 'newusers': 0,
                                  'sessions': 0, 'avgsd': 0,
                                  'pgvps': 0}, }}
            break
    # LIFETIME DATA

    dictlt = analytics_data.parse('Age group  lifetime')
    dictlt = dictlt.loc[8:,
             ['Age group : lifetime', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', ]]
    dictlt = dictlt.dropna()

    dictlt = {'age':
                  {'18':
                       {'users': dictlt.loc[14, 'Unnamed: 1'], 'newusers': dictlt.loc[14, 'Unnamed: 2'],
                        'sessions': dictlt.loc[14, 'Unnamed: 3'], 'avgsd': int(dictlt.loc[14, 'Unnamed: 4']),
                        'pgvps': float(round(dictlt.loc[14, 'Unnamed: 5'], 2))},
                   '25': {'users': dictlt.loc[15, 'Unnamed: 1'], 'newusers': dictlt.loc[15, 'Unnamed: 2'],
                          'sessions': dictlt.loc[15, 'Unnamed: 3'], 'avgsd': int(dictlt.loc[15, 'Unnamed: 4']),
                          'pgvps': float(round(dictlt.loc[15, 'Unnamed: 5'], 2))},
                   '35': {'users': dictlt.loc[16, 'Unnamed: 1'], 'newusers': dictlt.loc[16, 'Unnamed: 2'],
                          'sessions': dictlt.loc[16, 'Unnamed: 3'], 'avgsd': int(dictlt.loc[16, 'Unnamed: 4']),
                          'pgvps': float(round(dictlt.loc[16, 'Unnamed: 5'], 2))},

                   }}

    return render(request, 'blogFiles/age_group.html', locals())


#BLOG LOCATION


@login_required(login_url='login')
def bloglocation(request):
    dict7 = analytics_data.parse('Location last 7 days')

    dict7 = dict7.loc[14:, ['Location last 7 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]

    dict7 = dict7.dropna().head(10)

    '''
    City Users NewUsers AvgDuration
    mum  150    59       93
    del  569    452      76
    '''

    dict7 = {'1': {'name': dict7.loc[14, 'Location last 7 days'], 'users': dict7.loc[14, 'Unnamed: 1'],
                   'newusers': dict7.loc[14, 'Unnamed: 2'], 'sessions': dict7.loc[14, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[14, 'Unnamed: 4'])},
             '2': {'name': dict7.loc[15, 'Location last 7 days'], 'users': dict7.loc[15, 'Unnamed: 1'],
                   'newusers': dict7.loc[15, 'Unnamed: 2'], 'sessions': dict7.loc[15, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[15, 'Unnamed: 4'])},
             '3': {'name': dict7.loc[16, 'Location last 7 days'], 'users': dict7.loc[16, 'Unnamed: 1'],
                   'newusers': dict7.loc[16, 'Unnamed: 2'], 'sessions': dict7.loc[16, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[16, 'Unnamed: 4'])},
             '4': {'name': dict7.loc[17, 'Location last 7 days'], 'users': dict7.loc[17, 'Unnamed: 1'],
                   'newusers': dict7.loc[17, 'Unnamed: 2'], 'sessions': dict7.loc[17, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[17, 'Unnamed: 4'])},
             '5': {'name': dict7.loc[18, 'Location last 7 days'], 'users': dict7.loc[18, 'Unnamed: 1'],
                   'newusers': dict7.loc[18, 'Unnamed: 2'], 'sessions': dict7.loc[18, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[18, 'Unnamed: 4'])}}

    dict14 = analytics_data.parse('Location last 14 days')
    dict14 = dict14.loc[14:, ['Location last 14 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dict14 = dict14.dropna().head(10)

    dict14 = {'1': {'name': dict14.loc[14, 'Location last 14 days'], 'users': dict14.loc[14, 'Unnamed: 1'],
                    'newusers': dict14.loc[14, 'Unnamed: 2'], 'sessions': dict14.loc[14, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[14, 'Unnamed: 4'])},
              '2': {'name': dict14.loc[15, 'Location last 14 days'], 'users': dict14.loc[15, 'Unnamed: 1'],
                    'newusers': dict14.loc[15, 'Unnamed: 2'], 'sessions': dict14.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[15, 'Unnamed: 4'])},
              '3': {'name': dict14.loc[16, 'Location last 14 days'], 'users': dict14.loc[16, 'Unnamed: 1'],
                    'newusers': dict14.loc[16, 'Unnamed: 2'], 'sessions': dict14.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[16, 'Unnamed: 4'])},
              '4': {'name': dict14.loc[17, 'Location last 14 days'], 'users': dict14.loc[17, 'Unnamed: 1'],
                    'newusers': dict14.loc[17, 'Unnamed: 2'], 'sessions': dict14.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[17, 'Unnamed: 4'])},
              '5': {'name': dict14.loc[18, 'Location last 14 days'], 'users': dict14.loc[18, 'Unnamed: 1'],
                    'newusers': dict14.loc[18, 'Unnamed: 2'], 'sessions': dict14.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[18, 'Unnamed: 4'])}}

    dictlm = analytics_data.parse('Location last month')
    dictlm = dictlm.loc[14:, ['Location last month', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dictlm = dictlm.dropna().head(10)

    dictlm = {'1': {'name': dictlm.loc[14, 'Location last month'], 'users': dictlm.loc[14, 'Unnamed: 1'],
                    'newusers': dictlm.loc[14, 'Unnamed: 2'], 'sessions': dictlm.loc[14, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[14, 'Unnamed: 4'])},
              '2': {'name': dictlm.loc[15, 'Location last month'], 'users': dictlm.loc[15, 'Unnamed: 1'],
                    'newusers': dictlm.loc[15, 'Unnamed: 2'], 'sessions': dictlm.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[15, 'Unnamed: 4'])},
              '3': {'name': dictlm.loc[16, 'Location last month'], 'users': dictlm.loc[16, 'Unnamed: 1'],
                    'newusers': dictlm.loc[16, 'Unnamed: 2'], 'sessions': dictlm.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[16, 'Unnamed: 4'])},
              '4': {'name': dictlm.loc[17, 'Location last month'], 'users': dictlm.loc[17, 'Unnamed: 1'],
                    'newusers': dictlm.loc[17, 'Unnamed: 2'], 'sessions': dictlm.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[17, 'Unnamed: 4'])},
              '5': {'name': dictlm.loc[18, 'Location last month'], 'users': dictlm.loc[18, 'Unnamed: 1'],
                    'newusers': dictlm.loc[18, 'Unnamed: 2'], 'sessions': dictlm.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[18, 'Unnamed: 4'])}}

    dicttm = analytics_data.parse('Location this month')
    dicttm = dicttm.loc[14:, ['Location this month', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dicttm = dicttm.dropna().head(10)

    dicttm = {'1': {'name': dicttm.loc[14, 'Location this month'], 'users': dicttm.loc[14, 'Unnamed: 1'],
                    'newusers': dicttm.loc[14, 'Unnamed: 2'], 'sessions': dicttm.loc[14, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[14, 'Unnamed: 4'])},
              '2': {'name': dicttm.loc[15, 'Location this month'], 'users': dicttm.loc[15, 'Unnamed: 1'],
                    'newusers': dicttm.loc[15, 'Unnamed: 2'], 'sessions': dicttm.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[15, 'Unnamed: 4'])},
              '3': {'name': dicttm.loc[16, 'Location this month'], 'users': dicttm.loc[16, 'Unnamed: 1'],
                    'newusers': dicttm.loc[16, 'Unnamed: 2'], 'sessions': dicttm.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[16, 'Unnamed: 4'])},
              '4': {'name': dicttm.loc[17, 'Location this month'], 'users': dicttm.loc[17, 'Unnamed: 1'],
                    'newusers': dicttm.loc[17, 'Unnamed: 2'], 'sessions': dicttm.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[17, 'Unnamed: 4'])},
              '5': {'name': dicttm.loc[18, 'Location this month'], 'users': dicttm.loc[18, 'Unnamed: 1'],
                    'newusers': dicttm.loc[18, 'Unnamed: 2'], 'sessions': dicttm.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[18, 'Unnamed: 4'])}}

    dictlt = analytics_data.parse('Location lifetime')
    dictlt = dictlt.loc[14:, ['Location lifetime', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dictlt = dictlt.dropna().head(10)

    dictlt = {'1': {'name': dictlt.loc[14, 'Location lifetime'], 'users': dictlt.loc[14, 'Unnamed: 1'],
                    'newusers': dictlt.loc[14, 'Unnamed: 2'], 'sessions': dictlt.loc[14, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[14, 'Unnamed: 4'])},
              '2': {'name': dictlt.loc[15, 'Location lifetime'], 'users': dictlt.loc[15, 'Unnamed: 1'],
                    'newusers': dictlt.loc[15, 'Unnamed: 2'], 'sessions': dictlt.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[15, 'Unnamed: 4'])},
              '3': {'name': dictlt.loc[16, 'Location lifetime'], 'users': dictlt.loc[16, 'Unnamed: 1'],
                    'newusers': dictlt.loc[16, 'Unnamed: 2'], 'sessions': dictlt.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[16, 'Unnamed: 4'])},
              '4': {'name': dictlt.loc[17, 'Location lifetime'], 'users': dictlt.loc[17, 'Unnamed: 1'],
                    'newusers': dictlt.loc[17, 'Unnamed: 2'], 'sessions': dictlt.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[17, 'Unnamed: 4'])},
              '5': {'name': dictlt.loc[18, 'Location lifetime'], 'users': dictlt.loc[18, 'Unnamed: 1'],
                    'newusers': dictlt.loc[18, 'Unnamed: 2'], 'sessions': dictlt.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[18, 'Unnamed: 4'])}}

    return render(request, 'blogFiles/location.html', locals())


#INTERNATIONAL

@login_required(login_url='login')
def international(request):
    dict7 = analytics_data.parse('Int last 7 days')

    dict7 = dict7.loc[14:, ['Int last 7 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]

    dict7 = dict7.dropna().head(10)

    '''
    City Users NewUsers AvgDuration
    mum  150    59       93
    del  569    452      76
    '''

    dict7 = {'1': {'name': dict7.loc[15, 'Int last 7 days'], 'users': dict7.loc[15, 'Unnamed: 1'],
                   'newusers': dict7.loc[15, 'Unnamed: 2'], 'sessions': dict7.loc[15, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[15, 'Unnamed: 4'])},
             '2': {'name': dict7.loc[16, 'Int last 7 days'], 'users': dict7.loc[16, 'Unnamed: 1'],
                   'newusers': dict7.loc[16, 'Unnamed: 2'], 'sessions': dict7.loc[16, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[16, 'Unnamed: 4'])},
             '3': {'name': dict7.loc[17, 'Int last 7 days'], 'users': dict7.loc[17, 'Unnamed: 1'],
                   'newusers': dict7.loc[17, 'Unnamed: 2'], 'sessions': dict7.loc[17, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[17, 'Unnamed: 4'])},
             '4': {'name': dict7.loc[18, 'Int last 7 days'], 'users': dict7.loc[18, 'Unnamed: 1'],
                   'newusers': dict7.loc[18, 'Unnamed: 2'], 'sessions': dict7.loc[18, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[18, 'Unnamed: 4'])},
             '5': {'name': dict7.loc[19, 'Int last 7 days'], 'users': dict7.loc[19, 'Unnamed: 1'],
                   'newusers': dict7.loc[19, 'Unnamed: 2'], 'sessions': dict7.loc[19, 'Unnamed: 3'],
                   'avgsd': int(dict7.loc[19, 'Unnamed: 4'])}}

    dict14 = analytics_data.parse('Int last 14 days')
    dict14 = dict14.loc[14:, ['Int last 14 days', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dict14 = dict14.dropna().head(10)

    dict14 = {'1': {'name': dict14.loc[15, 'Int last 14 days'], 'users': dict14.loc[15, 'Unnamed: 1'],
                    'newusers': dict14.loc[15, 'Unnamed: 2'], 'sessions': dict14.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[15, 'Unnamed: 4'])},
              '2': {'name': dict14.loc[16, 'Int last 14 days'], 'users': dict14.loc[16, 'Unnamed: 1'],
                    'newusers': dict14.loc[16, 'Unnamed: 2'], 'sessions': dict14.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[16, 'Unnamed: 4'])},
              '3': {'name': dict14.loc[17, 'Int last 14 days'], 'users': dict14.loc[17, 'Unnamed: 1'],
                    'newusers': dict14.loc[17, 'Unnamed: 2'], 'sessions': dict14.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[17, 'Unnamed: 4'])},
              '4': {'name': dict14.loc[18, 'Int last 14 days'], 'users': dict14.loc[18, 'Unnamed: 1'],
                    'newusers': dict14.loc[18, 'Unnamed: 2'], 'sessions': dict14.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[18, 'Unnamed: 4'])},
              '5': {'name': dict14.loc[19, 'Int last 14 days'], 'users': dict14.loc[19, 'Unnamed: 1'],
                    'newusers': dict14.loc[19, 'Unnamed: 2'], 'sessions': dict14.loc[19, 'Unnamed: 3'],
                    'avgsd': int(dict14.loc[19, 'Unnamed: 4'])}}

    dictlm = analytics_data.parse('Int last month')
    dictlm = dictlm.loc[14:, ['Int last month', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dictlm = dictlm.dropna().head(10)

    dictlm = {'1': {'name': dictlm.loc[15, 'Int last month'], 'users': dictlm.loc[15, 'Unnamed: 1'],
                    'newusers': dictlm.loc[15, 'Unnamed: 2'], 'sessions': dictlm.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[15, 'Unnamed: 4'])},
              '2': {'name': dictlm.loc[16, 'Int last month'], 'users': dictlm.loc[16, 'Unnamed: 1'],
                    'newusers': dictlm.loc[16, 'Unnamed: 2'], 'sessions': dictlm.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[16, 'Unnamed: 4'])},
              '3': {'name': dictlm.loc[17, 'Int last month'], 'users': dictlm.loc[17, 'Unnamed: 1'],
                    'newusers': dictlm.loc[17, 'Unnamed: 2'], 'sessions': dictlm.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[17, 'Unnamed: 4'])},
              '4': {'name': dictlm.loc[18, 'Int last month'], 'users': dictlm.loc[18, 'Unnamed: 1'],
                    'newusers': dictlm.loc[18, 'Unnamed: 2'], 'sessions': dictlm.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[18, 'Unnamed: 4'])},
              '5': {'name': dictlm.loc[19, 'Int last month'], 'users': dictlm.loc[19, 'Unnamed: 1'],
                    'newusers': dictlm.loc[19, 'Unnamed: 2'], 'sessions': dictlm.loc[19, 'Unnamed: 3'],
                    'avgsd': int(dictlm.loc[19, 'Unnamed: 4'])}}

    dicttm = analytics_data.parse('Int this month')
    dicttm = dicttm.loc[14:, ['Int this month', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dicttm = dicttm.dropna().head(10)

    dicttm = {'1': {'name': dicttm.loc[15, 'Int this month'], 'users': dicttm.loc[15, 'Unnamed: 1'],
                    'newusers': dicttm.loc[15, 'Unnamed: 2'], 'sessions': dicttm.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[15, 'Unnamed: 4'])},
              '2': {'name': dicttm.loc[16, 'Int this month'], 'users': dicttm.loc[16, 'Unnamed: 1'],
                    'newusers': dicttm.loc[16, 'Unnamed: 2'], 'sessions': dicttm.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[16, 'Unnamed: 4'])},
              '3': {'name': dicttm.loc[17, 'Int this month'], 'users': dicttm.loc[17, 'Unnamed: 1'],
                    'newusers': dicttm.loc[17, 'Unnamed: 2'], 'sessions': dicttm.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[17, 'Unnamed: 4'])},
              '4': {'name': dicttm.loc[18, 'Int this month'], 'users': dicttm.loc[18, 'Unnamed: 1'],
                    'newusers': dicttm.loc[18, 'Unnamed: 2'], 'sessions': dicttm.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[18, 'Unnamed: 4'])},
              '5': {'name': dicttm.loc[19, 'Int this month'], 'users': dicttm.loc[19, 'Unnamed: 1'],
                    'newusers': dicttm.loc[19, 'Unnamed: 2'], 'sessions': dicttm.loc[19, 'Unnamed: 3'],
                    'avgsd': int(dicttm.loc[19, 'Unnamed: 4'])}}

    dictlt = analytics_data.parse('Int lifetime')
    dictlt = dictlt.loc[14:, ['Int lifetime', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
    dictlt = dictlt.dropna().head(10)

    dictlt = {'1': {'name': dictlt.loc[15, 'Int lifetime'], 'users': dictlt.loc[15, 'Unnamed: 1'],
                    'newusers': dictlt.loc[15, 'Unnamed: 2'], 'sessions': dictlt.loc[15, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[15, 'Unnamed: 4'])},
              '2': {'name': dictlt.loc[16, 'Int lifetime'], 'users': dictlt.loc[16, 'Unnamed: 1'],
                    'newusers': dictlt.loc[16, 'Unnamed: 2'], 'sessions': dictlt.loc[16, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[16, 'Unnamed: 4'])},
              '3': {'name': dictlt.loc[17, 'Int lifetime'], 'users': dictlt.loc[17, 'Unnamed: 1'],
                    'newusers': dictlt.loc[17, 'Unnamed: 2'], 'sessions': dictlt.loc[17, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[17, 'Unnamed: 4'])},
              '4': {'name': dictlt.loc[18, 'Int lifetime'], 'users': dictlt.loc[18, 'Unnamed: 1'],
                    'newusers': dictlt.loc[18, 'Unnamed: 2'], 'sessions': dictlt.loc[18, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[18, 'Unnamed: 4'])},
              '5': {'name': dictlt.loc[19, 'Int lifetime'], 'users': dictlt.loc[19, 'Unnamed: 1'],
                    'newusers': dictlt.loc[19, 'Unnamed: 2'], 'sessions': dictlt.loc[19, 'Unnamed: 3'],
                    'avgsd': int(dictlt.loc[19, 'Unnamed: 4'])}}

    return render(request, 'blogFiles/international.html', locals())


#OPERATION SYSTEM

@login_required(login_url='login')
def operatingsystem(request):
    dict7 = analytics_data.parse('Device last 7 days')
    dict7 = dict7.loc[14:, ['Device last 7 days', 'Unnamed: 1', 'Unnamed: 2', ]]
    dict7 = dict7.dropna()

    dict7 = {'1': {'name': dict7.loc[14, 'Device last 7 days'], 'sessions': dict7.loc[14, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[14, 'Unnamed: 2'])},
             '2': {'name': dict7.loc[15, 'Device last 7 days'], 'sessions': dict7.loc[15, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[15, 'Unnamed: 2'])},
             '3': {'name': dict7.loc[16, 'Device last 7 days'], 'sessions': dict7.loc[16, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[16, 'Unnamed: 2'])},
             '4': {'name': dict7.loc[17, 'Device last 7 days'], 'sessions': dict7.loc[17, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[17, 'Unnamed: 2'])},
             '5': {'name': dict7.loc[18, 'Device last 7 days'], 'sessions': dict7.loc[18, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[18, 'Unnamed: 2'])},
             }

    dict14 = analytics_data.parse('Device last 14 days')
    dict14 = dict14.loc[14:, ['Device last 14 days', 'Unnamed: 1', 'Unnamed: 2', ]]
    dict14 = dict14.dropna()

    dict14 = {'1': {'name': dict14.loc[14, 'Device last 14 days'], 'sessions': dict14.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[14, 'Unnamed: 2'])},
              '2': {'name': dict14.loc[15, 'Device last 14 days'], 'sessions': dict14.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[15, 'Unnamed: 2'])},
              '3': {'name': dict14.loc[16, 'Device last 14 days'], 'sessions': dict14.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[16, 'Unnamed: 2'])},
              '4': {'name': dict14.loc[17, 'Device last 14 days'], 'sessions': dict14.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[17, 'Unnamed: 2'])},
              '5': {'name': dict14.loc[18, 'Device last 14 days'], 'sessions': dict14.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[18, 'Unnamed: 2'])},
              }

    dictlm = analytics_data.parse('Device last last month')
    dictlm = dictlm.loc[14:, ['Device last last month', 'Unnamed: 1', 'Unnamed: 2', ]]
    dictlm = dictlm.dropna()

    dictlm = {'1': {'name': dictlm.loc[14, 'Device last last month'], 'sessions': dictlm.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlm.loc[15, 'Device last last month'], 'sessions': dictlm.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlm.loc[16, 'Device last last month'], 'sessions': dictlm.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlm.loc[17, 'Device last last month'], 'sessions': dictlm.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlm.loc[18, 'Device last last month'], 'sessions': dictlm.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[18, 'Unnamed: 2'])},
              }

    dicttm = analytics_data.parse('Device this month')
    dicttm = dicttm.loc[14:, ['Device this month', 'Unnamed: 1', 'Unnamed: 2', ]]
    dicttm = dicttm.dropna()

    dicttm = {'1': {'name': dicttm.loc[14, 'Device this month'], 'sessions': dicttm.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dicttm.loc[15, 'Device this month'], 'sessions': dicttm.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dicttm.loc[16, 'Device this month'], 'sessions': dicttm.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dicttm.loc[17, 'Device this month'], 'sessions': dicttm.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dicttm.loc[18, 'Device this month'], 'sessions': dicttm.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[18, 'Unnamed: 2'])},
              }

    dictlt = analytics_data.parse('Device lifetime')
    dictlt = dictlt.loc[14:, ['Device lifetime', 'Unnamed: 1', 'Unnamed: 2', ]]
    dictlt = dictlt.dropna()

    dictlt = {'1': {'name': dictlt.loc[14, 'Device lifetime'], 'sessions': dictlt.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlt.loc[15, 'Device lifetime'], 'sessions': dictlt.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlt.loc[16, 'Device lifetime'], 'sessions': dictlt.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlt.loc[17, 'Device lifetime'], 'sessions': dictlt.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlt.loc[18, 'Device lifetime'], 'sessions': dictlt.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[18, 'Unnamed: 2'])},
              }

    return render(request,'blogFiles/os.html', locals())

#Interest Group

@login_required(login_url='login')
def bloginterest(request):


    dict7 = analytics_data.parse('interest last 7 days')
    dict7 = dict7.loc[14:20, ['interest last 7 days', 'Unnamed: 1', 'Unnamed: 2']]

    dict7 = {'1': {'name': dict7.loc[14, 'interest last 7 days'], 'sessions': dict7.loc[14, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[14, 'Unnamed: 2'])},
             '2': {'name': dict7.loc[15, 'interest last 7 days'], 'sessions': dict7.loc[15, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[15, 'Unnamed: 2'])},
             '3': {'name': dict7.loc[16, 'interest last 7 days'], 'sessions': dict7.loc[16, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[16, 'Unnamed: 2'])},
             '4': {'name': dict7.loc[17, 'interest last 7 days'], 'sessions': dict7.loc[17, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[17, 'Unnamed: 2'])},
             '5': {'name': dict7.loc[18, 'interest last 7 days'], 'sessions': dict7.loc[18, 'Unnamed: 1'],
                   'avgsd': int(dict7.loc[18, 'Unnamed: 2'])}, }

    dict14 = analytics_data.parse('interest last 14 days')
    dict14 = dict14.loc[14:20, ['interest last 14 days', 'Unnamed: 1', 'Unnamed: 2']]

    dict14 = {'1': {'name': dict14.loc[14, 'interest last 14 days'], 'sessions': dict14.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[14, 'Unnamed: 2'])},
              '2': {'name': dict14.loc[15, 'interest last 14 days'], 'sessions': dict14.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[15, 'Unnamed: 2'])},
              '3': {'name': dict14.loc[16, 'interest last 14 days'], 'sessions': dict14.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[16, 'Unnamed: 2'])},
              '4': {'name': dict14.loc[17, 'interest last 14 days'], 'sessions': dict14.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[17, 'Unnamed: 2'])},
              '5': {'name': dict14.loc[18, 'interest last 14 days'], 'sessions': dict14.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[18, 'Unnamed: 2'])}, }

    dictlm = analytics_data.parse('interest last month')
    dictlm = dictlm.loc[14:20, ['interest last month', 'Unnamed: 1', 'Unnamed: 2']]

    dictlm = {'1': {'name': dictlm.loc[14, 'interest last month'], 'sessions': dictlm.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlm.loc[15, 'interest last month'], 'sessions': dictlm.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlm.loc[16, 'interest last month'], 'sessions': dictlm.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlm.loc[17, 'interest last month'], 'sessions': dictlm.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlm.loc[18, 'interest last month'], 'sessions': dictlm.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dictlm.loc[18, 'Unnamed: 2'])}, }

    dicttm = analytics_data.parse('interest this month')
    dicttm = dicttm.loc[14:20, ['interest this month', 'Unnamed: 1', 'Unnamed: 2']]

    dicttm = {'1': {'name': dicttm.loc[14, 'interest this month'], 'sessions': dicttm.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dicttm.loc[15, 'interest this month'], 'sessions': dicttm.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dicttm.loc[16, 'interest this month'], 'sessions': dicttm.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dicttm.loc[17, 'interest this month'], 'sessions': dicttm.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dicttm.loc[18, 'interest this month'], 'sessions': dicttm.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dicttm.loc[18, 'Unnamed: 2'])}, }

    dictlt = analytics_data.parse('interest lifetime')
    dictlt = dictlt.loc[14:20, ['interest lifetime', 'Unnamed: 1', 'Unnamed: 2']]

    dictlt = {'1': {'name': dictlt.loc[14, 'interest lifetime'], 'sessions': dictlt.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlt.loc[15, 'interest lifetime'], 'sessions': dictlt.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlt.loc[16, 'interest lifetime'], 'sessions': dictlt.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlt.loc[17, 'interest lifetime'], 'sessions': dictlt.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlt.loc[18, 'interest lifetime'], 'sessions': dictlt.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[18, 'Unnamed: 2'])}, }

    return render(request, 'blogFiles/interest.html', locals())

@login_required(login_url='login')
def articles(request):

    dict7 = analytics_data.parse('page last 7 days')
    dict7 = dict7.loc[14:20, ['page last 7 days', 'Unnamed: 1', 'Unnamed: 2']]

    dict7 = {'1': {'name': dict7.loc[14, 'page last 7 days'], 'users': dict7.loc[14, 'Unnamed: 1'],
                   'pageviews': int(dict7.loc[14, 'Unnamed: 2'])},
             '2': {'name': dict7.loc[15, 'page last 7 days'], 'users': dict7.loc[15, 'Unnamed: 1'],
                   'pageviews': int(dict7.loc[15, 'Unnamed: 2'])},
             '3': {'name': dict7.loc[16, 'page last 7 days'], 'users': dict7.loc[16, 'Unnamed: 1'],
                   'pageviews': int(dict7.loc[16, 'Unnamed: 2'])},
             '4': {'name': dict7.loc[17, 'page last 7 days'], 'users': dict7.loc[17, 'Unnamed: 1'],
                   'pageviews': int(dict7.loc[17, 'Unnamed: 2'])},
             '5': {'name': dict7.loc[18, 'page last 7 days'], 'users': dict7.loc[18, 'Unnamed: 1'],
                   'pageviews': int(dict7.loc[18, 'Unnamed: 2'])}, }

    dict14 = analytics_data.parse('page last 14 days')
    dict14 = dict14.loc[14:20, ['page last 14 days', 'Unnamed: 1', 'Unnamed: 2']]

    dict14 = {'1': {'name': dict14.loc[14, 'page last 14 days'], 'users': dict14.loc[14, 'Unnamed: 1'],
                    'pageviews': int(dict14.loc[14, 'Unnamed: 2'])},
              '2': {'name': dict14.loc[15, 'page last 14 days'], 'users': dict14.loc[15, 'Unnamed: 1'],
                    'pageviews': int(dict14.loc[15, 'Unnamed: 2'])},
              '3': {'name': dict14.loc[16, 'page last 14 days'], 'users': dict14.loc[16, 'Unnamed: 1'],
                    'pageviews': int(dict14.loc[16, 'Unnamed: 2'])},
              '4': {'name': dict14.loc[17, 'page last 14 days'], 'users': dict14.loc[17, 'Unnamed: 1'],
                    'pageviews': int(dict14.loc[17, 'Unnamed: 2'])},
              '5': {'name': dict14.loc[18, 'page last 14 days'], 'users': dict14.loc[18, 'Unnamed: 1'],
                    'pageviews': int(dict14.loc[18, 'Unnamed: 2'])}, }

    dictlm = analytics_data.parse('page last month')
    dictlm = dictlm.loc[14:20, ['page last month', 'Unnamed: 1', 'Unnamed: 2']]

    dictlm = {'1': {'name': dictlm.loc[14, 'page last month'], 'users': dictlm.loc[14, 'Unnamed: 1'],
                    'pageviews': int(dictlm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlm.loc[15, 'page last month'], 'users': dictlm.loc[15, 'Unnamed: 1'],
                    'pageviews': int(dictlm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlm.loc[16, 'page last month'], 'users': dictlm.loc[16, 'Unnamed: 1'],
                    'pageviews': int(dictlm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlm.loc[17, 'page last month'], 'users': dictlm.loc[17, 'Unnamed: 1'],
                    'pageviews': int(dictlm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlm.loc[18, 'page last month'], 'users': dictlm.loc[18, 'Unnamed: 1'],
                    'pageviews': int(dictlm.loc[18, 'Unnamed: 2'])}, }

    dicttm = analytics_data.parse('page this month')
    dicttm = dicttm.loc[14:20, ['page this month', 'Unnamed: 1', 'Unnamed: 2']]

    dicttm = {'1': {'name': dicttm.loc[14, 'page this month'], 'users': dicttm.loc[14, 'Unnamed: 1'],
                    'pageviews': int(dicttm.loc[14, 'Unnamed: 2'])},
              '2': {'name': dicttm.loc[15, 'page this month'], 'users': dicttm.loc[15, 'Unnamed: 1'],
                    'pageviews': int(dicttm.loc[15, 'Unnamed: 2'])},
              '3': {'name': dicttm.loc[16, 'page this month'], 'users': dicttm.loc[16, 'Unnamed: 1'],
                    'pageviews': int(dicttm.loc[16, 'Unnamed: 2'])},
              '4': {'name': dicttm.loc[17, 'page this month'], 'users': dicttm.loc[17, 'Unnamed: 1'],
                    'pageviews': int(dicttm.loc[17, 'Unnamed: 2'])},
              '5': {'name': dicttm.loc[18, 'page this month'], 'users': dicttm.loc[18, 'Unnamed: 1'],
                    'pageviews': int(dicttm.loc[18, 'Unnamed: 2'])}, }

    dictlt = analytics_data.parse('page lifetime')
    dictlt = dictlt.loc[14:20, ['page lifetime', 'Unnamed: 1', 'Unnamed: 2']]

    dictlt = {'1': {'name': dictlt.loc[14, 'page lifetime'], 'users': dictlt.loc[14, 'Unnamed: 1'],
                    'pageviews': int(dictlt.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlt.loc[15, 'page lifetime'], 'users': dictlt.loc[15, 'Unnamed: 1'],
                    'pageviews': int(dictlt.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlt.loc[16, 'page lifetime'], 'users': dictlt.loc[16, 'Unnamed: 1'],
                    'pageviews': int(dictlt.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlt.loc[17, 'page lifetime'], 'users': dictlt.loc[17, 'Unnamed: 1'],
                    'pageviews': int(dictlt.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlt.loc[18, 'page lifetime'], 'users': dictlt.loc[18, 'Unnamed: 1'],
                    'pageviews': int(dictlt.loc[18, 'Unnamed: 2'])}, }

    return render(request,'blogFiles/articles.html', locals())


# MOBILE APP


@login_required(login_url='login')
def screens(request):
    # IOS Screens

    dict14 = app_data.parse('IOS screens')

    dict14 = dict14.loc[14:20, ['IOS screens', 'Unnamed: 1', 'Unnamed: 2']]

    dict14 = app_data.parse('IOS screens')
    dict14 = dict14.loc[14:20, ['IOS screens', 'Unnamed: 1', 'Unnamed: 2']]

    dict14 = {'1': {'name': dict14.loc[14, 'IOS screens'], 'sessions': dict14.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[14, 'Unnamed: 2'])},
              '2': {'name': dict14.loc[15, 'IOS screens'], 'sessions': dict14.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[15, 'Unnamed: 2'])},
              '3': {'name': dict14.loc[16, 'IOS screens'], 'sessions': dict14.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[16, 'Unnamed: 2'])},
              '4': {'name': dict14.loc[17, 'IOS screens'], 'sessions': dict14.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[17, 'Unnamed: 2'])},
              '5': {'name': dict14.loc[18, 'IOS screens'], 'sessions': dict14.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dict14.loc[18, 'Unnamed: 2'])}, }

    dictlt = app_data.parse('IOS screens lt')
    dictlt = dictlt.loc[14:20, ['IOS screens lt', 'Unnamed: 1', 'Unnamed: 2']]

    dictlt = {'1': {'name': dictlt.loc[14, 'IOS screens lt'], 'sessions': dictlt.loc[14, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[14, 'Unnamed: 2'])},
              '2': {'name': dictlt.loc[15, 'IOS screens lt'], 'sessions': dictlt.loc[15, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[15, 'Unnamed: 2'])},
              '3': {'name': dictlt.loc[16, 'IOS screens lt'], 'sessions': dictlt.loc[16, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[16, 'Unnamed: 2'])},
              '4': {'name': dictlt.loc[17, 'IOS screens lt'], 'sessions': dictlt.loc[17, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[17, 'Unnamed: 2'])},
              '5': {'name': dictlt.loc[18, 'IOS screens lt'], 'sessions': dictlt.loc[18, 'Unnamed: 1'],
                    'avgsd': int(dictlt.loc[18, 'Unnamed: 2'])}, }

    # ANDROID Screens

    a_dict14 = app_data.parse('Android screens')
    a_dict14 = a_dict14.loc[14:20, ['Android screens', 'Unnamed: 1', 'Unnamed: 2']]

    a_dict14 = {'1': {'name': a_dict14.loc[14, 'Android screens'], 'sessions': a_dict14.loc[14, 'Unnamed: 1'],
                    'avgsd': int(a_dict14.loc[14, 'Unnamed: 2'])},
              '2': {'name': a_dict14.loc[15, 'Android screens'], 'sessions': a_dict14.loc[15, 'Unnamed: 1'],
                    'avgsd': int(a_dict14.loc[15, 'Unnamed: 2'])},
              '3': {'name': a_dict14.loc[16, 'Android screens'], 'sessions': a_dict14.loc[16, 'Unnamed: 1'],
                    'avgsd': int(a_dict14.loc[16, 'Unnamed: 2'])},
              '4': {'name': a_dict14.loc[17, 'Android screens'], 'sessions': a_dict14.loc[17, 'Unnamed: 1'],
                    'avgsd': int(a_dict14.loc[17, 'Unnamed: 2'])},
              '5': {'name': a_dict14.loc[18, 'Android screens'], 'sessions': a_dict14.loc[18, 'Unnamed: 1'],
                    'avgsd': int(a_dict14.loc[18, 'Unnamed: 2'])}, }

    a_dictlt = app_data.parse('Android screens lt')
    a_dictlt = a_dictlt.loc[14:20, ['Android screens lt', 'Unnamed: 1', 'Unnamed: 2']]

    a_dictlt = {'1': {'name': a_dictlt.loc[14, 'Android screens lt'], 'sessions': a_dictlt.loc[14, 'Unnamed: 1'],
                      'avgsd': int(a_dictlt.loc[14, 'Unnamed: 2'])},
                '2': {'name': a_dictlt.loc[15, 'Android screens lt'], 'sessions': a_dictlt.loc[15, 'Unnamed: 1'],
                      'avgsd': int(a_dictlt.loc[15, 'Unnamed: 2'])},
                '3': {'name': a_dictlt.loc[16, 'Android screens lt'], 'sessions': a_dictlt.loc[16, 'Unnamed: 1'],
                      'avgsd': int(a_dictlt.loc[16, 'Unnamed: 2'])},
                '4': {'name': a_dictlt.loc[17, 'Android screens lt'], 'sessions': a_dictlt.loc[17, 'Unnamed: 1'],
                      'avgsd': int(a_dictlt.loc[17, 'Unnamed: 2'])},
                '5': {'name': a_dictlt.loc[18, 'Android screens lt'], 'sessions': a_dictlt.loc[18, 'Unnamed: 1'],
                      'avgsd': int(a_dictlt.loc[18, 'Unnamed: 2'])}, }

    return render(request, 'appFiles/screens.html', locals())


#App users

@login_required(login_url='login')
def appusers(request):


    def incompleteinstalls():

        lst = []

        for x in result.values():

            try:

                lst.append(x['city'])



            except KeyError:

                pass

        lst = len(lst)

        totalinstalls = []

        for x in result.values():

            try:

                totalinstalls.append(x['email'])

            except KeyError:
                pass

        totalinstalls = len(totalinstalls)

        incomplete = totalinstalls - lst

        complete = totalinstalls - incomplete

        return incomplete, totalinstalls, complete

    incominstalls = incompleteinstalls()[0]
    totalinstalls = incompleteinstalls()[1]
    completeinstalls = incompleteinstalls()[2]

    return render(request, 'appFiles/app-users.html', locals())



# APP LOCATIONS

@login_required(login_url='login')
def applocation(request):


    def city():

        lst = []

        for x in result.values():

            try:


                lst.append(x['city'])



            except KeyError:

                pass

        return lst

    lst = dict(Counter(city()))

    def totalusers():

        totalinstalls = []

        for x in result.values():

            try:

                totalinstalls.append(x['email'])

            except KeyError:
                pass

        return len(totalinstalls)

    #for the sake of space

    newdelhi = lst['New Delhi']

    totalinstalls = totalusers()
    totalcities = len(lst.keys())

    return render(request, 'appFiles/location.html', locals())


# App uesr Interest

@login_required(login_url='login')
def appinterest(request):


    def industry():

        lst = []

        for x in result.values():

            try:

                lst.append(x['industry'])


            except KeyError:

                pass

        return Counter(lst)

    def interest():

        lst = []

        for x in result.values():

            try:

                lst.append(x['interests'])

            except KeyError:

                pass

        lst = [x.values() for x in lst]

        lst2 = []

        for x in lst:

            for y in x:
                lst2.append(y)

        lst3 = [x.values() for x in lst2]

        lst3 = [x[0] for x in lst3]

        return Counter(lst3)

    test = industry()

    interest = dict(interest())
    industry = dict(industry())


    #VARIABLES INTEREST

    Travel = interest['Travel']
    Photography = interest['Photography']
    Music = interest['Music']
    Art = interest['Art']
    Entrepreneurship = interest['Entrepreneurship']
    Technology = interest['Technology']
    Fashion = interest['Fashion']
    Film = interest['Film']
    Reading = interest['Reading']
    Fitness = interest['Fitness']
    Social = interest['Social Cause']
    Interior = interest['Interior Decor']
    Makeup = interest['Makeup & Beauty']
    Jewellery = interest['Jewellery']

    # VARIABLES INDUSTRY

    branding = industry['Branding, Design & Visual Arts']
    web = industry['Web, Tech & Innovation']
    photography = industry['Photography & Videography']
    advertising = industry['Advertising, Marketing & PR']
    other = industry['Other']
    art = industry['Art, Architecture & Interiors']
    business = industry['Business & Industry']
    music = industry['Music']
    fashion = industry['Fashion Styling & Blogging']
    food = industry['Food & Beverage']
    film = industry['Film & Production']
    writing = industry['Writing & Journalism']
    clothing = industry['Clothing & Jewellery']
    travel = industry['Travel & Hospitality']
    health = industry['Health & Fitness']
    hair = industry['Hair & Beauty']
    gifts = industry['Gifts & Accessories']
    weddings = industry['Weddings & Events']
    social = industry['Social Work & Activism']

    return  render(request, 'appFiles/interest.html', locals())


# App Trending profiles

@login_required(login_url='login')
def trendingProfiles(request):
    fullname = []
    views = []
    profilepicture = []
    city = []
    industry = []
    title = []
    profilekey = []
    followers = []

    for x in result.values():

        if len(result.keys()[result.values().index(x)]) > 27:

            try:

                profilekey.append(result.keys()[result.values().index(x)])

            except:

                pass

            try:

                title.append(x['title'])

            except:

                title.append('Unknown')

            try:

                views.append(x['views_count'])

            except:

                views.append(0)

            try:

                fullname.append((x['firstName'] + ' ' + x['lastName']))

            except:

                fullname.append('Unknown')

            try:



                profilepicture.append(x['photoURL'])



            except:

                profilepicture.append('Unknown')

            try:

                city.append(x['city'])

            except:

                city.append('Unknown')

            try:

                industry.append(x['industry'])

            except:

                industry.append('Unknown')

            try:

                followers.append(len(x['followers']))

            except:

                followers.append(0)

    profilepicture = [x.replace('uploads', 'https://api.dyscoapp.com/uploads') for x in profilepicture]

    profilekey = ["https://www.dyscoapp.com/app/profile/" + x for x in profilekey]

    dictviews = {'views': views, 'fullname': fullname, 'title': title, 'city': city, 'photourl': profilepicture,
                 'followers': followers, 'profilekey' : profilekey}

    dictviews = pd.DataFrame.from_dict(dictviews)

    dictviews = dictviews.sort_values('followers', ascending=False)





    first = {'name': list(dictviews.head()['fullname'])[0], 'followers': list(dictviews.head()['followers'])[0],
             'photourl': list(dictviews.head()['photourl'])[0], 'title': list(dictviews.head()['title'])[0],
             'city': list(dictviews.head()['city'])[0], 'profilekey' : list(dictviews.head()['profilekey'])[0] }

    second = {'name': list(dictviews.head()['fullname'])[1], 'followers': list(dictviews.head()['followers'])[1],
              'photourl': list(dictviews.head()['photourl'])[1], 'title': list(dictviews.head()['title'])[1],
              'city': list(dictviews.head()['city'])[1], 'profilekey' : list(dictviews.head()['profilekey'])[1]}

    third = {'name': list(dictviews.head()['fullname'])[2], 'followers': list(dictviews.head()['followers'])[2],
             'photourl': list(dictviews.head()['photourl'])[2], 'title': list(dictviews.head()['title'])[2],
             'city': list(dictviews.head()['city'])[2], 'profilekey' : list(dictviews.head()['profilekey'])[2]}

    fourth = {'name': list(dictviews.head()['fullname'])[3], 'followers': list(dictviews.head()['followers'])[3],
              'photourl': list(dictviews.head()['photourl'])[3], 'title': list(dictviews.head()['title'])[3],
              'city': list(dictviews.head()['city'])[3], 'profilekey' : list(dictviews.head()['profilekey'])[3]}

    fifth = {'name': list(dictviews.head()['fullname'])[4], 'followers': list(dictviews.head()['followers'])[4],
             'photourl': list(dictviews.head()['photourl'])[4], 'title': list(dictviews.head()['title'])[4],
             'city': list(dictviews.head()['city'])[4], 'profilekey' : list(dictviews.head()['profilekey'])[4]}

    sixth = {'name': list(dictviews.head(6)['fullname'])[5], 'followers': list(dictviews.head(6)['followers'])[5],
             'photourl': list(dictviews.head(6)['photourl'])[5], 'title': list(dictviews.head(6)['title'])[5],
             'city': list(dictviews.head(6)['city'])[5], 'profilekey' : list(dictviews.head(6)['profilekey'])[5]}



    #TOP POSTS


    postedby = []
    hearts = []
    views = []
    shares = []
    repost = []
    title = []
    description = []
    createdDate = []
    postedbyName = []
    postedbyUrl = []
    monthCreated = []
    yearCreated = []
    mediaurl = []

    for x in app_result.values():

        try:

            try:

                mediaurl.append(x['embedly']['thumbnail_url'])

            except KeyError:

                data = x['image_data']['full_image']
                mediaurl.append(data.replace('uploads', 'https://api.dyscoapp.com/uploads'))



        except KeyError:
            mediaurl.append('https://thumbs.dreamstime.com/t/cartoon-group-people-saying-no-raised-fists-vector-65676914.jpg')

        try:

            title.append(x['title'])

        except KeyError:
            title.append('unknown')

        try:

            description.append(x['description']['text'])


        except KeyError:
            description.append('unknown')

        try:
            createdDate.append(x['post_created_at'][:10])

        except KeyError:
            createdDate.append('unknown')

        try:
            monthCreated.append(int(x['post_created_at'][5:7]))

        except KeyError:
            monthCreated.append('unknown')

        try:
            yearCreated.append(int(x['post_created_at'][0:4]))

        except KeyError:
            yearCreated.append('unknown')

        try:

            repost.append(x['shareDysco'])

        except:
            repost.append(0)

        try:

            shares.append(x['share'])

        except KeyError:
            shares.append(0)

        try:

            hearts.append(len(x['hearts']))

        except KeyError:
            hearts.append(0)

        try:

            views.append(len(x['views']))

        except KeyError:
            views.append(0)

        try:
            # postedby.append(result.keys()[result.values().index(x)])
            postedby.append(x['userid'])

        except KeyError:
            postedby.append('uknown')

        try:
            postedbyUrl.append(app_result.keys()[app_result.values().index(x)])

        except:
            postedbyUrl.append('unknown')

    # mediaurl = [x.replace('uploads', 'https://api.dyscoapp.com/uploads') for x in mediaurl]

    postedbyUrl = ['https://www.dyscoapp.com/app/p/' + x for x in postedbyUrl]

    posts = {'title': title, 'description': description, 'postedby': postedby, 'hearts': hearts,
             'views': views, 'shares': shares, 'repost': repost, 'createdDate': createdDate, 'postedbyUrl': postedbyUrl,
             'monthCreated': monthCreated, 'yearCreated': yearCreated, 'mediaurl': mediaurl}

    posts = pd.DataFrame.from_dict(posts)

    posts['score'] = (posts['hearts'] * 3) + (posts['shares'] * 5) + posts['views'] + (posts['repost'] * 5)

    posts = posts.sort_values('score', ascending=False)

    # TOP 5 POSTS

    top5 = posts.head()

    for y in top5['postedby']:

        for x in users.values():

            if users.keys()[users.values().index(x)] == y:
                postedbyName.append(x['firstName'])

    top5['postedby'] = postedbyName

    # top5month

    current_year = int(date.today().year)
    current_month = int(date.today().month)
    month_postedbyName = []

    top5month = posts[posts['yearCreated'] == current_year][posts['monthCreated'] == current_month].head()

    for y in top5month['postedby']:

        for x in users.values():

            if users.keys()[users.values().index(x)] == y:
                month_postedbyName.append(x['firstName'])

    top5month['postedby'] = month_postedbyName

    month5 = {'1': {'title': list(top5month['title'])[0], 'description': list(top5month['description'])[0][:60],
                    'postedby': list(top5month['postedby'])[0], 'hearts': list(top5month['hearts'])[0],
                    'views': list(top5month['views'])[0], 'shares': list(top5month['shares'])[0],
                    'repost': list(top5month['repost'])[0], 'createdDate': list(top5month['createdDate'])[0],
                    'postedbyUrl': list(top5month['postedbyUrl'])[0],
                    'monthCreated': list(top5month['monthCreated'])[0],
                    'yearCreated': list(top5month['yearCreated'])[0], 'mediaurl': list(top5month['mediaurl'])[0],
                    'score': list(top5month['score'])[0]},
              '2': {'title': list(top5month['title'])[1], 'description': list(top5month['description'])[1][:60],
                    'postedby': list(top5month['postedby'])[1], 'hearts': list(top5month['hearts'])[1],
                    'views': list(top5month['views'])[1], 'shares': list(top5month['shares'])[1],
                    'repost': list(top5month['repost'])[1], 'createdDate': list(top5month['createdDate'])[1],
                    'postedbyUrl': list(top5month['postedbyUrl'])[1],
                    'monthCreated': list(top5month['monthCreated'])[1],
                    'yearCreated': list(top5month['yearCreated'])[1], 'mediaurl': list(top5month['mediaurl'])[1],
                    'score': list(top5month['score'])[1]},
              '3': {'title': list(top5month['title'])[2], 'description': list(top5month['description'])[2][:60],
                    'postedby': list(top5month['postedby'])[2], 'hearts': list(top5month['hearts'])[2],
                    'views': list(top5month['views'])[2], 'shares': list(top5month['shares'])[2],
                    'repost': list(top5month['repost'])[2], 'createdDate': list(top5month['createdDate'])[2],
                    'postedbyUrl': list(top5month['postedbyUrl'])[2],
                    'monthCreated': list(top5month['monthCreated'])[2],
                    'yearCreated': list(top5month['yearCreated'])[2], 'mediaurl': list(top5month['mediaurl'])[2],
                    'score': list(top5month['score'])[2]},
              '4': {'title': list(top5month['title'])[3], 'description': list(top5month['description'])[3][:60],
                    'postedby': list(top5month['postedby'])[3], 'hearts': list(top5month['hearts'])[3],
                    'views': list(top5month['views'])[3], 'shares': list(top5month['shares'])[3],
                    'repost': list(top5month['repost'])[3], 'createdDate': list(top5month['createdDate'])[3],
                    'postedbyUrl': list(top5month['postedbyUrl'])[3],
                    'monthCreated': list(top5month['monthCreated'])[3],
                    'yearCreated': list(top5month['yearCreated'])[3], 'mediaurl': list(top5month['mediaurl'])[3],
                    'score': list(top5month['score'])[3]},
              '5': {'title': list(top5month['title'])[4], 'description': list(top5month['description'])[4][:60],
                    'postedby': list(top5month['postedby'])[4], 'hearts': list(top5month['hearts'])[4],
                    'views': list(top5month['views'])[4], 'shares': list(top5month['shares'])[4],
                    'repost': list(top5month['repost'])[4], 'createdDate': list(top5month['createdDate'])[4],
                    'postedbyUrl': list(top5month['postedbyUrl'])[4],
                    'monthCreated': list(top5month['monthCreated'])[4],
                    'yearCreated': list(top5month['yearCreated'])[4], 'mediaurl': list(top5month['mediaurl'])[4],
                    'score': list(top5month['score'])[4]}}

    alltop5 = {'1': {'title': list(top5['title'])[0], 'description': list(top5['description'])[0][:60],
                     'postedby': list(top5['postedby'])[0], 'hearts': list(top5['hearts'])[0],
                     'views': list(top5['views'])[0], 'shares': list(top5['shares'])[0],
                     'repost': list(top5['repost'])[0], 'createdDate': list(top5['createdDate'])[0],
                     'postedbyUrl': list(top5['postedbyUrl'])[0],
                     'monthCreated': list(top5['monthCreated'])[0], 'yearCreated': list(top5['yearCreated'])[0],
                     'mediaurl': list(top5['mediaurl'])[0], 'score': list(top5['score'])[0]},
               '2': {'title': list(top5['title'])[1], 'description': list(top5['description'])[1][:60],
                     'postedby': list(top5['postedby'])[1], 'hearts': list(top5['hearts'])[1],
                     'views': list(top5['views'])[1], 'shares': list(top5['shares'])[1],
                     'repost': list(top5['repost'])[1], 'createdDate': list(top5['createdDate'])[1],
                     'postedbyUrl': list(top5['postedbyUrl'])[1],
                     'monthCreated': list(top5['monthCreated'])[1], 'yearCreated': list(top5['yearCreated'])[1],
                     'mediaurl': list(top5['mediaurl'])[1], 'score': list(top5['score'])[1]},
               '3': {'title': list(top5['title'])[2], 'description': list(top5['description'])[2][:60],
                     'postedby': list(top5['postedby'])[2], 'hearts': list(top5['hearts'])[2],
                     'views': list(top5['views'])[2], 'shares': list(top5['shares'])[2],
                     'repost': list(top5['repost'])[2], 'createdDate': list(top5['createdDate'])[2],
                     'postedbyUrl': list(top5['postedbyUrl'])[2],
                     'monthCreated': list(top5['monthCreated'])[2], 'yearCreated': list(top5['yearCreated'])[2],
                     'mediaurl': list(top5['mediaurl'])[2], 'score': list(top5['score'])[2]},
               '4': {'title': list(top5['title'])[3], 'description': list(top5['description'])[3][:60],
                     'postedby': list(top5['postedby'])[3], 'hearts': list(top5['hearts'])[3],
                     'views': list(top5['views'])[3], 'shares': list(top5['shares'])[3],
                     'repost': list(top5['repost'])[3], 'createdDate': list(top5['createdDate'])[3],
                     'postedbyUrl': list(top5['postedbyUrl'])[3],
                     'monthCreated': list(top5['monthCreated'])[3], 'yearCreated': list(top5['yearCreated'])[3],
                     'mediaurl': list(top5['mediaurl'])[3], 'score': list(top5['score'])[3]},
               '5': {'title': list(top5['title'])[4], 'description': list(top5['description'])[4][:60],
                     'postedby': list(top5['postedby'])[4], 'hearts': list(top5['hearts'])[4],
                     'views': list(top5['views'])[4], 'shares': list(top5['shares'])[4],
                     'repost': list(top5['repost'])[4], 'createdDate': list(top5['createdDate'])[4],
                     'postedbyUrl': list(top5['postedbyUrl'])[4],
                     'monthCreated': list(top5['monthCreated'])[4], 'yearCreated': list(top5['yearCreated'])[4],
                     'mediaurl': list(top5['mediaurl'])[4], 'score': list(top5['score'])[4]}}




    return render(request, 'appFiles/trending.html', locals())


