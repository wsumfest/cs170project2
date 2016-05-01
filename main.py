import os
import sys


class Problem():
    """A representation of the graph problem that we are working with"""
    def __init__(self, num_nodes=0, child_nodes=[], adj_matrix=[]):
        self.num_nodes = num_nodes
        self.child_nodes = child_nodes
        self.adj_matrix = adj_matrix
        self.child_set = set(child_nodes)

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
        return self.get_adj_matrix


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

def main(directory):
    output_file = "solutions.out"

    for root, folder, files in os.walk(directory):

        write_handle = open(output_file, "w")
        for fil in files:
            if fil == ".DS_Store":
                continue
            filepath = os.path.join(root, fil)
            problem_instance = Problem()
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
            
            
            handle.close()
        write_handle.close()

if __name__ == "__main__":
    input_dir = "phase1-processed"
    main(input_dir)