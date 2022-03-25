
import random
import string

WORD_LIST_FILENAME = "vaardi.txt"  # fails ar visiem slepenajiem vārdiem.


def lasiit_vaardus(faila_nosaukums="vaardi.txt"):
    # Nolasa failu
    print("Nolasa vārdus no faila.")
    fails = open(faila_nosaukums, 'r')

    # Izlasa vienu līniju
    liinija = fails.readline()

    # Sadala textu vietās kur ir atstarpe.
    vaardu_list = liinija.split()

    return vaardu_list


def dabuut_slepeno_vaardu(vaardu_list):
    return random.choice(vaardu_list)


def paarbauda_uzvaru(slepenais_vaards, mineetie_burti):
    uzvara = True
    for burts in slepenais_vaards:
        if burts not in mineetie_burti:
            uzvara = False
    return uzvara


def sagatavot_vaardu_drukai(slepenais_vaards, mineetie_burti):
    vaards = ""
    for burts in slepenais_vaards:
        if burts in mineetie_burti:
            vaards = vaards + burts + " "
        else:
            vaards = vaards + "_ "
    return vaards


def dabuut_nemineetos_burtus(mineeties_burti):
    alfabeets = string.ascii_lowercase
    for burts in mineeties_burti:
        if burts in alfabeets:
            alfabeets = alfabeets.replace(burts, "")
    print(alfabeets)


def paarbauda_burtu(slepenais_vaards, burts):
    return burts in slepenais_vaards


def karaatavas(vaardu_list):

    # dabūt slepeno vārdu
    slepenais_vaards = dabuut_slepeno_vaardu(vaardu_list)
    mineetie_burti = []
    dziiviibas = 6

    # spēles ievads
    print("Laipni lūgts spēlē Karātavas!")
    print("Es vēlos lai tu uzmini vārdu ar ", len(slepenais_vaards), " burtiem.")
    while True:

        # pārbauda mineejumus, iziet no loop ja dziiviibas <= 0
        if dziiviibas <= 0:
            print("\nAtvaino tev beidzās minējumi, tu zaudēji. Slepenais vārds bija: ", slepenais_vaards, end='')
            break

        # izdrukā spēles dizainu
        print("------------------------------")
        print("Tev ir palikuši", dziiviibas, "minējumi.")
        dabuut_nemineetos_burtus(mineetie_burti)
        print("Pagaidām uzminēts: ", end="")
        print(sagatavot_vaardu_drukai(slepenais_vaards, mineetie_burti), end="")
        mineejums = input("Lūdzu veic jaunu minējumu: ").lower()

        # Pārbauda spēlētāja ievadīto burtu
        if mineejums == "#":
            print("Spēle beidzās.", end='')
            break
        elif not mineejums.isalpha():
            print("Brīdinājums! Šis simbols neatbilst prasībām.")
        elif mineejums in mineetie_burti:
            print("Brīdinājums! Tu jau minēji šo burtu.")
        else:
            mineetie_burti.append(mineejums)

            # Pārbauda vai spēlētājs uzvarēja, vai pārbauda vai minējums bija pareizs.
            if paarbauda_uzvaru(slepenais_vaards, mineetie_burti):
                print("Apsveicu, tu uzvarēji, slepenais vārds bija:", slepenais_vaards)
                break
            elif paarbauda_burtu(slepenais_vaards, mineejums):
                print("Labs minējums!")
            else:
                dziiviibas -= 1
                print("Šis burts nav slepenajā vārdā.")


if __name__ == "__main__":

    # nolasa vārdus
    vaardu_list = lasiit_vaardus()

    # galvenais spēles cikls.
    while True:
        print(">>>>><<<<<")
        karaatavas(vaardu_list)
        if input("\nVai tu vēlētos spēlēt vēlreiz? [y/n] ") == "n":
            break
    print("Atā, jauku dienu!", end='')
