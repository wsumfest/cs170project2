import os
import operator
import networkx as nx

class Problem():
    """A representation of the graph problem that we are working with"""
    def __init__(self, instance_number, num_nodes=0, child_nodes=[], adj_matrix=[]):
        self.instance_number = instance_number
        self.num_nodes = num_nodes
        self.child_nodes = child_nodes
        self.adj_matrix = adj_matrix
        self.child_set = set(child_nodes)
        self.vertices = []
        self.edges = []
        self.solution = "" #### effeciency

    def set_num_nodes(self, num):
        self.num_nodes = num

    def get_num_nodes(self):
        return self.num_nodes

    def set_child_nodes(self, children):
        self.child_nodes = children
        self.child_set = set(children)

    def get_child_nodes(self):
        return self.child_nodes

    def set_adj_matrix(self, mat):
        self.adj_matrix = mat

    def get_adj_matrix(self):
        return self.adj_matrix

    def set_edges_and_vertices(self):
        for num in range(0,self.num_nodes - 1):
            self.vertices.append(num)
            for j in range(0,self.num_nodes - 1):
                if (self.get_adj_matrix())[num][j] == 1:
                    self.edges.append((num, j))

    def get_solution(self):
        return self.solution




"strips the string of the new line character, returns an integer"
def until_new_line(string):
    valid_set = [1,2,3,4,5,6,7,8,9,0]
    for item in valid_set:
        item = str(item)
    index = 0
    while string[index] in valid_set:
        index += 1
    new_str = string[0:index -1]
    return int(new_str)
    
"returns an array of child nodes from a string, seperating nodes by spaces"
def get_array_from_string(string):
    output = []
    temp = [item for item in filter(None, string.split(' '))]
    for item in temp:
        try:
            new_item = int(item)
            output.append(new_item)
        except ValueError, e:
            continue
    return output


"""Takes an instance of our problem and writes to our output file,
   transforms into vertices and edges to make search easier. Implementing
    the Top Tradinc Cycles code """
def compute(problem):
    problem.set_edges_and_vertices()
    net_graph = nx.DiGraph()
    net_graph.add_edges_from(problem.edges)

    temp = list()

    while True:
        try:
            this = []
            cycle = nx.find_cycle(net_graph)
            for pair in cycle:
                if pair[0] not in this:
                    this.append(pair[0])
                if pair[1] not in this:
                    this.append(pair[1])
            net_graph.remove_nodes_from(this)
            if len(cycle) < 5:
                temp.append(this)

        except Exception, e:
            new_copy = []
            for donor_cycle in temp:
                new_temp = [str(i) for i in donor_cycle]
                new_copy.append(new_temp)
                    
            final_copy = ""

            for donor_cycle in new_copy:
                donor_string = " ".join(donor_cycle)
                new_string = donor_string.rstrip()
                new_string += "; "

                final_copy += new_string

            problem.solution = final_copy

            return

    return





def main(directory):

    problems = []

    output_file = "solutions.out"

    for root, folder, files in os.walk(directory):

        write_handle = open(output_file, "w")
        for fil in files:
            if fil == ".DS_Store":
                continue

            instance_stripped = fil[:-3]
            file_number = int(instance_stripped)
            filepath = os.path.join(root, fil)
            problem_instance = Problem(instance_number=file_number)
            problems.append(problem_instance)
            handle = open(filepath, "r")
            ### sets the number of nodes in the problem instance ###
            num_nodes = handle.readline()
            num_nodes = until_new_line(num_nodes)
            problem_instance.set_num_nodes(num_nodes)
            ### sets the children node in the problem instance ###
            child_nodes = handle.readline()
            child_nodes = get_array_from_string(child_nodes)
            problem_instance.set_child_nodes(child_nodes)
            ### sets the adjacency matrix for the graph ###
            new_line = handle.readline()
            while new_line:
                vector = get_array_from_string(new_line)
                problem_instance.adj_matrix.append(vector)
                new_line = handle.readline()
            ### close the handle because we are done reading data from input ###
            handle.close()
            ### Now we can start working on our problem ###
            compute(problem_instance)

        ### Sort problems by instance number, we are ready to write to output ###
        problems.sort(key=operator.attrgetter("instance_number"))
        for problem in problems:
            if problem.solution == "":
                problem.solution = "None"
            write_handle.write(problem.solution)
            write_handle.write("\n")

        write_handle.close()

if __name__ == "__main__":
    input_dir = "phase1-processed"
    main(input_dir)


