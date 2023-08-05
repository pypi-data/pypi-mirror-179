import networkx as nx
import numpy as np


class ReachFinder:

    def __init__(self, G: nx.Graph) -> None:
        """Find reach (Amount of nodes that you can visit from a 
        node in a directed graph) for a graph G.

        Args:
            G (nx.Graph): Networkx Graph.
        
        Example:
            rf = ReachFinder(G)
            reach = rf.find_all_nodes()
        """
        self.G = G
        self.reached_from = {node: set() for node in G.nodes}
        self.calls = 0

    def find_all_nodes(self) -> dict[set]:
        """Get reach of every node in network.

        Returns:
            dict[set]: Reached nodes for each node.
        """
        for n in self.G.nodes:
            self.find_from_node(n)

        print(f"\rDone. Function called {self.calls} times.")
        return self.reached_from

    def find_from_node(self, node: str, path: list = None) -> set:
        """
        Gets the reach of a node.

        Args:
            node (str): Node to search from.
            path (list, optional): List of nodes reached before. Defaults to None.

        Returns:
            set: Reached nodes for the selected node.
        """

        # Si ya estuve acá, no hago nada.
        if len(self.reached_from[node]) == 0:
            self.reached_from[node].add(node)
            if path is None:
                path = []

            neighbors = list(nx.neighbors(self.G, node))
            for neigh in neighbors:
                if np.random.uniform(low=0, high=1, size=1) >= 1-self.p:
                    if neigh not in path:
                        reach_from_neigh = self.find_from_node(
                            neigh, path=path+[node])
                        self.reached_from[node].update(reach_from_neigh)
                    else:
                        self.reached_from[node].update(
                            self.reached_from[neigh])
                        self.reached_from[neigh] = self.reached_from[node]

            self.calls += 1
            print(f"\rFunction called {self.calls} times.", end="")

        return self.reached_from[node]

    # Remove self nodes in scope.
    @staticmethod
    def remove_self_edges(reach):
        for k, v in reach.items():
            if v is not None:
                try:
                    v.remove(k)
                except KeyError:
                    print(k, "no estaba en el reach.")
                if v is None:
                    reach[k] = set()
            else:
                reach[k] = set()

        return reach
