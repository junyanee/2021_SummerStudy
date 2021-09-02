answer = ''
new_id = input().lower()

for elem in new_id:
	if elem.isalpha() or elem.isdigit() or elem in ['-', '_', '.']:
		answer += elem
		
	while '..' in answer:
		answer = answer.replace('..', '.')
		
	if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
  if answer[-1] == '.':
    answer = answer[:-1]
    
  if answer == '':
  	answer = 'a'
  
  if len(answer) > 15:
  	answer = answer[:15]
  	if answer[-1] == '.':
  		answer = answer[:-1]
  
  while len(answer) < 3:
  	answer += answer[-1]
  	
print(answer)
