from wordcloud import WordCloud, get_single_color_func
import matplotlib.pyplot as plt
from Search import getWordData

def createWordCloud(word, colorblind=False):
    data = getWordData(word)
    word_frequency = {word[0]:word[1] for word in data}
    word_sentiments = sentiment_colour_pairings(data, colorblind)
    sentiment_colour_func = SimpleGroupedColorFunc(word_sentiments, "black")

    cloud = WordCloud(background_color='black').generate_from_frequencies(word_frequency)
    cloud.recolor(color_func = sentiment_colour_func)

    return cloud

def plotWordCloud(word, colorblind=False):
    cloud = createWordCloud(word, colorblind)
    plt.figure()
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def sentiment_colour_pairings(data, colorblind=False):
    """
    Places words in a list assigned to a discrete colour value in a dict
    Spectrum goes from magenta (- sentiment) through to green (+)
    Assumes data in form [[word,freq,sentiment]].
    """

    ColorBlind = ["#FF007F","#FF3399","#FF66B2","#FF99CC","#FFCCE5","#FFFFFF","#CCFFCC","#99FF99","#66FF66","#33FF33","#00FF00"]
    #NonColorBlind goes from red to green
    NonColorBlind = ["#FF0000","#FF3333","#FF6666","#FF9999","#FFCCCC","#FFFFFF","#CCFFCC","#99FF99","#66FF66","#33FF33","#00FF00"]
    if colorblind:
        chosenColorScheme = ColorBlind
    else:
        chosenColorScheme = NonColorBlind
    pairings = {colour:[] for colour in chosenColorScheme}
    for item in data:
        word = item[0]
        sentiment = item[2]
        if sentiment < -0.9:
            pairings[chosenColorScheme[0]].append(word)
        elif sentiment < -0.7:
            pairings[chosenColorScheme[1]].append(word)
        elif sentiment < -0.5:
            pairings[chosenColorScheme[2]].append(word)
        elif sentiment < -0.3:
            pairings[chosenColorScheme[3]].append(word)
        elif sentiment < -0.1:
            pairings[chosenColorScheme[4]].append(word)
        elif sentiment < 0.1:
            pairings[chosenColorScheme[5]].append(word)
        elif sentiment < 0.3:
            pairings[chosenColorScheme[6]].append(word)
        elif sentiment < 0.5:
            pairings[chosenColorScheme[7]].append(word)
        elif sentiment < 0.7:
            pairings[chosenColorScheme[8]].append(word)
        elif sentiment < 0.9:
            pairings[chosenColorScheme[9]].append(word)
        else:
            pairings[chosenColorScheme[10]].append(word)
    return pairings

class SimpleGroupedColorFunc(object):
    """Class used from sample code https://amueller.github.io/word_cloud/auto_examples/colored_by_group.html#sphx-glr-auto-examples-colored-by-group-py

       Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)