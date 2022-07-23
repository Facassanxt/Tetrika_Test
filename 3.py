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
    markup_segments = []
    for segment in intervals:
        for i, time in enumerate(intervals[segment]):
            if i % 2 == 0:
                markup_segments.append((time, 'start'))
            else:
                markup_segments.append((time, 'end'))
    return markup_segments

def removing_anomalies(intervals):
    filter_segments = []
    for i in range(0,len(intervals),2):
        if intervals[i][0] >= intervals[i+1][0]:
            print(f"Ошибка в интервале ({i}) и ({i+1})")
        else:
            filter_segments.append(intervals[i])
            filter_segments.append(intervals[i+1])
    return filter_segments

def pooling(intervals):
    all_segments = []
    return all_segments

def appearance(intervals):
    markup_segments = markup(intervals)
    filter_segments = removing_anomalies(markup_segments)
    # all_segments = pooling(filter_segments)
    all_segments = filter_segments
    filter_segments.sort()
    total_time = 0
    cnt_start = 0
    s = ""
    for i, k in enumerate(all_segments):
        if k[1] == 'start':
            s += "( "
            cnt_start += 1
        else:
            s += ") "
            cnt_start -= 1
        if cnt_start == 3:
            total_time += all_segments[i+1][0]-k[0]
    print(s)
    print(total_time)
    return total_time
    
tests = [
    {'data': {'lesson': [0, 3600],
            'pupil': [140, 189, 190, 195, 196, 3272],
            'tutor': [90, 230, 243, 3273]},
    'answer': 3117
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [-11, 1700, 7, 1742, 1712, 1713, 1764, 2350, 1789, 1782, 1934, 2209, 2295, 2296, 2306, 3680, 2358, 2973, 3049, 3680, 3700, 4075, 3702, 3703, 3724, 3724, 3779, 3841],
             'tutor': [-2765, -2436, -51, 2348, 2349, 3663]},
    'answer': 3577
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [-11, 1742, 1764, 1782, 1789, 3680],
             'tutor': [-2765, -2436, -51, 2348, 2349, 3663]},
    'answer': 3577
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [-11, 1742, 1764, 3680, 3700, 4075],
             'tutor': [-2765, -2436, -51, 2348, 2349, 3663]},
    'answer': 3577
    },
    {'data': {'lesson': [0, 3600],
             'pupil': [33, 4347],
             'tutor': [17, 66, 68, 4341]},
    'answer': 3565
    },
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
]

if __name__ == '__main__':
    appearance(tests[1]['data'])
    # for i, test in enumerate(tests):
    #     test_answer = appearance(test['data'])
    #     assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
