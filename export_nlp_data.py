import numpy as np
import pandas


class ExportData:

    def __init__(self, raw_lists, rop_lists):
        self.relation = rop_lists[0]
        self.order = rop_lists[1]
        self.properties = rop_lists[2]

    """ Graphically displays the sentence in a ROP chart 
    Relation  |  Order  |  Properties
    Relation: The way in which two subjects interact
    Order: The order of the sentence subjects from background to foreground
    Properties: describing factors of a subject

    EXAMPLE: the blue cat wears a hat on a brown table
    Relation:  Order:  Properties:
       -       table      brown
     under       |         -
       -        cat       blue        
     under       |         -
       -        hat        -

    :return rop: will return chart
    :type rop: pandas dataFrame
    """
    def create_rop_chart(self):
        # TODO: make this section cleaner; remove any extra copies
        rop_relation = self.relation
        rop_order = self.order
        rop_properties = self.properties

        # TODO: make sure the relation list is compliant with the parsing method
        # Parse the relation list and create a numpy array:
        for relation in rop_relation:
            index = rop_relation.index(relation)
            if index % 2 == 0:
                rop_relation.insert(index, "-")
        rel = np.array([rop_relation])
        rel = np.vstack(rel)

        # Parse the order list and create a numpy array:
        for subject in rop_order:
            index = rop_order.index(subject)
            if index % 2 == 1:
                rop_order.insert(index, "|")
        order = np.array([rop_order])
        order = np.vstack(order)

        # Parse the properties list and create a numpy array:
        for prop in rop_properties:
            index = rop_properties.index(prop)
            if index % 2 == 1:
                rop_properties.insert(index, "-")
        prop = np.array([rop_properties])
        prop = np.vstack(prop)

        # Create chart:
        rop_array = np.concatenate((rel, order, prop), axis=1)
        rop_chart = pandas.DataFrame(data=rop_array, columns=["Relation:", "Order:", "Properties:"])
        print(rop_chart)

    """ Generates the image creation script """
    def generate_image_code(self):
        # Currently not implemented
        pass

    """ Exports a file containing the image creation script 
    :return image_file: .txt file of image script
    """
    def create_file(self):
        # Currently not implemented
        pass
