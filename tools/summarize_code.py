import ast, json, os, io, tokenize

def extract_comments(path):
    comments = []
    with open(path, 'rb') as f:
        for toktype, tok, *_ in tokenize.tokenize(f.readline):
            if toktype == tokenize.COMMENT:
                comments.append(tok.strip())
    return comments

def summarize_file(path, root):
    with open(path, encoding='utf-8') as f:
        source = f.read()
    tree = ast.parse(source, path)
    summary = {
        "doc": ast.get_docstring(tree),
        "classes": {},
        "functions": {},
        "comments": extract_comments(path)
    }
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            methods = {}
            for m in node.body:
                if isinstance(m, ast.FunctionDef):
                    methods[m.name] = {
                        "args": [a.arg for a in m.args.args],
                        "doc": ast.get_docstring(m)
                    }
            summary["classes"][node.name] = {
                "doc": ast.get_docstring(node),
                "methods": methods
            }
        elif isinstance(node, ast.FunctionDef):
            summary["functions"][node.name] = {
                "args": [a.arg for a in node.args.args],
                "doc": ast.get_docstring(node)
            }
    return summary

def main():
    src = os.path.join(os.path.dirname(__file__), "..", "vendor", "rubpy")
    out = os.path.join(os.path.dirname(__file__), "..", "rubpy_full_summary.json")
    result = {}
    for root, _, files in os.walk(src):
        for f in files:
            if not f.endswith(".py"):
                continue
            path = os.path.join(root, f)
            key = os.path.relpath(path, src).replace(os.sep, "_")
            result[key] = summarize_file(path, root)
    with open(out, "w", encoding="utf-8") as j:
        json.dump(result, j, indent=2, ensure_ascii=False)
    print("Full summary written to", out)

if __name__ == "__main__":
    main()