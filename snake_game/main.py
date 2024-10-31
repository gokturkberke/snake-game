from tkinter import *
import turtle
import time
import random

# Oyun ekranını ayarlama
oyun_ekrani = turtle.Screen()
oyun_ekrani.title("Snake Game")
oyun_ekrani.setup(width=1400, height=800)
oyun_ekrani.bgcolor('orange')
oyun_ekrani.tracer(0) # Ekranın sürekli güncellenmesini engellemek

yilan_kafasi = turtle.Turtle()
yilan_kafasi.speed(0)
yilan_kafasi.color('black')
yilan_kafasi.shape('circle')
yilan_kafasi.penup()
yilan_kafasi.goto(0,0)
yilan_kafasi.direction = 'stop'

yilan_hizi = 0.15
kuyruk = []
puan = 0

yem = turtle.Turtle()
yem.speed(0)
yem.color('red')
yem.shape("circle")
yem.penup()
yem.goto(0,100)
yem.shapesize(0.80,0.80)


puan_tahtasi = turtle.Turtle()
puan_tahtasi.speed(0)
puan_tahtasi.color('white')
puan_tahtasi.shape('square')
puan_tahtasi.penup()
puan_tahtasi.goto(0,350)
puan_tahtasi.hideturtle()
puan_tahtasi.write("Skor: {}".format(puan), align='center', font=("Courier", 30, 'normal'))

def hareket():
    if yilan_kafasi.direction == 'up':
        y = yilan_kafasi.ycor()
        yilan_kafasi.sety(y + 10)
    if yilan_kafasi.direction == 'down':
        y = yilan_kafasi.ycor()
        yilan_kafasi.sety(y - 10)
    if yilan_kafasi.direction == 'right':
        x = yilan_kafasi.xcor()
        yilan_kafasi.setx(x + 10)
    if yilan_kafasi.direction == 'left':
        x = yilan_kafasi.xcor()
        yilan_kafasi.setx(x - 10)

def yukari_gidis():
    if yilan_kafasi.direction != 'down':
        yilan_kafasi.direction = 'up'

def asagi_gidis():
    if yilan_kafasi.direction != 'up':
        yilan_kafasi.direction = 'down'

def saga_gidis():
    if yilan_kafasi.direction != 'left':
        yilan_kafasi.direction = 'right'

def sola_gidis():
    if yilan_kafasi.direction != 'right':
        yilan_kafasi.direction = 'left'

oyun_ekrani.listen()
oyun_ekrani.onkey(yukari_gidis, 'Up')
oyun_ekrani.onkey(asagi_gidis, 'Down')
oyun_ekrani.onkey(sola_gidis, 'Left')
oyun_ekrani.onkey(saga_gidis, 'Right')

while True:
    oyun_ekrani.update()

    if yilan_kafasi.xcor() > 700 or yilan_kafasi.xcor() < -700 or yilan_kafasi.ycor() > 400 or yilan_kafasi.ycor() < -400:
        time.sleep(1)
        yilan_kafasi.goto(0, 0)
        yilan_kafasi.direction = 'stop'

        for i in kuyruk:
            i.goto(5000, 5000)

        yilan_hizi = 0.15
        kuyruk = []
        puan_tahtasi.clear()
        puan = 0
        puan_tahtasi.write('Skor: {}'.format(puan), align='center', font=('Courier', 30, 'normal'))

    hareket()
    time.sleep(yilan_hizi)

    if yilan_kafasi.distance(yem) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        yem.goto(x, y)

        puan += 10
        puan_tahtasi.clear()
        puan_tahtasi.write('Skor: {}'.format(puan), align='center', font=('Courier', 30, 'normal'))

        yilan_hizi -= 0.01

        ek_kuyruk = turtle.Turtle()
        ek_kuyruk.speed(0)
        ek_kuyruk.shape('circle')
        ek_kuyruk.color('black')
        ek_kuyruk.penup()
        kuyruk.append(ek_kuyruk)

    for i in range(len(kuyruk) - 1, 0, -1):
        x = kuyruk[i - 1].xcor()
        y = kuyruk[i - 1].ycor()
        kuyruk[i].goto(x, y)

    if len(kuyruk) > 0:
        x = yilan_kafasi.xcor()
        y = yilan_kafasi.ycor()
        kuyruk[0].goto(x, y)
