import spacy


class Nlp:

    # TODO: add support for punctuation (, ; : . ? ! `)
    # TODO: add support for special characters
    def __init__(self, sentence):
        # Load spaCy models:
        self.nlp_sm = spacy.load("en_core_web_sm")
        self.nlp_lg = spacy.load("en_core_web_lg")

        # Run the sentence through the models:
        self.sentence_sm = self.nlp_sm(sentence)
        self.sentence_lg = self.nlp_lg(sentence)

        # TODO: remove any extra lists
        # General lists:
        self.word_array = []
        self.classification_list = []
        self.lemma_list = []

        # Object list:
        self.subjects = []

        # ROP data lists:
        self.relation = []
        self.order = []
        self.properties = []

    """ Tokenizes and classifies each of the words in the sentence """
    def tokenize_and_classify(self):
        for token in self.sentence_sm:
            self.word_array.append(token.text)
            self.classification_list.append(token.pos_)
            self.lemma_list.append(token.lemma_)

    """ Removes all articles """
    def eliminate_words(self):
        for count in range(len(self.classification_list)):
            if self.classification_list[count] == "DET":
                self.classification_list.remove(count)
                self.word_array.remove(count)
                self.lemma_list.remove(count)

    """ Determines the objects inside the sentence """
    def determine_objects(self):
        for pos in self.classification_list:
            # Check for noun and proper nouns
            if (pos == "NOUN") or (pos == "PROPN"):
                self.subjects.append(pos)
            # Check for pronouns
            elif pos == "PRON":
                self.subjects.append(pos)

    """ Determines the properties of each of the words """
    def determine_properties(self):
        for token in self.sentence_sm:
            self.properties.append([child for child in token.children])

        for count in range(len(self.properties)):
            internal_list = self.properties[count]
            if not internal_list:
                self.properties[count] = "-"
            if len(internal_list) == "1":
                temp_string = internal_list[0]
                self.properties[count] = temp_string

    """ Determine the order of the objects when stacked to create an image (Z axis)"""
    def determine_order(self):

        pass

    """ Determines the relation between two objects in 2D space """
    def determine_relation(self):

        pass

    """ returns all the raw lists
    :return raw_lists: list containing lists in the following order: 
        words, classification, lemma, subjects, relation, order, properties
    """
    def raw_lists_return(self):
        raw_lists = [self.word_array,
                     self.classification_list,
                     self.lemma_list,
                     self.subjects,
                     self.relation,
                     self.order,
                     self.properties]

        return raw_lists

    """ Parse the ROP lists into dataFrame format
    :return rop_list: list containing three lists in R, O, P order for dataFrame
    """
    def parse_rop_chart_data(self):
        rop_relation = self.relation
        rop_order = self.order
        rop_properties = self.properties

        # TODO: make sure the relation list is compliant with the parsing method
        # Parse the relation list:
        for relation in rop_relation:
            index = rop_relation.index(relation)
            if index % 2 == 0:
                rop_relation.insert(index, "-")

        # Parse the order list:
        for subject in rop_order:
            index = rop_order.index(subject)
            if index % 2 == 1:
                rop_order.insert(index, "|")

        # Parse the properties list:
        for prop in rop_properties:
            index = rop_properties.index(prop)
            if index % 2 == 1:
                rop_properties.insert(index, "-")

        rop_list = [rop_relation, rop_order, rop_properties]
        return rop_list

    """ Parse the ROP lists into an  
    :return rop_code: list containing three lists in R, O, P order for image code
    """
    def parse_rop_image_code(self):
        # Currently not implemented
        pass
