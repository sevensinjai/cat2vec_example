import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentence(object):
    def __init__(self, filepath):
        self.__filepath__ = filepath

    def __iter__(self):
        for line in open(self.__filepath__):
            yield line.replace(" ","").split(",,")

generator = MySentence("/Users/felixleung/Desktop/horse racing/ELT/script/cat2vec")

model = gensim.models.Word2Vec(generator)

model.save('cat2vec_model')
model.wv.save_word2vec_format("cat2vec_model.txt")

logging.info("DONE")