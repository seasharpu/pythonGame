from random import randint


# Kollar om en zombie finns bakom dörren som användaren valt
def kolla_zombie_bakom_dörr(svar_dörr, antal_dörrar, zombie_dörr_lista):
    if 'Ingen Zombie' in zombie_dörr_lista[svar_dörr - 1]:
        return True
    else:
        return False


#Går igenom listan av zombies och returnerar indexen av dörren med zombien bakom.
def var_fanns_zombie(zombie_dörr_lista):
    for i in range(len(zombie_dörr_lista)):
        if zombie_dörr_lista[i] == "Zombie":
            return i + 1


# Skapar en list av zombies
def skapa_zombie_list(antal_dörrar):
    random_zombie = randint(0, antal_dörrar - 1)
    zombie_dörr_lista = []
    for i in range(antal_dörrar):  # Lägger en en zombie i en slumpmässig dörr
        if i == random_zombie:
            zombie_dörr_lista.append('Zombie')
        else:
            zombie_dörr_lista.append('Ingen Zombie')
    return zombie_dörr_lista


def kolla_svar_matte(faktor, tabell, svar_matte):
    return svar_matte == faktor * tabell


def input_valid_int(fråga, feltext, min, max):
    while True:  # Loopa tills korrekt värde skrivs in
        str = input(fråga)
        if str.isdigit():  # Bara innehåller siffror (0-9)
            svar = int(str)
            if svar >= min and svar <= max:
                return svar  # Korrekt tal, returnera värdet
            else:
                print(feltext)
                return False
        else:
            print(feltext)
            return False


def main():
    spela_igen_input = 'j'
    while spela_igen_input == 'j':
        faktor_använd = []
        antal_dörrar = 12
        antal_frågor = 12
        antal_klarade_frågor = 0
        print("Välkommen till Zombie-spelet!")
        fråga_multiplikations_tabell = 'Ange multiplikationstabell mellan 2-12: '
        tabell = input_valid_int(fråga_multiplikations_tabell,
                                                         "Inte ett giltigt nummer", 2, 12)
        while tabell == False:
            tabell = input_valid_int(fråga_multiplikations_tabell,
                                                             "Inte ett giltigt nummer", 2, 12)
        while antal_frågor > 0 and antal_frågor <= 12:  # Håller spelet i en loop så länge spelaren har frågor kvar.
            zombie_dörr_lista = skapa_zombie_list(antal_dörrar)
            # Skapar en slumpmässig faktor och kollar sedan om den redan finns i listan av använda faktorer, om så är fallet så genereras en ny faktor.
            faktor = randint(1, 12)
            while faktor in faktor_använd:
                faktor = randint(1, 12)
            faktor_använd.append(faktor)

            fråga = (f"vad blir {faktor} * {tabell}? ")
            svar_matte = int(input(fråga))
            if kolla_svar_matte(faktor, tabell, svar_matte) == True:
                print('Rätt svar!')
                if antal_dörrar < 2:
                    antal_frågor -= 1
                    antal_klarade_frågor += 1
                    print(
                            f"Du har klarat {antal_klarade_frågor} frågor och har {antal_frågor} kvar"
                    )
                if (antal_frågor < 1):
                    print("Du vann!")
                    spela_igen_input = input('Vill du spela igen? (j/n): ')
                    break
            else:
                print('Fel svar! Game over!')
                spela_igen_input = input('Vill du spela igen? (j/n): ')
                break

            if antal_frågor > 1:  # Spelet kommer använda dörr-komponenten av spelet så länge det finns mer än en fråga kvar.
                fråga_dörr = f'du kan öppna {antal_dörrar} dörrar, vilken väljer du?: '
                svar_dörr = input_valid_int(fråga_dörr, "Inte ett giltigt nummer", 1,
                                                                        antal_dörrar)
                while svar_dörr == False:
                    svar_dörr = input_valid_int(fråga_dörr, "Inte ett giltigt nummer", 1,
                                                                            antal_dörrar)

                dörr_svar = kolla_zombie_bakom_dörr(svar_dörr, antal_dörrar,
                                                                                        zombie_dörr_lista)

                if dörr_svar == True:
                    print('Rätt svar!')
                    zombie_dörr_nr = var_fanns_zombie(zombie_dörr_lista)
                    print(f"Zombien fanns bakom dörr nr: {zombie_dörr_nr} ")
                    antal_dörrar -= 1
                    antal_frågor -= 1
                    antal_klarade_frågor += 1
                    print(
                            f"Du har klarat {antal_klarade_frågor} frågor och har {antal_frågor} kvar"
                    )
                else:
                    print('Där fanns en zombie! Game over!')
                    spela_igen_input = input('Vill du spela igen? (j/n)')
                    break

    print('Tack för att du spelade!')


main()
