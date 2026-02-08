import matplotlib.pyplot as plt

def simple_bar(data, title):
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    ax.set_title(title)
    return fig
