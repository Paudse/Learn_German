file_name = "./Lernwortschatz_Deutsch/page_11.txt"



###
import random
from termcolor import colored
import os
os.system('color')

def test(file_name):
	with open(file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	de = []
	ch = []
	for i in range (0,len(data)):
		# print(i%3)
		# print(data[i])
		if i%3 == 0:
			de.append(data[i].replace('\n', ''))
		if i%3 == 1:
			ch.append(data[i].replace('\n', ''))

	# for j in range (0,len(de)):
		# print(de[j], ' : ',ch[j])

	not_finished = 1
	k = 0

	while not_finished:
		print('<', k+1 , '/', len(de) , '>')
		ans_num = ['1', '2']

		ans = ['', '']
		for m in range(0,2):
			r = list(range(0,k)) + list(range(k+1, 2))
			# print(r)
			ans[m] = ch[random.choice(r)]

		print(colored(de[k], 'yellow'))
		correct_ans = random.randint(0, 1)
		ans[correct_ans] = ch[k]

		for l in range (0, len(ans_num)):
			print('(', ans_num[l], ')', ans[l])

		input_ans = input('Your answer: ')

		if input_ans == str(correct_ans+1):
			print(colored('Correct!', 'green'))
			k = k + 1
		else:
			print(colored('Wrong. Try again.', 'red'))
		print('--------------------------------------')
		if k == len(de):
			not_finished = 0
			print(colored("test finished", 'blue'))

if __name__ == '__main__':
	test(file_name)




