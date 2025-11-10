from typing import List

def format_newspaper(paragraphs: List[List[str]], width: int) -> str:
    """
    paragraphs: list of paragraphs; each paragraph is a list of chunks (strings).
    width: maximum number of characters per inner line (border asterisks are outside this width).
    Returns a single string: the newspaper page with borders and centered lines.
    """
    if width < 0:
        raise ValueError("width must be non-negative")

    lines = []
    for paragraph in paragraphs:
        # start each paragraph on a new line
        current = ""
        for chunk in paragraph:
            if len(chunk) > width:
                raise ValueError(f"Chunk too long for width: '{chunk}' (len={len(chunk)})")
            if current == "":
                current = chunk
            else:
                # if adding chunk (with one space) fits, append; otherwise flush and start new line
                if len(current) + 1 + len(chunk) <= width:
                    current += " " + chunk
                else:
                    lines.append(current)
                    current = chunk
        # after finishing paragraph, flush current line (even if empty)
        if current != "":
            lines.append(current)
        else:
            # paragraph might be empty -> produce an empty inner line
            lines.append("")

    # if no content lines, produce a single blank line to be enclosed
    if not lines:
        lines = [""]

    # build bordered page
    top_bot = "*" * (width + 2)
    out = [top_bot]
    for ln in lines:
        # center the line within width
        ln_len = len(ln)
        if ln_len > width:
            # should not happen due to earlier check, but keep safe: truncate (or could raise)
            content = ln[:width]
        else:
            leftover = width - ln_len
            left = leftover // 2
            right = leftover - left
            content = " " * left + ln + " " * right
        out.append("*" + content + "*")
    out.append(top_bot)
    return "\n".join(out)

print(format_newspaper([["hello", "world"],["how", "areYou" "doing"],["Please look", "and align","to center"]], 16))