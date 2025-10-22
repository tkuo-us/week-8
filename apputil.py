from collections import defaultdict
import numpy as np
import re


class MarkovText:
    def __init__(self, corpus):
        """
        Initialize the MarkovText object with a given text corpus.
        The corpus is split into tokens (words) for further processing.
        """
        # remove long whitespaces (see regex101.com)
        corpus = re.sub(r"\s+", " ", corpus)
        # remove punctuation
        corpus = re.sub(r'[^\w\s]', "", corpus)
        # remove leading/trailing whitespaces
        corpus = corpus.strip()
        self.corpus = corpus

        self.tokens = corpus.split()
        self._term_dict = None

    def get_term_dict(self):
        """
        Build a transition dictionary (term_dict) that maps each word (state)
        to a list of possible next words (transitions).
        
        Example:
            For the text "Healing comes from taking responsibility",
            term_dict might look like:
            {
                'Healing': ['comes'],
                'comes': ['from'],
                'from': ['taking'],
                ...
            }
        """
        td = defaultdict(list)
        for i in range(len(self.tokens) - 1):
            td[self.tokens[i]].append(self.tokens[i + 1])
        self.term_dict = dict(td)
        return self.term_dict

    def generate(self, seed_term=None, term_count=15, restart_on_deadend=True):
        """
        Generate text using a Markov Chain model.

        Args:
            term_count (int): Number of tokens to generate.
            seed_term (str, optional): Starting word. Raises ValueError if not in corpus.
            restart_on_deadend (bool): If True, randomly restarts when reaching a dead-end state.

        Returns:
            str: A string of generated text.
        """
        # use the term dictionary built in ex1
        term_dict = self.term_dict or self.get_term_dict()
        if not term_dict:
            return ""

        rng = np.random.default_rng()
        keys = list(term_dict.keys())

        # choose the starting term
        if seed_term is None:
            current = rng.choice(keys)
        else:
            if seed_term not in term_dict:
                raise ValueError(f"seed_term '{seed_term}' not found in corpus.")
            current = seed_term

        output = [current]

        # generate the next term
        for _ in range(term_count - 1):
            followers = term_dict.get(current, [])

            if not followers:
                if restart_on_deadend:
                    # Restart from a random term if no successor exists
                    current = rng.choice(keys)
                    output.append(current)
                    continue
                else:
                    # Stop generation early
                    break

            # Randomly select the next word (duplicates imply frequency weighting)
            current = rng.choice(followers)
            output.append(current)

        return " ".join(output)