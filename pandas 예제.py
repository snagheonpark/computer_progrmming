import pandas as pd

#데이터 프레임 샘플

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}
print('일반')
print(pd.DataFrame(data))
print('----------------------------')
print('프레임 컬럼 순서 변경')
print(pd.DataFrame(data, columns = ['성적', '학번']))
print('----------------------------')
print('프레임 인덱스 나열 변경')
print(pd.DataFrame(data, columns = ['성적', '학번'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))
print('행렬 변환')
print(pd.DataFrame(data, columns = ['성적', '학번'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']).transpose()) # or .T

#데이터 통계

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}

# 주요 통계 지표
frame = pd.DataFrame(data)
print(frame.describe())
print('---------------------------')
# 데이터 구조
print(frame.info())
print('---------------------------')
# 중복 제거
print(frame['성적'].unique())
print('---------------------------')
# Group by
print(frame['성적'].value_counts())

#데이터 정렬

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}

frame = pd.DataFrame(data)
print(frame.sort_values(by = ['성적'], ascending = True))
print('---------------------------')
# 인덱스 선택
print(frame.sort_values(by = ['성적'], ascending = True).iloc[2])
print('---------------------------')
# 조건에 따른 필터
print(frame[frame['성적'] > 80])
print('---------------------------')
# 필터의 유니크 체이닝
print(frame[frame['성적'] > 80]['성적'].unique())
print('---------------------------')
# 최대값, 평균값
print(frame['성적'].max())
print(frame['성적'].argmax())
print('---------------------------')
# 삭제 - 로우인 경우 기본설정
print(frame.drop(0))
print('---------------------------')
# 삭제 - 컬럼명인 경우 axis = 1 필요
print(frame.drop(['성적'], axis = 1))
print('---------------------------')
# 삭제 - 완전삭제의 경우 inplace = True 필요
print(frame.drop(['성적'], axis = 1, inplace = True))

#데이터 연산

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}
frame = pd.DataFrame(data)
# 산술 연산
print(frame['성적'] + 4)
print('---------------------------')
# 산술 연산 - 컬럼 생성
frame['합계'] = frame['학번'] + frame['성적']
print(frame)
frame['평균'] = frame['합계'].mean()
print(frame)
print('---------------------------')

#데이터 샘플링

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]
}
frame = pd.DataFrame(data)

# 샘플링 - 전체 데이터중 일부 추출
print(frame.sample(n = 4))
print('---------------------------')
# 샘플링 - 전체 데이터중 일부 비율 추출 ( 10% )
# 복원 추출을 할 경우 ( frac 1이상 인경우 ) replace = True 추가
print(frame.sample(frac = 0.1))
print('---------------------------')
print(frame.sample(frac = 2, replace = True))
# 샘플링 - 가중치 부여 ( 성적이 높은 로우가 비교적 샘플링 대상 )
print(frame.sample(frac = 0.2, weights = '성적'))
print('---------------------------')
# 샘플링 - 열기준 추출
print(frame.sample(n = 1, axis = 1))

#원핫인코딩 :prefix에 설정된 문자열을 제외한 숫자형태의 값을 숫자형으로 변경 이후, 새로이 통계 데이터를 생성

data = {
   '노선' : ['1호선', '2호선', '5호선', '1호선', '1호선', '5호선', '2호선']
}
frame = pd.DataFrame(data)
print(pd.get_dummies(frame['노선'], prefix = '노선'))

#결측치 처리

data = {
    '학번' : range(2000, 2010)
    , '성적' : [85, None, 75, 70, None, 100, None, 85, 80, 85]
}
frame = pd.DataFrame(data)
print(frame)
print('---------------------------')
# None 데이터 체크
print(frame.isna())
print('---------------------------')
# None 데이터 개수
print(frame.isna().sum())
print('---------------------------')
# 결측치 데이터 치환
print(frame.fillna(0))
# 결측치 데이터 치환 반영 안되어 있음
print(frame)
# 결측치 데이터 치환 실 반영
frame['성적'].fillna(0, inplace = True)
# 결측치 데이터 치환 반영 되어 있음
print(frame)



