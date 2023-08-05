from difflib import SequenceMatcher
import jellyfish
def are_words_similar(s1: str, s2: str, threshold_jel: int = 2,threshold_seq: float = 0.80) -> bool:
    """Verify if s1 match of s2 with difference words is less or equls to  threshold_jel OR difference words is more than threshold_seq

    Args:
        s1 (str): words one
        s2 (str): words two
        threshold_jel (int, optional): _description_. Defaults to 2.
        threshold_seq (float, optional): _description_. Defaults to 0.80.

    Returns:
        bool: Match or not
    """
    res1= jellyfish.damerau_levenshtein_distance(s1, s2) 
    res2 = SequenceMatcher(a=s1, b=s2).ratio() 
    return res1<= threshold_jel or res2 >threshold_seq