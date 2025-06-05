def hide(source: str, target: str):
    return source.replace(target, len(target) * '*')