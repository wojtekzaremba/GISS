
import csv
import os

def format_check(file) -> bool:
    '''Funkcja zwraca wartosc logiczna True w przypadku, gdy format pliku csv
     jest zgodny z wytycznymi w pozostalych przypadkach funkcja zwraca wartosc
      logiczna False '''
    state = False
    flag = 0
    firstrow = ["X","Y","Z"]
    for row in file:
        if(len(row)==4):
            print(len(row),"\n")
            state = True
        else:
            state = False
            break
        for element in row[:-1]:
            try:
                print(int(element),"\n")
                if(int(element)>=(-50000) and int(element)<=50000):
                    state = True
                else:
                    state = False
                    return state
            except ValueError:
                flag+=1
                print("Obsluzono wyjatek",element)
                if(flag>3):
                    state = False
                    return state
                else:
                    if(element != firstrow[flag-1]):
                        print(element,"dasgasdgsdg  ",row[flag-1])
                        state = False
                        return state
    return state


def norm_file(file) -> list:
    '''Funkcja normalizuje dane zawarte w pliku csv zgodnie z wytycznymi'''

    for row in range(len(file)-1):
        for i in range(len(file[row])-1):
            file[row+1][i] = int(file[row+1][i])/50000
            file[row+1][i] = str(file[row+1][i])
            #print(num_data[row][i],"\n")
            #print(type(num_data[2][2]))
    print (file)
    return file




currentdict_files = os.listdir(os.getcwd())

for file in currentdict_files:
    if file.endswith('.csv'):
        with open(file) as csvfile:
            my_file=csv.reader(csvfile,delimiter=';')
            data = list(my_file)
            checked = format_check(data)

            if checked is True:
                norm_data=norm_file(data)
            else:
                print("Format pliku jest niepoprawny")

        if checked is True:
            print("Format pliku jest poprawny!!!!!!")
            with open(file,"w") as csvfile:
                my_file=csv.writer(csvfile,delimiter=';')
                for row in norm_data:

                    my_file.writerow(row)
