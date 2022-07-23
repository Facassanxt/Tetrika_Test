#Задача №3.
# Когда пользователь заходит на страницу урока, мы сохраняем время его захода. 
# Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), 
# мы фиксируем время выхода с урока. Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. 
# В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

# lesson – начало и конец урока
# pupil – интервалы присутствия ученика
# tutor – интервалы присутствия учителя
# Интервалы устроены следующим образом – это всегда список из четного количества элементов. 
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
# Нужно написать функцию, которая получает на вход словарь с интервалами 
# и возвращает время общего присутствия ученика и учителя на уроке (в секундах).

def markup(intervals):
    '''Маркеризация интервалов'''
    markup_segments = []
    for i, time in enumerate(intervals):
        if i % 2 == 0:
            markup_segments.append((time, 'start'))
        else:
            markup_segments.append((time, 'end'))
    return markup_segments

def removing_anomalies(intervals):
    '''Удаление аномальных интервалов'''
    filter_segments = []
    for i in range(0,len(intervals),2):
        if intervals[i][0] >= intervals[i+1][0]:
            print(f"Ошибка в интервале {i} = ({intervals[i][0]},{intervals[i+1][0]})")
        else:
            filter_segments.append(intervals[i])
            filter_segments.append(intervals[i+1])
    return filter_segments

def pooling(intervals):
    '''Объединение общих интервалов'''
    pooling_segments = []
    intervals.sort()
    cnt_start = 0
    for i in range(0,len(intervals)):
        if cnt_start == 0:
            pooling_segments.append(intervals[i])
        cnt_start = cnt_start + 1 if intervals[i][1] == 'start' else cnt_start - 1
        if cnt_start == 0:
            pooling_segments.append(intervals[i])
    return pooling_segments

def appearance(intervals):
    all_segments = []
    for segment in intervals:
        markup_segments = markup(intervals[segment])
        filter_segments = removing_anomalies(markup_segments)
        pooling_segments = pooling(filter_segments)
        print(segment,pooling_segments)
        all_segments += pooling_segments
    all_segments.sort()
    total_time = 0
    cnt_start = 0
    for i, k in enumerate(all_segments):
        cnt_start = cnt_start + 1 if k[1] == 'start' else cnt_start - 1
        if cnt_start == 3:
            total_time += all_segments[i+1][0]-k[0]
    print(total_time)
    return total_time

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [-100, 3800],
             'tutor': [100, -100, 0, 3600]},
    'answer': 3600
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [1, 2],
             'tutor': [-1, 0, 1, 2]},
    'answer': 1
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [-200, 15,-100,16,-50,17,-10,18,0,40],
             'tutor': [10000, 12000, 0, 3600]},
    'answer': 40
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
