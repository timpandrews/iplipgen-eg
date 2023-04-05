from markov_textgen import MarkovTextGenerator


def make_training_data(corpus="corpus.txt", output='markov_textgen.json'):

    with open(corpus, 'r', encoding='utf-8') as fp:
        set4 = fp.read()

    gen = MarkovTextGenerator(load_model=False)
    gen.train(set4)
    gen.save_model(output)


make_training_data()