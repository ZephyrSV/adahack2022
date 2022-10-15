
from wordcloud import WordCloud, get_single_color_func
import matplotlib.pyplot as plt


def sentiment_colour_pairings(data):
    """
    Places words in a list assigned to a discrete colour value in a dict
    Spectrum goes from magenta (- sentiment) through to green (+)
    Assumes data in form [[word,freq,sentiment]].
    """
    pairings = {colour:[] for colour in ["#FF007F","#FF3399","#FF66B2","#FF99CC","#FFCCE5","#FFFFFF","#CCFFCC","#99FF99","#66FF66","#33FF33","#00FF00"]}
    for item in data:
        word = item[0]
        sentiment = item[2]
        if sentiment < -0.9:
            pairings["#FF007F"].append(word)
        elif sentiment < -0.7:
            pairings["#FF3399"].append(word)
        elif sentiment < -0.5:
            pairings["#FF66B2"].append(word)
        elif sentiment < -0.3:
            pairings["#FF99CC"].append(word)
        elif sentiment < -0.1:
            pairings["#FFCCE5"].append(word)
        elif sentiment < 0.1:
            pairings["#FFFFFF"].append(word)
        elif sentiment < 0.3:
            pairings["#CCFFCC"].append(word)
        elif sentiment < 0.5:
            pairings["#99FF99"].append(word)
        elif sentiment < 0.7:
            pairings["#66FF66"].append(word)
        elif sentiment < 0.9:
            pairings["#33FF33"].append(word)
        else:
            pairings["#00FF00"].append(word)
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

sample_data = [["apple",30,0.75],["banana", 14, -0.5], ["coconut", 10, 0],["lalala",25,-0.1],["eddde",19,0.75],["tttt",14, -0.5]]
sample_word_frequency = {word[0]:word[1] for word in sample_data}
sample_word_sentiments = sentiment_colour_pairings(sample_data)
sentiment_colour_func = SimpleGroupedColorFunc(sample_word_sentiments, "black")

cloud = WordCloud(background_color='black').generate_from_frequencies(sample_word_frequency)
cloud.recolor(color_func = sentiment_colour_func)

plt.figure()
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()