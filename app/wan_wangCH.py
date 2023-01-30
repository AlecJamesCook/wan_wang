
def wanWangCH(number):

    ling = '零'
    yi = '一'
    er = '二'
    san = '三'
    si = '四'
    wu = '五'
    liu = '六'
    qi = '七'
    ba = '八'
    jiu = '九'
    shi = '十'

    bai = '百'
    qian = '千'
    wan = '万'
    yi2 = '亿'

    liang2 = '两'

    counter = 0
    result = 0

    for digit in number:

        print(counter)

        if digit == shi:
            if number[counter-1] == ling:
                result += 10
        if digit == bai:
            if number[counter-1] == ling:
                result += 100
        if digit == qian:
            if number[counter-1] == ling:
                result += 1000

        if digit == yi:
            if counter != (len(number)-1):

                if number[counter+1] == shi:
                    if (counter+2) <= (len(number)-1):
                        if number[counter+2] == wan:
                            result += (10 * 10000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == wan:
                            result += (10 * 10000)
                            counter += 1
                            continue

                    if (counter+2) <= (len(number)-1):
                        if number[counter+2] == yi2:
                            result += (10 * 100000000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == yi2:
                            result += (10 * 100000000)
                            counter += 1
                            continue
                    else:
                        result += 10

                elif number[counter+1] == bai:
                    if (counter+2) <= (len(number)-1):
                        if number[counter+2] == wan:
                            result += (100 * 10000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == wan:
                            result += (100 * 10000)
                            counter += 1
                            continue
                    if (counter+4) <= (len(number)-1):
                        if number[counter+4] == wan:
                            result += (100 * 10000)
                            counter += 1
                            continue
                    if (counter+5) <= (len(number)-1):
                        if number[counter+5] == wan:
                            result += (100 * 10000)
                            counter += 1
                            continue

                    if (counter+2) <= (len(number)-1):
                        if number[counter+2] == yi2:
                            result += (100 * 100000000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == yi2:
                            result += (100 * 100000000)
                            counter += 1
                            continue
                    if (counter+4) <= (len(number)-1):
                        if number[counter+4] == yi2:
                            result += (100 * 100000000)
                            counter += 1
                            continue
                    if (counter+5) <= (len(number)-1):
                        if number[counter+5] == yi2:
                            result += (100 * 100000000)
                            counter += 1
                            continue
                    else: 
                        result += 100

                elif number[counter+1] == qian:
                    if (counter+2) <= (len(number)-1) :
                        if number[counter+2] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue
                    if (counter+4) <= (len(number)-1):
                        if number[counter+4] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue
                    if (counter+5) <= (len(number)-1):
                       if number[counter+5] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue
                    if (counter+6) <= (len(number)-1):
                        if number[counter+6] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue
                    if (counter+7) <= (len(number)-1):
                        if number[counter+7] == wan:
                            result += (1000 * 10000)
                            counter += 1
                            continue

                    if (counter+2) <= (len(number)-1) :
                        if number[counter+2] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    if (counter+3) <= (len(number)-1):
                        if number[counter+3] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    if (counter+4) <= (len(number)-1):
                        if number[counter+4] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    if (counter+5) <= (len(number)-1):
                       if number[counter+5] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    if (counter+6) <= (len(number)-1):
                        if number[counter+6] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    if (counter+7) <= (len(number)-1):
                        if number[counter+7] == yi2:
                            result += (1000 * 100000000)
                            counter += 1
                            continue
                    else:
                        result += 1000
                        
                elif number[counter+1] == wan:
                    result += (10000)

                elif number[counter+1] == yi2:
                    result += 100000000
            else:
                result += 1

        counter += 1

        print('digit:', digit)
        print('result:', result)

    print(result)

wanWangCH('一千一百一十一亿一千一百一十一万零一百零一')