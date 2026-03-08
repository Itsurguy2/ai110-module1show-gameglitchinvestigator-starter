import pytest
from app import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

class TestGetRangeForDifficulty:
    def test_easy(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal(self):
        assert get_range_for_difficulty("Normal") == (1, 100)

    def test_hard(self):
        assert get_range_for_difficulty("Hard") == (1, 200)

    def test_hard_is_harder_than_normal(self):
        _, hard_high = get_range_for_difficulty("Hard")
        _, normal_high = get_range_for_difficulty("Normal")
        assert hard_high > normal_high

    def test_unknown_difficulty_defaults_to_normal(self):
        assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---

class TestParseGuess:
    def test_valid_integer(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_valid_float_truncated(self):
        ok, value, err = parse_guess("7.9")
        assert ok is True
        assert value == 7
        assert err is None

    def test_empty_string(self):
        ok, value, err = parse_guess("")
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_none_input(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_non_numeric_string(self):
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_negative_number(self):
        ok, value, err = parse_guess("-5")
        assert ok is True
        assert value == -5

    def test_zero(self):
        ok, value, err = parse_guess("0")
        assert ok is True
        assert value == 0


# --- check_guess ---

class TestCheckGuess:
    def test_correct_guess(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message

    def test_guess_too_high(self):
        outcome, message = check_guess(80, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_guess_too_low(self):
        outcome, message = check_guess(20, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_hint_direction_too_high_says_lower(self):
        _, message = check_guess(99, 1)
        assert "LOWER" in message

    def test_hint_direction_too_low_says_higher(self):
        _, message = check_guess(1, 99)
        assert "HIGHER" in message

    def test_guess_one_above(self):
        outcome, _ = check_guess(51, 50)
        assert outcome == "Too High"

    def test_guess_one_below(self):
        outcome, _ = check_guess(49, 50)
        assert outcome == "Too Low"


# --- update_score ---

class TestUpdateScore:
    def test_win_early_gives_high_points(self):
        score = update_score(0, "Win", 1)
        assert score > 0

    def test_win_score_decreases_with_more_attempts(self):
        score_early = update_score(0, "Win", 1)
        score_late = update_score(0, "Win", 5)
        assert score_early > score_late

    def test_win_minimum_points_is_10(self):
        # attempt_number=100 would give 100 - 10*101 = -910, clamped to 10
        score = update_score(0, "Win", 100)
        assert score == 10

    def test_too_low_deducts_score(self):
        score = update_score(50, "Too Low", 1)
        assert score == 45

    def test_too_high_on_odd_attempt_deducts(self):
        score = update_score(50, "Too High", 1)
        assert score == 45

    def test_too_high_on_even_attempt_adds(self):
        score = update_score(50, "Too High", 2)
        assert score == 55

    def test_unknown_outcome_unchanged(self):
        score = update_score(50, "Unknown", 1)
        assert score == 50


# --- range validation (logic mirrored from submit block) ---

class TestRangeValidation:
    @pytest.mark.parametrize("difficulty, guess, expected_valid", [
        ("Easy",   0,   False),  # below range
        ("Easy",   1,   True),   # lower bound
        ("Easy",   20,  True),   # upper bound
        ("Easy",   21,  False),  # above range
        ("Normal", 100, True),
        ("Normal", 101, False),
        ("Hard",   200, True),
        ("Hard",   201, False),
    ])
    def test_guess_within_range(self, difficulty, guess, expected_valid):
        low, high = get_range_for_difficulty(difficulty)
        in_range = low <= guess <= high
        assert in_range == expected_valid
