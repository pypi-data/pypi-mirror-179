how to use:

1: use get_sentence_sentiment("your sentence here") > to get the sentiment of a single sentence.
    input > a string sentence
    output > a float: 0 - neutral
                      >0 - positive - happy
                      <0 - negative - angry

2: use get_text_sentiment("your text here, with commas. and also many lines") > to get a list of all sentences sentiments.
    input > a string text
    output > a list of each sentences sentiment > [0.2, -1, -0.7, 3,...3, 0.6]

    !!!important!!! each sentence is the text is seperated by commas "," and dots "."

more explanations can be found in github or the documentation
source code is also on github