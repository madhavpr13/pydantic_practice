from typing import Optional


class ValidationError(Exception):
    pass


class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self._ssn = ssn

    @property
    def ssn(self):
        return "XXX-XX-" + self._ssn[-4:]

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, ssn={self.ssn})"


def create_person_from_dict(person_dict) -> Optional[Person]:
    try:
        return Person(**person_dict)
    except ValidationError as ex:
        print(f"Exception occurred: {ex}")
        return None


if __name__ == "__main__":
    person_dict = {"name": "Isaac", "age": 84, "ssn": "123-45-6789"}
    print(create_person_from_dict(person_dict))
