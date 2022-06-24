from random import randint, random
from tkinter import *
from tkinter import ttk
import time

import numpy as np
import tk
from matplotlib import colors, pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


from BatAlgorithm import *
# Przekazać wartości z pól tekstowych do tej funkcji
# Zaimplementować obliczanie i wyświetlanie pomiaru czasu
from AlgorytmNietoperz import *
colors = []
populationSize =[]
i = 0
j = 0

def eggholder(X):
    # X is a np.array
    return (-(X[1] + 47) * np.sin(np.sqrt(abs(X[0] / 2 + (X[1] + 47)))) - X[0] * np.sin(
        np.sqrt(abs(X[0] - (X[1] + 47)))))

def schaffer(X):
    return (0.5 + (((np.sin((X[0] ** 2 + X[1] ** 2) ** 2) ** 2) - 0.5)/
                   ((1 + 0.001 * (X[0] ** 2 + X[1] ** 2)) ** 2)))


def DifferentialEvolution(populationSize: int, generations: int,xbound,ybound,function):
    # CONSTANTS as defined by the question
    dimensionSize = 2  # (x, y)
    bounds = [(xbound, ybound), (xbound, ybound)]
    crossoverProbability = 0.8
    K = 0.5

    generations_AvgFitness = []
    generations_GlobMinFitness = []
    generations_GlobMaxFitness = []

    # Initialize random parents
    parents = [np.array([random.uniform(bounds[j][0], bounds[j][1]) for j in range(dimensionSize)]) for i in
               range(populationSize)]

    generationNumber = 0

    while (generationNumber < generations):
        generationNumber += 1
        children = []  # The new children will be added here
        childrenmax = []
        F = random.uniform(-2.0, 2.0)  # Our F is to be randomly generated every generation

        for index, vector in enumerate(parents):
            # Remove the parent vector so that R1, R2 and R3 won't be selected as the parent vector
            pruned_parents = parents.copy()
            pruned_parents.pop(index)

            # This while loop exists only if the Vector_Trial is out of bounds (i.e. not between (-512, 512))
            while (True):
                Vector_R1, Vector_R2, Vector_R3 = random.sample(pruned_parents, 3)

                #  Mutant Vector
                Vector_Mutant = vector + K * (Vector_R1 - vector) + F * (Vector_R2 - Vector_R3)

                # Trial Vector
                Vector_Trial = np.array([0.0 for i in range(dimensionSize)])

                # Crossover
                for gene in range(dimensionSize):
                    crossoverRealtime = random.random()

                    if crossoverRealtime < crossoverProbability:
                        Vector_Trial[gene] = Vector_Mutant[gene]
                    else:
                        Vector_Trial[gene] = vector[gene]

                # Check if the Trial Vector is in bounds (i.e. between (-512, 512))
                flagInBounds = True
                for i in range(dimensionSize):
                    if not ((bounds[i][0] < Vector_Trial[i]) and (Vector_Trial[i] < bounds[i][1])):
                        flagInBounds = False
                        break

                # Elitism: Get the better vector w.r.t. fitness
                if flagInBounds:
                    if function(Vector_Trial) < function(vector):
                        children.append(Vector_Trial)
                        childrenmax.append(vector) #dodawanie do maximum
                    else:
                        children.append(vector)
                        childrenmax.append(Vector_Trial) #dodawanie do maximum
                    break


        # Calculate values for plotting
        parents_values = [(function(i), i) for i in parents]
        parents_values.sort() #sortowanie po najmniejszych
        generations_GlobMinFitness.append(parents_values[0][0]) #przypisanie najmniejszych wartości
        parents_values.sort(reverse=True) #sortowanie po najwiekszych
        generations_GlobMaxFitness.append(parents_values[0][0])#przypisanie największych wartości
        average = 0
        for child in parents_values:
            average += child[0]

        generations_AvgFitness.append(average / populationSize)

        parents = children.copy()


    # Plot
    figure = Figure(figsize=(5, 4), dpi=115)

    subplot = figure.add_subplot(111)

    subplot.plot(generations_GlobMinFitness,label="GlobalMinimum", color="red")
    subplot.plot(generations_AvgFitness,label="Avarage Minimum", color="black")
    figure.supxlabel("Generation \n| Black-GlobalMinimum|\n|Red-Avarage Minimum|",size="5")
    figure.supylabel("Fitness",size=5)
    print("\nMinimum Globalne: "+str(generations_GlobMinFitness[len(generations_GlobMinFitness) - 1]))



    canvas = FigureCanvasTkAgg(figure, master=app)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, app)
    toolbar.update()
    canvas.get_tk_widget().place(relx=0.5, rely=0.6, anchor=CENTER)


