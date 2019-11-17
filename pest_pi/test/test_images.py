""" Testing pest_pi.image """

from pest_pi import image


def test_get_classifier_type():
    model = image.get_classifier()
    assert str(type(model)) == "<class 'tensorflow.python.keras.engine.training.Model'>"
