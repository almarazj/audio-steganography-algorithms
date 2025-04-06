def bit_error_rate(hidden: list, retrieved: list) -> float:
    """
    Calculate the Bit Error Rate (BER) between two sequences of bits.
    """
    if len(hidden) != len(retrieved):
        raise ValueError("The lengths of the two sequences must be equal.")

    errors = sum(h != r for h, r in zip(hidden, retrieved))
    ber = errors / len(hidden)

    return ber*100
