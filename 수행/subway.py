# 부산 지하철 환승 탐색 프로그램
# DFS(깊이 우선 탐색) + 스택 사용

graph = {
    '남포': ['서면'],
    '서면': ['남포', '시청', '대연'],
    '시청': ['서면'],
    '대연': ['서면', '해운대'],
    '해운대': ['대연'],
    '대저': ['미남'],
    '미남': ['대저', '사직', '낙민'],
    '사직': ['미남'],
    '낙민': ['미남']
}

# 방문한 역 저장
visited = []

# DFS용 스택
stack = []

# 사용자 입력
start = input("출발역 입력: ")
end = input("도착역 입력: ")

# 역 존재 여부 확인
if start not in graph or end not in graph:
    print("존재하지 않는 역입니다.")

else:

    # 시작역 스택에 추가
    stack.append(start)

    # 도착 여부 확인 변수
    found = False

    # DFS 시작
    while len(stack) > 0:

        # 스택에서 데이터 꺼내기
        current = stack.pop()

        # 방문하지 않은 역인 경우
        if current not in visited:

            # 방문 처리
            visited.append(current)

            # 도착역 확인
            if current == end:
                found = True
                break

            # 연결된 역 탐색
            for next_station in graph[current]:

                # 방문하지 않은 역만 스택에 추가
                if next_station not in visited:
                    stack.append(next_station)

    # 결과 출력
    if found:
        print(end, "역까지 이동 가능합니다.")

    else:
        print(end, "역까지 이동할 수 없습니다.")