#-----------------------------------------------------------------
#chatgpt onerisi
# import turtle
# import time
# import random

# # Oyun ekranını ayarlama
# window = turtle.Screen()
# window.title("Snake Game")
# window.setup(width=1400, height=800)
# window.bgcolor('orange')
# window.tracer(0)  # Ekranın sürekli güncellenmesini engellemek

# # Yılan Başlatma
# snake_head = turtle.Turtle()
# snake_head.speed(0)
# snake_head.color('black')
# snake_head.shape('circle')
# snake_head.penup()
# snake_head.goto(0, 0)
# snake_head.direction = 'stop'

# # Oyun değişkenleri
# snake_speed = 0.15
# score = 0
# snake_body = []

# # Yem Başlatma
# food = turtle.Turtle()
# food.speed(0)
# food.color('red')
# food.shape("circle")
# food.penup()
# food.goto(0, 100)
# food.shapesize(0.80, 0.80)

# # Skor Tahtası
# score_board = turtle.Turtle()
# score_board.speed(0)
# score_board.color('white')
# score_board.penup()
# score_board.hideturtle()
# score_board.goto(0, 350)


# def update_score():
#     score_board.clear()
#     score_board.write("Score: {}".format(score), align='center', font=("Courier", 30, 'normal'))


# def move():
#     if snake_head.direction == 'up':
#         snake_head.sety(snake_head.ycor() + 20)
#     elif snake_head.direction == 'down':
#         snake_head.sety(snake_head.ycor() - 20)
#     elif snake_head.direction == 'right':
#         snake_head.setx(snake_head.xcor() + 20)
#     elif snake_head.direction == 'left':
#         snake_head.setx(snake_head.xcor() - 20)


# def go_up():
#     if snake_head.direction != 'down':
#         snake_head.direction = 'up'


# def go_down():
#     if snake_head.direction != 'up':
#         snake_head.direction = 'down'


# def go_right():
#     if snake_head.direction != 'left':
#         snake_head.direction = 'right'


# def go_left():
#     if snake_head.direction != 'right':
#         snake_head.direction = 'left'


# def check_collision():
#     global snake_speed, score, snake_body

#     # Sınır kontrolü
#     if (snake_head.xcor() > 700 or snake_head.xcor() < -700 or
#             snake_head.ycor() > 400 or snake_head.ycor() < -400):
#         reset_game()

#     # Yem ile çarpışma kontrolü
#     if snake_head.distance(food) < 20:
#         relocate_food()
#         increase_score()
#         grow_snake()


# def reset_game():
#     global snake_speed, score, snake_body
#     time.sleep(1)
#     snake_head.goto(0, 0)
#     snake_head.direction = 'stop'
#     for segment in snake_body:
#         segment.goto(5000, 5000)  # Kuyruk parçalarını ekrandan kaldırır
#     snake_body.clear()
#     snake_speed = 0.15
#     score = 0
#     update_score()


# def relocate_food():
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     food.goto(x, y)


# def increase_score():
#     global score, snake_speed
#     score += 10
#     snake_speed -= 0.01
#     update_score()


# def grow_snake():
#     new_segment = turtle.Turtle()
#     new_segment.speed(0)
#     new_segment.shape('circle')
#     new_segment.color('black')
#     new_segment.penup()
#     snake_body.append(new_segment)


# def update_snake_body():
#     # Kuyruk hareketi
#     for i in range(len(snake_body) - 1, 0, -1):
#         x = snake_body[i - 1].xcor()
#         y = snake_body[i - 1].ycor()
#         snake_body[i].goto(x, y)
#     if len(snake_body) > 0:
#         snake_body[0].goto(snake_head.xcor(), snake_head.ycor())


# # Klavye Kontrolleri
# window.listen()
# window.onkey(go_up, 'Up')
# window.onkey(go_down, 'Down')
# window.onkey(go_left, 'Left')
# window.onkey(go_right, 'Right')


# # Ana oyun döngüsü
# update_score()
# while True:
#     window.update()
#     check_collision()
#     move()
#     update_snake_body()
#     time.sleep(snake_speed)
