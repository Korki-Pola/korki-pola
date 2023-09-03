def sito_arystotelesa():
    try: 
        user_input = int(input('Podaj zasieg do przeszukania: '))
        
        lista = [x for x in range(user_input + 1)]
    
        if len(lista) >= 2:
            lista[0] = None
            lista[1] = None
            
            def mapuj_do_none(num, elem):
                if num != None and num % elem == 0 and num != elem:
                    return None
                else:
                    return num

            for elem in lista:
                if elem != None:
                    lista = list(map(lambda num: mapuj_do_none(num, elem), lista))
                    
        print(list(filter(lambda elem: elem != None, lista)))
        
    except ValueError:
        print('Zla wartosc - pierdol sie')


if __name__ == '__main__':
    # sito_arystotelesa()
    pass

    

    
