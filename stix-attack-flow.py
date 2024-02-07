from stix2 import Indicator, Identity
from stix2 import Bundle
import stix2
from stix2 import ExtensionDefinition
from stix2 import ExternalReference

af_documentation_external_reference = ExternalReference(
	source_name = "Documentation",
	description = "Documentation for Attack Flow",
	url = "https://center-for-threat-informed-defense.github.io/attack-flow"
)

af_github_external_reference = ExternalReference(
	source_name = "GitHub",
	description = "Source code repository for Attack Flow",
	url = "https://github.com/center-for-threat-informed-defense/attack-flow"
)

mitre_identity = Identity(name="MITRE Engenuity Center for Threat-Informed Defense")
personal_identity = Identity(name="John Hammond", contact_information="john.hammond@huntresslabs.com")

attack_flow_extension = ExtensionDefinition(
	name="Attack Flow",
	created_by_ref = mitre_identity.id,
	extension_types = ["new-sdo"],
    description="Extends STIX 2.1 with features to create Attack Flows.",
    schema="https://center-for-threat-informed-defense.github.io/attack-flow/stix/attack-flow-schema-2.0.0.json",
    version="2.0.0",
    external_references = [af_documentation_external_reference, af_github_external_reference,]
    )

@stix2.v21.CustomObject(
    'attack-flow', [
        ('name', stix2.properties.StringProperty(required=True)),
        ('spec_version', stix2.properties.StringProperty(required=True)),
        ('description', stix2.properties.StringProperty(required=False)),
        ('scope', stix2.properties.StringProperty(required=True)),
        ('start_refs', stix2.properties.ListProperty(stix2.properties.ReferenceProperty(valid_types=['identifier']))),
    ], 
    extension_name=attack_flow_extension.id, 
    is_sdo=True,
)
class AttackFlowObject:
    pass

attack_flow_object = AttackFlowObject(
	name= "CISA AA22-138B VMWare Workspace (Alt)",
	description = "Alternative method used to exploit VMWare Workspace ONE Access",
	scope = "incident",
	spec_version = "2.1",
	created_by_ref=personal_identity
	)



bundle = Bundle(objects = [
			attack_flow_extension,
			mitre_identity,
			attack_flow_object,
			personal_identity,
			]
		)
print(bundle.serialize(pretty=True))


with open("test-flow.json", "w") as filp:
	filp.write(bundle.serialize())