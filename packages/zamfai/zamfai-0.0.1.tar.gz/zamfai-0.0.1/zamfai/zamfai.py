import matplotlib
import matplotlib.pyplot as plt
class Zamfai():
    def __init__(self) -> None:
        pass
    def show():
        
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.subplots_adjust(top=0.85)

        # Set titles for the figure and the subplot respectively
        fig.suptitle('morocco\'s motherfucker', fontsize=14, fontweight='bold')
        ax.set_title('axes title')

        ax.set_xlabel('xlabel')
        ax.set_ylabel('ylabel')

        # Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
        ax.axis([0, 10, 0, 10])

        ax.text(3, 8, '+ 18', style='italic',
                bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

        #ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

        #ax.text(3, 2, 'get down')

        ax.text(0.95, 0.01, 'hahahahaha',
                verticalalignment='bottom', horizontalalignment='right',
                transform=ax.transAxes,
                color='green', fontsize=15)

        ax.text(1.8, 0.8, 'Faical')
        ax.annotate('This one here', xy=(2, 1), xytext=(3, 4),
                    arrowprops=dict(facecolor='black', shrink=0.05))

        plt.show()

# %%
