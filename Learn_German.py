
folder = "./My_Wortschatz/"
file = "日常生活口語相關詞彙短語"

###
foler_file_name = folder + file + ".txt"

###
import random
from termcolor import colored
import os
os.system('color')
os.system('mode con: cols=100 lines=20')

def test(foler_file_name):
	with open(foler_file_name, "r", encoding='utf-8') as f: 
		data = f.readlines()

	de = []
	ch = []
	for i in range (0,len(data)):
		# print(i%3)
		# print(data[i])
		if i%2 == 0:
			de.append(data[i].replace('\n', ''))
		if i%2 == 1:
			ch.append(data[i].replace('\n', ''))

	# for j in range (0,len(de)):
		# print(de[j], ' : ',ch[j])

	not_finished = 1
	k = 0
	score = 0

	while not_finished:
		print('<', k+1 , '/', len(de) , '>')
		ans_num = ['1', '2']

		ans = ['', '']
		for m in range(0,2):
			r = list(range(0,k)) + list(range(k+1, 2))
			# print(r)
			ans[m] = ch[random.choice(r)]

		print(colored(de[k], 'yellow', attrs=['bold']))
		correct_ans = random.randint(0, 1)
		ans[correct_ans] = ch[k]

		for l in range (0, len(ans_num)):
			print('(', ans_num[l], ')', ans[l])

		input_ans = input('Your answer: ')

		if input_ans == str(correct_ans+1):
			print(colored('Correct!', 'green'))
			score = score + 1
			k = k + 1
		else:
			print(colored('Wrong. Try again.', 'red'))
			score = score - 1
			if not os.path.exists('./fault_record'):
				os.makedirs('./fault_record')
			with open('./fault_record/fault_' + page + ".txt", "a", encoding='utf-8') as file:
				wrong_message = de[k] + '\n' + ch[k] + '\n'
				file.write(wrong_message)

		print('--------------------------------------')
		if k == len(de):
			not_finished = 0
			if score == len(de):
				print(colored('Your score: '+ str(score)+ '/'+ str(len(de)) + '   GREAT!!!', 'green'))
			else:
				print(colored('Your score: '+ str(score)+ '/'+ str(len(de)), 'red'))
			print(colored("test finished", 'cyan'))

if __name__ == '__main__':
	test(foler_file_name)




