import uuid


def print_uuid4():
    result = uuid.uuid4()
    print(result)
    print(result.hex)
    print(result.urn)


def print_uuid5():
    result = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    print(result)
    print(result.hex)
    print(result.urn)


print_uuid4()
print_uuid5()
