def wan_wang(number):


    shi = '十'
    bai = '百'
    qian = '千'
    wan = '万'
    yi2 = '亿'

    CharacterDict = {
        '零':0,
        '一':1,
        '二':2,
        '两':2,
        '三':3,
        '四':4,
        '五':5,
        '六':6,
        '七':7,
        '八':8,
        '九':9,
    }

    PinyinDict = {
        '零':'líng ',
        '一':'yī ',
        '二':'èr ',
        '两':'liǎng ',
        '三':'sān ',
        '四':'sì ',
        '五':'wǔ ',
        '六':'liù ',
        '七':'qī ',
        '八':'bā ',
        '九':'jiǔ ',
        '十':'shí ',
        '百':'bǎi ',
        '千':'qiān ',
        '万':'wàn ',
        '亿':'yì '
    }

    ArabicDict = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        
    }

    def calculator(digit, number, counter):

        result = 0

        if counter != (len(number)-1):
        
            if number[counter+1] == shi:

                # WAN
                if (counter+2) <= (len(number)-1):
                    if number[counter+2] == wan:
                        result += ((digit*10) * 10000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == wan:
                        result += ((digit*10) * 10000)
                        return result

                #YI
                if (counter+2) <= (len(number)-1):
                    if number[counter+2] == yi2:
                        result += ((digit*10) * 100000000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == yi2:
                        result += ((digit*10) * 100000000)
                        return result

                #NO WAN NO YI
                else:
                    result += (digit * 10)
                    return result

            elif number[counter+1] == bai:
                
                #WAN
                if (counter+2) <= (len(number)-1):
                    if number[counter+2] == wan:
                        result += ((digit*100) * 10000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == wan:
                        result += ((digit*100) * 10000)
                        return result
                if (counter+4) <= (len(number)-1):
                    if number[counter+4] == wan:
                        result += ((digit*100) * 10000)
                        return result
                if (counter+5) <= (len(number)-1):
                    if number[counter+5] == wan:
                        result += ((digit*100) * 10000)
                        return result

                #YI
                if (counter+2) <= (len(number)-1):
                    if number[counter+2] == yi2:
                        result += ((digit*100) * 100000000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == yi2:
                        result += ((digit*100) * 100000000)
                        return result
                if (counter+4) <= (len(number)-1):
                    if number[counter+4] == yi2:
                        result += ((digit*100) * 100000000)
                        return result
                if (counter+5) <= (len(number)-1):
                    if number[counter+5] == yi2:
                        result += ((digit*100) * 100000000)
                        return result

                #NO WAN NO YI
                else: 
                    result += (digit * 100)
                    return result

            elif number[counter+1] == qian:

                #WAN
                if (counter+2) <= (len(number)-1) :
                    if number[counter+2] == wan:
                        result += ((digit*1000) * 10000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == wan:
                        result += ((digit*1000) * 10000)
                        return result
                if (counter+4) <= (len(number)-1):
                    if number[counter+4] == wan:
                        result += ((digit*1000) * 10000)
                        return result
                if (counter+5) <= (len(number)-1):
                    if number[counter+5] == wan:
                        result += ((digit*1000) * 10000)
                        return result
                if (counter+6) <= (len(number)-1):
                    if number[counter+6] == wan:
                        result += ((digit*1000) * 10000)
                        return result
                if (counter+7) <= (len(number)-1):
                    if number[counter+7] == wan:
                        result += ((digit*1000) * 10000)
                        return result

                #YI
                if (counter+2) <= (len(number)-1) :
                    if number[counter+2] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result
                if (counter+3) <= (len(number)-1):
                    if number[counter+3] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result
                if (counter+4) <= (len(number)-1):
                    if number[counter+4] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result
                if (counter+5) <= (len(number)-1):
                    if number[counter+5] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result
                if (counter+6) <= (len(number)-1):
                    if number[counter+6] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result
                if (counter+7) <= (len(number)-1):
                    if number[counter+7] == yi2:
                        result += ((digit*1000) * 100000000)
                        return result

                #NO WAN NO YI
                else:
                    result += (digit * 1000)
                    return result
                    
            elif number[counter+1] == wan:
                result += (digit * 10000)
                return result

            elif number[counter+1] == yi2:
                result += (digit * 100000000)
                return result

        if counter == (len(number)-1) and number[counter-1] == shi:
            if len(number) == 2:
                result += (digit + 10)
                return result
            if len(number) > 2 and number[counter-2] not in CharacterDict:
                result += (digit + 10)
                return result
            else:
                result += digit
                return result

    counter = 0
    total = 0

    for digit in number:

        if digit in CharacterDict:
            total += calculator(CharacterDict[digit], number, counter)

        counter += 1
    
    pinyin_result = ''

    for character in number:
        if character in PinyinDict:
            pinyin_result += PinyinDict[character]

    print(number)
    print(pinyin_result)
    print(total)
        

wan_wang('一百四十九')

