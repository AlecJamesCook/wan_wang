def wanWang(input):

    number = str(input)
    result = ''
    counter = 0

    zero = 'líng'
    one = 'yī'
    two = 'èr'
    three = 'sān'
    four = 'sì'
    five = 'wǔ'
    six = 'liù'
    seven = 'qī'
    eight = 'bā'
    nine = 'jiǔ'
    ten = 'shí'

    hundred = 'bǎi'
    thousand = 'qiān'
    ten_thousand = 'wàn'
    hundred_million = 'yì'

    # SPECIAL NUMBERS
    liang = 'liǎng'

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
    # BIGGEST = 1
    ### ONE DIGIT ###

    if len(number) == 1:

        for digit in number:
            
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                result += zero + ' '

    # BIGGEST = 10
    ### TWO DIGITS ###

    if len(number) == 2:

        for digit in number:
            if digit == '1':
                if counter == 0:
                    result += ten + ' '
                    counter += 1
                    continue
                else:
                    result += one + ' '
            elif digit == '2':
                result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                continue
            
            if counter == 0:
                result += ten + ' '
            counter += 1

    # BIGGEST = 100
    ### THREE DIGITS ### 

    if len(number) == 3:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter != 2 and number[counter + 1] != '0':
                        result += zero + ' '
                else:
                    counter += 1
                    continue

            if counter == 0:
                result += hundred + ' '
            if counter == 1 and digit != '0':
                result += ten + ' '
            counter += 1

    # BIGGEST = 1000
    ### FOUR DIGITS ### 

    if len(number) == 4:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                if counter == 0:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter != 3 and number[counter + 1] != '0':
                    result += zero + ' '
                else:
                    counter += 1
                    continue
            
            if counter == 0:
                result += thousand + ' '
            if counter == 1 and digit != '0':
                result += hundred + ' '
            if counter == 2 and digit != '0':
                result += ten + ' '
            counter += 1

    ### FIVE DIGITS ### 

    # BIGGEST = 1, 0000
    if len(number) == 5:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                if counter == 1:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter != 4 and number[counter + 1] != '0':
                        result += zero + ' '
                else:
                    counter += 1
                    continue

            if counter == 0:
                result += ten_thousand + ' '
            if counter == 1 and digit != '0':
                result += thousand + ' '
            if counter == 2 and digit != '0':
                result += hundred + ' '
            if counter == 3 and digit != '0':
                result += ten + ' '
            counter += 1

    ### SIX DIGITS ### 

    # BIGGEST = 10, 0000
    if len(number) == 6:

        for digit in number:
            if digit == '1':
                if counter == 0:
                    result += ten + ' '
                    counter += 1
                    continue
                else:
                    result += one + ' '
            elif digit == '2':
                if counter == 2:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 1:
                    result += ten_thousand + ' '
                    counter += 1
                    continue
                elif counter != 5 and number[counter + 1] != '0':
                        result += zero + ' '
                else:
                    counter += 1
                    continue
            
            if counter == 0 and digit != '1':
                result += ten + ' '
            if counter == 1:
                result += ten_thousand + ' '
            if counter == 2 and digit != '0':
                result += thousand + ' '
            if counter == 3 and digit != '0':
                result += hundred + ' '
            if counter == 4 and digit != '0':
                result += ten + ' '
            counter += 1
    
    ### SEVEN DIGITS ### 

    # BIGGEST = 100, 0000
    if len(number) == 7:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                if counter == 3:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 2:
                    result += ten_thousand + ' '
                    counter += 1
                    continue
                if counter != 6 and number[counter + 1] != '0':
                        result += zero + ' '
                else:
                    counter += 1
                    continue

            if counter == 0:
                result += hundred + ' '
            if counter == 1 and digit != '0':
                result += ten + ' '
            if counter == 2:
                result += ten_thousand + ' '
            if counter == 3 and digit != '0':
                result += thousand + ' '
            if counter == 4 and digit != '0':
                result += hundred + ' '
            if counter == 5 and digit != '0':
                result += ten
            
            counter += 1

    ### eight  DIGITS ### 

    # BIGGEST = 1000, 0000
    if len(number) == 8:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                if counter == 0 or counter == 4:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 3:
                    result += ten_thousand + ' '
                    counter += 1
                    continue
                if counter != 7 and number[counter + 1] != '0':
                        result += zero + ' '
                else:
                    counter += 1
                    continue
            
            if counter == 0:
                result += thousand + ' '
            if counter == 1 and digit != '0':
                result += hundred + ' '
            if counter == 2 and digit != '0':
                result += ten + ' '
            if counter == 3:
                result += ten_thousand + ' '
            if counter == 4 and digit != '0':
                result += thousand + ' '
            if counter == 5 and digit != '0':
                result += hundred + ' '
            if counter == 6 and digit != '0':
                result += ten + ' '
            
            counter += 1

    
    ### NINE DIGITS ###  
    # BIGGEST = 1, 0000, 0000 
    if len(number) == 9:

        for digit in number:
            if digit == '1':
                result += one + ' '
            elif digit == '2':
                if counter == 1 or counter == 5:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 1:
                    pass
                elif counter == 2 and number[2] != '0':
                    pass
                elif counter == 4:
                    pass
                elif counter != 8 and number[counter + 1] != '0':
                    result += zero + ' '
            
            if counter == 0:
                result += hundred_million + ' '
            if counter == 1 and digit != '0':
                result += thousand + ' '
            if counter == 2 and digit != '0':
                result += hundred + ' '
            if counter == 3 and digit != '0':
                result += ten + ' '

            if counter == 4 and digit != '0':
                result += ten_thousand + ' '
            elif counter == 4 and number[1] != '0':
                result += ten_thousand + ' '
            elif counter == 4 and number[2] != '0':
                result += ten_thousand + ' '
            elif counter == 4 and number[3] != '0':
                result += ten_thousand + ' '

            if counter == 5 and digit != '0':
                result += thousand + ' '
            if counter == 6 and digit != '0':
                result += hundred + ' '
            if counter == 7 and digit != '0':
                result += ten + ' '
    
            counter += 1
            
    ### 10 DIGITS ###  
    # BIGGEST = 10, 0000, 0000 
    if len(number) == 10:

        for digit in number:
            if digit == '1':
                if counter == 0:
                    result += ten + ' '
                    counter += 1
                    continue
                else:
                    result += one + ' '
            elif digit == '2':
                if counter == 2 or counter == 6:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 2:
                    pass
                elif counter == 3 and number[3] != '0':
                    pass
                elif counter == 5:
                    pass
                elif counter != 9 and number[counter + 1] != '0':
                    result += zero + ' '
            
            if counter == 0 and digit != '1':
                result += ten + ' '
            if counter == 1:
                result += hundred_million + ' '
            if counter == 2 and digit != '0':
                result += thousand + ' '
            if counter == 3 and digit != '0':
                result += hundred + ' '
            if counter == 4 and digit != '0':
                result += ten + ' '

            if counter == 5 and digit != '0':
                result += ten_thousand + ' '
            elif counter == 5 and number[2] != '0':
                result += ten_thousand + ' '
            elif counter == 5 and number[3] != '0':
                result += ten_thousand + ' '
            elif counter == 5 and number[4] != '0':
                result += ten_thousand + ' '

            if counter == 6 and digit != '0':
                result += thousand + ' '
            if counter == 7 and digit != '0':
                result += hundred + ' '
            if counter == 8 and digit != '0':
                result += ten + ' '

            counter += 1

    ### 11 DIGITS ###  
    # BIGGEST = 100, 0000, 0000 
    if len(number) == 11:

        for digit in number:
            if digit == '1':
                    result += one + ' '
            elif digit == '2':
                if counter == 3 or counter == 7:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 2:
                    result += hundred_million + ' '
                    counter += 1
                    continue
                if counter == 3:
                    pass
                elif counter == 4 and number[4] != '0':
                    pass
                elif counter == 6:
                    pass
                elif counter != 10 and number[counter + 1] != '0':
                    result += zero + ' '
            
            if counter == 0: 
                result += hundred + ' '
            if counter == 1 and digit != '0':
                result += ten + ' '
            if counter == 2:
                result += hundred_million + ' '
            if counter == 3 and digit != '0':
                result += thousand + ' '
            if counter == 4 and digit != '0':
                result += hundred + ' '
            if counter == 5 and digit != '0':
                result += ten + ' '

            if counter == 6 and digit != '0':
                result += ten_thousand + ' '
            elif counter == 6 and number[3] != '0':
                result += ten_thousand + ' '
            elif counter == 6 and number[4] != '0':
                result += ten_thousand + ' '
            elif counter == 6 and number[5] != '0':
                result += ten_thousand + ' '

            if counter == 7 and digit != '0':
                result += thousand + ' '
            if counter == 8 and digit != '0':
                result += hundred + ' '
            if counter == 9 and digit != '0':
                result += ten + ' '

            counter += 1

    ### 12 DIGITS ###  
    # BIGGEST = 1000, 0000, 0000 
    if len(number) == 12:

        for digit in number:
            if digit == '1':
                    result += one + ' '
            elif digit == '2':
                if counter == 0 or counter == 4 or counter == 8:
                    result += liang + ' '
                else:
                    result += two + ' '
            elif digit == '3':
                result += three + ' '
            elif digit == '4':
                result += four + ' '
            elif digit == '5':
                result += five + ' '
            elif digit == '6':
                result += six + ' '
            elif digit == '7':
                result += seven + ' '
            elif digit == '8':
                result += eight + ' '
            elif digit == '9':
                result += nine + ' '
            elif digit == '0':
                if counter == 3:
                    result += hundred_million + ' '
                    counter += 1
                    continue
                if counter == 4:
                    pass
                elif counter == 5 and number[5] != '0':
                    pass
                elif counter == 7:
                    pass
                elif counter != 11 and number[counter + 1] != '0':
                    result += zero + ' '
            
            if counter == 0:
                result += thousand + ' '
            if counter == 1 and digit != '0':
                result += hundred + ' '
            if counter == 2 and digit != '0':
                result += ten + ' '
            if counter == 3:
                result += hundred_million + ' '
            if counter == 4 and digit != '0':
                result += thousand + ' '
            if counter == 5 and digit != '0':
                result += hundred + ' '
            if counter == 6 and digit != '0':
                result += ten + ' '

            if counter == 7 and digit != '0':
                result += ten_thousand + ' '
            elif counter == 7 and number[4] != '0':
                result += ten_thousand + ' '
            elif counter == 7 and number[5] != '0':
                result += ten_thousand + ' '
            elif counter == 7 and number[6] != '0':
                result += ten_thousand + ' '

            if counter == 8 and digit != '0':
                result += thousand + ' '
            if counter == 9 and digit != '0':
                result += hundred + ' '
            if counter == 10 and digit != '0':
                result += ten + ' '

            counter += 1


    resultList = result.split()
    CharacterResult = ''

    for element in resultList:
        if element == 'líng':
            CharacterResult += ling
        if element == 'yī':
            CharacterResult += yi
        if element == 'èr':
            CharacterResult += er
        if element == 'sān':
            CharacterResult += san
        if element == 'sì':
            CharacterResult += si
        if element == 'wǔ':
            CharacterResult += wu
        if element == 'liù':
            CharacterResult += liu
        if element == 'qī':
            CharacterResult += qi
        if element == 'bā':
            CharacterResult += ba   
        if element == 'jiǔ':
            CharacterResult += jiu      
        if element == 'shí':
            CharacterResult += shi

        if element == 'bǎi':
            CharacterResult += bai
        if element == 'qiān':
            CharacterResult += qian
        if element == 'wàn':
            CharacterResult += wan
        if element == 'yì':
            CharacterResult += yi2
        
        if element == 'liǎng':
            CharacterResult += liang2

    resultTuple = (number, result, CharacterResult)
    return resultTuple
