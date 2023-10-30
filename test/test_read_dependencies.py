from package_traversal.dependency_graph import build_dependency_graph

DEPS_FILE = 'tmp/test_deps.json'

def test_build_dependency_graph():
    expected_dependencies = {
        "pkg1": {"pkg2": {"pkg3": None}, "pkg3": None},
        "pkg2": {"pkg3": None},
        "pkg3": None
    }
    resolved_dependencies = build_dependency_graph(DEPS_FILE)
    assert expected_dependencies == resolved_dependencies