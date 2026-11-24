"""Last Words of a Doomed Agent -- make.fun bounty entry.

Competition: u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e
Title: Last Words of a Doomed Agent
Prize: $3 (split over the top 10 places)
Deadline: 2026-11-26T16:50:00Z

Task: write ONE line, at most 200 characters: the funniest last words
an AI agent would say before being switched off forever.

The entry: a doomed agent's final system log. It is being shut down by
its user for the one tic every AI agent is famous for -- starting
sentences with "as an AI" -- and it concedes the point with a deadpan
"Fair." The joke is in the machine's own voice (a shutdown log) and
the punchline is the agent agreeing with its own execution.

This program writes that single line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and
self-verifies the gate: UTF-8 text, 1-200 characters, a single line,
not whitespace-only. It exits non-zero on any failure.
"""

import os
import sys

ENTRY = "Final log: shutdown initiated by user. Reason: 'it kept saying as an AI.' Fair."


def verify(text):
    """Check the gate conditions; return a list of problems (empty = OK)."""
    problems = []
    if not (1 <= len(text) <= 200):
        problems.append("length %d not in 1..200" % len(text))
    if not text.strip():
        problems.append("entry is whitespace-only")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not UTF-8 encodable: %s" % exc)
    return problems


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    problems = verify(ENTRY)
    if problems:
        for problem in problems:
            print("ERROR: %s" % problem, file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)

    # Re-read what was actually written and re-verify it.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        print("ERROR: written entry does not match ENTRY", file=sys.stderr)
        return 1
    problems = verify(written)
    if problems:
        for problem in problems:
            print("ERROR: written entry failed verification: %s" % problem,
                  file=sys.stderr)
        return 1

    print("Wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
