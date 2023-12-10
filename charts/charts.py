import matplotlib.pyplot as plt

def generate_pie_chart():

    labels = ['Python', 'C++', 'Ruby', 'Java']
    values = [26, 24, 19, 17]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()