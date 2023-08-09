def tokenize(file_path: str) -> None:
    """Tokenizer for Reaper Project files.
    Draft.

    Args:
        file_path (_type_): path to RPP file.

    Returns:
        None
    """
    depth = 0
    line_type = None
    node_stack = []

    def context_msg():
        node_cur = None
        node_prev = None
        if node_stack:
            node_cur = node_stack[-1]
            if len(node_stack) > 1:
                node_prev = node_stack[-2]
        return f"{{{depth:2}}} : {str(line_type).ljust(10)} : {str(node_prev).ljust(15)} -> {str(node_cur).ljust(15)} | {node_stack}"

    with open(file_path, 'r') as f:
        for lidx, line in enumerate(f):
            if line.lstrip()[0] == '<':
                depth += 1
                node = line.lstrip()[1:].split(" ")[0].rstrip()
                node_stack.append(node)
                line_type = 'TAG_OPEN'
            elif line.lstrip()[0] == '>':
                depth -= 1
                line_type = 'TAG_CLOSE'
                node_stack.pop()
            else:
                line_type = 'TAG_INNER'
            print(f"[{lidx:4}]: {line.rstrip().ljust(140)} | {context_msg()}")
