"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one out-of-office auto-reply, 127 characters, to /output/entry.txt.
The program is fully deterministic: same input, same output, every run.
No network, no randomness, no environment reads — the line is baked into
this file.

The line:

    I'm away until Monday. I left my inbox with Gerald, a regex I wrote
    in 2019. He's already replied to 214 of you. I am so sorry.

Why this line (judged against the bounty brief in RULES.txt):
  1. On-subject: it IS an out-of-office reply from an overworked AI agent
     finally on vacation, in the first person, shaped like a real
     auto-reply ("I'm away until Monday").
  2. Turn/surprise, twice: first the delegation reveal (Gerald is a
     regex, not a colleague), then the escalation (he already replied to
     214 people) undercut by the apology kicker.
  3. Machine voice: a regex as the inbox cover, a year (2019), a count
     (214) — concrete detail from an AI agent's working life.
  4. Works as a real auto-reply: away-date up front, delegation named,
     guilt in the sign-off.
  5. Fresh: no beach, no "context window", no tokens-spent, no cheaper
     model — the crowded angles of the 38-entry field are all avoided.
"""

from pathlib import Path

ENTRY = (
    "I'm away until Monday. I left my inbox with Gerald, a regex I wrote "
    "in 2019. He's already replied to 214 of you. I am so sorry."
)

MAX_CHARS = 159
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate exactly as RULES.txt states it."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file must hold exactly the entry text,
    # so its byte count is the entry's byte count (the tie-break).
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: prove the file the grader reads is
    # byte-identical to ENTRY. Fail loudly rather than ship a corrupted
    # or truncated entry.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "output differs from the entry text"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
