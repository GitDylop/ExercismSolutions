def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    i = 1
    aliquots = 0
    while i < number:
        if number % i == 0:
            aliquots += i
        i += 1

    if aliquots == number:
        return "perfect"
    elif aliquots > number:
        return "abundant"
    else:
        return "deficient"
