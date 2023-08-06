import json
from pathlib import Path
from typing import Any, Dict, List

from helix_personmatching.fhir_manager.fhir_loader import FhirLoader
from helix_personmatching.logics.rules_generator import RulesGenerator
from helix_personmatching.logics.score_calculator import ScoreCalculator
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.matchers.matcher import Matcher
from helix_personmatching.models.rule import Rule


def test_exact_match() -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    with open(data_dir.joinpath("patient1.json")) as file:
        resource1_json = file.read()

    with open(data_dir.joinpath("patient2.json")) as file:
        resource2_json = file.read()

    source: ScoringInput = FhirLoader.get_scoring_input(resource_json=resource1_json)
    target: ScoringInput = FhirLoader.get_scoring_input(resource_json=resource2_json)

    rules: List[Rule] = RulesGenerator.generate_rules()
    scores: List[Dict[str, Any]] = ScoreCalculator.calculate_score(
        rules=rules, source=source, target=target
    )

    print(json.dumps(scores, default=str))

    with open(data_dir.joinpath("expected_scores.json")) as file:
        expected_scores = json.loads(file.read())

    assert scores == expected_scores

    final_score: float = ScoreCalculator.calculate_total_score(
        rules=rules, source=source, target=target
    )

    assert final_score == 87.76455026455027

    matcher = Matcher()

    match: bool = matcher.match(source_json=resource1_json, target_json=resource2_json)

    assert match is True
