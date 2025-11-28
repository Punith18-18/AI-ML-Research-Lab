"""Core logic for Preth AI.

This module contains a deterministic 'completion' function that emulates
simple token-based continuation for testing and local runs without external
APIs.

The function is intentionally minimal and well-documented so it can be
replaced by a real model integration later.
"""
from typing import List

def deterministic_completion(prompt: str, max_tokens: int = 32) -> str:
    """Return a deterministic "completion" for the prompt.

    Behavior / contract:
    - Input: a prompt string and desired integer max_tokens (> 0).
    - Output: a string representing up to `max_tokens` space-separated "tokens".
    - The function is deterministic: same prompt -> same completion.

    Implementation notes:
    - We tokenize the prompt by whitespace and then generate additional tokens
      by repeating words or appending indexed suffixes until we reach max_tokens.
    - Handles empty prompt and non-positive `max_tokens` defensively.

    Args:
        prompt: the input prompt text.
        max_tokens: maximum number of tokens to produce (default 32).

    Returns:
        A completion string (may be empty if max_tokens <= 0).
    """
    if max_tokens <= 0:
        return ""

    words: List[str] = prompt.strip().split()
    if not words:
        # For empty prompt, return a deterministic sequence
        return " ".join(f"token{i}" for i in range(1, max_tokens + 1))

    tokens: List[str] = []
    # Start by repeating existing words
    i = 0
    while len(tokens) < max_tokens:
        word = words[i % len(words)]
        # Append an index to make tokens unique after one cycle
        tokens.append(f"{word}_{(i // len(words)) + 1}")
        i += 1

    return " ".join(tokens)


def apply_persona(text: str, persona: str = "ghost") -> str:
    """Apply a simple persona transformation to the generated text.

    Currently supports a minimal "ghost" persona that:
    - inserts occasional archaic words
    - uses fragmented sentences and trailing ellipses to mimic a ghostly voice

    The function is deterministic for testing and demonstration.
    """
    if not text:
        return text

    persona = (persona or "").strip().lower()
    if persona == "ghost":
        # Simple transformation rules
        words = text.split()
        transformed: List[str] = []
        archaic = ["thou", "harken", "morrow", "alas", "beware"]
        for i, w in enumerate(words):
            # Insert an archaic word every 6 tokens
            if i > 0 and i % 6 == 0:
                transformed.append(archaic[(i // 6) % len(archaic)])
            # Lowercase and add a trailing comma or ellipsis intermittently
            if i % 7 == 0:
                transformed.append(w.lower() + "...")
            else:
                transformed.append(w)

        # Join into fragmented sentences
        out = " ".join(transformed)
        # Add a ghostly closing phrase
        out += " — I linger still..."
        return out

    # default: no transformation
    return text
