import json

def build_dependency_graph(filename: str) -> dict:
    """Given a json file, reads the dependencies into a dictionary representing the graph"""

    dependencies = None
    with open(filename, "r") as file:
        dependencies = json.load(file)
    
    graph = {}
    for package_name in dependencies:
        build_graph(package_name, dependencies, graph)

    return graph

def build_graph(package_name: str, all_deps: dict, graph: dict) -> dict:
    """Recursively builds the dependency graph for the given package."""
    package_deps = all_deps[package_name]

    # Base case: If this package has no deps, set the resolved value to None
    if len(package_deps) == 0:
        graph[package_name] = None
        return
    
    # If we have seen this package before, stop here
    if package_name in graph:
        return graph[package_name]

    # Otherwise, for each of the unresolved deps of this package, resolve them
    graphed_deps = {
        dependent: build_graph(dependent, all_deps, graph) 
        for dependent in package_deps 
    }

    # Now that we have resolved the package, we can save it for later
    graph[package_name] = graphed_deps

    return graphed_deps
