n = int(input())
acceptedCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
for _ in range(n):
    countDigits = 0
    repeatCount = 1
    skip_outer = False
    card_number = input()
    if card_number[0] in ['4', '5', '6']:
        for char in card_number:
            if char in acceptedCharacters:
                if char != '-':
                    countDigits += 1
                continue
            else:
                skip_outer = True
        if skip_outer == True:
            print('Invalid')
            continue
        if countDigits != 16:
            print('Invalid')
            continue
        if '-' in card_number:
            temp_list = card_number.split('-')
            for item in temp_list:
                if len(item) == 4:
                    continue
                else:
                    skip_outer = True
                    break
            if skip_outer == True:
                print('Invalid')
                continue
            card_number = "".join(temp_list)

        for i in range(0, len(card_number)-1):
            if card_number[i] == card_number[i+1]:
                repeatCount += 1
                if repeatCount == 4:
                    skip_outer = True
                    break
            else:
                repeatCount = 1
        if skip_outer == True:
            print('Invalid')
            continue
    else:
        print('Invalid')
        continue
    print('Valid')
