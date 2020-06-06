import pandas


class ExportData:

    def __init__(self, relation, objects, properties):
        self.Relation = relation
        self.Objects = objects
        self.Properties = properties

    """ Graphically displays the sentence in a ROP chart 
    Relation  |  Order  |  Properties
    Relation: The way in which two subjects interact
    Order: The order of the sentence subjects from background to foreground
    Properties: describing factors of a subject

    EXAMPLE: the blue cat wears a hat on a brown table
    Relation   Order   Properties
       -       table      brown
     under       |         -
       -        cat       blue        
     under       |         -
       -        hat        -

    :return rop: will return chart
    :type rop: pandas dataFrame
    """
    def create_rop_chart(self):
        pass

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
