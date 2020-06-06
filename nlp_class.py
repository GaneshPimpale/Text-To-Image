import spacy


class Nlp:

    # TODO: add support for punctuation (, ; : . ? ! `)
    # TODO: add support for special characters
    def __init__(self, sentence):
        self.nlp = spacy.load("en_core_web_sm")
        self.sentence = sentence

        self.word_array = []
        self.classification_list = []
        self.lemma_list = []

        self.relation = []
        self.objects = []
        self.properties = []

    """ Tokenizes and classifies each of the words in the sentence """
    def tokenize_and_classify(self):
        sent = self.nlp(self.sentence)
        for token in sent:
            self.word_array.append(token.text)
            self.classification_list.append(token.pos_)
            self.lemma_list.append(token.lemma_)

    """ Removes all articles """
    def eliminate_words(self):
        for pos in self.classification_list:
            if pos == "DET":
                self.word_array.remove(pos)
                self.classification_list.remove(pos)
                self.lemma_list.remove(pos)

    """ Determine the properties of each of the  """
    def determine_properties(self):
        sent = self.nlp(self.sentence)
        temp_dep_list = []
        for dep in sent:
            temp_dep_list.append(dep)

        for val in temp_dep_list:
            if not val:
                temp_dep_list[val] = "-"
            #if self.classification_list[val] != ""
        self.properties = temp_dep_list

    """ determines the relation between two objects in 2D space """
    def determine_relation(self):
        pass

    """  """
    def create_comparison_tree(self):
        pass

    """  """
    def parse_tree(self):
        pass
