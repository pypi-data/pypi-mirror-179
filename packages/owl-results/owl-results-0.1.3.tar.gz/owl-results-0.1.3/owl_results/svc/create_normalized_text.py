#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform NLU results into a Graph Structure """


from baseblock import BaseObject

from owl_results.dto.typedefs import ParseResults
from owl_results.dto.typedefs import DependencyGraph


class CreateNormalizedText(BaseObject):
    """ Transform NLU results into Normalized Text

    Sample Ontology:
        Pay_Bill, No_Computer

    Sample Input Text:
        "How can I pay my bill if I don't have a computer?"

    Sample Output:
        "How can I pay_bill if no_computer?"
    """

    def __init__(self):
        """ Change Log

        Created:
            29-Nov-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/owl-results/issues/4
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                results: ParseResults) -> DependencyGraph:
        """ Entry Point

        Args:
            results (list): the deepNLU results

        Returns:
            list: a flat list
        """

        normals = []

        def iterate_token(token: dict):
            normals.append(token['normal'])

        for i in range(len(results)):
            paragraph = results[i]

            for j in range(len(paragraph)):
                sentence = paragraph[j]

                for token in sentence:
                    iterate_token(token)

        return normals
