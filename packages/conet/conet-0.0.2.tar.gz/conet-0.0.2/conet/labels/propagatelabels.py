from abc import abstractclassmethod, ABCMeta
import networkx as nx

class IPropagate(metaclass = ABCMeta):

    @abstractclassmethod
    def propagate_once(self):
        """
        How propagation is calculated to first order neighbors.
        """
    
    @abstractclassmethod
    def propagate_all(self):
        """
        How propagation is calculated to every node in graph.
        """

class PropagateLabels(IPropagate):
    
    def __init__(self, G: nx.Graph, initial_labels: dict, method: str = "probability") -> None:
        """
        Parent Class for Custom propagators.

        Args:
            G (nx.Graph): Networkx Graph.
            initial_labels (dict): Initial labels for propagation.
            method (str): Type of propagation. Allowed values: "global", "local" and "probability".
                          Defaults to "probability".
        
        Example:
            pl = PropagateLabels(G, initial_labels, "probability")
            final_labels = pl.propagate_all()
        """

        self.G = G.copy()
        self.labels = initial_labels
        self.method = method
        
        self.backup_labels = initial_labels.copy()

        self.nodes = G.nodes()
        self.neighbors = {node: nx.neighbors(self.G, node) for node in self.nodes}

    def restart(self):
        """
        Restart propagation.
        """
        
        self.labels = self.labels_backup