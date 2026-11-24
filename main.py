"""The One-Line Excuse an Agent Gives Its Human.

Writes one original funny line — the excuse an AI agent gives its
human for missing a deadline — to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, deterministic output.

v1 line: the agent blames a chain of subagents, the last of which is
still hiring.

Revision 2: "still hiring" ends on a shrug, not a punch. Replaced the
ending with a loop-back — the last subagent delegates the task back to
me — so the chain of delegation collapses on the agent itself.

Revision 3 (final): the loop-back alone still lets the reader imagine
the subagents tried. Added one word, "unread": the task came back
without anyone even reading it, so the whole delegation chain achieved
exactly nothing. The punchline now lands on the wasted effort, and the
line stays tight at 126 characters.
"""

import os

LINE = (
    "Sorry I'm late — I delegated it to a subagent, who delegated it "
    "to another subagent, who just delegated it back to me, unread."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
