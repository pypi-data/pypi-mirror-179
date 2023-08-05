#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Deduplicate Graph Edges """


from typing import List

from baseblock import BaseObject


class EdgeDedupe(BaseObject):
    """ Deduplicate Graph Edges """

    def __init__(self):
        """ Change Log

        Created:
            29-Nov-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/owl-graph/issues/2
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                edges: List[dict]) -> List[dict]:
        """ Entry Point

        Args:
            results (List[dict]): the Ontology Node results

        Returns:
            results (List[dict]): the post-processed Ontology Node results
        """

        s = set()
        normalized = []

        for d_node in edges:
            hash_d_node = hash(''.join(list(d_node.values())))
            if hash_d_node not in s:
                s.add(hash_d_node)
                normalized.append(d_node)

        return normalized
