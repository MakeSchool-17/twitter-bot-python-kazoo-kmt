from flask import Flask
import markov_chain
import parsing_tokenizing_byRE

app = Flask(__name__)

@app.route('/')
def tweet():
    # return 'Hello World!'
    # PLEASE SET THE CORPUS.txt AND TWEET LENGTH
    filename = "corpus.txt"
    words_list = parsing_tokenizing_byRE.parsing(filename)
    tuple_of_hashtable = markov_chain.store_to_hashtable(words_list)
    tweet_length = 20
    output_words = markov_chain.random_walk(tuple_of_hashtable, words_list, tweet_length)
    return(' '.join(output_words))

if __name__ == '__main__':
    app.run()
