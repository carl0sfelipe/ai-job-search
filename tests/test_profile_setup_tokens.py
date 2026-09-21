"""Guards leftover /setup tokens on this fork's live /apply inputs.

`/apply` reads 02-behavioral-profile.md for cover-letter voice and
04-job-evaluation.md for fit. cv/main_example.tex is one of the three
factual sources in the grounding audit. Unfilled [YOUR_*] tokens on
those paths produce drafts that fail closed as ungrounded or leak
placeholders. Template files (05, 06, cover_example.tex) keep their
tokens on purpose and are not checked here.
"""
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / ".claude" / "skills" / "job-application-assistant"
MASTER_CV = REPO / "cv" / "main_example.tex"

BEHAVIORAL_LEFTOVERS = (
    "[YOUR_NAME]",
    "[PROFILE_TYPE]",
    "[DRIVE_1]",
    "[BEHAVIOR_1]",
    "[ENVIRONMENT_PREFERENCE_1]",
    "[AREA_1]",
)

EVAL_LEFTOVERS = (
    "[YOUR_FINANCIAL_SITUATION_CONTEXT]",
    "[YOUR_SCHEDULE_CONSTRAINTS]",
    "[YOUR_GROWTH_PRIORITIES]",
)

CV_LEFTOVERS = (
    "[YOUR_NAME]",
    "[Job Title]",
    "[your.email@example.com]",
    "[First]",
    "[Last]",
)


class PersonalizedProfileSetup(unittest.TestCase):
    def test_behavioral_profile_has_no_setup_tokens(self):
        text = (SKILLS / "02-behavioral-profile.md").read_text(encoding="utf-8")
        for token in BEHAVIORAL_LEFTOVERS:
            self.assertNotIn(token, text, f"unfilled /setup token in 02: {token}")
        self.assertIn("self-assessment", text.lower())

    def test_job_evaluation_life_situation_is_filled(self):
        text = (SKILLS / "04-job-evaluation.md").read_text(encoding="utf-8")
        for token in EVAL_LEFTOVERS:
            self.assertNotIn(token, text, f"unfilled /setup token in 04: {token}")
        self.assertIn("Remote Brazil", text)

    def test_master_cv_is_the_public_profile_not_the_stock_template(self):
        text = MASTER_CV.read_text(encoding="utf-8")
        for token in CV_LEFTOVERS:
            self.assertNotIn(token, text, f"unfilled /setup token in master CV: {token}")
        self.assertIn("carlosfelipe2050@gmail.com", text)
        self.assertIn("Carlos Felipe Siqueira Batista", text)
        self.assertIn("Deloitte", text)
        self.assertIn("Claude Code", text)


if __name__ == "__main__":
    unittest.main()
