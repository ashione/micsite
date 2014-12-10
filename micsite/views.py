__author__ = 'tj'
# coding=utf-8
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput

from django.contrib.auth.decorators import login_required

from forms import LoginForm, ChangepwdForm
from notify.models import Node

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
            #    return render_to_response('index.html', RequestContext(request))
                return index(request)
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('index.html', RequestContext(request,{'changepwd_success':True}))
            else:
                return render_to_response('changepwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))
        else:
            return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))

from micsite.dataconvert import  data2list

@login_required
def index(request,nodeid=0):

    limit = 6  # 每页显示的记录数
    latest_node_list = Node.objects.all()

    paginator = Paginator(latest_node_list, limit)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    turn = request.GET.get('turn')  # 获取跳转

    print 'before:',page

    if turn is not None:
        page = int(page) + int(turn)

    print 'after:',page

    try:
        latest_node_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        latest_node_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        latest_node_list = paginator.page(paginator.num_pages)  # 取最后一页的记录


    node = None

    if nodeid is not 0 :
        try:
            node = Node.objects.get(id=nodeid)

            targetHost = node.nodeip
            udpServer = UdpServer()
            data = udpServer.tcpServer(targetHost)
            node.nodeinfo = data
            node.save()

        except (KeyError, Node.DoesNotExist) :
            # Redisplay the question voting form.
            return render(request, 'index.html', {
                'latest_node_list': latest_node_list,
                'node_errors': True,

            })
        except socket.timeout :
            return render(request, 'index.html', {
                'latest_node_list': latest_node_list,
                'node_timeout': True,

            })
    if node is not None :
        cpudist, memorydist, disklistdist = data2list(node.nodeinfo)
        return render_to_response('index.html',
                                  RequestContext(request,
                                                 {'latest_node_list' : latest_node_list,
                                                  'single' : node,
                                                 'cpudist' : cpudist,
                                                 'memorydist' : memorydist,
                                                 'disklistdist' : disklistdist,}))

    return render_to_response('index.html', RequestContext(request,{'latest_node_list' : latest_node_list, 'single' : node}))




from django_ajax.decorators import ajax
def test(request):

    return render_to_response('test.html', RequestContext(request ))


from micsite.udpserver import *
def test_view(request):

    if request.method == 'POST' :
        targetHost = request.POST.get('targethost', '')
        udpServer = UdpServer()
        data = udpServer.tcpServer(targetHost)
    else :
        data = "Null"

    return render_to_response('test.html', RequestContext(request,{'ajax' : data }))
