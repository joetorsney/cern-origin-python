from package_traversal.dependency_graph import build_dependency_graph

if __name__ == '__main__':
    print(build_dependency_graph('tmp/deps.json'))