import pytest

from {{cookiecutter.package_name}}.context import Context, Resource


class TestContext:
    def test_context(self) -> None:
        context = Context(None)
        assert isinstance(context, Context)

        resources = {"resource_one": "object_one"}
        context = Context(resources)
        assert isinstance(context, Context)

        resource_one = context.resource_one
        assert resource_one == "object_one"

        del context.resource_one

        with pytest.raises(AttributeError):
            context.resource_one

        context.resource_two = "object_two"
        assert context.resource_two == "object_two"


class TestResource:
    def test_resource(self) -> None:
        assert str(Resource.RESOURCE_ONE) == "RESOURCE_ONE"
