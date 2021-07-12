from django.shortcuts import render
from app.models import Question1, Question2, Question3, Question4, Question5
import json


def base(request):
    return render(request, 'admin/base.html')


def start(request):
    return render(request, 'app/start.html')


def q1(request):
    return render(request, 'app/questions/q1.html')


def q2(request):
    return render(request, 'app/questions/q2.html')


def q3(request):
    return render(request, 'app/questions/q3.html')


def q4(request):
    return render(request, 'app/questions/q4.html')


def q5(request):
    return render(request, 'app/questions/q5.html')


def q1_post(request):
    if request.method == 'POST':
        q1_result(request).save()
        return render(request, 'app/questions/q2.html')


def q2_post(request):
    if request.method == 'POST':
        q2_result(request).save()
        return render(request, "app/questions/q3.html")


def q3_post(request):
    if request.method == 'POST':
        q3_result(request).save()
        return render(request, "app/questions/q4.html")


def q4_post(request):
    if request.method == 'POST':
        q4_result(request).save()
        return render(request, "app/questions/q5.html")


def q5_post(request):
    if request.method == 'POST':
        userid = request.user.id
        q5_result(request).save()
        result1 = Question1.objects.values().filter(userid=userid).last()["q1_result1"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result1"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result1"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result1"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result1"]
        result2 = Question1.objects.values().filter(userid=userid).last()["q1_result2"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result2"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result2"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result2"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result2"]
        result3 = Question1.objects.values().filter(userid=userid).last()["q1_result3"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result3"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result3"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result3"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result3"]
        result4 = Question1.objects.values().filter(userid=userid).last()["q1_result4"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result4"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result4"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result4"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result4"]
        result5 = Question1.objects.values().filter(userid=userid).last()["q1_result5"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result5"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result5"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result5"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result5"]
        result_response = {
            "result1": result1,
            "result2": result2,
            "result3": result3,
            "result4": result4,
            "result5": result5
        }
        return render(request, "app/chart.html", {'result_response': json.dumps(result_response)})


def chart(request):
    userid = request.user.id
    if userid == Question1.objects.values().filter(userid=userid).last()['userid']:
        result1 = Question1.objects.values().filter(userid=userid).last()["q1_result1"] + \
              Question2.objects.values().filter(userid=userid).last()["q2_result1"] + \
              Question3.objects.values().filter(userid=userid).last()["q3_result1"] + \
              Question4.objects.values().filter(userid=userid).last()["q4_result1"] + \
              Question5.objects.values().filter(userid=userid).last()["q5_result1"]
        result2 = Question1.objects.values().filter(userid=userid).last()["q1_result2"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result2"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result2"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result2"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result2"]
        result3 = Question1.objects.values().filter(userid=userid).last()["q1_result3"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result3"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result3"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result3"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result3"]
        result4 = Question1.objects.values().filter(userid=userid).last()["q1_result4"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result4"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result4"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result4"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result4"]
        result5 = Question1.objects.values().filter(userid=userid).last()["q1_result5"] + \
            Question2.objects.values().filter(userid=userid).last()["q2_result5"] + \
            Question3.objects.values().filter(userid=userid).last()["q3_result5"] + \
            Question4.objects.values().filter(userid=userid).last()["q4_result5"] + \
            Question5.objects.values().filter(userid=userid).last()["q5_result5"]
        result_response = {
            "result1": result1,
            "result2": result2,
            "result3": result3,
            "result4": result4,
            "result5": result5
        }
        return render(request, 'app/chart.html', {'result_response': json.dumps(result_response)})
    else:
        return render(request, 'app/new.html')


def q1_result(request):
    userid = request.user.id
    if 'button1' in request.POST:
        result_list = [1, 1, 1, 0, 0]
    if 'button2' in request.POST:
        result_list = [0, 1, 1, 1, 0]
    if 'button3' in request.POST:
        result_list = [0, 0, 1, 1, 1]
    if 'button4' in request.POST:
        result_list = [1, 0, 0, 1, 1]
    if 'button5' in request.POST:
        result_list = [1, 1, 0, 0, 1]
    result = Question1(userid=userid, q1_result1=result_list[0], q1_result2=result_list[1], q1_result3=result_list[2],
                       q1_result4=result_list[3], q1_result5=result_list[4])
    return result


def q2_result(request):
    userid = request.user.id
    if 'button1' in request.POST:
        result_list = [1, 1, 1, 0, 0]
    if 'button2' in request.POST:
        result_list = [0, 1, 1, 1, 0]
    if 'button3' in request.POST:
        result_list = [0, 0, 1, 1, 1]
    if 'button4' in request.POST:
        result_list = [1, 0, 0, 1, 1]
    if 'button5' in request.POST:
        result_list = [1, 1, 0, 0, 1]
    result = Question2(userid=userid, q2_result1=result_list[0], q2_result2=result_list[1], q2_result3=result_list[2],
                       q2_result4=result_list[3], q2_result5=result_list[4])
    return result


def q3_result(request):
    userid = request.user.id
    if 'button1' in request.POST:
        result_list = [1, 1, 1, 0, 0]
    if 'button2' in request.POST:
        result_list = [0, 1, 1, 1, 0]
    if 'button3' in request.POST:
        result_list = [0, 0, 1, 1, 1]
    if 'button4' in request.POST:
        result_list = [1, 0, 0, 1, 1]
    if 'button5' in request.POST:
        result_list = [1, 1, 0, 0, 1]
    result = Question3(userid=userid, q3_result1=result_list[0], q3_result2=result_list[1], q3_result3=result_list[2],
                       q3_result4=result_list[3], q3_result5=result_list[4])
    return result


def q4_result(request):
    userid = request.user.id
    if 'button1' in request.POST:
        result_list = [1, 1, 1, 0, 0]
    if 'button2' in request.POST:
        result_list = [0, 1, 1, 1, 0]
    if 'button3' in request.POST:
        result_list = [0, 0, 1, 1, 1]
    if 'button4' in request.POST:
        result_list = [1, 0, 0, 1, 1]
    if 'button5' in request.POST:
        result_list = [1, 1, 0, 0, 1]
    result = Question4(userid=userid, q4_result1=result_list[0], q4_result2=result_list[1], q4_result3=result_list[2],
                       q4_result4=result_list[3], q4_result5=result_list[4])
    return result


def q5_result(request):
    userid = request.user.id
    if 'button1' in request.POST:
        result_list = [1, 1, 1, 0, 0]
    if 'button2' in request.POST:
        result_list = [0, 1, 1, 1, 0]
    if 'button3' in request.POST:
        result_list = [0, 0, 1, 1, 1]
    if 'button4' in request.POST:
        result_list = [1, 0, 0, 1, 1]
    if 'button5' in request.POST:
        result_list = [1, 1, 0, 0, 1]
    result = Question5(userid=userid, q5_result1=result_list[0], q5_result2=result_list[1], q5_result3=result_list[2],
                       q5_result4=result_list[3], q5_result5=result_list[4])
    return result
