from dataclasses import dataclass


@dataclass
class RuleAttributeScore:
    attribute: str
    score: float
    present: bool
