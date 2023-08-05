import networkx as nx

from embedding.learn import learn_embeddings
from embedding.graph import Graph


class Node2Vec:

    def __init__(self, G: nx.Graph, p: float = 1, q: float = 1, directed: bool = False, num_walks: int = 300,
                 walk_length: int = 80, dimensions: int = 8, window_size: int = 10, workers: int = 1,
                 epochs: int = 1, output: str = "Output.emb") -> None:
        """
        Node2Vec algorithm for Python.
        Args:
            p (float, optional): Node2Vec Parameter. Defaults to 1.
            q (float, optional): Node2Vec Parameter. Defaults to 1.
            directed (bool, optional): True if network is directed. Defaults to False.
            num_walks (int, optional): Amount of random walks. Defaults to 300.
            walk_length (int, optional): Size of random walks. Defaults to 80.
            dimensions (int, optional): Number of dimensions in embedding.. Defaults to 8.
            window_size (int, optional): Amounts of words used for each sentence in Word2Vec. 
                                         Defaults to 10.
            workers (int, optional): Amount of workers for cpu. Defaults to 1.
            epochs (int, optional): Amounts of epochs for train. Defaults to 1.
            output (str, optional): Filename of output. Defaults to "Output.emb".

        Example:
            n2v = Node2Vec(nx.Graph)
            n2v.fit()
        """

        self.G = G
        self.p = p
        self.q = q
        self.directed = directed
        self.num_walks = num_walks
        self.walk_length = walk_length
        self.dimensions = dimensions
        self.window_size = window_size
        self.workers = workers
        self.epochs = epochs
        self.output = output

        nx.set_edge_attributes(self.G, 1, name="weight")
        self.n2vG = Graph(self.G, directed=directed, p=p, q=q)

    def fit(self):
        self.n2vG.preprocess_transition_probs()
        walks = self.n2vG.simulate_walks(self.num_walks, self.walk_length)
        walks = [list(map(str, walk)) for walk in walks]

        learn_embeddings(walks, dimensions=self.dimensions, window_size=self.window_size,
                         workers=self.workers, epochs=self.epochs, output=self.output)
