#!/usr/bin/env python3
import os, ast, json

ROOT = "all_py"  # پوشه‌ای که پر کردیم

summary = {}

for dirpath, _, files in os.walk(ROOT):
    for fname in files:
        if not fname.endswith(".py"): continue
        path = os.path.join(dirpath, fname)
        modname = path.replace(ROOT + "/", "")
        with open(path, encoding="utf-8") as f:
            src = f.read()
        try:
            tree = ast.parse(src)
        except Exception as e:
            continue
        funcs, classes = [], []
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                funcs.append({"name": node.name, "doc": ast.get_docstring(node) or ""})
            if isinstance(node, ast.ClassDef):
                methods = []
                for m in node.body:
                    if isinstance(m, ast.FunctionDef):
                        methods.append({"name": m.name, "doc": ast.get_docstring(m) or ""})
                classes.append({"name": node.name, "doc": ast.get_docstring(node) or "", "methods": methods})
        summary[modname] = {"functions": funcs, "classes": classes}
        
with open("all_py_summary.json", "w", encoding="utf-8") as out:
    json.dump(summary, out, ensure_ascii=False, indent=2)

print("✅ summary → all_py_summary.json")
