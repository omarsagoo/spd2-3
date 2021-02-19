# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_integral(graph):   # Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_largest_value(li):  # Rename this function to reflect what it's doing.
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_largest_value(li))

############################
def convert_sentence_to_array(sentence):  # Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(convert_sentence_to_array('If you were a vegetable, you’d be a ‘cute-cumber.'))
