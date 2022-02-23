import matplotlib.pyplot as plt
import pygal
from pygal.style import DarkStyle
from word_frequency_non_class_functions import count_words

filenames = ['A Christmas Carol.txt', "A Doll's House.txt", 'A Modest Proposal.txt', 'A Tale of Two Cities.txt', "Alice's Adventures in Wonderland.txt", 'Crime and Punishment.txt', 'Dracula.txt',
    'Frankenstein.txt', 'Great Expectations.txt', "Grimm's Fairy Tales.txt", 'Heart of Darkness.txt', 'Jane Eyre.txt', 'Metamorphosis.txt', 'Moby-Dick.txt', 'Pride and Prejudice.txt', 'The Adventures of Sherlock Holmes.txt',
    'The Great Gatsby.txt', 'The Importance of Being Earnest.txt', 'The Picture of Dorian Gray.txt', 'The Prince.txt', 'The Scarlet Letter.txt', 'The Strange Case of Dr Jekyll and Mr Hyde.txt', 'Twas the Night before Christmas.txt',
    ]

results=[]
for filename in filenames:
    result = count_words(filename)
    results.append(result)


hist = pygal.Bar(fill = True, style=DarkStyle, x_label_rotation=45)

hist.title = "Number of unique words in the top 24 most downloaded books on Project Gutenberg."
hist.x_labels = ['A Christmas Carol', "A Doll's House", 'A Modest Proposal', 'A Tale of Two Cities', "Alice's Adventures in Wonderland", 'Crime and Punishment', 'Dracula',
    'Frankenstein', 'Great Expectations', "Grimm's Fairy Tales", 'Heart of Darkness', 'Jane Eyre', 'Metamorphosis', 'Moby-Dick', 'Pride and Prejudice', 'The Adventures of Sherlock Holmes',
    'The Great Gatsby', 'The Importance of Being Earnest', 'The Picture of Dorian Gray', 'The Prince', 'The Scarlet Letter', 'The Strange Case of Dr Jekyll and Mr Hyde', 'Twas the Night before Christmas',
    ]
hist.x_title = "Book names"
hist._y_title = "Number of unique words"

hist.add('Books', results)
hist.render_to_file('unique_words_visual.svg')