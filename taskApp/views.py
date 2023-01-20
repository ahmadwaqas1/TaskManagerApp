from django.shortcuts import render,HttpResponse,redirect
from .models import Task,User
import datetime
from datetime import datetime,date
from django.contrib.auth import login as auth_login
from accounts import views as user_account_view

# Create your views here.
is_finished = False

def index(request):
    # if request.user.is_authenticated:
    print(request.user.id)

    task_past_deadline = 0
    
    # tasks = Task.objects.all().order_by('id')
    tasks = Task.objects.all().order_by('id').filter(user_id=request.user.id)

    recent_tasks = Task.objects.order_by('-task_st_date').filter(user_id=request.user.id)[:3]

    task_count = Task.objects.all().filter(user_id=request.user.id).count()
    
    task_completed = tasks.filter(is_Finished=True)
    task_end_status = tasks.order_by('task_end_date')
    

    # task_completed = Task.objects.all().filter(is_Finished=True)
    # task_end_status = Task.objects.all().order_by('task_end_date')

        #    TASK Finished OR NOT....
        

    for items in task_end_status:
        date_ = datetime.date(items.task_end_date)
        time_ = str(datetime.time(items.task_end_date))
        time_now = str(datetime.strptime(str(time_),"%H:%M:%S").now().time())
        time_ = time_.replace(':', '')
        time_now=time_now.replace(':','')
        if date.today() > date_:
            task_past_deadline += 1
            if items.is_Finished is False:
                items.is_Finished = True
                items.save()
        elif date.today() == date_:
            if time_now >= time_:
                task_past_deadline += 1
                if items.is_Finished is False:
                    items.is_Finished = True
                    items.save()
        


    if task_count > 0:
        task_imp_valid = tasks.filter(is_Finished=False)
        task_imp_count = task_imp_valid.filter(is_important=True).count()
        task_imp_percent = (task_imp_count*100)/task_count
        task_finish_percent = (task_past_deadline*100)/task_count
        task_failed_count = tasks.filter(is_failed=True).count()

    else:
        task_count = 0
        task_imp_percent = 0
        task_finish_percent =0
        
    if task_past_deadline == 0:
        task_failed_percent = 0
    else:
        task_failed_percent = (task_failed_count * 100) / task_past_deadline

    context =   {'tasks' : tasks, 
                'recent_task' : recent_tasks,
                'task_count' : task_count,
                'task_imp_percent' : task_imp_percent, 
                'task_finish_percent' : task_finish_percent,
                'task_failed_percent' : task_failed_percent
                }
    
        
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            title = request.POST['taskname']
            discreption = request.POST['taskdiscription']
            task_end_date = request.POST['Task-DeadLine']
            important = request.POST.get('Is-Important',False)

            task_list=Task(title = title, discreption = discreption, task_end_date = task_end_date, is_important = important,
             user_id = User.objects.get(id=request.user.id))
            # print(task_list.user_id)
            
            if "submit" in request.POST:
                task_list.save()
                print("Saved...")
                return redirect('index')
            else:
                print("please login first")
                return render(request, 'index.html', context)
            
        return render(request, 'index.html', context)
    else:
        print("Please login first")
        return render(request,'index.html',context)


def detail(request,id):
    task_detail = Task.objects.get(pk=id)
    print("View called Detail!")

    if request.method == 'POST':
        title = request.POST['name']
        discreption = request.POST['discription']
        task_end_date = request.POST['date']
        important = request.POST.get('is-important',False)
        finished = request.POST.get('is-Finished',False)
        task_list_updated = Task(id = id, title = title, discreption = discreption, task_end_date = task_end_date, is_important = important,
        is_Finished=finished, user_id = User.objects.get(id=request.user.id))        

        if "submit" in request.POST:
            task_detail.delete()
            task_list_updated.save()
            print("Saved...")
            return redirect('/')

    return render(request,'taskdetail.html',{'task_detail':task_detail})

def delete(request, id):
    task_delete = Task.objects.get(pk=id)
    print("View called Deletion!")

    if request.method == 'POST':
        if "delete" in request.POST:
            task_delete.delete()
            return redirect('/')
    return redirect('/')        


def taskCompleted(request, id):
    task = Task.objects.get(pk=id)
    print("View called for Completion!")
    if request.method == "POST":
        if 'submit-yes' in request.POST:
            task.is_completed = True
            task.is_failed = False
            print("Task is completed successfully")
            task.save()
        elif 'submit-no' in request.POST:
            task.is_completed = True
            task.is_failed = True
            print("Task Failed")
            task.save()

    return redirect('/')