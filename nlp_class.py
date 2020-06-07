import spacy


class Nlp:

    # TODO: add support for punctuation (, ; : . ? ! `)
    # TODO: add support for special characters
    def __init__(self, sentence):
        self.nlp_sm = spacy.load("en_core_web_sm")
        self.nlp_lg = spacy.load("en_core_web_lg")
        self.sentence = sentence

        self.word_array = []
        self.classification_list = []
        self.lemma_list = []

        self.objects = []

        self.relation = []
        self.order = []
        self.properties = []

    """ Tokenizes and classifies each of the words in the sentence """
    def tokenize_and_classify(self):
        sent = self.nlp_sm(self.sentence)
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
        sent = self.nlp_sm(self.sentence)
        temp_dep_list = []

        for token in sent:
            temp_dep_list.append([child for child in token.children])

        for val in range(len(temp_dep_list)):
            internal_dep_list = temp_dep_list[val]
            if not internal_dep_list:
                temp_dep_list[val] = "-"
            if len(internal_dep_list) == "1":
                temp_string = internal_dep_list[0]
                temp_dep_list[val] = temp_string

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
