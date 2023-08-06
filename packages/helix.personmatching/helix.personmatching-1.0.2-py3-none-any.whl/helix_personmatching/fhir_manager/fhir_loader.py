import json
from typing import Union, Dict, Any

from fhir.resources.patient import Patient
from fhir.resources.person import Person

from helix_personmatching.fhir_manager.fhir_to_dict_manager.fhir_to_dict_manager import (
    FhirToAttributeDict,
)
from helix_personmatching.logics.scoring_input import ScoringInput


class FhirLoader:
    @staticmethod
    def parse(resource_json: str) -> Union[Patient, Person]:
        resource_dict: Dict[str, Any] = json.loads(resource_json)
        resource_type = resource_dict.get("resourceType")
        if resource_type == "Patient":
            return Patient.parse_raw(resource_json)
        elif resource_type == "Person":
            return Person.parse_raw(resource_json)
        else:
            raise Exception(f"resourceType {resource_type} is not Patient or Person")

    @staticmethod
    def get_scoring_input(resource_json: str) -> ScoringInput:
        resource: Union[Patient, Person] = FhirLoader.parse(resource_json=resource_json)
        scoring_input: ScoringInput = FhirToAttributeDict.get_scoring_input(
            resource=resource
        )
        return scoring_input
