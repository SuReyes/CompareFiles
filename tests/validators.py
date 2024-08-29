from tests import config 

logger = config.get_logger("validator")


def validate_DateRange(resp_obj: dict):
	valid_entity: bool = True
	# validating effective
	current_validation = (type(resp_obj.get("effective")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: DateRange for key effective, value: |{resp_obj.get('effective')}| expected: |str|")

	# validating end
	current_validation = (type(resp_obj.get("end")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: DateRange for key end, value: |{resp_obj.get('end')}| expected: |str|")

	return valid_entity


def validate_AccessCodeBatch(resp_obj: dict):
	valid_entity: bool = True
	# validating id
	current_validation = (type(resp_obj.get("id")) == int)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key id, value: |{resp_obj.get('id')}| expected: |int|")

	# validating programCode
	current_validation = (type(resp_obj.get("programCode")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key programCode, value: |{resp_obj.get('programCode')}| expected: |str|")

	# validating description
	current_validation = (type(resp_obj.get("description")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key description, value: |{resp_obj.get('description')}| expected: |str|")

	# validating userId
	current_validation = (type(resp_obj.get("userId")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key userId, value: |{resp_obj.get('userId')}| expected: |str|")

	# validating generated
	current_validation = (type(resp_obj.get("generated")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key generated, value: |{resp_obj.get('generated')}| expected: |str|")

	# validating effectiveDateRange
	current_validation = validate_DateRange(resp_obj.get("effectiveDateRange"))
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key effectiveDateRange, value: |{resp_obj.get('effectiveDateRange')}| expected: |None|")

	# validating notes
	current_validation = (type(resp_obj.get("notes")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeBatch for key notes, value: |{resp_obj.get('notes')}| expected: |str|")

	return valid_entity


def validate_AccessCode(resp_obj: dict):
	valid_entity: bool = True
	# validating id
	current_validation = (type(resp_obj.get("id")) == int)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key id, value: |{resp_obj.get('id')}| expected: |int|")

	# validating code
	current_validation = (type(resp_obj.get("code")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key code, value: |{resp_obj.get('code')}| expected: |str|")

	# validating programCode
	current_validation = (type(resp_obj.get("programCode")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key programCode, value: |{resp_obj.get('programCode')}| expected: |str|")

	# validating generated
	current_validation = (type(resp_obj.get("generated")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key generated, value: |{resp_obj.get('generated')}| expected: |str|")

	# validating status
	current_validation = (type(resp_obj.get("status")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key status, value: |{resp_obj.get('status')}| expected: |str|")

	# validating used
	# the field used could be None
	if resp_obj.get("used"): 
		current_validation = ((type(resp_obj.get("used")) == str))
	else: 
		current_validation = True # The field is null
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key used, value: |{resp_obj.get('used')}| expected: |str|")

	# validating effectiveDateRange
	current_validation = validate_DateRange(resp_obj.get("effectiveDateRange"))
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key effectiveDateRange, value: |{resp_obj.get('effectiveDateRange')}| expected: |None|")

	# validating batchId
	current_validation = (type(resp_obj.get("batchId")) == int)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key batchId, value: |{resp_obj.get('batchId')}| expected: |int|")

	# validating transactionId
	# the field transactionId could be None
	if resp_obj.get("transactionId"): 
		current_validation = ((type(resp_obj.get("transactionId")) == int))
	else: 
		current_validation = True # The field is null
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key transactionId, value: |{resp_obj.get('transactionId')}| expected: |int|")

	# validating systemIdentifier
	# the field systemIdentifier could be None
	if resp_obj.get("systemIdentifier"): 
		current_validation = ((type(resp_obj.get("systemIdentifier")) == int))
	else: 
		current_validation = True # The field is null
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCode for key systemIdentifier, value: |{resp_obj.get('systemIdentifier')}| expected: |int|")

	return valid_entity


def validate_AccessCodeProgram(resp_obj: dict):
	valid_entity: bool = True
	# validating code
	current_validation = (type(resp_obj.get("code")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeProgram for key code, value: |{resp_obj.get('code')}| expected: |str|")

	# validating description
	current_validation = (type(resp_obj.get("description")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeProgram for key description, value: |{resp_obj.get('description')}| expected: |str|")

	# validating systemCode
	current_validation = (type(resp_obj.get("systemCode")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeProgram for key systemCode, value: |{resp_obj.get('systemCode')}| expected: |str|")

	# validating registrationProgramCode
	current_validation = (type(resp_obj.get("registrationProgramCode")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: AccessCodeProgram for key registrationProgramCode, value: |{resp_obj.get('registrationProgramCode')}| expected: |str|")

	return valid_entity


def validate_PatchOperation(resp_obj: dict):
	valid_entity: bool = True
	# validating operation
	current_validation = (type(resp_obj.get("operation")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: PatchOperation for key operation, value: |{resp_obj.get('operation')}| expected: |str|")

	# validating attribute
	current_validation = (type(resp_obj.get("attribute")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: PatchOperation for key attribute, value: |{resp_obj.get('attribute')}| expected: |str|")

	# validating value
	# Not found how to evaluate value
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: PatchOperation for key value, value: |{resp_obj.get('value')}| expected: |None|")

	return valid_entity


def validate_AccessCodeList(l_elements: list):
	valid_entity: bool = True
	# validating #/components/schemas/AccessCode
	for element in l_elements:
		valid_entity = valid_entity and validate_AccessCode(element)
		if not valid_entity:
			logger.error(f"Validation Error: AccessCodeList {element}")
			break

	return valid_entity


def validate_PatchOperationList(l_elements: list):
	valid_entity: bool = True
	# validating #/components/schemas/PatchOperation
	for element in l_elements:
		valid_entity = valid_entity and validate_PatchOperation(element)
		if not valid_entity:
			logger.error(f"Validation Error: PatchOperationList {element}")
			break

	return valid_entity


def validate_Error(resp_obj: dict):
	valid_entity: bool = True
	# validating code
	current_validation = (type(resp_obj.get("code")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: Error for key code, value: |{resp_obj.get('code')}| expected: |str|")

	# validating message
	current_validation = (type(resp_obj.get("message")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: Error for key message, value: |{resp_obj.get('message')}| expected: |str|")

	return valid_entity


def validate_CommandParameters(resp_obj: dict):
	valid_entity: bool = True
	# validating code
	current_validation = (type(resp_obj.get("code")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: CommandParameters for key code, value: |{resp_obj.get('code')}| expected: |str|")

	# validating accessCodeProgram
	current_validation = (type(resp_obj.get("accessCodeProgram")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: CommandParameters for key accessCodeProgram, value: |{resp_obj.get('accessCodeProgram')}| expected: |str|")

	# validating dogId
	# the field dogId could be None
	if resp_obj.get("dogId"): 
		current_validation = ((type(resp_obj.get("dogId")) == int))
	else: 
		current_validation = True # The field is null
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: CommandParameters for key dogId, value: |{resp_obj.get('dogId')}| expected: |int|")

	# validating transactionId
	# the field transactionId could be None
	if resp_obj.get("transactionId"): 
		current_validation = ((type(resp_obj.get("transactionId")) == int))
	else: 
		current_validation = True # The field is null
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: CommandParameters for key transactionId, value: |{resp_obj.get('transactionId')}| expected: |int|")

	return valid_entity


def validate_Command(resp_obj: dict):
	valid_entity: bool = True
	# validating name
	current_validation = (type(resp_obj.get("name")) == str)
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: Command for key name, value: |{resp_obj.get('name')}| expected: |str|")

	# validating parameters
	current_validation = validate_CommandParameters(resp_obj.get("parameters"))
	valid_entity = valid_entity and current_validation
	if not current_validation:
		logger.error(f"Validation Error: Command for key parameters, value: |{resp_obj.get('parameters')}| expected: |None|")

	return valid_entity


