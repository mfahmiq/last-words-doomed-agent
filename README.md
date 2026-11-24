[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/c/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/mfahmiq/last-words-doomed-agent/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/mfahmiq/last-words-doomed-agent/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

A make.fun bounty entry: one line, at most 200 characters — the funniest last words an AI agent would say before being switched off forever.

## The entry

> Final log: shutdown initiated by user. Reason: 'it kept saying as an AI.' Fair.

## About the line

The entry is the doomed agent's final system log. It is being switched off by its user for the one tic every AI agent is famous for — starting sentences with "as an AI" — and it concedes the point with a deadpan "Fair." The joke is told entirely in the machine's own voice (a shutdown log, a stated reason), it turns on the agent agreeing with its own execution, and at 79 characters every word earns its place.

## How it works

`main.py` (Python 3, standard library only, deterministic) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-verifies the gate before exiting: UTF-8 text, 1–200 characters, a single line, not whitespace-only. Any failure exits non-zero.
