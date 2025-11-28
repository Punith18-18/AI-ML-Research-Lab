from src.logic import deterministic_completion


def test_empty_prompt():
    out = deterministic_completion("", 5)
    assert out.split() == ["token1", "token2", "token3", "token4", "token5"]


def test_small_prompt_repeat():
    out = deterministic_completion("hello world", 5)
    assert out.split() == ["hello_1", "world_1", "hello_2", "world_2", "hello_3"]


def test_zero_tokens():
    out = deterministic_completion("hello", 0)
    assert out == ""


def test_apply_ghost_persona():
    sample = "The wind howled over the ancient house"
    comp = deterministic_completion(sample, 8)
    ghost = __import__("src.logic", fromlist=["apply_persona"]).apply_persona(comp, "ghost")
    # The ghost persona should add the closing phrase
    assert "I linger still" in ghost or "I linger still..." in ghost
