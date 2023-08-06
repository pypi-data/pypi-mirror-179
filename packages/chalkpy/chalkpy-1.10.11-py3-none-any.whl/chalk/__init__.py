import inspect
from typing import Any, Callable, Optional, Union

from chalk.features import Cron, Environments, Tags, description, is_primary, owner, tags
from chalk.features.resolver import OfflineResolver, OnlineResolver, Resolver, offline, online, parse_function
from chalk.state import State
from chalk.streams import stream
from chalk.utils import MachineType
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import ScheduleOptions
from chalk.utils.environment_parsing import env_var_bool

__all__ = [
    "Cron",
    "Environments",
    "ScheduleOptions",
    "State",
    "Tags",
    "batch",
    "description",
    "is_primary",
    "offline",
    "online",
    "owner",
    "realtime",
    "stream",
    "tags",
]


def realtime(
    fn: Optional[Callable] = None,
    /,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Optional[Union[ScheduleOptions, Cron]] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
):
    """
    :param fn: The function that you're decorating as a resolver.

    :param environment: Environments are used to trigger behavior
        in different deployments such as staging, production, and
        local development. For example, you may wish to interact with
        a vendor via an API call in the production environment, and
        opt to return a constant value in a staging environment.

        Environment can take one of three types:

            - None (default) - candidate to run in every environment
            - str - run only in this environment
            - list[str] - run in any of the specified environment and no others

        Read more at https://docs.chalk.ai/docs/resolver-environments

    :param tags: Tags allow you to scope requests within an
        environment. Both tags and environment need to match for a
        resolver to be a candidate to execute.

        You might consider using tags, for example, to change out
        whether you want to use a sandbox environment for a vendor,
        or to bypass the vendor and return constant values in a
        staging environment.

        Read more at https://docs.chalk.ai/docs/resolver-tags

    :param cron: You can schedule resolvers to run on a
        pre-determined schedule via the cron argument to resolver
        decorators.

        Cron can sample all examples, a subset of all examples,
        or a custom provided set of examples.

        Read more at https://docs.chalk.ai/docs/resolver-cron

    :param machine_type: You can optionally specify that resolvers
        need to run on a machine other than the default. Must be
        configured in your deployment.

    :param when: Like tags, `when` can filter when a resolver
        is eligible to run. Unlike tags, `when` can use feature values,
        so that you can write resolvers like:

            @realtime(when=User.risk_profile == "low" or User.is_employee)
            def resolver_fn(...) -> ...:
                ...

    :return: A callable function! You can unit test resolvers
        as you would unit test any other code.

        Read more at https://docs.chalk.ai/docs/unit-tests
    """
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals

    def decorator(fn: Callable, cf: str = caller_filename):
        parsed = parse_function(fn, caller_globals, caller_locals)
        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
            raise ValueError(f"Duplicate resolver {parsed.fqn}")
        if parsed.output is None:
            raise ValueError(f"Realtime resolvers must return features; '{parsed.fqn}' returns None")

        resolver = OnlineResolver(
            filename=cf,
            function_definition=parsed.function_definition,
            fqn=parsed.fqn,
            doc=parsed.doc,
            inputs=parsed.inputs,
            output=parsed.output,
            fn=parsed.function,
            environment=None if environment is None else list(ensure_tuple(environment)),
            tags=None if tags is None else list(ensure_tuple(tags)),
            max_staleness=None,
            cron=cron,
            machine_type=machine_type,
            when=when,
            state=parsed.state,
            default_args=parsed.default_args,
        )
        Resolver.registry.append(resolver)
        Resolver.hook and Resolver.hook(resolver)

        # Return the decorated resolver, which notably implements __call__() so it acts the same as
        # the underlying function if called directly, e.g. from test code
        return resolver

    return decorator(fn) if fn else decorator


def batch(
    fn: Optional[Callable] = None,
    /,
    environment: Optional[Environments] = None,
    tags: Optional[Tags] = None,
    cron: Union[ScheduleOptions, Cron] = None,
    machine_type: Optional[MachineType] = None,
    when: Optional[Any] = None,
):
    """
    :param fn: The function that you're decorating as a resolver.

    :param environment: Environments are used to trigger behavior
        in different deployments such as staging, production, and
        local development. For example, you may wish to interact with
        a vendor via an API call in the production environment, and
        opt to return a constant value in a staging environment.

        Environment can take one of three types:

            - None (default) - candidate to run in every environment
            - str - run only in this environment
            - list[str] - run in any of the specified environment and no others

        Read more at https://docs.chalk.ai/docs/resolver-environments

    :param tags: Tags allow you to scope requests within an
        environment. Both tags and environment need to match for a
        resolver to be a candidate to execute.

        You might consider using tags, for example, to change out
        whether you want to use a sandbox environment for a vendor,
        or to bypass the vendor and return constant values in a
        staging environment.

        Read more at https://docs.chalk.ai/docs/resolver-tags

    :param cron: You can schedule resolvers to run on a
        pre-determined schedule via the cron argument to resolver
        decorators.

        Cron can sample all examples, a subset of all examples,
        or a custom provided set of examples.

        Read more at https://docs.chalk.ai/docs/resolver-cron

    :param machine_type: You can optionally specify that resolvers
        need to run on a machine other than the default. Must be
        configured in your deployment.

    :param when: Like tags, `when` can filter when a resolver
        is eligible to run. Unlike tags, `when` can use feature values,
        so that you can write resolvers like:

            @batch(when=User.risk_profile == "low" or User.is_employee)
            def resolver_fn(...) -> ...:
                ...

    :return: A callable function! You can unit test resolvers
        as you would unit test any other code.

    Read more at https://docs.chalk.ai/docs/unit-tests
    """

    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename
    caller_globals = caller_frame.frame.f_globals
    caller_locals = caller_frame.frame.f_locals

    def decorator(args, cf=caller_filename):
        parsed = parse_function(args, caller_globals, caller_locals)
        if not env_var_bool("CHALK_ALLOW_REGISTRY_UPDATES") and parsed.fqn in {s.fqn for s in Resolver.registry}:
            raise ValueError(f"Duplicate resolver {parsed.fqn}")
        if parsed.output is None:
            raise ValueError(f"Batch resolvers must return features; '{parsed.fqn}' returns None")
        resolver = OfflineResolver(
            filename=cf,
            function_definition=parsed.function_definition,
            fqn=parsed.fqn,
            doc=parsed.doc,
            inputs=parsed.inputs,
            output=parsed.output,
            fn=parsed.function,
            environment=None if environment is None else list(ensure_tuple(environment)),
            tags=None if tags is None else list(ensure_tuple(tags)),
            max_staleness=None,
            cron=cron,
            machine_type=machine_type,
            when=when,
            state=parsed.state,
            default_args=parsed.default_args,
        )
        Resolver.registry.append(resolver)
        Resolver.hook and Resolver.hook(resolver)
        return args

    return decorator(fn) if fn else decorator
