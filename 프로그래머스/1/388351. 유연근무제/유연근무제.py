def solution(schedules, timelogs, startday):
    answer = 0
    
    # 1. 출근 인정 시각 계산 함수
    def get_limit_time(schedule):
        hh = schedule // 100
        mm = schedule % 100
        
        mm += 10
        if mm >= 60:
            hh += 1
            mm -= 60
            
        return hh * 100 + mm

    # 2. 각 직원별로 루프
    for i in range(len(schedules)):
        limit_time = get_limit_time(schedules[i])
        is_winner = True
        
        # 3. 7일간의 출근 기록 확인
        for day_idx in range(7):
            # 현재 기록된 날의 요일 계산 (1: 월, ..., 6: 토, 7: 일)
            # startday에서 day_idx만큼 지난 후의 요일
            current_day = (startday + day_idx - 1) % 7 + 1
            
            # 주말(토요일 6, 일요일 7)은 체크하지 않음
            if current_day >= 6:
                continue
            
            # 평일인데 출근 인정 시각을 넘겼다면 탈락
            if timelogs[i][day_idx] > limit_time:
                is_winner = False
                break
        
        if is_winner:
            answer += 1
            
    return answer