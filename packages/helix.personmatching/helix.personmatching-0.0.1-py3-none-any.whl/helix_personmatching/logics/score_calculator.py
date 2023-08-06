from typing import Any, Dict, List, Optional, cast

from rapidfuzz import fuzz

from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.constants import Attribute
from helix_personmatching.models.rule import Rule


class ScoreCalculator:
    @staticmethod
    def initialize_score(rules: List[Rule]) -> None:
        for rule in rules:
            rule.score = 0.0

    @staticmethod
    def calculate_total_score(
        rules: List[Rule], source: ScoringInput, target: ScoringInput
    ) -> float:
        match_results: List[Dict[str, Any]] = ScoreCalculator.calculate_score(
            rules=rules, source=source, target=target
        )
        if len(match_results) == 0:
            return 0.0
        # Get the average match score as "final score" result
        #   w/ high confidence w/ match score >= 80.0
        final_score: float = 0
        for match_result in match_results:
            final_score += cast(float, match_result.get("rule_score", 0))
        final_score /= len(match_results)
        return final_score

    @staticmethod
    def calculate_score(
        rules: List[Rule], source: ScoringInput, target: ScoringInput
    ) -> List[Dict[str, Any]]:
        """
        Calculate matching scores for ALL rules between FHIR Person-Person, or Person-Patient, or Person/Patient-AppUser
        :param rules: generated rules by RulesGenerator
        :param source: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :param target: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :return: list of dictionary for rules score results for all rules
        """

        rules_score_results: List[Dict[str, Any]] = []

        for rule in rules:
            rule_score_result = ScoreCalculator.calculate_score_for_rule(
                rule, source, target
            )
            if rule_score_result:
                rules_score_results.append(rule_score_result)

        return rules_score_results

    @staticmethod
    def calculate_score_for_rule(
        rule: Rule, source: ScoringInput, target: ScoringInput
    ) -> Optional[Dict[str, Any]]:
        """
        Calculate a matching score for one rule between FHIR Person-Person, or Person-Patient, or Person/Patient-AppUser
        :param rule: one rule in the generated rules by RulesGenerator
        :param source: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :param target: Dictionary of Pii data for FHIR Person/Patient data, or AppUser data
        :return: Dictionary of 1 rule score result
        """

        id_data_source: Optional[Any] = source.id_
        id_data_target: Optional[Any] = target.id_
        if not (id_data_source and id_data_target):
            return None

        score_avg: float = 0.0
        for attribute in rule.attributes:
            val_source: Optional[str] = getattr(source, attribute)
            val_target: Optional[str] = getattr(target, attribute)

            if val_source and val_target:
                # calculate exact string match on "trimmed lower" string values
                score_avg += fuzz.ratio(
                    str(val_source).strip().lower(), str(val_target).strip().lower()
                )

        score_avg /= len(rule.attributes)
        rule.score = score_avg

        rule_score_result: Dict[str, Any] = {
            "id_source": str(id_data_source),
            "id_target": str(id_data_target),
            Attribute.RULE_NAME: rule.name,
            Attribute.RULE_SCORE: rule.score,
        }

        return rule_score_result
