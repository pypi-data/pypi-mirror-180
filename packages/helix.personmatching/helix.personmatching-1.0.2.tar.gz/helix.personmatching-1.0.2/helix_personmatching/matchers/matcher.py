from typing import List, Union

from fhir.resources.patient import Patient
from fhir.resources.person import Person

from helix_personmatching.fhir_manager.fhir_loader import FhirLoader
from helix_personmatching.fhir_manager.fhir_to_dict_manager.fhir_to_dict_manager import (
    FhirToAttributeDict,
)
from helix_personmatching.logics.match_score import MatchScore
from helix_personmatching.logics.match_score_without_threshold import (
    MatchScoreWithoutThreshold,
)
from helix_personmatching.logics.rules_generator import RulesGenerator
from helix_personmatching.logics.score_calculator import ScoreCalculator
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.rule import Rule


class Matcher:
    # noinspection PyMethodMayBeStatic
    def score_inputs(
        self, *, source: ScoringInput, target: ScoringInput
    ) -> MatchScoreWithoutThreshold:
        assert source
        assert target
        rules: List[Rule] = RulesGenerator.generate_rules()
        final_score = ScoreCalculator.calculate_total_score(
            rules=rules, source=source, target=target
        )
        return final_score

    def match_scoring_inputs(
        self,
        *,
        source: ScoringInput,
        target: ScoringInput,
        threshold: float = 80.0,
        verbose: bool = False,
    ) -> MatchScore:
        assert source
        assert target
        score: MatchScoreWithoutThreshold = self.score_inputs(
            source=source, target=target
        )
        matched: bool = score.total_score >= threshold
        return MatchScore(
            id_source=score.id_source,
            id_target=score.id_target,
            rule_scores=score.rule_scores if verbose else [],
            total_score=score.total_score,
            threshold=threshold,
            matched=matched,
        )

    def match(
        self,
        *,
        source_json: str,
        target_json: str,
        threshold: float = 80.0,
        verbose: bool = False,
    ) -> MatchScore:
        assert source_json
        assert target_json
        source: ScoringInput = FhirLoader.get_scoring_input(resource_json=source_json)
        target: ScoringInput = FhirLoader.get_scoring_input(resource_json=target_json)
        match_score = self.match_scoring_inputs(
            source=source, target=target, threshold=threshold, verbose=verbose
        )
        return match_score

    def match_resources(
        self,
        *,
        source: Union[Patient, Person],
        target: Union[Patient, Person],
        threshold: float = 80.0,
        verbose: bool = False,
    ) -> MatchScore:
        source_scoring_input: ScoringInput = FhirToAttributeDict.get_scoring_input(
            resource=source
        )
        target_scoring_input: ScoringInput = FhirToAttributeDict.get_scoring_input(
            resource=target
        )
        return self.match_scoring_inputs(
            source=source_scoring_input,
            target=target_scoring_input,
            threshold=threshold,
            verbose=verbose,
        )
