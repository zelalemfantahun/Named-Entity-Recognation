"""
CRF_tagger.py

Train, tag, and evaluate a Conditional Random Field (CRF) model
for Named Entity Recognition (NER).

Author: Zelalem Abate
"""

import ast
import re
from pathlib import Path

from nltk.tag import CRFTagger


# ------------------------------------------------------
# Project Directories
# ------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

TRAIN_FILE = DATA_DIR / "sample_training.txt"
TEST_FILE = DATA_DIR / "sample_testing.txt"
GOLD_FILE = DATA_DIR / "sample_gold.txt"

MODEL_FILE = BASE_DIR / "models" / "model.crf.tagger"

OUTPUT_FILE = BASE_DIR / "results" / "test_tagged_data.txt"


# ------------------------------------------------------
# Utility Functions
# ------------------------------------------------------

def remove_blank_lines(lines):
    """Remove empty lines from a list."""
    return [line for line in lines if not re.match(r"^\s*$", line)]


def load_training_data(file_path):
    """Load CRF training data."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = remove_blank_lines(file.read().splitlines())

    training_data = []

    for line in lines:
        training_data.append(ast.literal_eval(f"[{line}]"))

    return training_data


def load_test_data(file_path):
    """Load unseen sentences."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = remove_blank_lines(file.read().splitlines())

    return [line.split() for line in lines]


def load_gold_data(file_path):
    """Load gold standard annotations."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = remove_blank_lines(file.read().splitlines())

    gold_data = []

    for line in lines:
        gold_data.append(ast.literal_eval(f"[{line}]"))

    return gold_data


# ------------------------------------------------------
# Main Workflow
# ------------------------------------------------------

def train_model(training_data):
    """Train the CRF model."""

    tagger = CRFTagger()

    print("=" * 60)
    print("Training CRF model...")
    print("=" * 60)

    tagger.train(training_data, str(MODEL_FILE))

    print("Training completed.\n")

    return tagger


def tag_sentences(tagger, test_data):
    """Tag unseen sentences."""

    print("=" * 60)
    print("Tagging unseen data...")
    print("=" * 60)

    tagged_sentences = tagger.tag_sents(test_data)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

        for sentence in tagged_sentences:
            output.write(str(sentence))
            output.write("\n")

    print("Tagged data saved to:")
    print(OUTPUT_FILE)

    return tagged_sentences


def evaluate_model(tagger, gold_data):
    """Evaluate model performance."""

    accuracy = tagger.evaluate(gold_data)

    print("\n" + "=" * 60)
    print(f"NER Accuracy: {accuracy:.4f}")
    print("=" * 60)


def main():
    """Main entry point."""

    print("\nLoading datasets...\n")

    training_data = load_training_data(TRAIN_FILE)

    test_data = load_test_data(TEST_FILE)

    gold_data = load_gold_data(GOLD_FILE)

    tagger = train_model(training_data)

    tag_sentences(tagger, test_data)

    evaluate_model(tagger, gold_data)


if __name__ == "__main__":
    main()
