from tkinter import HIDDEN, NORMAL, Tk, Canvas
from turtle import *
import turtle
import colorsys
import time
import random
import subprocess
subprocess.check_call(['pip','install','-r','requirements.txt'])

ml = [
"What is the capital of Armenia?Yerevan,Paris,Brasília,New Delhi,Cairo",
"What is the capital of France?Paris,Yerevan,Cairo,New Delhi,Brasília",
"What is the capital of Brazil?Brasilia,Cairo,New Delhi,Paris,Yerevan",
"What is the capital of Egypt?Cairo,Yerevan,Paris,Brasília,New Delhi",
"What is the capital of India?New Delhi,Yerevan,Brasília,Cairo,Paris",
]

indexes_list = []

while len(indexes_list) < 5:
	num = random.randint(0, len(ml)-1)
	if num not in indexes_list:
		indexes_list.append(num)

tmp = []
for i in indexes_list:
	tmp.append(ml[i])

questions = {}
for line in tmp:
	q,a = line.split("?")
	questions[q] = a

cnt = 0
for q, a in questions.items():
	print(q + "?")
	tmp = a.split(",")
	correct = tmp[0]
	random.shuffle(tmp)
	#for el in tmp:
		#print(el)
	print("\n".join(tmp))
	answ = input("Please enter your answer: ")
	if answ.lower() == correct.lower():
		cnt += 1
		print("Correct. You have %d/%d" %(cnt, len(questions)))
	else:
		print("Nope. The correct answer was " + correct)
print("End of the game. You got %d/%d" %(cnt, len(questions)))


if cnt == 5:
		height = 360
		width = 360
		screen = Screen()
		screen.screensize(width, height)

		speed(0)
		bgcolor('black')
		h=0.1
		pensize(4)

		def fun():
			global h
			for i in range(4):
				c=colorsys.hsv_to_rgb(h,1,1)
				fillcolor(c)
				h+=0.004
				begin_fill()
				fd(50)
				rt(20)
				fd(40)
				rt(9)
				end_fill()
		for j in range(50):
			fun()
			goto(0,0)
			rt(10)

		turtle.penup()
		turtle.setpos(0,-410)   
		turtle.pendown()
		turtle.color('purple')
		Style = ('Courier', 50, 'italic')
		turtle.write('5/5, You Won Genius!', font=Style, align='center')
		turtle.hideturtle()
		turtle.done()
		turtle.ht()
		
elif cnt < 5:
	def toggle_eyes():
		current_color = c.itemcget(eye_left, 'fill')
		new_color = c.body_color if current_color == 'white' else 'white'
		current_state = c.itemcget(pupil_left, 'state')
		new_state = NORMAL if current_state == HIDDEN else HIDDEN
		c.itemconfigure(pupil_left, state=new_state)
		c.itemconfigure(pupil_right, state=new_state)
		c.itemconfigure(eye_left, fill=new_color)
		c.itemconfigure(eye_right, fill=new_color)

	def blink():
			toggle_eyes()
			root.after(250, toggle_eyes)
			root.after(2000, blink)

	def cheeky(event):
			hide_happy(event)
			
			return

	def show_happy(event):
			if (20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350):
				c.itemconfigure(cheek_left, state=NORMAL)
				c.itemconfigure(cheek_right, state=NORMAL)
				c.itemconfigure(mouth_happy, state=NORMAL)
				c.itemconfigure(mouth_normal, state=HIDDEN)
				c.itemconfigure(mouth_sad, state=HIDDEN)
				c.happy_level = 10
			return

	def hide_happy(event):
			c.itemconfigure(cheek_left, state=HIDDEN)
			c.itemconfigure(cheek_right, state=HIDDEN)
			c.itemconfigure(mouth_happy, state=HIDDEN)
			c.itemconfigure(mouth_normal, state=NORMAL)
			c.itemconfigure(mouth_sad, state=HIDDEN)
			return

	def sad():
			if c.happy_level == 0:
				c.itemconfigure(mouth_happy, state=HIDDEN)
				c.itemconfigure(mouth_normal, state=HIDDEN)
				c.itemconfigure(mouth_sad, state=NORMAL)
			else:
				c.happy_level -= 1
			root.after(5000, sad)

	root = Tk()
	
	c = Canvas(root, width=450, height=420)
	c.create_text(220,390,fill="red",font="Times 20 italic bold",
                        text="Oh no you failed my friend, play again", justify="center")
	c.configure(bg='DarkBlue', highlightthickness=0)
	c.body_color = 'SkyBlue'

	body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

	eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
	pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
	eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
	pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')


	mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
	mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
	mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)



	cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
	cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

	c.pack()
	c.bind('<Motion>', show_happy)
	c.bind('<Leave>', hide_happy)
	c.bind('<Double-1>', cheeky)


	c.happy_level = 10


	root.after(1000, blink)
	root.after(2000, sad)
	root.mainloop()

			







	



