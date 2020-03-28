from django.shortcuts import render
from main.models import Game
import random
import time
import math

def init(request):
    return render(request, "main.html")

def create(request):
    # players_num = request.GET.get("players_num")
    name_op = request.GET.get("name")
    room_num = round(random.random() * 100)
    players = {name_op: [1, 0]}
    new_game = Game(room=room_num, status=0, op=name_op, players=str(players), record="", time=time.time())
    new_game.save()
    return render(request, "game.html", {
        "op": 1,
        "status": 0,
        "room_num": room_num,
        "name": name_op,
        "players": players,
    })

def join(request):
    room_num = request.GET.get("room_num")
    name = request.GET.get("name")
    result = Game.objects.get(room=room_num)
    players = eval(result.players)
    if name in players:
        if name == result.op:
            op = 1
        else:
            op = 0
    else:
        if result.status == 0:
            op = 0
            players[name] = [len(players) + 1, 0]
            Game.objects.filter(room=room_num).update(players=players)
        else:
            return render(request, "main.html", {"note": "游戏已开始"})
    record = result.record
    return render(request, "game.html", {
        "op": op,
        "status": result.status,
        "room_num": room_num,
        "name": name,
        "players": players,
        "record": record,
    })

def leave(request):
    room_num = request.POST.get("room_num")
    name = request.POST.get("name")
    try:
        result = Game.objects.get(room=room_num)
        players = eval(result.players)
        del players[name]
        Game.objects.filter(room=room_num).update(players=players)
    except:
        pass
    return render(request, "main.html", {"note": "已离开游戏"})

def update(request,*note):
    room_num = request.POST.get("room_num")
    name = request.POST.get("name")
    try:
        result = Game.objects.get(room=room_num)
    except:
        return render(request, "main.html",{"note": "游戏不存在"})
    try:
        note = note[0]
    except:
        note = ""
    try:
        record = eval(result.record)
    except:
        record = []
    players = eval(result.players)
    if name == result.op:
        op = 1
    else:
        op = 0
    role = players[name][1]
    try:
        secret_num = len(eval(result.secret))
    except:
        secret_num = ""
    return render(request, "game.html", {
        "op": op,
        "status": result.status,
        "room_num": room_num,
        "name": name,
        "players": players,
        "record": record,
        "note": note,
        "role": role,
        "secret_num": secret_num,
    })

def start(request):
    room_num = request.POST.get("room_num")
    name = request.POST.get("name")
    result = Game.objects.get(room=room_num)
    players = eval(result.players)
    players_num = len(players)
    if players_num in range(5,11):
        bad = math.ceil(players_num / 3)
        good = players_num - bad
        order_list = list(range(1, players_num + 1))
        random.shuffle(order_list)
        role_list = [1 for i in range(good)] + [2 for i in range(bad)]
        random.shuffle(role_list)
        print(order_list,role_list)
        for i in range(0,players_num):
            players[list(players.keys())[i]] = [order_list[i], role_list[i]]
        if players_num ==5:
            mode = [2, 3, 2, 3, 3]
        elif players_num ==6:
            mode = [2, 3, 4, 3, 4]
        elif players_num == 7:
            mode = [2, 3, 3, -4, 4]
        else:
            mode = [3, 4, 4, -5, 5]
        record = [f"游戏开始，{players_num}人局,任务成功需要{str(mode)}"]
        mode.append([])
        mode.append([])
        Game.objects.filter(room=room_num).update(status=1, players=str(players), mission=str(mode), record=str(record))
        role = players[name][1]
        return render(request, "game.html", {
            "op": 1,
            "status": 1,
            "room_num": room_num,
            "name": name,
            "players": players,
            "record": record,
            "note": "游戏已开始",
            "role": role,
        })
    else:
        return update(request, "游戏人数要在5-10之间")

def delete(request):
    Game.objects.filter(room=request.POST.get("room_num")).delete()
    return render(request, "main.html",{"note": "游戏已删除"})

def vote(request,choice):
    note="投票成功"
    room_num = request.POST.get("room_num")
    name = request.POST.get("name")
    try:
        result = Game.objects.get(room=room_num)
    except:
        return render(request, "main.html",{"note": "游戏不存在"})
    try:
        record = eval(result.record)
    except:
        record = []
    status = result.status
    players = eval(result.players)
    mission = eval(result.mission)
    if name == result.op:
        op = 1
    else:
        op = 0
    role = players[name][1]
    print(mission)
    if name not in mission[5] + mission[6]:
        print(123)
        if choice == 0:
            mission[6].append(name)
        else:
            mission[5].append(name)
    else:
        note = "你投过票了喂!"
    if len(mission[5])+len(mission[6]) == abs(mission[status-1]):
        if mission[status-1]>0:
            if len(mission[6])>0:
                record.append(f"第{status}轮任务失败，{mission[status-1]}人投票，{len(mission[6])}失败票")
            else:
                record.append(f"第{status}轮任务成功，{mission[status - 1]}人投票,{len(mission[6])}失败票")
        elif mission[status-1]<0:
            if len(mission[6])>1:
                record.append(f"第{status}轮任务失败，{-mission[status-1]}人投票，{len(mission[6])}失败票")
            else:
                record.append(f"第{status}轮任务成功，{-mission[status - 1]}人投票,{len(mission[6])}失败票")
        if status == 5:
            record.append("游戏结束")
        else:
            status += 1
        mission[5] = []
        mission[6] = []
    Game.objects.filter(room=room_num).update(status=status, mission=str(mission), record=str(record))
    return render(request, "game.html", {
        "op": op,
        "status": result.status,
        "room_num": room_num,
        "name": name,
        "players": players,
        "record": record,
        "note": note,
        "role": role,
    })

def secret(request,reset):
    note="秘密投票成功"
    room_num = request.POST.get("room_num")
    name = request.POST.get("name")
    try:
        result = Game.objects.get(room=room_num)
    except:
        return render(request, "main.html",{"note": "游戏不存在"})
    players = eval(result.players)
    if name == result.op:
        op = 1
    else:
        op = 0
    role = players[name][1]
    try:
        record = eval(result.record)
    except:
        record = []
    if reset == 0:
        try:
            secret = eval(result.secret)
        except:
            secret = []
        if name not in secret:
            secret.append(name)
            Game.objects.filter(room=room_num).update(secret=str(secret))
        else:
            note="你投过票了啊！"
    elif reset ==1:
        Game.objects.filter(room=room_num).update(secret="")
        note = "秘密投票重置成功"

    return render(request, "game.html", {
        "op": op,
        "status": result.status,
        "room_num": room_num,
        "name": name,
        "players": players,
        "record": record,
        "note": note,
        "role": role,
    })