def fruits_sals_data(fruits,sals_data):
    import matplotlib.pyplot as plt
    import numpy as np

    pie_explode = [0.2, 0, 0, 0]
    mycolors = ["#8B5A2B", "#8B7E66", "#CDAF95", "#8B4726"]

    plt.axis("equal") #等縱橫比
    plt.pie(sals_data, labels = fruits, explode = pie_explode, colors = mycolors, shadow = True, autopct='%1.1f%%')
    plt.legend(loc='upper left')
    plt.title("The ""Four Kings"" of fruit sales in 2021")
    plt.show()
fruits_sals_data(["Pineapple", "Sakyamuni", "Wax Apple", "Mango"],[35, 25, 25, 15])