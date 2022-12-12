import sys
import re
from dataclasses import dataclass
from aoc.day05.Move import Move

class Dijkstra:
    
     # Calculate the minimum distance between startNode and endNode.
     # The algorithm expects, that there are exactly [nodeCount] nodes with names from 0 to [nodeCount - 1]
     # @param: nodeCount the total number of nodes
     # @param: startNOde the name of the start node
     # @param: endNode the name of the end node
     # @param: edges defines all edges (Map<Int, Set<EdgeDistance>>). An edge starts at the key of the map and ends in 0 .. n other nodes.
     #         A target node is of type [EdgeDistance],
     #         which contains the name of the target node and the distance between the key and the target
    def shortest_path(self, nodeCount: int, startNode: int, endNode: int, edges: {}):
        distances  = [1000000000 for x in range(nodeCount)]
        preds  = [-1 for x in range(nodeCount)]
        distances[startNode] = 0
        queue = [ 0 ]
        added = set([0])
        while len(queue) > 0:
            u = self.min(queue, distances)
            queue.remove(u)
            if u == endNode:
                return DijkstraResult(preds, distances[u])
            for v in edges[u]:
                if v.node not in queue and v.node not in added:
                    queue.append(v.node)
                    added.add(v.node)
                if v.node in queue:
                    newDistance = distances[u] + v.weight
                    if newDistance < distances[v.node]:
                        distances[v.node] = newDistance
                        preds[v.node] = u
        raise

    def min(self, queue, distances):
        minimum = min([distances[x] for x in queue])
        for q in queue:
            if distances[q] == minimum:
                return q
        raise

@dataclass
class EdgeDistance:
    node: int
    weight: int

@dataclass
class DijkstraResult:
    preds: []
    length: int

    def __init__(self, preds, length):
        self.preds = preds
        self.length = length

    def shortest_path(self, start: int, end: int):
        path = [ end ]
        while path[-1] != start:
            path.append(self.preds[path[-1]])
        path.reverse()
        return path