def generatePlot():

    # Start pomiaru czasu
    # Start algorytmu
    y = [i**2 for i in range(101)]
    # Koniec pomiaru czasu

    a = int(population_input.get())
    b = int(population_input.get())

    if(clicked.get() == "Algorytm Genetyczny" and clicked2.get() == "EggHolder"):
        start = time.time()
        DifferentialEvolution(a, b,-512,512,eggholder)
        end =time.time()
        print("Algorytm Genetyczny - Eggholder | Czas : "+str(end-start))
        print("Generacje: " + str(a) + "|Populacje: " + str(b))
    elif(clicked.get() == "Algorytm Genetyczny" and clicked2.get() == "SCHAFFER FUNCTION N. 2"):
        start = time.time()
        DifferentialEvolution(a,b,-100,100,schaffer)
        end =time.time()
        print("Algorytm Genetyczny - SCHAFFER FUNCTION N. 2 | Czas : "+str(end-start))
        print("Generacje: " + str(a) + "|Populacje: " + str(b))
    elif(clicked.get() == "BatAlgorithm" and clicked2.get() == "SCHAFFER FUNCTION N. 2"):
        start = time.time()
        bat(a,b,app,clicked2.get())
        end =time.time()
        print("BatAlgorithm - SCHAFFER FUNCTION N. 2 | Czas : "+str(end-start))
        print("Generacje: " + str(a) + "|Populacje: " + str(b))
    elif(clicked.get() == "BatAlgorithm" and clicked2.get() == "EggHolder"):
        start = time.time()
        bat(a,b,app,clicked2.get())
        end =time.time()
        print("BatAlgorithm - EggHolder | Czas : "+str(end-start))
        print("Generacje: " + str(a) + "|Populacje: " + str(b))



# Create window object
app = Tk()

app.title("AI Project")
app.geometry("700x800")

# OptionMenu

# Population Size
population_number = StringVar()
population_label = Label(app, text="Population Size", font=("bold", 14))
population_label.place(relx=0.5, rely=0.05, anchor=CENTER)
population_input = Entry(app, textvariable=population_number)
population_input.place(relx=0.5, rely=0.08, anchor=CENTER)

# Generation Size
generation_number = StringVar()
generation_label = Label(app, text="Generation Size", font=("bold", 14))
generation_label.place(relx=0.5, rely=0.11, anchor=CENTER)
generation_input = Entry(app, textvariable=generation_number)
generation_input.place(relx=0.5, rely=0.14, anchor=CENTER)


#ComboBox
options = ["BatAlgorithm", "Algorytm Genetyczny"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(app, clicked, *options)
drop.place(relx=0.5, rely=0.2, anchor=CENTER)

optionss = ["EggHolder", "SCHAFFER FUNCTION N. 2"]
clicked2 = StringVar()
clicked2.set(optionss[0])
drop2 = OptionMenu(app, clicked2, *optionss)
drop2.place(relx=0.5, rely=0.25, anchor=CENTER,relwidth=0.168)

#Button
generate_btn = Button(app, text="Generate", width=12, command=generatePlot)
generate_btn.place(relx=0.5, rely=0.3, anchor=CENTER)

# Start program
app.mainloop()
