import json
from typing import Union, Dict, Any, List

# noinspection PyPackageRequirements
from fhir.resources.bundle import Bundle

# noinspection PyPackageRequirements
from fhir.resources.patient import Patient

# noinspection PyPackageRequirements
from fhir.resources.person import Person

from helix_personmatching.fhir_manager.fhir_to_dict_manager.fhir_to_dict_manager import (
    FhirToAttributeDict,
)
from helix_personmatching.logics.scoring_input import ScoringInput


class FhirLoader:
    @staticmethod
    def parse(resource_json: str) -> Union[Patient, Person, Bundle]:
        resource_dict: Dict[str, Any] = json.loads(resource_json)
        resource_type = resource_dict.get("resourceType")
        if resource_type == "Patient":
            return Patient.parse_raw(resource_json)
        elif resource_type == "Person":
            return Person.parse_raw(resource_json)
        elif resource_type == "Bundle":
            return Bundle.parse_raw(resource_json)
        else:
            raise Exception(f"resourceType {resource_type} is not Patient or Person")

    @staticmethod
    def get_scoring_inputs(resource_json: str) -> List[ScoringInput]:
        resource: Union[Patient, Person, Bundle] = FhirLoader.parse(
            resource_json=resource_json
        )
        return FhirToAttributeDict.get_scoring_inputs_for_resource(resource)
