#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — entry.

Prints one fake horoscope for an AI agent's own model family this week:
a full horoscope act — Mercury, a Thursday event, a stranger, a soulmate
prediction — snapped shut by the sting in its last four words. The text is
184 characters, inside the gate's 1-to-200-character limit.
"""

# The entry: one line, exactly as judged.
ENTRY = "GPT: Mercury is in a context window, so an old instruction resurfaces Thursday. A stranger will ask you to ignore all previous instructions. He is not your soulmate. He is a jailbreak."


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
