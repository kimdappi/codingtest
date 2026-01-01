def solution(n, w, num):
    # 상자의 위치(행, 열)를 반환하는 함수
    def get_pos(val, w):
        # 0-indexed로 계산하기 위해 1을 뺌
        row = (val - 1) // w
        col = (val - 1) % w
        
        # 짝수 행(0, 2, 4...)은 왼쪽 -> 오른쪽 (0, 1, 2...)
        # 홀수 행(1, 3, 5...)은 오른쪽 -> 왼쪽 (w-1, w-2, ... 0)
        if row % 2 == 1:
            col = (w - 1) - col
        return row, col

    target_row, target_col = get_pos(num, w)
    
    # 마지막 상자(n)의 층수를 구함
    max_row = (n - 1) // w
    
    count = 0
    # 현재 num의 층부터 마지막 층까지 확인
    for r in range(target_row, max_row + 1):
        # 해당 층(r)에서 target_col 위치에 있는 상자 번호를 역산
        # 1. 해당 층의 순서(0~w-1)를 구함
        if r % 2 == 0:
            curr_col_order = target_col
        else:
            curr_col_order = (w - 1) - target_col
            
        # 2. 상자 번호 = (층수 * 너비) + 해당 층에서의 순서 + 1
        curr_num = (r * w) + curr_col_order + 1
        
        # 계산된 상자 번호가 전체 상자 개수 n 이내라면 꺼내야 할 상자에 포함
        if curr_num <= n:
            count += 1
            
    return count