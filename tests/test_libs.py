def test_imports():
    """Test that parse_anything and prompt_llm can be successfully imported."""
    try:
        from lmlab import parse_anything, prompt_llm

        assert parse_anything is not None
        assert prompt_llm is not None
    except ImportError as e:
        raise AssertionError(f"Failed to import modules: {e}")


if __name__ == "__main__":
    test_imports()
