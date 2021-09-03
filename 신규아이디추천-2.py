
def solution(new_id):
    # step 1. 대문자 -> 소문자
    new_id = new_id.lower()
    
    # step 2. 규격 외 문자 제거
    for s in new_id:
        if s in ALPHABET or s in NUMBER or s in SPECIAL:
            continue
        else:
            new_id = new_id.replace(s, '')

    # step 3. 연속 마침표 제거
    while '..' in new_id: # '..'이 존재하지 않을 때 까지 반복, 최종적으로 1개의 '.'가 남게 된다.
        new_id = new_id.replace('..', '.')
        
    # step 4. 처음과 끝에 있는 . 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
        if len(new_id) != 0 and new_id[-1] == '.': # 처음과 끝이 모두 '.' 인 경우 처리
            new_id = new_id[:-1]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # step 5. 빈 문자열이라면 'a' 대입
    if len(new_id) == 0:
        new_id = 'a'
        
    # step 6. 16자가 넘어갈 경우 처리
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
    # step 7. 2자 이하일 경우 처리
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

    return new_id
    
new_id = input()
solution(new_id)
