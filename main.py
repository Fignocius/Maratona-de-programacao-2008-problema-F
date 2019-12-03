def scanner(n, magnitudes):
    magnitudes.append(magnitudes[0])
    magnitudes.append(magnitudes[1])

    if n > 0:
        count = 0
        key = 2
        #print(magnitudes)
        while key < len(magnitudes):
            dir_anterior = magnitudes[key - 1] - magnitudes[key - 2]
            #print("dir_anterior", dir_anterior)
            anterior = magnitudes[key - 1]
            dir_atual = magnitudes[key] - anterior
            #print("dir_atual", dir_atual)
            if dir_atual * dir_anterior < 0:
                count += 1
            #print("count", count)
            key += 1

        return count
    else:
        return False


#n = int(input("Amostras "))
#magnitudes = list(map(int, input("Valores ").split()))
#print(scanner(n, magnitudes))

