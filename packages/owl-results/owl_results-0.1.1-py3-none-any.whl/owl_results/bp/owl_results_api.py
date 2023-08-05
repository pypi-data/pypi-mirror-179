#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Transform NLU results into a Graph Structure """


from baseblock import BaseObject

from owl_results.svc import CreateGraphStructure
from owl_results.svc import PostProcessStructure

from owl_results.dto.typedefs import ParseResults
from owl_results.dto.typedefs import DependencyGraph


class OwlResultsAPI(BaseObject):
    """ Transform NLU results into a Graph Structure

    The output is a dictionary with 'nodes' and 'edges'
    """

    def __init__(self):
        """ Change Log

        Created:
            29-Nov-2022
            craigtrim@gmail.com
            *   refactored out of 'create-graph-structure'
                https://github.com/craigtrim/spacy-token-parser/issues/5
        """
        BaseObject.__init__(self, __name__)

    def to_graph(self,
                 results: ParseResults) -> DependencyGraph:
        """ Create a Graph Structure from incoming Parse Results

        Args:
            results (list): the deepNLU results

        Returns:
            DependencyGraph: The output structure for a Graph
                This Graph structure is typically suitable to for any Graph application
                The output structure has the Nodes and Edges required for simple ETL into any Graph viz engine
        """

        graph_results = CreateGraphStructure().process(results)
        return PostProcessStructure().process(graph_results)

    def to_normalized_text(results: ParseResults) -> str:
        """ Create a normalized text string of output

        Sample Ontology:
            Pay_Bill, No_Computer

        Sample Input Text:
            "How can I pay my bill if I don't have a computer?"

        Sample Output:
            "How can I pay_bill if no_computer?"

        Args:
            results (list): the deepNLU results

        Returns:
            str: the normalized text output
        """
        pass
