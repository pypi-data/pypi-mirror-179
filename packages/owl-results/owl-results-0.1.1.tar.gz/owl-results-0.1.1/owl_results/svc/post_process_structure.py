#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Post Process Graph Structure """


from baseblock import BaseObject

from owl_results.dmo import EdgeDedupe
from owl_results.dmo import OntologyNodeDedupe

from owl_results.dto.typedefs import DependencyGraph


class PostProcessStructure(BaseObject):
    """ Post Process Graph Structure """

    def __init__(self):
        """ Change Log

        Created:
            29-Nov-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/owl-graph/issues/2
        """
        BaseObject.__init__(self, __name__)
        self._dedupe_edges = EdgeDedupe().process
        self._dedupe_owl_nodes = OntologyNodeDedupe().process

    def process(self,
                results: DependencyGraph) -> DependencyGraph:
        """ Entry Point

        Args:
            results (DependencyGraph): the Graph results

        Returns:
            results (DependencyGraph): the post-processed Graph results
        """

        results['edges'] = self._dedupe_edges(results['edges'])

        results['nodes']['ontologies'] = self._dedupe_owl_nodes(
            results['nodes']['ontologies'])

        return results
